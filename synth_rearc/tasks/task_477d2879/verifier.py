from synth_rearc.core import *

from .helpers import connected_components_477d2879, white_neighbor_count_477d2879


def _split_markers_477d2879(
    white: Indices,
    zeros: Indices,
    markers: tuple[Object, ...],
) -> tuple[frozenset[Object], frozenset[Object]]:
    x0 = None
    x1 = None
    for x2 in range(ONE << len(markers)):
        x3 = frozenset(obj for k, obj in enumerate(markers) if (x2 >> k) & ONE)
        x4 = difference(markers, x3)
        x5 = combine(white, toindices(merge(x3)))
        x6 = combine(zeros, toindices(merge(x4)))
        x7 = connected_components_477d2879(x5)
        x8 = connected_components_477d2879(x6)
        if any(sum(ulcorner(obj) in comp for obj in x3) != ONE for comp in x7):
            continue
        x9 = T
        for x10 in x8:
            x11 = {color(obj) for obj in x4 if ulcorner(obj) in x10}
            if len(x11) != ONE:
                x9 = F
                break
        if not x9:
            continue
        x12 = sum(white_neighbor_count_477d2879(white, ulcorner(obj)) for obj in x3)
        x13 = (size(x3), -x12, tuple(sorted(ulcorner(obj) for obj in x3)))
        if x1 is None or x13 < x1:
            x0 = (x3, x4)
            x1 = x13
    if x0 is None:
        raise ValueError("could not split markers into object and background roles")
    return x0


def verify_477d2879(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = ofcolor(I, ZERO)
    x2 = objects(I, T, F, T)
    x3 = matcher(color, ONE)
    x4 = compose(flip, x3)
    x5 = tuple(sorted(sfilter(x2, x4), key=ulcorner))
    x6, x7 = _split_markers_477d2879(x0, x1, x5)
    x8 = toindices(merge(x6))
    x9 = toindices(merge(x7))
    x10 = combine(x0, x8)
    x11 = combine(x1, x9)
    x12 = connected_components_477d2879(x10)
    x13 = connected_components_477d2879(x11)
    x14 = {ulcorner(obj): color(obj) for obj in x6}
    x15 = {ulcorner(obj): color(obj) for obj in x7}
    x16 = canvas(ZERO, shape(I))
    x17 = x16
    for x18 in x12:
        x19 = next(value for loc, value in x14.items() if loc in x18)
        x17 = fill(x17, x19, x18)
    for x18 in x13:
        x19 = next(value for loc, value in x15.items() if loc in x18)
        x17 = fill(x17, x19, x18)
    return x17
