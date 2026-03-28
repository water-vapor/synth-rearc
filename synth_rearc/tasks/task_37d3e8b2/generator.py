from synth_rearc.core import *


GRID_HEIGHTS_37D3E8B2 = (17, 17, 17, 18, 19)
GRID_WIDTHS_37D3E8B2 = (16, 17, 17, 18)
OBJECT_COUNTS_37D3E8B2 = (4, 5, 5, 6)
HOLE_COUNTS_37D3E8B2 = (
    ONE,
    ONE,
    ONE,
    TWO,
    TWO,
    TWO,
    TWO,
    THREE,
    THREE,
    THREE,
    FOUR,
    FOUR,
    FOUR,
)
SIZE_OPTIONS_37D3E8B2 = {
    ONE: ((4, 3), (4, 4), (5, 4), (3, 4), (4, 5)),
    TWO: ((3, 7), (4, 5), (4, 6), (5, 4), (5, 5), (4, 7)),
    THREE: ((5, 5), (5, 6), (5, 7), (6, 5), (6, 6)),
    FOUR: ((5, 6), (5, 7), (6, 5), (6, 6), (7, 5), (7, 7), (8, 5), (9, 5), (9, 7)),
}
TRANSFORMS_37D3E8B2 = (identity, hmirror, vmirror, rot180)


def _holecolor_37d3e8b2(
    count: Integer,
) -> Integer:
    if count == ONE:
        return ONE
    if count == TWO:
        return TWO
    if count == THREE:
        return THREE
    return SEVEN


def _holecount_37d3e8b2(
    grid: Grid,
) -> Integer:
    x0 = objects(grid, T, F, F)
    x1 = colorfilter(x0, ZERO)
    x2 = rbind(bordering, grid)
    x3 = compose(flip, x2)
    x4 = sfilter(x1, x3)
    return size(x4)


