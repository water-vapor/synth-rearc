from synth_rearc.core import *


def _line_completion(x0: Indices):
    x1 = frozenset(i for i, _ in x0)
    x2 = frozenset(j for _, j in x0)
    x3 = frozenset(i - j for i, j in x0)
    x4 = frozenset(i + j for i, j in x0)
    if size(x1) == ONE:
        x5 = minimum(x1)
        return connect((x5, minimum(x2)), (x5, maximum(x2)))
    if size(x2) == ONE:
        x5 = minimum(x2)
        return connect((minimum(x1), x5), (maximum(x1), x5))
    if size(x3) == ONE:
        return connect(ulcorner(x0), lrcorner(x0))
    if size(x4) == ONE:
        return connect(urcorner(x0), llcorner(x0))
    return None


def _rectangular_completion(x0: Indices):
    x1 = ulcorner(x0)
    x2 = lrcorner(x0)
    x3 = tuple(
        sum((x4, x5) in x0 for x5 in range(x1[ONE], x2[ONE] + ONE))
        for x4 in range(x1[ZERO], x2[ZERO] + ONE)
    )
    x6 = tuple(
        sum((x4, x5) in x0 for x4 in range(x1[ZERO], x2[ZERO] + ONE))
        for x5 in range(x1[ONE], x2[ONE] + ONE)
    )
    if len(set(x3)) <= TWO and len(set(x6)) <= TWO:
        return backdrop(x0)
    return None


def verify_52df9849(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = tuple(sorted(x2 for x2 in palette(I) if x2 != x0))
    x2 = []
    for x3 in x1:
        x4 = ofcolor(I, x3)
        x5 = _line_completion(x4)
        x6 = branch(x5 is None, _rectangular_completion(x4), x5)
        if x6 is not None and x6 != x4:
            x7 = colorcount(I, x3)
            x2.append((x7, x3, x6))
    x8 = I
    for _, x9, x10 in sorted(x2, key=lambda item: (-item[ZERO], -item[ONE])):
        x11 = recolor(x9, x10)
        x8 = paint(x8, x11)
    return x8
