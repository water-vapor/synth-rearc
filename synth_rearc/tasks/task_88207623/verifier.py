from synth_rearc.core import *


def verify_88207623(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = colorfilter(x0, TWO)
    x2 = colorfilter(x0, FOUR)
    x3 = tuple(obj for obj in x0 if color(obj) not in (TWO, FOUR))
    x4 = I
    for x5 in x1:
        x6 = extract(x2, lambda y: adjacent(x5, y))
        x7 = leftmost(x5)
        x8 = greater(leftmost(x6), x7)
        x9 = tuple(
            obj
            for obj in x3
            if hmatching(x5, obj) and ((rightmost(obj) < x7) if x8 else (leftmost(obj) > x7))
        )
        x10 = argmin(x9, lambda obj: manhattan(x5, obj))
        x11 = color(x10)
        x12 = toindices(x6)
        x13 = frozenset((i, subtract(double(x7), j)) for i, j in x12)
        x14 = recolor(x11, x13)
        x4 = underpaint(x4, x14)
    return x4