def _disconnected_cells_37d3e8b2(
    height: Integer,
    width: Integer,
    count: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0 = tuple(product(interval(ZERO, height, ONE), interval(ZERO, width, ONE)))
    if len(x0) < count:
        return None
    for _ in range(80):
        x1 = list(sample(x0, count))
        x2 = True
        for x3, x4 in enumerate(x1):
            for x5 in x1[x3 + ONE:]:
                if manhattan(initset(x4), initset(x5)) == ONE:
                    x2 = False
                    break
            if not x2:
                break
        if x2:
            return tuple(x1)
    return None


def _grow_holes_37d3e8b2(
    height: Integer,
    width: Integer,
    seeds: tuple[IntegerTuple, ...],
) -> frozenset[IntegerTuple]:
    x0 = [set([x1]) for x1 in seeds]
    x1 = max(ZERO, min(height * width // FOUR, len(seeds) + randint(ZERO, max(len(seeds) - ONE, ZERO))))
    x2 = sum(len(x3) for x3 in x0)
    x3 = 0
    while x2 < x1 and x3 < 200:
        x3 += ONE
        x4 = randint(ZERO, len(x0) - ONE)
        x5 = set()
        for x6 in x0[x4]:
            for x7 in dneighbors(x6):
                if ZERO <= x7[ZERO] < height and ZERO <= x7[ONE] < width:
                    x5.add(x7)
        x5 = [x8 for x8 in x5 if x8 not in x0[x4]]
        shuffle(x5)
        x6 = False
        for x7 in x5:
            x8 = False
            for x9, x10 in enumerate(x0):
                if x9 == x4:
                    continue
                if x7 in x10:
                    x8 = True
                    break
                for x11 in x10:
                    if manhattan(initset(x7), initset(x11)) == ONE:
                        x8 = True
                        break
                if x8:
                    break
            if x8:
                continue
            x0[x4].add(x7)
            x2 += ONE
            x6 = True
            break
        if not x6:
            continue
    return frozenset(x4 for x5 in x0 for x4 in x5)


def _sample_object_grid_37d3e8b2(
    holes: Integer,
) -> Grid:
    x0 = choice(SIZE_OPTIONS_37D3E8B2[holes])
    x1 = choice((T, F))
    x2 = (x0[ONE], x0[ZERO]) if x1 else x0
    x3, x4 = x2
    x5 = _disconnected_cells_37d3e8b2(x3 - TWO, x4 - TWO, holes)
    if x5 is None:
        return _sample_object_grid_37d3e8b2(holes)
    x6 = _grow_holes_37d3e8b2(x3 - TWO, x4 - TWO, x5)
    x7 = shift(x6, (ONE, ONE))
    x8 = canvas(EIGHT, x2)
    x9 = fill(x8, ZERO, x7)
    x10 = choice(TRANSFORMS_37D3E8B2)(x9)
    x11 = _holecount_37d3e8b2(x10)
    if x11 != holes:
        return _sample_object_grid_37d3e8b2(holes)
    return x10


def _bbox_clear_37d3e8b2(
    placed: tuple[tuple[int, int, int, int], ...],
    top: Integer,
    left: Integer,
    height: Integer,
    width: Integer,
) -> Boolean:
    x0 = top - ONE
    x1 = left - ONE
    x2 = top + height
    x3 = left + width
    for x4, x5, x6, x7 in placed:
        if not (x2 < x4 or x6 < x0 or x3 < x5 or x7 < x1):
            return False
    return True


def _place_objects_37d3e8b2(
    dims: tuple[tuple[int, int], ...],
    height: Integer,
    width: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0 = tuple(sorted(range(len(dims)), key=lambda x1: dims[x1][ZERO] * dims[x1][ONE], reverse=True))
    x1 = [None for _ in dims]
    x2 = []
    for x3 in x0:
        x4, x5 = dims[x3]
        x6 = [
            (x7, x8)
            for x7 in range(height - x4 + ONE)
            for x8 in range(width - x5 + ONE)
            if _bbox_clear_37d3e8b2(tuple(x2), x7, x8, x4, x5)
        ]
        if len(x6) == ZERO:
            return None
        if x2:
            x7 = tuple(x8[ZERO] for x8 in x2)
            x8 = tuple(x9[ONE] for x9 in x2)
            x9 = sum(x7) // len(x7)
            x10 = sum(x8) // len(x8)
            x6 = sorted(
                x6,
                key=lambda x11: (
                    abs(x11[ZERO] - x9) + abs(x11[ONE] - x10),
                    randint(ZERO, 9),
                ),
            )
            x11 = min(len(x6), 20)
            x12 = choice(tuple(x6[:x11]))
        else:
            x12 = choice(tuple(x6))
        x1[x3] = x12
        x2.append((x12[ZERO], x12[ONE], x12[ZERO] + x4 - ONE, x12[ONE] + x5 - ONE))
    return tuple(x1)


def _sample_layout_37d3e8b2() -> tuple[tuple[Grid, ...], tuple[IntegerTuple, ...], tuple[int, int], tuple[int, ...]]:
    while True:
        x0 = choice(OBJECT_COUNTS_37D3E8B2)
        x1 = tuple(choice(HOLE_COUNTS_37D3E8B2) for _ in range(x0))
        if len({x2 for x2 in x1}) < min(3, x0):
            continue
        x2 = tuple(_sample_object_grid_37d3e8b2(x3) for x3 in x1)
        x3 = tuple(shape(x4) for x4 in x2)
        x4 = choice(GRID_HEIGHTS_37D3E8B2)
        x5 = choice(GRID_WIDTHS_37D3E8B2)
        x6 = sum(x7[ZERO] * x7[ONE] for x7 in x3)
        if x6 > (x4 * x5) // 2:
            continue
        x7 = _place_objects_37d3e8b2(x3, x4, x5)
        if x7 is None:
            continue
        return x2, x7, (x4, x5), x1


def generate_37d3e8b2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1, x2, x3 = _sample_layout_37d3e8b2()
        x4 = canvas(ZERO, x2)
        x5 = canvas(ZERO, x2)
        for x6, x7, x8 in zip(x0, x1, x3):
            x9 = ofcolor(x6, EIGHT)
            x10 = shift(x9, x7)
            x11 = fill(x4, EIGHT, x10)
            x12 = _holecolor_37d3e8b2(x8)
            x13 = fill(x5, x12, x10)
            x4 = x11
            x5 = x13
        if len(objects(x4, T, F, T)) != len(x0):
            continue
        return {"input": x4, "output": x5}
