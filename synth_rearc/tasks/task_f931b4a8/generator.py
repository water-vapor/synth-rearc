from __future__ import annotations

from synth_rearc.core import *


QUADRANT_SIZES_F931B4A8 = (TWO, FOUR, FOUR, SIX, EIGHT)
MAX_OUTPUT_DIM_F931B4A8 = 24


def _hconcat_many_f931b4a8(
    grids: tuple[Grid, ...],
) -> Grid:
    x0 = first(grids)
    for x1 in grids[ONE:]:
        x0 = hconcat(x0, x1)
    return x0


def _vconcat_many_f931b4a8(
    grids: tuple[Grid, ...],
) -> Grid:
    x0 = first(grids)
    for x1 in grids[ONE:]:
        x0 = vconcat(x0, x1)
    return x0


def _substitute_template_f931b4a8(
    control: Grid,
    template: Grid,
) -> Grid:
    x0 = tuple(tuple(replace(template, ZERO, x1) for x1 in x2) for x2 in control)
    x3 = tuple(_hconcat_many_f931b4a8(x4) for x4 in x0)
    return _vconcat_many_f931b4a8(x3)


def _random_count_quadrant_f931b4a8(
    side: Integer,
    count: Integer,
    palette0: tuple[Integer, ...],
) -> Grid:
    x0 = [[ZERO for _ in range(side)] for _ in range(side)]
    x1 = choice(("prefix", "rowbands", "scatter"))
    if x1 == "scatter":
        x2 = sample([(i, j) for i in range(side) for j in range(side)], count)
        for i, j in x2:
            x0[i][j] = choice(palette0)
    else:
        x3 = [choice(palette0) for _ in range(side)]
        x4 = [(i, j) for i in range(side) for j in range(side)]
        for i, j in x4[:count]:
            x0[i][j] = x3[i] if x1 == "rowbands" else choice(palette0)
        x5 = tuple(tuple(x6) for x6 in x0)
        x6 = choice((identity, rot90, rot180, rot270, hmirror, vmirror))
        return x6(x5)
    return tuple(tuple(x7) for x7 in x0)


def _control_grid_f931b4a8(
    side: Integer,
    palette0: tuple[Integer, ...],
) -> Grid:
    x0 = choice(("solid", "solid", "rows", "full"))
    if x0 == "solid":
        return canvas(choice(palette0), (side, side))
    if x0 == "rows":
        x1 = tuple(tuple(choice(palette0) for _ in range(side)) for _ in range(side))
        x2 = tuple(tuple(x3[ZERO] for _ in range(side)) for x3 in x1)
        if numcolors(x2) > ONE:
            return x2
    x4 = tuple(tuple(choice(palette0) for _ in range(side)) for _ in range(side))
    if numcolors(x4) == ONE:
        x5 = (
            other(palette0, x4[ZERO][ZERO])
            if len(palette0) > ONE
            else other(remove(ZERO, interval(ZERO, TEN, ONE)), x4[ZERO][ZERO])
        )
        x6 = [list(x7) for x7 in x4]
        x6[-1][-1] = x5
        return tuple(tuple(x8) for x8 in x6)
    return x4


def _mixed_template_f931b4a8(
    side: Integer,
    palette0: tuple[Integer, ...],
) -> Grid:
    x0 = choice(("checker", "frame", "stripes", "diagonal", "scatter"))
    if x0 == "checker":
        x1 = choice(palette0)
        x2 = choice((ZERO, choice(palette0)))
        return tuple(
            tuple(x1 if (i + j) % TWO == ZERO else x2 for j in range(side))
            for i in range(side)
        )
    if x0 == "frame":
        x3 = choice(palette0)
        x4 = canvas(ZERO, (side, side))
        x5 = box(asindices(x4))
        x6 = fill(x4, x3, x5)
        if side > THREE and choice((T, F)):
            x7 = other(palette0, x3) if len(palette0) > ONE else x3
            x8 = inbox(asindices(x4))
            x6 = fill(x6, x7, x8)
            x6 = replace(x6, x7, ZERO)
        return x6
    if x0 == "stripes":
        x9 = [choice(palette0) if choice((T, F)) else ZERO for _ in range(side)]
        if all(x10 == ZERO for x10 in x9):
            x9[randint(ZERO, side - ONE)] = choice(palette0)
        if all(x10 != ZERO for x10 in x9):
            x9[randint(ZERO, side - ONE)] = ZERO
        return tuple(tuple(x9[i] for _ in range(side)) for i in range(side))
    if x0 == "diagonal":
        x11 = [[ZERO for _ in range(side)] for _ in range(side)]
        x12 = choice(palette0)
        for x13 in range(side):
            x11[x13][x13] = x12
        if choice((T, F)):
            x14 = choice(palette0)
            for x15 in range(side):
                x11[x15][side - x15 - ONE] = x14
        return tuple(tuple(x16) for x16 in x11)
    x17 = [[ZERO for _ in range(side)] for _ in range(side)]
    x18 = randint(ONE, side * side - ONE)
    x19 = sample([(i, j) for i in range(side) for j in range(side)], x18)
    for i, j in x19:
        x17[i][j] = choice(palette0)
    return tuple(tuple(x20) for x20 in x17)


def generate_f931b4a8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x1 = choice(QUADRANT_SIZES_F931B4A8)
        x2 = tuple(sample(x0, randint(TWO, min(FIVE, len(x0)))))
        x3 = tuple(sample(x0, randint(ONE, min(FOUR, len(x0)))))
        x4 = tuple(sample(x0, randint(ONE, min(FOUR, len(x0)))))
        x5 = choice((F, F, F, T))
        x6 = _control_grid_f931b4a8(x1, x3)
        if x5:
            x7 = canvas(ZERO, (x1, x1))
            x8 = x6
            x9 = unifint(diff_lb, diff_ub, (TWO, x1))
            x10 = unifint(diff_lb, diff_ub, (TWO, x1))
        else:
            x7 = _mixed_template_f931b4a8(x1, x4)
            x11 = palette(x7)
            x12 = remove(ZERO, x11)
            if not both(contained(ZERO, x11), greater(size(x12), ZERO)):
                continue
            x8 = _substitute_template_f931b4a8(x6, x7)
            x13 = min(MAX_OUTPUT_DIM_F931B4A8, height(x8))
            x14 = min(MAX_OUTPUT_DIM_F931B4A8, width(x8))
            x9 = unifint(diff_lb, diff_ub, (TWO, x13))
            x10 = unifint(diff_lb, diff_ub, (TWO, x14))
        x13 = _random_count_quadrant_f931b4a8(x1, x9, x2)
        x14 = _random_count_quadrant_f931b4a8(x1, x10, x2)
        x15 = hconcat(x13, x14)
        x16 = hconcat(x6, x7)
        x17 = vconcat(x15, x16)
        x18 = crop(x8, ORIGIN, (x9, x10))
        if x17 == x18:
            continue
        if numcolors(x18) == ONE:
            continue
        return {"input": x17, "output": x18}
