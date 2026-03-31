from synth_rearc.core import *

from .helpers import (
    BLOCK_COUNT_981571DC,
    DIAGONAL_BLOCK_BANK_981571DC,
    OFF_DIAGONAL_BLOCK_BANK_981571DC,
    block_981571dc,
    block_has_zero_981571dc,
    dmirror_block_981571dc,
    freeze_rows_981571dc,
    match_unique_block_981571dc,
    mutable_rows_981571dc,
    paint_block_981571dc,
    transpose_fill_981571dc,
)


def verify_981571dc(
    I: Grid,
) -> Grid:
    x0 = transpose_fill_981571dc(I)
    x1 = mutable_rows_981571dc(x0)
    for x2 in range(BLOCK_COUNT_981571DC):
        x3 = block_981571dc(x1, x2, x2)
        if block_has_zero_981571dc(x3):
            x4 = match_unique_block_981571dc(x3, DIAGONAL_BLOCK_BANK_981571DC)
            if x4 is None:
                return x0
            paint_block_981571dc(x1, x2, x2, x4)
        for x5 in range(x2 + ONE, BLOCK_COUNT_981571DC):
            x6 = block_981571dc(x1, x2, x5)
            if not block_has_zero_981571dc(x6):
                continue
            x7 = match_unique_block_981571dc(x6, OFF_DIAGONAL_BLOCK_BANK_981571DC)
            if x7 is None:
                return x0
            paint_block_981571dc(x1, x2, x5, x7)
            paint_block_981571dc(x1, x5, x2, dmirror_block_981571dc(x7))
    x8 = freeze_rows_981571dc(x1)
    return transpose_fill_981571dc(x8)
