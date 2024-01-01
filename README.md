# Image Exif Batch Renamer

## Arguments

- -d/--directory: defaults to current directory (.)
- -p/--pattern: matching pattern. Defaults to "[O]", which will rename everything to their original name.
- -t/--test: Test flag. Don't actually rename the files.

## Patterns
[A] - Aperture
[ISO] - ISO
[SS] - Shutter speed in fractional denominator (1/60s = "60"). "s" suffix for whole seconds. "30 seconds" = "30s". It breaks on whole+fractional, giving numerator-denominaotr as whole integers.
[O] - Original filename, no extension
[C] - Arbitraty count. Useful to prevent duplicate filenames, which breaks things.
