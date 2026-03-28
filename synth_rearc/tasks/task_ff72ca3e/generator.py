from synth_rearc.core import *

from .helpers import chebyshev_ff72ca3e, clip_patch_ff72ca3e, square_patch_ff72ca3e
from .verifier import verify_ff72ca3e


def _safe_marker_ff72ca3e(
    loc: IntegerTuple,
    centers: tuple[IntegerTuple, ...],
    radii: tuple[Integer, ...],
) -> Boolean:
    for x0, x1 in zip(centers, radii):
        if chebyshev_ff72ca3e(loc, x0) < add(x1, ONE):
            return False
    return True


def generate_ff72ca3e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (NINE, 30))
        x1 = unifint(diff_lb, diff_ub, (EIGHT, 20))
        if max(x0, x1) > min(x0, x1) + min(x0, x1) // TWO + TWO:
            continue
        x2 = astuple(x0, x1)
        x3 = product(interval(ZERO, x0, ONE), interval(ZERO, x1, ONE))
        x4 = min(FOUR, max(ONE, x0 * x1 // 150 + ONE))
        x5 = unifint(diff_lb, diff_ub, (ONE, x4))
        x6 = max(ONE, min(SIX, (min(x0, x1) - ONE) // TWO))
        x7 = tuple()
        x8 = tuple()
        x9 = tuple()
        x10 = frozenset()
        x11 = ZERO
        while len(x7) < x5 and x11 < 400:
            x11 = increment(x11)
            x12 = unifint(diff_lb, diff_ub, (ONE, x6))
            x13 = add(add(x12, x12), ONE)
            if x13 > x0 or x13 > x1:
                continue
            x14 = randint(ZERO, subtract(x0, x13))
            x15 = randint(ZERO, subtract(x1, x13))
            x16 = astuple(add(x14, x12), add(x15, x12))
            x17 = square_patch_ff72ca3e(x16, x12)
            x18 = clip_patch_ff72ca3e(outbox(x17), x2)
            x19 = combine(x17, x18)
            if len(x18) == ZERO:
                continue
            if len(intersection(x19, x10)) > ZERO:
                continue
            x7 = x7 + (x16,)
            x8 = x8 + (x12,)
            x9 = x9 + (x17,)
            x10 = combine(x10, x19)
        if len(x7) != x5:
            continue
        x20 = frozenset()
        for x21, x22, x23 in zip(x7, x8, x9):
            x24 = clip_patch_ff72ca3e(outbox(x23), x2)
            x25 = tuple(
                x26 for x26 in x24
                if x26 not in x20 and _safe_marker_ff72ca3e(x26, x7, x8)
            )
            if len(x25) == ZERO:
                x20 = frozenset()
                break
            x20 = insert(choice(x25), x20)
        if len(x20) != x5:
            continue
        x27 = difference(x3, merge((frozenset(x7), merge(x9), x20)))
        x28 = tuple(x29 for x29 in x27 if _safe_marker_ff72ca3e(x29, x7, x8))
        x30 = min(len(x28), unifint(diff_lb, diff_ub, (ZERO, min(NINE, add(multiply(x5, THREE), TWO)))))
        x31 = frozenset(sample(x28, x30)) if x30 > ZERO else frozenset()
        x32 = combine(x20, x31)
        x33 = canvas(ZERO, x2)
        x34 = fill(x33, FOUR, frozenset(x7))
        x35 = fill(x34, FIVE, x32)
        x36 = canvas(ZERO, x2)
        for x37 in x9:
            x36 = fill(x36, TWO, x37)
        x38 = fill(x36, FIVE, x32)
        x39 = fill(x38, FOUR, frozenset(x7))
        if x35 == x39:
            continue
        if verify_ff72ca3e(x35) != x39:
            continue
        return {"input": x35, "output": x39}
