# Image Exif Batch Renamer

I created this to support another project, where I was sampling files by exif data. 
I needed a way to easily load only certain image files, so just encoding the filename with the appropriate data was easy.

## Arguments

- **-d [--directory]**: defaults to current directory (.)
- **-p [--pattern]**: matching pattern. Defaults to "[O]", which will rename everything to their original name.
- **-t [--test]: Test flag. Runs, but won't actually rename the files.

## Patterns
- [A] Aperture
- [ISO] - ISO
- [SS] - Shutter speed in fractional denominator (1/60s = "60"). "s" suffix for whole seconds. "30 seconds" = "30s". It breaks on whole+fractional, giving numerator-denominaotr as whole integers.
- [O] - Original filename, no extension
- [C] - Arbitrarily ordered count. Useful to prevent duplicate filenames, which breaks things.

## Example Usage

This will change "IMG0001.jpg" to s60_a4_iso400_1.jpg"
> -p s[SS]_a[A]_iso[ISO]_[C] -d test/

## Todo
- Datetime support with standard formats
- Safe mode to to a dry run, check if errors, then run normal run

I don't plan on recursive directory searching, supporting regex, or adding graceful failure.
