from synth_rearc.core import *


def verify_db695cfb(
    I: Grid,
) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = ofcolor(I, SIX)
    x2 = tuple(sorted(x0))
    x3 = set()
    x4 = set()
    for x5, x6 in enumerate(x2):
        for x7 in x2[add(x5, ONE):]:
            x8 = subtract(x7[0], x6[0])
            x9 = subtract(x7[1], x6[1])
            x10 = abs(x8) == abs(x9)
            if not x10:
                continue
            x11 = connect(x6, x7)
            x3 |= set(x11)
            x12 = set(x11) & set(x1)
            if x8 == x9:
                for x13 in x12:
                    x14 = combine(shoot(x13, UP_RIGHT), shoot(x13, DOWN_LEFT))
                    x4 |= set(x14)
            else:
                for x13 in x12:
                    x14 = combine(shoot(x13, UNITY), shoot(x13, NEG_UNITY))
                    x4 |= set(x14)
    x15 = fill(I, ONE, difference(x3, x1))
    x16 = fill(x15, SIX, x4)
    return x16
