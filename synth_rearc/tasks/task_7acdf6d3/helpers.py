from synth_rearc.core import *


def row_span_mask_7acdf6d3(obj: Patch) -> Indices:
    x0 = {}
    for x1, x2 in toindices(obj):
        if x1 not in x0:
            x0[x1] = []
        x0[x1].append(x2)
    x3 = frozenset()
    for x4, x5 in x0.items():
        x6 = connect((x4, min(x5)), (x4, max(x5)))
        x3 = combine(x3, x6)
    return x3


def row_hole_mask_7acdf6d3(obj: Patch) -> Indices:
    x0 = row_span_mask_7acdf6d3(obj)
    x1 = toindices(obj)
    x2 = difference(x0, x1)
    return x2
