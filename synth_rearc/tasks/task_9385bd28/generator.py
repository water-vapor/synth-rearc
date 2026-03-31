from __future__ import annotations

from synth_rearc.core import *

from .helpers import place_corner_shape_9385bd28
from .helpers import rectangle_indices_9385bd28


def _free_rectangle_9385bd28(
    dims: IntegerTuple,
    occupied: set[IntegerTuple],
    min_dims: IntegerTuple,
    max_dims: IntegerTuple,
    *,
    inside: tuple[Integer, Integer, Integer, Integer] | None = None,
) -> tuple[Integer, Integer, Integer, Integer] | None:
    x0, x1 = dims
    x2, x3 = min_dims
    x4, x5 = max_dims
    for _ in range(400):
        x6 = randint(x2, x4)
        x7 = randint(x3, x5)
        if inside is None:
            if subtract(x1, x7) < FIVE:
                continue
            x8 = randint(ZERO, subtract(x0, x6))
            x9 = randint(FIVE, subtract(x1, x7))
        else:
            x10, x11, x12, x13 = inside
            if either(x12 - x10 + ONE < x6, x13 - x11 + ONE < x7):
                continue
            x8 = randint(x10, subtract(add(x12, ONE), x6))
            x9 = randint(x11, subtract(add(x13, ONE), x7))
        x14 = rectangle_indices_9385bd28((x8, x9), (x6, x7))
        if x14 & occupied:
            continue
        return (x8, x9, subtract(add(x8, x6), ONE), subtract(add(x9, x7), ONE))
    return None


def _add_pair_9385bd28(
    grid: Grid,
    rect: tuple[Integer, Integer, Integer, Integer],
    color_value: Integer,
    orientation: str,
) -> tuple[Grid, tuple[Indices, ...]]:
    x0, x1, x2, x3 = rect
    if orientation == "main":
        x4 = toindices(place_corner_shape_9385bd28((x0, x1), "tl", color_value))
        x5 = toindices(place_corner_shape_9385bd28((subtract(x2, ONE), subtract(x3, ONE)), "br", color_value))
        x6 = fill(fill(grid, color_value, x4), color_value, x5)
        return x6, (x4, x5)
    x4 = toindices(place_corner_shape_9385bd28((x0, subtract(x3, ONE)), "tr", color_value))
    x5 = toindices(place_corner_shape_9385bd28((subtract(x2, ONE), x1), "bl", color_value))
    x6 = fill(fill(grid, color_value, x4), color_value, x5)
    return x6, (x4, x5)


def _legend_rows_9385bd28(
    sources: tuple[Integer, ...],
    mapping: dict[Integer, Integer | None],
    *,
    include_zero_blank: Boolean,
) -> tuple[tuple[Integer, Integer | None], ...]:
    x0 = []
    for x1 in sources:
        x2 = mapping.get(x1)
        if x2 == ZERO and include_zero_blank:
            x0.append((x1, ZERO))
        else:
            x0.append((x1, x2))
    return tuple(x0)


def _place_legend_9385bd28(
    grid: Grid,
    origin: IntegerTuple,
    rows: tuple[tuple[Integer, Integer | None], ...],
) -> Grid:
    x0 = grid
    x1, x2 = origin
    for x3, (x4, x5) in enumerate(rows):
        x6 = add(x1, x3)
        x0 = fill(x0, x4, initset((x6, x2)))
        if x5 is not None:
            x0 = fill(x0, x5, initset((x6, add(x2, ONE))))
    return x0


