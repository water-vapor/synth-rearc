from synth_rearc.core import *

from .helpers import component_patches_d93c6891
from .helpers import rectangle_patch_d93c6891


def generate_d93c6891(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (EIGHT, 16))
        x1 = unifint(diff_lb, diff_ub, (EIGHT, 16))
        x2 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
        x3 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
        x4 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
        x5 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
        x6 = add(x0, x2 + x3)
        x7 = add(x1, x4 + x5)
        x8 = canvas(ZERO, (x6, x7))
        x9 = rectangle_patch_d93c6891((x2, x4), (x0, x1))
        x10 = fill(x8, FOUR, x9)
        x11 = x10
        x12 = x10
        x13 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x14 = unifint(diff_lb, diff_ub, (ZERO, TWO))
        x15 = tuple("transformed" for _ in range(x13)) + tuple("plain" for _ in range(x14))
        x16 = list(x15)
        shuffle(x16)
        x17 = frozenset()
        x18 = []
        x19 = x2
        x20 = x4
        x21 = x2 + x0 - ONE
        x22 = x4 + x1 - ONE
        x23 = True
        for x24 in x16:
            x25 = False
            for _ in range(200):
                if x24 == "transformed":
                    x26 = unifint(diff_lb, diff_ub, (TWO, SIX))
                    x27 = unifint(diff_lb, diff_ub, (TWO, SIX))
                else:
                    x26 = unifint(diff_lb, diff_ub, (ONE, FIVE))
                    x27 = unifint(diff_lb, diff_ub, (TWO, SIX))
                    if choice((True, False)):
                        x26, x27 = x27, x26
                if x26 > x0 or x27 > x1:
                    continue
                x28 = choice(interval(x19, x21 - x26 + TWO, ONE))
                x29 = choice(interval(x20, x22 - x27 + TWO, ONE))
                x30 = None
                x31 = ZERO
                x32 = ZERO
                if x24 == "transformed":
                    x33 = x28 - x19
                    x34 = x21 - (x28 + x26 - ONE)
                    x35 = x29 - x20
                    x36 = x22 - (x29 + x27 - ONE)
                    x37 = []
                    if add(x35, x36) >= x27:
                        x37.append("top")
                    if add(x35, x36) >= x27:
                        x37.append("bottom")
                    if add(x33, x34) >= x26:
                        x37.append("left")
                    if add(x33, x34) >= x26:
                        x37.append("right")
                    if len(x37) == 0:
                        continue
                    x30 = choice(tuple(x37))
                    if x30 in ("top", "bottom"):
                        x38 = divide(add(x35, x36), x27)
                        x31 = unifint(diff_lb, diff_ub, (ONE, x38))
                        x39 = multiply(x31, x27)
                        x40 = max(ZERO, x39 - x36)
                        x41 = min(x39, x35)
                        x32 = randint(x40, x41)
                    else:
                        x38 = divide(add(x33, x34), x26)
                        x31 = unifint(diff_lb, diff_ub, (ONE, x38))
                        x39 = multiply(x31, x26)
                        x40 = max(ZERO, x39 - x34)
                        x41 = min(x39, x33)
                        x32 = randint(x40, x41)
                x33, x34, x35 = component_patches_d93c6891((x28, x29), (x26, x27), x30, x31, x32)
                x36 = combine(x33, x34)
                x37 = combine(backdrop(x36), outbox(x36))
                if size(intersection(x36, x17)) > ZERO:
                    continue
                if size(intersection(x37, x17)) > ZERO:
                    continue
                x17 = combine(x17, x37)
                x18.append((x24, x33, x34, x35))
                x25 = True
                break
            if not x25:
                x23 = False
                break
        if not x23:
            continue
        for x24, x25, x26, x27 in x18:
            x11 = fill(x11, SEVEN, x25)
            x12 = fill(x12, SEVEN, x25)
            if x24 == "transformed":
                x11 = fill(x11, FIVE, x26)
                x12 = fill(x12, FIVE, x27)
        return {"input": x11, "output": x12}
