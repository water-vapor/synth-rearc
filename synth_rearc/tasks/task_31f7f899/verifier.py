from synth_rearc.core import *


def verify_31f7f899(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = None
    for x2, x3 in enumerate(I):
        if SIX in x3:
            x1 = x2
            break
    x4 = objects(I, T, F, T)
    x5 = tuple(
        sorted(
            (
                x6 for x6 in x4
                if both(
                    color(x6) != SIX,
                    both(uppermost(x6) <= x1, x1 <= lowermost(x6)),
                )
            ),
            key=lambda x7: leftmost(x7),
        )
    )
    x6 = tuple(sorted(height(x7) for x7 in x5))
    x7 = I
    for x8 in x5:
        x7 = fill(x7, x0, x8)
    for x8, x9 in zip(x5, x6):
        x10 = color(x8)
        x11 = leftmost(x8)
        x12 = width(x8)
        x13 = subtract(x1, divide(x9, TWO))
        x14 = frozenset((x15, x16) for x15 in range(x13, add(x13, x9)) for x16 in range(x11, add(x11, x12)))
        x15 = recolor(x10, x14)
        x7 = paint(x7, x15)
    return x7
