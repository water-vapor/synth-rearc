from arc2.core import *

from .helpers import ABOVE_STEPS_652646ff, clipped_diamond_patch_652646ff, diamond_block_652646ff
from .verifier import verify_652646ff


def generate_652646ff(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ZERO, TEN, ONE)
    while True:
        x1 = choice((TWO, THREE, THREE, FOUR))
        x2 = choice((ONE, TWO, TWO))
        x3 = sample(x0, add(add(x1, x2), ONE))
        x4 = x3[ZERO]
        x5 = x3[ONE:add(ONE, x1)]
        x6 = x3[add(ONE, x1):]
        x7 = unifint(diff_lb, diff_ub, (TEN, 20))
        x8 = unifint(diff_lb, diff_ub, (TEN, 20))
        x9 = astuple(x7, x8)
        x10 = tuple(reversed(x5))
        x11 = False
        for _ in range(400):
            x12 = astuple(randint(-TWO, subtract(x7, FOUR)), randint(-TWO, subtract(x8, FOUR)))
            x13 = (x12,)
            x14 = (clipped_diamond_patch_652646ff(x12, x9),)
            x15 = True
            for _ in range(subtract(x1, ONE)):
                x16 = tuple()
                for x17 in ABOVE_STEPS_652646ff:
                    x18 = add(last(x13), x17)
                    x19 = clipped_diamond_patch_652646ff(x18, x9)
                    if len(x19) < EIGHT:
                        continue
                    if len(intersection(x19, last(x14))) == ZERO:
                        continue
                    if any(len(intersection(x19, x20)) > ZERO for x20 in x14[:-ONE]):
                        continue
                    x16 = x16 + (x18,)
                if len(x16) == ZERO:
                    x15 = False
                    break
                x21 = choice(x16)
                x13 = x13 + (x21,)
                x14 = x14 + (clipped_diamond_patch_652646ff(x21, x9),)
            if not x15:
                continue
            x22 = tuple()
            x23 = frozenset()
            for x24 in reversed(x14):
                x25 = difference(x24, x23)
                x22 = (x25,) + x22
                x23 = combine(x23, x24)
            x26 = tuple(len(x27) for x27 in x22)
            if minimum(x26) < EIGHT:
                continue
            x11 = True
            break
        if not x11:
            continue
        x27 = canvas(x4, x9)
        for x28, x29 in zip(x10, x13):
            x30 = clipped_diamond_patch_652646ff(x29, x9)
            x27 = fill(x27, x28, x30)
        x31 = totuple(ofcolor(x27, x4))
        x32 = minimum((FIVE, len(x31)))
        x33 = unifint(diff_lb, diff_ub, (TWO, x32))
        x34 = tuple(sample(x31, x33))
        for x35 in x34:
            x36 = choice(x6)
            x27 = fill(x27, x36, initset(x35))
        x37 = tuple(diamond_block_652646ff(x4, x38) for x38 in x5)
        x39 = x37[ZERO]
        for x40 in x37[ONE:]:
            x39 = vconcat(x39, x40)
        if verify_652646ff(x27) != x39:
            continue
        return {"input": x27, "output": x39}
