from synth_rearc.core import *


CANVAS_SIDE_88207623 = 30
GROUP_COUNT_BOUNDS_88207623 = (TWO, FOUR)
HEIGHT_BOUNDS_88207623 = (THREE, SIX)
WIDTH_BOUNDS_88207623 = (TWO, FIVE)
FINAL_SIDE_BOUNDS_88207623 = (14, 20)
MARKER_COLORS_88207623 = (ONE, THREE, FIVE, SIX, SEVEN, EIGHT, NINE)
BOX_MARGIN_88207623 = TWO


def _neighbors8_88207623(cell: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    i, j = cell
    return tuple(
        (i + di, j + dj)
        for di in (-ONE, ZERO, ONE)
        for dj in (-ONE, ZERO, ONE)
        if not (di == ZERO and dj == ZERO)
    )


def _connected_88207623(shape: frozenset[tuple[int, int]]) -> bool:
    if not shape:
        return False
    frontier = [next(iter(shape))]
    seen = {frontier[0]}
    while frontier:
        cell = frontier.pop()
        for neighbor in _neighbors8_88207623(cell):
            if neighbor in shape and neighbor not in seen:
                seen.add(neighbor)
                frontier.append(neighbor)
    return len(seen) == len(shape)


def _row_coverage_88207623(shape: frozenset[tuple[int, int]], height: int) -> bool:
    rows = {i for i, _ in shape}
    return rows == set(range(height))


def _shape_ok_88207623(shape: frozenset[tuple[int, int]], height: int) -> bool:
    cols = {j for _, j in shape}
    return (
        _connected_88207623(shape)
        and _row_coverage_88207623(shape, height)
        and ONE in cols
        and len(shape) >= height + ONE
    )


def _base_shape_88207623(height: int, width: int) -> frozenset[tuple[int, int]]:
    left = randint(ONE, width)
    right = randint(left, width)
    rows = []
    for _ in range(height):
        left = min(width, max(ONE, left + choice((NEG_ONE, ZERO, ONE))))
        right = min(width, max(left, right + choice((NEG_ONE, ZERO, ONE))))
        rows.append(set(range(left, right + ONE)))
    rows[randint(ZERO, height - ONE)].add(ONE)
    return frozenset((i, j) for i, row in enumerate(rows) for j in row)


def _mutate_shape_88207623(shape: frozenset[tuple[int, int]], height: int, width: int) -> frozenset[tuple[int, int]]:
    cells = set(shape)
    nsteps = randint(THREE, add(height, width))
    for _ in range(nsteps):
        cell = (randint(ZERO, height - ONE), randint(ONE, width))
        if cell in cells:
            candidate = frozenset(cells - {cell})
        else:
            candidate = frozenset(cells | {cell})
        if _shape_ok_88207623(candidate, height):
            cells = set(candidate)
    return frozenset(cells)


def _make_shape_88207623(height: int, width: int) -> frozenset[tuple[int, int]]:
    while True:
        shape = _base_shape_88207623(height, width)
        shape = _mutate_shape_88207623(shape, height, width)
        if _shape_ok_88207623(shape, height):
            return shape


def _reserve_box_88207623(top: int, bottom: int, left: int, right: int) -> frozenset[tuple[int, int]]:
    top = max(ZERO, subtract(top, BOX_MARGIN_88207623))
    left = max(ZERO, subtract(left, BOX_MARGIN_88207623))
    bottom = min(CANVAS_SIDE_88207623 - ONE, add(bottom, BOX_MARGIN_88207623))
    right = min(CANVAS_SIDE_88207623 - ONE, add(right, BOX_MARGIN_88207623))
    return frozenset(
        (i, j)
        for i in range(top, bottom + ONE)
        for j in range(left, right + ONE)
    )


def _place_group_88207623(
    reserved: frozenset[tuple[int, int]],
    height: int,
    width: int,
) -> tuple[int, int] | None:
    candidates = []
    for top in range(CANVAS_SIDE_88207623 - height + ONE):
        for axis in range(width, CANVAS_SIDE_88207623 - width):
            bottom = add(top, subtract(height, ONE))
            left = subtract(axis, width)
            right = add(axis, width)
            box = _reserve_box_88207623(top, bottom, left, right)
            if len(intersection(box, reserved)) == ZERO:
                candidates.append((top, axis))
    if len(candidates) == ZERO:
        return None
    return choice(candidates)


def _materialize_group_88207623(
    shape: frozenset[tuple[int, int]],
    top: int,
    axis: int,
    original_on_right: bool,
) -> tuple[frozenset[tuple[int, int]], frozenset[tuple[int, int]], frozenset[tuple[int, int]]]:
    line = frozenset((top + i, axis) for i in range(height(shape)))
    if original_on_right:
        source = frozenset((top + i, axis + j) for i, j in shape)
        target = frozenset((top + i, axis - j) for i, j in shape)
    else:
        source = frozenset((top + i, axis - j) for i, j in shape)
        target = frozenset((top + i, axis + j) for i, j in shape)
    return line, source, target


def _occupied_88207623(grid: Grid) -> frozenset[tuple[int, int]]:
    return frozenset(
        (i, j)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value != ZERO
    )


def generate_88207623(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        ngroups = unifint(diff_lb, diff_ub, GROUP_COUNT_BOUNDS_88207623)
        colors = sample(MARKER_COLORS_88207623, ngroups)
        reserved = frozenset({})
        gi = canvas(ZERO, (CANVAS_SIDE_88207623, CANVAS_SIDE_88207623))
        go = canvas(ZERO, (CANVAS_SIDE_88207623, CANVAS_SIDE_88207623))
        failed = False
        for color_value in colors:
            height_value = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_88207623)
            width_value = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_88207623)
            shape = _make_shape_88207623(height_value, width_value)
            placement = _place_group_88207623(reserved, height_value, width_value)
            if placement is None:
                failed = True
                break
            top, axis = placement
            original_on_right = choice((T, F))
            line, source, target = _materialize_group_88207623(shape, top, axis, original_on_right)
            far_targets = tuple(cell for cell in target if abs(subtract(cell[1], axis)) > ONE)
            marker = choice(far_targets if len(far_targets) > ZERO else tuple(target))
            gi = fill(gi, TWO, line)
            gi = fill(gi, FOUR, source)
            gi = fill(gi, color_value, initset(marker))
            go = fill(go, TWO, line)
            go = fill(go, FOUR, source)
            go = fill(go, color_value, target)
            reserved = combine(
                reserved,
                _reserve_box_88207623(top, add(top, subtract(height_value, ONE)), subtract(axis, width_value), add(axis, width_value)),
            )
        if failed:
            continue
        x0 = _occupied_88207623(gi)
        x1 = uppermost(x0)
        x2 = lowermost(x0)
        x3 = leftmost(x0)
        x4 = rightmost(x0)
        x5 = add(subtract(x2, x1), ONE)
        x6 = add(subtract(x4, x3), ONE)
        if x5 > FINAL_SIDE_BOUNDS_88207623[ONE] or x6 > FINAL_SIDE_BOUNDS_88207623[ONE]:
            continue
        x7 = unifint(diff_lb, diff_ub, (max(FINAL_SIDE_BOUNDS_88207623[ZERO], x5), min(FINAL_SIDE_BOUNDS_88207623[ONE], add(x5, FOUR))))
        x8 = unifint(diff_lb, diff_ub, (max(FINAL_SIDE_BOUNDS_88207623[ZERO], x6), min(FINAL_SIDE_BOUNDS_88207623[ONE], add(x6, FOUR))))
        x9 = max(ZERO, subtract(x2, subtract(x7, ONE)))
        x10 = min(x1, subtract(CANVAS_SIDE_88207623, x7))
        x11 = max(ZERO, subtract(x4, subtract(x8, ONE)))
        x12 = min(x3, subtract(CANVAS_SIDE_88207623, x8))
        if x9 > x10 or x11 > x12:
            continue
        x13 = randint(x9, x10)
        x14 = randint(x11, x12)
        gi = crop(gi, (x13, x14), (x7, x8))
        go = crop(go, (x13, x14), (x7, x8))
        if choice((T, F)):
            gi = hmirror(gi)
            go = hmirror(go)
        if choice((T, F)):
            gi = vmirror(gi)
            go = vmirror(go)
        if gi == go or mostcolor(gi) != ZERO:
            continue
        return {"input": gi, "output": go}
