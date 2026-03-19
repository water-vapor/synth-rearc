from arc2.core import *


def _make_component_e872b94a(
    target_h: Integer,
    target_w: Integer,
) -> Indices:
    for _ in range(200):
        x0 = randint(ZERO, target_w - ONE)
        x1 = [x0]
        for _ in range(1, target_h):
            x2 = [x0]
            if x0 > ZERO:
                x2.extend((x0 - ONE, x0 - ONE))
            if x0 < target_w - ONE:
                x2.extend((x0 + ONE, x0 + ONE))
            x0 = choice(x2)
            x1.append(x0)
        x3 = {(ZERO, x1[ZERO])}
        for x4 in range(1, target_h):
            x5 = x1[x4 - ONE]
            x6 = x1[x4]
            if x6 == x5:
                x3.add((x4, x6))
            elif randint(ZERO, ONE) == ZERO:
                x3 |= {(x4, x5), (x4, x6)}
            else:
                x3 |= {(x4 - ONE, x6), (x4, x6)}
        x7 = sample(range(target_h), randint(ZERO, min(2, target_h)))
        for x8 in x7:
            x9 = sorted(j for i, j in x3 if i == x8)
            x10 = min(x9)
            x11 = max(x9)
            x12 = []
            if x10 > ZERO:
                x12.append(NEG_ONE)
            if x11 < target_w - ONE:
                x12.append(ONE)
            if len(x12) == ZERO:
                continue
            x13 = choice(x12)
            x14 = x10 if x13 == NEG_ONE else target_w - ONE - x11
            x14 = min(x14, 2)
            if x14 <= ZERO:
                continue
            x15 = randint(ONE, x14)
            if x13 == NEG_ONE:
                x16 = {(x8, x10 - k) for k in range(ONE, x15 + ONE)}
            else:
                x16 = {(x8, x11 + k) for k in range(ONE, x15 + ONE)}
            x3 |= x16
        x17 = frozenset(x3)
        if randint(ZERO, ONE) == ONE:
            x17 = hmirror(x17)
        if randint(ZERO, ONE) == ONE:
            x17 = vmirror(x17)
        x17 = normalize(x17)
        if width(x17) < min(2, target_w):
            continue
        if size(x17) > target_h + target_w + 4:
            continue
        return x17
    raise RuntimeError("failed to build e872b94a component")


def generate_e872b94a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x1 = []
        x2 = []
        x3 = []
        x4 = branch(greater(x0, TWO), FOUR, FIVE)
        for _ in range(x0):
            x5 = unifint(diff_lb, diff_ub, (THREE, 12))
            x6 = unifint(diff_lb, diff_ub, (TWO, x4))
            x7 = _make_component_e872b94a(x5, x6)
            x1.append(x7)
            x2.append(height(x7))
            x3.append(width(x7))
        x8 = max(x2) + unifint(diff_lb, diff_ub, (ZERO, TWO))
        x9 = []
        for x10 in x2:
            x11 = x8 - x10
            if x11 == ZERO:
                x9.append(ZERO)
            else:
                x9.append(choice((ZERO, x11, randint(ZERO, x11))))
        x12 = unifint(diff_lb, diff_ub, (ZERO, ONE))
        x13 = unifint(diff_lb, diff_ub, (ZERO, TWO))
        x14 = [unifint(diff_lb, diff_ub, (ONE, TWO)) for _ in range(max(ZERO, x0 - ONE))]
        x15 = x12 + sum(x3) + x13 + sum(x14)
        gi = canvas(ZERO, (x8, x15))
        x16 = x12
        for x17, x18 in enumerate(x1):
            gi = fill(gi, FIVE, shift(x18, (x9[x17], x16)))
            x16 += x3[x17]
            if x17 < len(x14):
                x16 += x14[x17]
        x19 = objects(gi, T, T, F)
        x20 = colorfilter(x19, FIVE)
        if mostcolor(gi) != ZERO or size(x20) != x0:
            continue
        go = canvas(ZERO, astuple(increment(x0), ONE))
        return {"input": gi, "output": go}
