from synth_rearc.core import *


def _variants_50f325b5(patch: Patch) -> tuple[Patch, ...]:
    x0 = normalize(patch)
    x1 = normalize(dmirror(vmirror(x0)))
    x2 = normalize(dmirror(vmirror(x1)))
    x3 = normalize(dmirror(vmirror(x2)))
    x4 = normalize(hmirror(x0))
    x5 = normalize(vmirror(x0))
    x6 = normalize(dmirror(x0))
    x7 = normalize(cmirror(x0))
    out = []
    for candidate in (x0, x1, x2, x3, x4, x5, x6, x7):
        if candidate not in out:
            out.append(candidate)
    return tuple(out)


def verify_50f325b5(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = _variants_50f325b5(x0)
    x2 = []
    for x3 in x1:
        x4 = recolor(THREE, x3)
        x5 = occurrences(I, x4)
        for x6 in x5:
            x7 = shift(x3, x6)
            if x7 not in x2:
                x2.append(x7)
    x8 = sorted(
        x2,
        key=lambda patch: (
            uppermost(patch),
            leftmost(patch),
            lowermost(patch),
            rightmost(patch),
            tuple(sorted(patch)),
        ),
    )
    x9 = frozenset()
    x10 = I
    for x11 in x8:
        if size(intersection(x9, x11)) > ZERO:
            continue
        x10 = fill(x10, EIGHT, x11)
        x9 = combine(x9, x11)
    return x10
