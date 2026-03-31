from __future__ import annotations

from synth_rearc.core import *

from .helpers import enclosed_cells_aa4ec2a5, halo8_aa4ec2a5


def verify_aa4ec2a5(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = shape(I)
    x2 = objects(I, T, F, T)
    x3 = canvas(x0, x1)
    x4 = tuple(enclosed_cells_aa4ec2a5(x5) for x5 in x2)
    x5 = tuple(halo8_aa4ec2a5(x6, x1) for x6 in x2)
    x6 = fill(x3, TWO, merge(x5))
    x7 = fill(x6, SIX, merge(x4))
    x8 = tuple(
        recolor(branch(equality(size(x9), ZERO), color(x10), EIGHT), x10)
        for x9, x10 in zip(x4, x2)
    )
    x9 = paint(x7, merge(x8))
    return x9
