from arc2.core import *
from .verifier import verify_84f2aca1


FRAME_COLORS_84F2ACA1 = (TWO, THREE, FOUR, EIGHT)


def _expand_84f2aca1(
    patch: frozenset[IntegerTuple],
    radius: int,
) -> frozenset[IntegerTuple]:
    return frozenset(
        (i + di, j + dj)
        for i, j in patch
        for di in range(-radius, radius + ONE)
        for dj in range(-radius, radius + ONE)
    )


def _rect_84f2aca1(
    top: int,
    left: int,
    height_value: int,
    width_value: int,
) -> frozenset[IntegerTuple]:
    return frozenset(
        (i, j)
        for i in range(top, top + height_value)
        for j in range(left, left + width_value)
    )


def _frame_84f2aca1(
    top: int,
    left: int,
    height_value: int,
    width_value: int,
) -> tuple[frozenset[IntegerTuple], frozenset[IntegerTuple], frozenset[IntegerTuple]]:
    rect = _rect_84f2aca1(top, left, height_value, width_value)
    frame = box(rect)
    hole = delta(frame)
    return rect, frame, hole


def _hole_kinds_84f2aca1(nframes: int) -> tuple[int, ...]:
    kinds = [choice((ONE, TWO)) for _ in range(nframes)]
    if nframes > ONE:
        kinds[ZERO] = ONE
        kinds[ONE] = TWO
        shuffle(kinds)
    return tuple(kinds)


def _frame_colors_84f2aca1(nframes: int) -> tuple[int, ...]:
    if nframes == ONE:
        return (choice(FRAME_COLORS_84F2ACA1),)
    palette_size = randint(TWO, min(len(FRAME_COLORS_84F2ACA1), nframes))
    palette = sample(FRAME_COLORS_84F2ACA1, palette_size)
    colors = [choice(palette) for _ in range(nframes)]
    if len(set(colors)) == ONE and len(palette) > ONE:
        colors[-ONE] = choice(tuple(x for x in palette if x != colors[ZERO]))
    return tuple(colors)


def generate_84f2aca1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((T, F, F))
        if x0:
            x1 = unifint(diff_lb, diff_ub, (SIX, EIGHT))
            x2 = unifint(diff_lb, diff_ub, (SIX, EIGHT))
            x3 = ONE
        else:
            x1 = unifint(diff_lb, diff_ub, (11, 18))
            x2 = unifint(diff_lb, diff_ub, (11, 18))
            x3 = unifint(diff_lb, diff_ub, (TWO, min(SIX, max(TWO, (x1 * x2) // 28))))
        x4 = _hole_kinds_84f2aca1(x3)
        x5 = _frame_colors_84f2aca1(x3)
        x6 = frozenset({})
        x7 = []
        x8 = T
        for x9, x10 in zip(x4, x5):
            if x9 == ONE:
                x11, x12, x13 = THREE, THREE, FIVE
            else:
                x11, x12, x13 = choice(((THREE, FOUR, SEVEN), (FOUR, THREE, SEVEN)))
            x14 = []
            for x15 in range(x1 - x11 + ONE):
                for x16 in range(x2 - x12 + ONE):
                    x17, x18, x19 = _frame_84f2aca1(x15, x16, x11, x12)
                    x20 = _expand_84f2aca1(x17, ONE)
                    if len(intersection(x20, x6)) == ZERO:
                        x14.append((x17, x18, x19, x13))
            if len(x14) == ZERO:
                x8 = F
                break
            x21, x22, x23, x24 = choice(x14)
            x7.append({"color": x10, "rect": x21, "frame": x22, "hole": x23, "fill": x24})
            x6 = combine(x6, _expand_84f2aca1(x21, ONE))
        if not x8:
            continue
        x25 = canvas(ZERO, (x1, x2))
        x26 = canvas(ZERO, (x1, x2))
        for x27 in x7:
            x25 = fill(x25, x27["color"], x27["frame"])
            x26 = fill(x26, x27["color"], x27["frame"])
            x26 = fill(x26, x27["fill"], x27["hole"])
        if x25 == x26:
            continue
        if mostcolor(x25) != ZERO or mostcolor(x26) != ZERO:
            continue
        if verify_84f2aca1(x25) != x26:
            continue
        return {"input": x25, "output": x26}
