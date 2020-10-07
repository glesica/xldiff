# XL Diff

A dead-simple command line diffing of datasets stored in Excel
format (.xlsx).

## Usage

```
python -m xldiff file_left.xlsx file_right.xlsx
```

If the datasets match then the program will exit successfully
and produce no output. If they do not match then the first
non-matching row from the "left" and the "right" versions will
be printed and the program will terminate with a non-zero
exit code.

**OK, but what's it for?** Mostly to make it easier to verify
that data has been moved successfully from one system to another
or that a new "version" of a dataset has actually changed.
