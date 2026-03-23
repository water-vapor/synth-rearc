from arc2.core import *

from .helpers import (
    extract_lines_22425bda,
    line_sort_key_22425bda,
    output_from_lines_22425bda,
)


def verify_22425bda(I: Grid) -> Grid:
    x0 = extract_lines_22425bda(I)
    x1 = tuple(sorted(x0, key=lambda x2: line_sort_key_22425bda(I, x2)))
    x2 = output_from_lines_22425bda(x1)
    return x2
