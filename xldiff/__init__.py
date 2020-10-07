"""
A dead-simple command line diffing of datasets stored in Excel
format (.xlsx).
"""

__version__ = "0.1.0"

import sys

from xldiff.app import diff_files


def main():
    diff_files(sys.argv[1], sys.argv[2])