def _render_output_9385bd28(
    grid: Grid,
    specs: tuple[tuple[Integer, tuple[Integer, Integer, Integer, Integer], Integer | None, str, tuple[Indices, ...]], ...],
) -> Grid:
    x0 = grid
    x1 = tuple(sorted(specs, key=lambda item: ((item[1][2] - item[1][0] + ONE) * (item[1][3] - item[1][1] + ONE), item[0])))
    x2 = tuple(
        (
            x3,
            rectangle_indices_9385bd28(
                (x4[0], x4[1]),
                (subtract(x4[2], x4[0]) + ONE, subtract(x4[3], x4[1]) + ONE),
            ),
            x5,
            x6,
            x7,
        )
        for x3, x4, x5, x6, x7 in x1
    )
    x3 = mostcolor(grid)
    for _, _, x4, _, x5 in x2:
        if x4 == ZERO:
            x6 = frozenset(index for x7 in x5 for index in x7)
            x0 = fill(x0, x3, x6)
    for x4, x5, x6, x7, x8 in x2:
        if either(x6 is None, x6 == ZERO):
            continue
        if either(x6 == x4, x7 == "square"):
            x0 = fill(x0, x6, x5)
        else:
            x9 = tuple(
                intersection(x5, x10)
                for x11, x10, x12, _, x13 in x2
                if both(
                    x11 != x4,
                    both(
                        x12 is None,
                        any(len(intersection(x5, x14)) > ZERO for x14 in x13),
                    ),
                )
            )
            x10 = difference(x5, merge(x9)) if len(x9) > ZERO else x5
            x0 = underfill(x0, x6, x10)
    return x0


def generate_9385bd28(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = randint(10, 20)
        x1 = randint(10, 20)
        x2 = choice((ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE))
        x3 = [x4 for x4 in range(TEN) if both(x4 != x2, x4 != ZERO)]
        shuffle(x3)
        x4 = choice((THREE, FOUR, FOUR, FIVE))
        x5 = tuple(x3[:x4])
        x6 = list(x3[x4:])
        shuffle(x6)
        x7 = canvas(x2, (x0, x1))
        x8: set[IntegerTuple] = set()
        x9: list[tuple[Integer, tuple[Integer, Integer, Integer, Integer], Integer | None, str, tuple[Indices, ...]]] = []
        x10: dict[Integer, Integer | None] = {}
        x11 = max(TWO, subtract(x0, choice((TWO, THREE, FOUR, FIVE, SIX))))
        x12 = choice((ZERO, ONE, TWO))
        x13 = []
        for x14 in x5:
            x15 = choice(("pair", "pair", "pair", "square"))
            x16 = x15 == "square"
            if x16:
                x17 = _free_rectangle_9385bd28((x0, x1), x8, (TWO, TWO), (TWO, TWO))
                if x17 is None:
                    x13 = []
                    break
                x18 = rectangle_indices_9385bd28((x17[0], x17[1]), (TWO, TWO))
                x7 = fill(x7, x14, x18)
                x8 |= set(x18)
                x19 = (x18,)
            else:
                x19 = choice(("main", "cross"))
                if both(len(x13) > ZERO, choice((T, F, F))):
                    x20 = choice(x13)
                    x21 = max(3, subtract(x20[2], x20[0]))
                    x22 = max(3, subtract(x20[3], x20[1]))
                    x17 = _free_rectangle_9385bd28(
                        (x0, x1),
                        x8,
                        (THREE, THREE),
                        (min(8, x21), min(8, x22)),
                        inside=x20,
                    )
                else:
                    x17 = _free_rectangle_9385bd28(
                        (x0, x1),
                        x8,
                        (THREE, THREE),
                        (min(9, subtract(x0, ONE)), min(9, subtract(x1, FOUR))),
                    )
                if x17 is None:
                    x13 = []
                    break
                x7, x23 = _add_pair_9385bd28(x7, x17, x14, x19)
                x8 |= set(index for x24 in x23 for index in x24)
                x19 = x23
            x24 = None
            x25 = choice(("mapped", "mapped", "self", "blank"))
            if x25 == "self":
                x24 = x14
            elif x25 == "mapped":
                if len(x6) == ZERO:
                    x13 = []
                    break
                x24 = x6.pop()
            elif both(x2 != ZERO, choice((T, F, F))):
                x24 = ZERO
            x10[x14] = x24
            x9.append((x14, x17, x24, "square" if x16 else "pair", x19))
            x13.append(x17)
        if len(x13) != len(x5):
            continue
        x25 = tuple(sorted(x5, key=lambda value: (x10[value] is None, value)))
        x26 = []
        for x28 in x25:
            x29 = x10[x28]
            x26.append((x28, x29))
        x30 = tuple(x26)
        if add(x11, len(x30)) > x0:
            x11 = subtract(x0, len(x30))
        x31 = _place_legend_9385bd28(x7, (x11, x12), x30)
        x32 = _render_output_9385bd28(x31, tuple(x9))
        if x31 == x32:
            continue
        return {"input": x31, "output": x32}
