from typing import Optional, Tuple, Union

from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet


Row = Tuple[Cell, ...]
"""
A single row of data. This type is just a convenience.
"""

Diff = Union[Tuple[Row, Row], Tuple[Row, None], Tuple[None, Row]]
"""
A two-tuple of the left and right versions of a given row where
one of the versions might not exist (hence None).
"""


def print_row(row: Row):
    """
    Pretty-print the given row.

    :param row: The row to print
    """
    if row is None:
        print("MISSING")
        return
    print("|", end="")
    for cell in row:
        print(cell.value, end="|")
    print()


def first_difference(left: Worksheet, right: Worksheet) -> Optional[Tuple[Diff, int]]:
    """
    Compare two sheets and return the first difference found, if any,
    plus the index (starting from 1) of the row that differed.

    :param left: The left-hand sheet
    :param right: The right-hand sheet
    :return: The first difference and index or None
    """
    left_rows = left.iter_rows()
    right_rows = right.iter_rows()

    left_row: Union[Row, None]
    right_row: Union[Row, None]

    row_index = 0

    while True:
        left_row = next(left_rows, None)
        right_row = next(right_rows, None)
        row_index += 1

        if left_row is None and right_row is None:
            return None

        if left_row is None:
            return (None, right_row), row_index

        if right_row is None:
            return (left_row, None), row_index

        if not rows_match(left_row, right_row):
            return (left_row, right_row), row_index


def rows_match(left: Row, right: Row) -> bool:
    """
    Compare two rows.

    :param left: The left-hand row
    :param right: The right-hand row
    :return: True if the rows match, False otherwise
    """
    if len(left) != len(right):
        return False

    for (lv, rv) in zip(left, right):
        if lv.value != rv.value:
            return False

    return True
