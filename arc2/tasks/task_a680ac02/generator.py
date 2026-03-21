from arc2.core import *


FOUR_BY_FOUR_A680AC02 = (FOUR, FOUR)
FRAME_PATCH_A680AC02 = box(asindices(canvas(ZERO, FOUR_BY_FOUR_A680AC02)))
BLOCK_PATCH_A680AC02 = asindices(canvas(ZERO, FOUR_BY_FOUR_A680AC02))
COLORS_A680AC02 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _frame_grid_a680ac02(value: Integer) -> Grid:
    return fill(canvas(ZERO, FOUR_BY_FOUR_A680AC02), value, FRAME_PATCH_A680AC02)


def _shape_object_a680ac02(
    value: Integer,
    patch: Indices,
    location: IntegerTuple,
) -> Object:
    return shift(recolor(value, patch), location)


def _separated_a680ac02(
    a: IntegerTuple,
    b: IntegerTuple,
) -> Boolean:
    ai, aj = a
    bi, bj = b
    return ai + FIVE <= bi or bi + FIVE <= ai or aj + FIVE <= bj or bj + FIVE <= aj


def _sample_hollow_locs_a680ac02(
    vertical: Boolean,
    count: Integer,
) -> tuple[IntegerTuple, ...]:
    while True:
        locs = []
        if vertical:
            row = randint(ZERO, TWO)
            col = randint(ZERO, THREE)
            for _ in range(count):
                locs.append((row + randint(ZERO, ONE), col + randint(ZERO, TWO)))
                row = locs[-ONE][ZERO] + randint(FIVE, EIGHT)
        else:
            row = randint(ZERO, THREE)
            col = randint(ZERO, TWO)
            for _ in range(count):
                locs.append((row + randint(ZERO, TWO), col + randint(ZERO, ONE)))
                col = locs[-ONE][ONE] + randint(FIVE, EIGHT)
        x0 = tuple(i for i, _ in locs)
        x1 = tuple(j for _, j in locs)
        x2 = maximum(x0) - minimum(x0) + FOUR
        x3 = maximum(x1) - minimum(x1) + FOUR
        if vertical == greater(x2, x3):
            return tuple(locs)


def _sample_solid_locs_a680ac02(
    count: Integer,
    occupied: tuple[IntegerTuple, ...],
) -> tuple[IntegerTuple, ...]:
    locs = []
    attempts = ZERO
    while len(locs) < count and attempts < 300:
        attempts += ONE
        candidate = (randint(ZERO, 18), randint(ZERO, 18))
        x0 = tuple(occupied) + tuple(locs)
        if all(_separated_a680ac02(candidate, other) for other in x0):
            locs.append(candidate)
    return tuple(locs)


def _fit_locs_a680ac02(
    locs: tuple[IntegerTuple, ...],
) -> tuple[tuple[IntegerTuple, ...], Integer, Integer]:
    x0 = tuple(i for i, _ in locs)
    x1 = tuple(j for _, j in locs)
    x2 = minimum(x0)
    x3 = maximum(x0)
    x4 = minimum(x1)
    x5 = maximum(x1)
    x6 = x3 - x2 + FOUR
    x7 = x5 - x4 + FOUR
    x8 = 30 - x6
    x9 = 30 - x7
    x10 = randint(branch(greater(x8, ZERO), ONE, ZERO), min(SIX, x8))
    x11 = randint(branch(greater(x9, ZERO), ONE, ZERO), min(SIX, x9))
    x12 = randint(ZERO, min(SIX, x8 - x10))
    x13 = randint(ZERO, min(SIX, x9 - x11))
    x14 = subtract((x10, x11), (x2, x4))
    x15 = tuple(add(loc, x14) for loc in locs)
    x16 = x6 + x10 + x12
    x17 = x7 + x11 + x13
    return x15, x16, x17


def _pack_grids_a680ac02(
    grids: tuple[Grid, ...],
    vertical: Boolean,
) -> Grid:
    result = grids[ZERO]
    concat = vconcat if vertical else hconcat
    for grid in grids[ONE:]:
        result = concat(result, grid)
    return result


def generate_a680ac02(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        vertical = choice((T, F))
        nhollows = unifint(diff_lb, diff_ub, (TWO, THREE))
        nsolids = unifint(diff_lb, diff_ub, (TWO, THREE))
        hollow_locs = _sample_hollow_locs_a680ac02(vertical, nhollows)
        solid_locs = _sample_solid_locs_a680ac02(nsolids, hollow_locs)
        if len(solid_locs) != nsolids:
            continue
        x0 = hollow_locs + solid_locs
        x1, h, w = _fit_locs_a680ac02(x0)
        hollow_locs = x1[:nhollows]
        solid_locs = x1[nhollows:]
        colors = sample(COLORS_A680AC02, nhollows + nsolids)
        hollow_colors = tuple(colors[:nhollows])
        solid_colors = tuple(colors[nhollows:])
        gi = canvas(ZERO, (h, w))
        objs = [
            _shape_object_a680ac02(value, FRAME_PATCH_A680AC02, loc)
            for value, loc in zip(hollow_colors, hollow_locs)
        ]
        objs.extend(
            _shape_object_a680ac02(value, BLOCK_PATCH_A680AC02, loc)
            for value, loc in zip(solid_colors, solid_locs)
        )
        shuffle(objs)
        for obj in objs:
            gi = paint(gi, obj)
        x2 = tuple(i for i, _ in hollow_locs)
        x3 = tuple(j for _, j in hollow_locs)
        x4 = greater(maximum(x2) - minimum(x2) + FOUR, maximum(x3) - minimum(x3) + FOUR)
        x5 = ZERO if x4 else ONE
        x6 = tuple(sorted(zip(hollow_locs, hollow_colors), key=lambda item: item[ZERO][x5]))
        x7 = tuple(_frame_grid_a680ac02(value) for _, value in x6)
        go = _pack_grids_a680ac02(x7, x4)
        return {"input": gi, "output": go}
