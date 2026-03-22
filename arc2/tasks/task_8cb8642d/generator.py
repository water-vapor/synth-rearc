from arc2.core import *

from .helpers import make_rectangle_8cb8642d, transform_rectangle_8cb8642d


COLORS_8CB8642D = remove(ZERO, interval(ZERO, TEN, ONE))
BOARD_SHAPE_8CB8642D = (24, 24)


def _sample_dimensions_8cb8642d(
    diff_lb: float,
    diff_ub: float,
    nrectangles: Integer,
) -> IntegerTuple:
    x0 = branch(equality(nrectangles, ONE), (SIX, TEN), (SIX, NINE))
    x1 = branch(equality(nrectangles, ONE), (ZERO, FOUR), (ZERO, THREE))
    x2 = unifint(diff_lb, diff_ub, x0)
    x3 = unifint(diff_lb, diff_ub, x1)
    x4 = choice(("square", "wide", "tall"))
    if x4 == "square":
        return (x2, x2)
    if x4 == "wide":
        return (x2, x2 + x3)
    return (x2 + x3, x2)


def _expanded_bounds_8cb8642d(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> tuple[int, int, int, int]:
    x0 = top - ONE
    x1 = left - ONE
    x2 = top + height_
    x3 = left + width_
    return (x0, x1, x2, x3)


def _separated_8cb8642d(
    candidate: tuple[int, int, int, int],
    placed: tuple[tuple[int, int, int, int], ...],
) -> Boolean:
    x0, x1, x2, x3 = candidate
    for x4, x5, x6, x7 in placed:
        if not (x2 < x4 or x6 < x0 or x3 < x5 or x7 < x1):
            return F
    return T


def _place_rectangles_8cb8642d(
    dimensions: tuple[IntegerTuple, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    x0, x1 = BOARD_SHAPE_8CB8642D
    for _ in range(200):
        x2 = []
        x3 = []
        x4 = T
        for x5, x6 in dimensions:
            x7 = F
            for _ in range(200):
                x8 = randint(ZERO, x0 - x5)
                x9 = randint(ZERO, x1 - x6)
                x10 = _expanded_bounds_8cb8642d(x8, x9, x5, x6)
                if not _separated_8cb8642d(x10, tuple(x3)):
                    continue
                x2.append((x8, x9, x5, x6))
                x3.append(x10)
                x7 = T
                break
            if x7:
                continue
            x4 = F
            break
        if x4:
            return tuple(x2)
    raise RuntimeError("failed to place rectangles")


def _sample_padding_8cb8642d(
    limit: Integer,
) -> Integer:
    if limit <= ZERO:
        return ZERO
    return randint(ONE, min(FOUR, limit))


def generate_8cb8642d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((ONE, THREE))
        x1 = tuple(_sample_dimensions_8cb8642d(diff_lb, diff_ub, x0) for _ in range(x0))
        x2 = _place_rectangles_8cb8642d(x1)
        x3 = canvas(ZERO, BOARD_SHAPE_8CB8642D)
        x4 = canvas(ZERO, BOARD_SHAPE_8CB8642D)
        x5 = []
        for x6, x7, x8, x9 in x2:
            x10, x11 = sample(COLORS_8CB8642D, TWO)
            x12 = make_rectangle_8cb8642d(x6, x7, x8, x9)
            x3 = fill(x3, x10, x12)
            x13 = randint(x6 + ONE, x6 + x8 - TWO)
            x14 = randint(x7 + ONE, x7 + x9 - TWO)
            x15 = frozenset({(x13, x14)})
            x3 = fill(x3, x11, x15)
            x4 = transform_rectangle_8cb8642d(x4, x12, x10, x11)
            x5.append((x6, x7, x8, x9))
        x16 = tuple(x6 for x6, x7, x8, x9 in x5)
        x17 = tuple(x6 + x8 - ONE for x6, x7, x8, x9 in x5)
        x18 = tuple(x7 for x6, x7, x8, x9 in x5)
        x19 = tuple(x7 + x9 - ONE for x6, x7, x8, x9 in x5)
        x20 = minimum(x16)
        x21 = maximum(x17)
        x22 = minimum(x18)
        x23 = maximum(x19)
        x24, x25 = BOARD_SHAPE_8CB8642D
        x26 = _sample_padding_8cb8642d(x20)
        x27 = _sample_padding_8cb8642d(x22)
        x28 = _sample_padding_8cb8642d(x24 - ONE - x21)
        x29 = _sample_padding_8cb8642d(x25 - ONE - x23)
        x30 = subtract(x20, x26)
        x31 = subtract(x22, x27)
        x32 = add(subtract(x21, x20), add(x26, x28))
        x33 = add(subtract(x23, x22), add(x27, x29))
        x34 = crop(x3, (x30, x31), (increment(x32), increment(x33)))
        x35 = crop(x4, (x30, x31), (increment(x32), increment(x33)))
        if x34 == x35:
            continue
        x36 = colorcount(x34, ZERO)
        x37 = tuple(colorcount(x34, x38) for x38 in palette(x34) if x38 != ZERO)
        if x36 <= maximum(x37):
            continue
        return {"input": x34, "output": x35}
