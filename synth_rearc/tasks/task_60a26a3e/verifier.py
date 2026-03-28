from synth_rearc.core import *


def _plus_centers_60a26a3e(
    I: Grid,
):
    x0 = []
    for x1 in ofcolor(I, ZERO):
        x2 = T
        for x3 in dneighbors(x1):
            if not equality(index(I, x3), TWO):
                x2 = F
                break
        if x2:
            x0.append(x1)
    return tuple(sorted(x0))


def verify_60a26a3e(
    I: Grid,
) -> Grid:
    x0 = _plus_centers_60a26a3e(I)
    x1 = {}
    x2 = {}
    for x3 in x0:
        x4, x5 = x3
        if x4 not in x1:
            x1[x4] = []
        if x5 not in x2:
            x2[x5] = []
        x1[x4].append(x3)
        x2[x5].append(x3)
    x6 = I
    for x7 in x1.values():
        x8 = tuple(sorted(x7))
        for x9, x10 in zip(x8, x8[ONE:]):
            x11 = difference(difference(connect(x9, x10), initset(x9)), initset(x10))
            x6 = underfill(x6, ONE, x11)
    for x7 in x2.values():
        x8 = tuple(sorted(x7))
        for x9, x10 in zip(x8, x8[ONE:]):
            x11 = difference(difference(connect(x9, x10), initset(x9)), initset(x10))
            x6 = underfill(x6, ONE, x11)
    return x6
