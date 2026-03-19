from arc2.core import *

from .verifier import verify_ea9794b1


BOARD_SHAPE_EA9794B1 = (FIVE, FIVE)
UNIVERSE_EA9794B1 = frozenset((i, j) for i in range(FIVE) for j in range(FIVE))

COUNT_BOUNDS_EA9794B1 = {
    FOUR: (9, 17),
    THREE: (11, 17),
    NINE: (8, 17),
    EIGHT: (8, 15),
}

SCATTER_BAG_EA9794B1 = {
    FOUR: (F, F, F, T),
    THREE: (F, F, F, F, T),
    NINE: (F, F, T, T),
    EIGHT: (F, F, T, T),
}

EXTRA_BAG_EA9794B1 = {
    FOUR: (ZERO, ONE, ONE, TWO, TWO, THREE, FOUR, FIVE, SIX),
    THREE: (ZERO, ZERO, ONE, ONE, TWO, TWO, THREE, FOUR, FIVE),
    NINE: (ONE, ONE, TWO, TWO, THREE, FOUR, FIVE, SIX, SEVEN),
    EIGHT: (ONE, TWO, TWO, THREE, FOUR, FIVE, SIX, SEVEN),
}


def _neighbors_ea9794b1(
    loc: IntegerTuple,
) -> frozenset[IntegerTuple]:
    i, j = loc
    out = set()
    if positive(i):
        out.add((i - ONE, j))
    if i < FOUR:
        out.add((i + ONE, j))
    if positive(j):
        out.add((i, j - ONE))
    if j < FOUR:
        out.add((i, j + ONE))
    return frozenset(out)


def _blocked_ea9794b1(
    patch: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple]:
    out = set(patch)
    for loc in patch:
        out |= _neighbors_ea9794b1(loc)
    return frozenset(out)


def _grow_component_ea9794b1(
    ncells: Integer,
    blocked: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple] | None:
    available = UNIVERSE_EA9794B1 - blocked
    if len(available) < ncells:
        return None
    start = choice(tuple(available))
    patch = {start}
    while len(patch) < ncells:
        frontier = set()
        for loc in tuple(patch):
            frontier |= _neighbors_ea9794b1(loc)
        frontier = tuple((frontier & available) - patch)
        if len(frontier) == ZERO:
            return None
        patch.add(choice(frontier))
    return frozenset(patch)


def _scatter_sizes_ea9794b1(
    total: Integer,
) -> tuple[Integer, ...]:
    sizes = []
    rem = total
    while rem > ZERO:
        part = randint(ONE, min(FOUR, rem))
        sizes.append(part)
        rem -= part
    if len(sizes) == ONE:
        return (sizes[ZERO],)
    return tuple(sorted(sizes, reverse=True))


def _component_sizes_ea9794b1(
    color_value: Integer,
    total: Integer,
) -> tuple[Integer, ...]:
    if choice(SCATTER_BAG_EA9794B1[color_value]):
        return _scatter_sizes_ea9794b1(total)
    extra = min(choice(EXTRA_BAG_EA9794B1[color_value]), total - ONE)
    main = total - extra
    sizes = [main]
    rem = extra
    while rem > ZERO:
        part = randint(ONE, min(THREE, rem))
        sizes.append(part)
        rem -= part
    return tuple(sorted(sizes, reverse=True))


def _profile_ok_ea9794b1(
    patch: frozenset[IntegerTuple],
) -> Boolean:
    row_counts = [sum((i, j) in patch for j in range(FIVE)) for i in range(FIVE)]
    col_counts = [sum((i, j) in patch for i in range(FIVE)) for j in range(FIVE)]
    if row_counts.count(ZERO) > ONE:
        return F
    if col_counts.count(ZERO) > TWO:
        return F
    if max(row_counts) < TWO:
        return F
    if max(col_counts) < TWO:
        return F
    return T


def _build_mask_ea9794b1(
    color_value: Integer,
    diff_lb: float,
    diff_ub: float,
) -> frozenset[IntegerTuple] | None:
    target = unifint(diff_lb, diff_ub, COUNT_BOUNDS_EA9794B1[color_value])
    for _ in range(60):
        sizes = _component_sizes_ea9794b1(color_value, target)
        patch = frozenset()
        blocked = frozenset()
        failed = F
        for ncells in sizes:
            comp = _grow_component_ea9794b1(ncells, blocked)
            if comp is None:
                failed = T
                break
            patch = patch | comp
            blocked = _blocked_ea9794b1(patch)
        if failed:
            continue
        if len(patch) != target:
            continue
        if not _profile_ok_ea9794b1(patch):
            continue
        return patch
    return None


def _paint_quadrant_ea9794b1(
    color_value: Integer,
    patch: frozenset[IntegerTuple],
) -> Grid:
    return fill(canvas(ZERO, BOARD_SHAPE_EA9794B1), color_value, patch)


def _output_from_masks_ea9794b1(
    tl: frozenset[IntegerTuple],
    tr: frozenset[IntegerTuple],
    bl: frozenset[IntegerTuple],
    br: frozenset[IntegerTuple],
) -> Grid:
    x0 = canvas(ZERO, BOARD_SHAPE_EA9794B1)
    x1 = fill(x0, FOUR, tl)
    x2 = fill(x1, EIGHT, br)
    x3 = fill(x2, NINE, bl)
    x4 = fill(x3, THREE, tr)
    return x4


def _grid_color_count_ea9794b1(
    grid: Grid,
    value: Integer,
) -> Integer:
    return sum(cell == value for row in grid for cell in row)


def generate_ea9794b1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        tl = _build_mask_ea9794b1(FOUR, diff_lb, diff_ub)
        tr = _build_mask_ea9794b1(THREE, diff_lb, diff_ub)
        bl = _build_mask_ea9794b1(NINE, diff_lb, diff_ub)
        br = _build_mask_ea9794b1(EIGHT, diff_lb, diff_ub)
        if tl is None or tr is None or bl is None or br is None:
            continue
        go = _output_from_masks_ea9794b1(tl, tr, bl, br)
        if not (ONE <= _grid_color_count_ea9794b1(go, ZERO) <= FIVE):
            continue
        if not (NINE <= _grid_color_count_ea9794b1(go, THREE) <= 18):
            continue
        survivors = sum(
            _grid_color_count_ea9794b1(go, value) > ZERO
            for value in (FOUR, EIGHT, NINE)
        )
        if survivors < TWO:
            continue
        x0 = _paint_quadrant_ea9794b1(FOUR, tl)
        x1 = _paint_quadrant_ea9794b1(THREE, tr)
        x2 = _paint_quadrant_ea9794b1(NINE, bl)
        x3 = _paint_quadrant_ea9794b1(EIGHT, br)
        gi = vconcat(hconcat(x0, x1), hconcat(x2, x3))
        if verify_ea9794b1(gi) != go:
            continue
        return {"input": gi, "output": go}
