from synth_rearc.core import *


def _make_profile_bf32578f(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, tuple[int, ...]]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (2, 7))
        x1 = randint(ZERO, x0 - 1)
        x2 = [x1]
        x3 = unifint(diff_lb, diff_ub, (0, 3))
        for _ in range(x3):
            x4 = x2[-1]
            if x4 == ZERO:
                break
            x5 = randint(ONE, min(TWO, x4))
            x2.append(x4 - x5)
        x6 = unifint(diff_lb, diff_ub, (1, 5))
        x7 = tuple(x2) + repeat(x2[-1], x6 - 1) + tuple(reversed(x2[:-1]))
        if len(x7) < 5:
            continue
        if minimum(x7[1:-1]) == x0 - 1:
            continue
        return x0, x7


def _filled_patch_bf32578f(
    top: Integer,
    left: Integer,
    axis: Integer,
    profile: tuple[int, ...],
) -> Indices:
    x0 = frozenset()
    for x1, x2 in enumerate(profile):
        x3 = top + x1
        x4 = left + x2
        x5 = left + subtract(subtract(multiply(TWO, axis), x2), ONE)
        x6 = connect((x3, x4), (x3, x5))
        x0 = combine(x0, x6)
    return x0


def _outline_patch_bf32578f(
    patch: Indices,
) -> Indices:
    x0 = set()
    for x1 in patch:
        if any(x2 not in patch for x2 in dneighbors(x1)):
            x0.add(x1)
    return frozenset(x0)


def generate_bf32578f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1 = _make_profile_bf32578f(diff_lb, diff_ub)
        x2 = len(x1)
        x3 = multiply(TWO, x0)
        x4 = x2 + unifint(diff_lb, diff_ub, (0, 8))
        x5 = x3 + unifint(diff_lb, diff_ub, (0, 8))
        x6 = randint(ZERO, x4 - x2)
        x7 = randint(ZERO, x5 - x3)
        x8 = choice(interval(ONE, TEN, ONE))
        x9 = _filled_patch_bf32578f(x6, x7, x0, x1)
        x10 = _outline_patch_bf32578f(x9)
        x11 = sfilter(x10, lambda x12: x12[1] < x7 + x0)
        x12 = difference(x9, x10)
        if len(x11) == ZERO or len(x12) == ZERO:
            continue
        gi = fill(canvas(ZERO, (x4, x5)), x8, x11)
        go = fill(canvas(ZERO, (x4, x5)), x8, x12)
        if gi == go:
            continue
        return {"input": gi, "output": go}
