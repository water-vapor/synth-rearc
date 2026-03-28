from synth_rearc.core import *

from .helpers import distance_pairs_57edb29d, render_panel_57edb29d


def _panels_57edb29d(I: Grid) -> tuple[Grid, ...]:
    x0 = len(I)
    x1 = len(I[0])
    x2 = set()
    x3 = []
    for x4 in range(x0):
        for x5 in range(x1):
            if I[x4][x5] == FOUR or (x4, x5) in x2:
                continue
            x6 = [(x4, x5)]
            x2.add((x4, x5))
            x7 = []
            while len(x6) > ZERO:
                x8, x9 = x6.pop()
                x7.append((x8, x9))
                for x10, x11 in ((NEG_ONE, ZERO), (ONE, ZERO), (ZERO, NEG_ONE), (ZERO, ONE)):
                    x12 = x8 + x10
                    x13 = x9 + x11
                    if 0 <= x12 < x0 and 0 <= x13 < x1 and I[x12][x13] != FOUR and (x12, x13) not in x2:
                        x2.add((x12, x13))
                        x6.append((x12, x13))
            x14 = min(x15 for x15, _ in x7)
            x16 = min(x17 for _, x17 in x7)
            x18 = max(x19 for x19, _ in x7) - x14 + ONE
            x20 = max(x21 for _, x21 in x7) - x16 + ONE
            x3.append(crop(I, (x14, x16), (x18, x20)))
    return tuple(x3)


def verify_57edb29d(I: Grid) -> Grid:
    x0 = _panels_57edb29d(I)
    x1 = matcher(numcolors, ONE)
    x2 = extract(x0, x1)
    x3 = remove(x2, x0)
    x4 = apply(palette, x3)
    x5 = mostcommon(merge(x4))
    x6 = lbind(distance_pairs_57edb29d, x5)
    x7 = mapply(x6, x3)
    x8 = mostcolor(x2)
    x9 = shape(x2)
    x10 = render_panel_57edb29d(x8, x5, x9, x7)
    return x10
