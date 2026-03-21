from arc2.core import *


def _walk_profile(length: int, low: int, high: int) -> tuple[int, ...]:
    x0 = randint(low, high)
    x1 = [x0]
    for _ in range(length - ONE):
        x2 = x1[-ONE] + choice((-ONE, ZERO, ONE))
        x2 = max(low, min(high, x2))
        x1.append(x2)
    return tuple(x1)


def _extra_profile(length: int, caps: tuple[int, ...]) -> tuple[int, ...]:
    x0 = choice((ONE, ONE, TWO))
    x1 = tuple(randint(ZERO, length - ONE) for _ in range(x0))
    x2 = tuple(randint(ONE, max(TWO, length // THREE)) for _ in range(x0))
    x3 = tuple(randint(ONE, max(ONE, min(FOUR, max(caps)))) for _ in range(x0))
    x4 = []
    for x5, x6 in enumerate(caps):
        x7 = ZERO
        for x8, x9, x10 in zip(x1, x2, x3):
            x11 = max(ZERO, x10 - abs(x5 - x8) + randint(-ONE, ONE))
            x11 = min(x11, x9 + x10)
            x7 = max(x7, x11)
        x4.append(min(x6, x7))
    return tuple(x4)


def _row_from_counts(
    left_color: int,
    middle_color: int,
    right_color: int,
    left_count: int,
    middle_count: int,
    right_count: int,
) -> tuple[int, ...]:
    return (
        repeat(left_color, left_count)
        + repeat(middle_color, middle_count)
        + repeat(right_color, right_count)
    )


def generate_984d8a3e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ZERO, TEN, ONE)
    while True:
        x1 = unifint(diff_lb, diff_ub, (8, 18))
        x2 = sample(x0, THREE)
        x3, x4, x5 = x2
        x6 = unifint(diff_lb, diff_ub, (max(3, x1 // THREE), x1 - FOUR))
        x7 = max(THREE, x6 - TWO)
        x8 = min(x1 - TWO, x6 + THREE)
        x9 = _walk_profile(x1, x7, x8)
        if len(set(x9)) == ONE:
            continue
        x10 = tuple(x1 - max(x6 + ONE, x11) for x11 in x9)
        if max(x10) == ZERO:
            continue
        x11 = _extra_profile(x1, x10)
        if max(x11) == ZERO or min(x11) != ZERO:
            continue
        x12 = []
        for x13, x14 in zip(x9, x11):
            x15 = max(ZERO, x6 - x13 + ONE)
            x16 = x15 + x14
            x17 = x1 - x16 - x13
            if x17 < ZERO:
                break
            x18 = _row_from_counts(x3, x4, x5, x16, x13, x17)
            x12.append((x16, x13, x17, x18))
        if len(x12) != x1:
            continue
        x19 = tuple(x20[THREE] for x20 in x12)
        x20 = minimum(tuple(x21 + x22 - ONE for x21, x22, _, _ in x12))
        x21 = []
        for x22, x23, x24, _ in x12:
            x25 = max(ZERO, x20 - x23 + ONE)
            x26 = x22 - x25
            x27 = repeat(x3, x25) + repeat(x4, x23) + repeat(x3, x26) + repeat(x5, x24)
            x21.append(x27)
        x22 = tuple(x21)
        x23 = tuple(first(x24) for x24 in x19)
        x24 = tuple(last(x25) for x25 in x19)
        if mostcommon(x23) != x3 or mostcommon(x24) != x5:
            continue
        if sum(x25.count(x3) > ZERO for x25 in x19) <= x1 // TWO:
            continue
        if sum(x25.count(x5) > ZERO for x25 in x19) <= x1 // TWO:
            continue
        if x19 == x22:
            continue
        return {"input": x19, "output": x22}
