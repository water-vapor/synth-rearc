from arc2.core import *


WORK_H_7BB29440 = 30
WORK_W_7BB29440 = 30
PAD_CHOICES_7BB29440 = (ZERO, ONE, ONE, TWO, TWO, THREE, FOUR)
MARKER_COLORS_7BB29440 = (FOUR, FOUR, SIX, SIX)


def _paint_rectangle_7bb29440(
    grid: Grid,
    top: Integer,
    left: Integer,
    height0: Integer,
    width0: Integer,
    markers: tuple[tuple[Integer, IntegerTuple], ...],
) -> Grid:
    x0 = interval(top, add(top, height0), ONE)
    x1 = interval(left, add(left, width0), ONE)
    x2 = fill(grid, ONE, product(x0, x1))
    for x3, x4 in markers:
        x5 = (add(top, x4[0]), add(left, x4[1]))
        x2 = fill(x2, x3, initset(x5))
    return x2


def _sample_markers_7bb29440(
    height0: Integer,
    width0: Integer,
    nmarkers: Integer,
) -> tuple[tuple[Integer, IntegerTuple], ...]:
    x0 = [(i, j) for i in range(height0) for j in range(width0)]
    x1 = sample(x0, nmarkers)
    x2 = tuple(
        sorted(
            ((choice(MARKER_COLORS_7BB29440), x3) for x3 in x1),
            key=lambda x4: (x4[1][0], x4[1][1], x4[0]),
        )
    )
    return x2


def _separated_7bb29440(
    candidate: tuple[Integer, Integer, Integer, Integer],
    placed: tuple[Integer, Integer, Integer, Integer],
) -> Boolean:
    x0, x1, x2, x3 = candidate
    x4, x5, x6, x7 = placed
    return (
        add(x0, x2) < x4
        or add(x4, x6) < x0
        or add(x1, x3) < x5
        or add(x5, x7) < x1
    )


def _place_rectangles_7bb29440(
    specs: tuple[tuple[Integer, Integer, tuple[tuple[Integer, IntegerTuple], ...]], ...],
) -> tuple[tuple[Integer, Integer, Integer, Integer, tuple[tuple[Integer, IntegerTuple], ...]], ...] | None:
    x0 = list(range(len(specs)))
    shuffle(x0)
    x0.sort(key=lambda x1: multiply(specs[x1][0], specs[x1][1]), reverse=True)
    x1 = [None] * len(specs)
    x2: list[tuple[Integer, Integer, Integer, Integer]] = []
    x3 = None
    for x4 in x0:
        x5, x6, x7 = specs[x4]
        x8 = False
        for _ in range(400):
            if x3 is None:
                x9 = randint(FOUR, subtract(24, x5))
                x10 = randint(FOUR, subtract(24, x6))
            else:
                x9 = max(ZERO, subtract(x3[0], add(x5, THREE)))
                x10 = min(subtract(WORK_H_7BB29440, x5), add(x3[2], THREE))
                x11 = max(ZERO, subtract(x3[1], add(x6, THREE)))
                x12 = min(subtract(WORK_W_7BB29440, x6), add(x3[3], THREE))
                x9 = randint(x9, x10)
                x10 = randint(x11, x12)
            x11 = (x9, x10, x5, x6)
            if all(_separated_7bb29440(x11, x12) for x12 in x2):
                x1[x4] = (x9, x10, x5, x6, x7)
                x2.append(x11)
                if x3 is None:
                    x3 = (x9, x10, add(x9, x5), add(x10, x6))
                else:
                    x3 = (
                        min(x3[0], x9),
                        min(x3[1], x10),
                        max(x3[2], add(x9, x5)),
                        max(x3[3], add(x10, x6)),
                    )
                x8 = True
                break
        if not x8:
            return None
    return tuple(x1)


