import os
import warnings
import argparse
from fractions import Fraction
from exif import Image

tag_to_data = {"[A]": "f_number",
               "[SS]": "exposure_time",
               "[ISO]": "photographic_sensitivity",
               "[P]": "exposure_program",
               "[COMPRESSION]": "compression"}
count = 0
def rename_image(filename, exifdata, pattern):
    original, extension = os.path.splitext(filename)
    new_name = pattern

    #todo: datetime
    ## datetime

    ## exif
    for p,ex in tag_to_data.items():
        if p in new_name:
            new_name = new_name.replace(p,exifdata[ex])

    # Count is in an arbitrary order, but will prevent file duplicate names.
    if "[C]" in new_name:
        new_name = new_name.replace("[C]", str(count))

    if "[O]" in new_name:
        new_name = new_name.replace("[O]", original)
    return new_name+extension


def get_exif_dict(image):
    d = {}
    for data in image.list_all():

        # data cleanup
        if data == "f_number":
            a = image.get("f_number")
            d[data] = "{:n}".format(a)
            continue

        if data == "exposure_time":
            f = Fraction(image.get("exposure_time")).limit_denominator()
            if f.numerator == 1:
                d[data] = "{:n}".format(f.denominator)
            elif f.denominator == 1:
                d[data] = "{:n}s".format(f.numerator)
            else:
                d[data] = "{:n}-{:n}".format(f.numerator, f.denominator)
            continue
        d[data] = str(image.get(data)).strip()
    return d

def rename_dir(dir,pattern, dry_run=  False):
    names = []
    global count
    count = 0
    for file in os.listdir(dir):
        filepath = dir+file
        image = Image(filepath)
        if(image.has_exif):
            new_file = rename_image(file,get_exif_dict(image),pattern)
            if new_file in names:
                raise Exception("Error: Already a file with resulting name. Add [C] to pattern for counting."+new_file)
            names.append(new_file)
            count = count+1
            if not dry_run:
                if new_file != file:
                    os.rename(filepath,dir+new_file)

            print(f"rename {file} to {new_file}")
        else:
            print("skipping", file)
    return names

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with warnings.catch_warnings():
        # supress runtime warnings about improperly encoded EXIF.
        # We assume provided images are valid enough.
        warnings.filterwarnings("ignore","^.*ASCII tag contains.*$")

        parser = argparse.ArgumentParser(description='Rename a directory of images.')
        parser.add_argument("-d","--directory", default=".", help="Directory")
        parser.add_argument("-p", "--pattern",type=str,default="[O]")
        parser.add_argument("-t", "--test", default=False, action="store_true")

        args = parser.parse_args()
        #handle flags
        rename_dir(args.directory,args.pattern, args.test)

        # results
        print("Renamed {count} images".format(count=count))