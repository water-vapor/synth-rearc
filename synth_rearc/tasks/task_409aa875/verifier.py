from __future__ import annotations

from collections import Counter

from synth_rearc.core import *

from .helpers import ordered_objects_409aa875, projection_target_409aa875


def verify_409aa875(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = ordered_objects_409aa875(x0)
    x2 = Counter()
    x3 = Counter()
    for x4 in x1:
        x5 = projection_target_409aa875(x4)
        x6 = None
        for x7, x8 in enumerate(x1):
            if x5 in toindices(x8):
                x6 = x7
                break
        if x6 is None:
            if index(I, x5) is not None:
                x2[x5] += ONE
        else:
            x3[x6] += ONE
    x9 = I
    for x10, x11 in sorted(x2.items()):
        x12 = branch(greater(x11, ONE), ONE, NINE)
        x13 = fill(x9, x12, frozenset({x10}))
        x9 = x13
    for x14, x15 in sorted(x3.items()):
        x16 = branch(greater(x15, ONE), ONE, NINE)
        x17 = fill(x9, x16, x1[x14])
        x9 = x17
    return x9