def _target_marker_count_7bb29440(
    area: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Integer:
    x0 = ONE if area > NINE else TWO
    x1 = min(THREE, subtract(area, ONE))
    return unifint(diff_lb, diff_ub, (x0, x1))


def _distractor_spec_7bb29440(
    target_markers: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Integer, tuple[tuple[Integer, IntegerTuple], ...]] | None:
    x0 = unifint(diff_lb, diff_ub, (THREE, TEN))
    x1 = unifint(diff_lb, diff_ub, (THREE, TEN))
    x2 = multiply(x0, x1)
    x3 = add(target_markers, ONE)
    x4 = min(SIX, subtract(x2, ONE), max(x3, add(divide(x2, THREE), ONE)))
    if x3 > x4:
        return None
    x5 = unifint(diff_lb, diff_ub, (x3, x4))
    x6 = _sample_markers_7bb29440(x0, x1, x5)
    return (x0, x1, x6)


def generate_7bb29440(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    from .verifier import verify_7bb29440

    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, SIX))
        x1 = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        x2 = choice((FIVE, FIVE, FIVE, SIX))
        x3 = multiply(x1, x2)
        x4 = _target_marker_count_7bb29440(x3, diff_lb, diff_ub)
        x5 = _sample_markers_7bb29440(x1, x2, x4)
        x6: list[tuple[Integer, Integer, tuple[tuple[Integer, IntegerTuple], ...]]] = [(x1, x2, x5)]
        while len(x6) < x0:
            x7 = _distractor_spec_7bb29440(x4, diff_lb, diff_ub)
            if x7 is None:
                continue
            x6.append(x7)
        x8 = _place_rectangles_7bb29440(tuple(x6))
        if x8 is None:
            continue

        x9 = min(x10 for x10, _, _, _, _ in x8)
        x10 = min(x11 for _, x11, _, _, _ in x8)
        x11 = max(add(x12, x14) for x12, _, x14, _, _ in x8)
        x12 = max(add(x13, x15) for _, x13, _, x15, _ in x8)
        x13 = choice(PAD_CHOICES_7BB29440)
        x14 = choice(PAD_CHOICES_7BB29440)
        x15 = choice(PAD_CHOICES_7BB29440)
        x16 = choice(PAD_CHOICES_7BB29440)
        x17 = add(subtract(x11, x9), add(x13, x14))
        x18 = add(subtract(x12, x10), add(x15, x16))
        x19 = sum(multiply(x20, x21) for _, _, x20, x21, _ in x8)
        x20 = sum(len(x21) for _, _, _, _, x21 in x8)
        x21 = subtract(x19, x20)
        while x17 < TEN:
            x14 = increment(x14)
            x17 = increment(x17)
        while x18 < TEN:
            x16 = increment(x16)
            x18 = increment(x18)
        while subtract(multiply(x17, x18), x19) <= x21:
            if both(x17 < WORK_H_7BB29440, x17 <= x18):
                x14 = increment(x14)
                x17 = increment(x17)
            elif x18 < WORK_W_7BB29440:
                x16 = increment(x16)
                x18 = increment(x18)
            elif x17 < WORK_H_7BB29440:
                x14 = increment(x14)
                x17 = increment(x17)
            else:
                break
        if either(greater(x17, 24), greater(x18, 25)):
            continue
        if subtract(multiply(x17, x18), x19) <= x21:
            continue

        x22 = canvas(ZERO, (x17, x18))
        x23 = None
        for x24, x25 in enumerate(x8):
            x26, x27, x28, x29, x30 = x25
            x31 = add(subtract(x26, x9), x13)
            x32 = add(subtract(x27, x10), x15)
            x22 = _paint_rectangle_7bb29440(x22, x31, x32, x28, x29, x30)
            if x24 == ZERO:
                x23 = crop(x22, (x31, x32), (x28, x29))

        if x23 is None:
            continue
        if mostcolor(x22) != ZERO:
            continue
        if verify_7bb29440(x22) != x23:
            continue
        return {"input": x22, "output": x23}
