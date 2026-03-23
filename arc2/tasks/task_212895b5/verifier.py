from arc2.core import *

from .helpers import (
    arm_paths_212895b5,
    block_origin_212895b5,
    diagonal_paths_212895b5,
    flatten_paths_212895b5,
)


def verify_212895b5(
    I: Grid,
) -> Grid:
    x0 = block_origin_212895b5(I)
    x1 = arm_paths_212895b5(I, x0)
    x2 = diagonal_paths_212895b5(I, x0)
    x3 = flatten_paths_212895b5(x1)
    x4 = flatten_paths_212895b5(x2)
    x5 = fill(I, FOUR, x3)
    x6 = fill(x5, TWO, x4)
    return x6
