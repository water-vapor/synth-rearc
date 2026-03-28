from synth_rearc.core import *


FG_COLORS_E21A174A = remove(ZERO, interval(ZERO, TEN, ONE))
HEIGHT_OPTIONS_E21A174A = (ONE, TWO, TWO, THREE, THREE, FOUR)


def _centered_start_e21a174a(width: Integer, span: Integer) -> Integer:
    x0 = subtract(width, span)
    x1 = divide(x0, TWO)
    x2 = max(ZERO, subtract(x1, ONE))
    x3 = min(x0, add(x1, ONE))
    return randint(x2, x3)


def _rows_to_patch_e21a174a(rows: tuple[tuple[tuple[int, int], ...], ...]) -> Indices:
    return frozenset(
        (i, j)
        for i, segments in enumerate(rows)
        for start, stop in segments
        for j in range(start, stop)
    )


def _connected_patch_e21a174a(patch: Indices, height_value: Integer, width_value: Integer) -> Boolean:
    x0 = canvas(ZERO, (height_value, width_value))
    x1 = fill(x0, ONE, patch)
    x2 = objects(x1, T, T, F)
    x3 = colorfilter(x2, ONE)
    return equality(size(x3), ONE)


def _solid_rows_e21a174a(height_value: Integer, width_value: Integer) -> tuple[tuple[tuple[int, int], ...], ...]:
    x0 = ((ZERO, width_value),)
    return tuple(x0 for _ in range(height_value))


def _bar_stem_rows_e21a174a(
    height_value: Integer,
    width_value: Integer,
    top_full: Boolean,
) -> tuple[tuple[tuple[int, int], ...], ...]:
    x0 = randint(ONE, subtract(height_value, ONE))
    x1 = max(ONE, subtract(width_value, TWO))
    x2 = randint(ONE, x1)
    x3 = _centered_start_e21a174a(width_value, x2)
    x4 = ((ZERO, width_value),)
    x5 = ((x3, add(x3, x2)),)
    x6 = tuple(x4 for _ in range(x0))
    x7 = tuple(x5 for _ in range(subtract(height_value, x0)))
    x8 = combine(x6, x7)
    return x8 if top_full else x8[::-1]


def _box_rows_e21a174a(height_value: Integer, width_value: Integer) -> tuple[tuple[tuple[int, int], ...], ...]:
    x0 = ONE if width_value <= FIVE else choice((ONE, ONE, TWO))
    x1 = min(x0, divide(subtract(width_value, ONE), TWO))
    x2 = ((ZERO, width_value),)
    x3 = ((ZERO, x1), (subtract(width_value, x1), width_value))
    x4 = tuple(x3 for _ in range(subtract(height_value, TWO)))
    x5 = (x2,)
    x6 = (x2,)
    return combine(combine(x5, x4), x6)


def _split_bridge_rows_e21a174a(height_value: Integer, width_value: Integer) -> tuple[tuple[tuple[int, int], ...], ...]:
    x0 = max(ONE, min(THREE, divide(subtract(width_value, ONE), TWO)))
    x1 = randint(ONE, x0)
    x2 = ((ZERO, x1), (subtract(width_value, x1), width_value))
    x3 = max(ZERO, subtract(x1, ONE))
    x4 = min(width_value, add(subtract(width_value, x1), ONE))
    x5 = ((x3, x4),)
    x6 = ((ZERO, width_value),)
    if height_value == TWO:
        return choice(((x2, x5), (x6, x2), (x2, x6)))
    if height_value == THREE:
        return choice(((x2, x5, x2), (x2, x5, x6), (x6, x2, x5), (x6, x2, x6)))
    x7 = tuple(x6 for _ in range(subtract(height_value, THREE)))
    x8 = choice(((x2, x5, x6), (x6, x2, x5), (x2, x5, x2)))
    return combine(x8, x7)


def _box_stem_rows_e21a174a(height_value: Integer, width_value: Integer) -> tuple[tuple[tuple[int, int], ...], ...]:
    x0 = randint(ONE, subtract(height_value, THREE))
    x1 = max(ONE, subtract(width_value, TWO))
    x2 = randint(ONE, x1)
    x3 = _centered_start_e21a174a(width_value, x2)
    x4 = ((x3, add(x3, x2)),)
    x5 = tuple(x4 for _ in range(x0))
    x6 = _box_rows_e21a174a(subtract(height_value, x0), width_value)
    return combine(x5, x6)


def _shape_rows_e21a174a(
    height_value: Integer,
    width_value: Integer,
) -> tuple[tuple[tuple[int, int], ...], ...]:
    x0 = [_solid_rows_e21a174a]
    if height_value >= TWO:
        x0.extend((
            lambda h, w: _bar_stem_rows_e21a174a(h, w, T),
            lambda h, w: _bar_stem_rows_e21a174a(h, w, F),
        ))
        if width_value >= FIVE:
            x0.append(_split_bridge_rows_e21a174a)
    if height_value >= THREE:
        x0.append(_box_rows_e21a174a)
    if height_value >= FOUR:
        x0.append(_box_stem_rows_e21a174a)
    while True:
        x1 = choice(x0)
        x2 = x1(height_value, width_value)
        x3 = _rows_to_patch_e21a174a(x2)
        if _connected_patch_e21a174a(x3, height_value, width_value):
            return x2


def _object_spec_e21a174a(
    diff_lb: float,
    diff_ub: float,
    grid_width: Integer,
    center_col: Integer,
    height_value: Integer,
) -> tuple[Integer, Integer, tuple[tuple[tuple[int, int], ...], ...]]:
    if choice((T, T, F)):
        x0 = max(THREE, subtract(grid_width, FIVE))
        x1 = subtract(grid_width, TWO)
        x2 = unifint(diff_lb, diff_ub, (x0, x1))
    else:
        x2 = unifint(diff_lb, diff_ub, (THREE, subtract(grid_width, TWO)))
    x3 = subtract(center_col, divide(x2, TWO))
    x4 = max(ONE, min(x3, subtract(subtract(grid_width, x2), ONE)))
    x5 = max(ONE, subtract(x4, ONE))
    x6 = min(subtract(subtract(grid_width, x2), ONE), add(x4, ONE))
    x7 = randint(x5, x6)
    x8 = _shape_rows_e21a174a(height_value, x2)
    return x7, x2, x8


def _place_object_e21a174a(
    grid: Grid,
    color_value: Integer,
    top: Integer,
    left: Integer,
    rows: tuple[tuple[tuple[int, int], ...], ...],
) -> Grid:
    x0 = _rows_to_patch_e21a174a(rows)
    x1 = shift(x0, (top, left))
    return fill(grid, color_value, x1)


def generate_e21a174a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x1 = [choice(HEIGHT_OPTIONS_E21A174A) for _ in range(x0)]
        x2 = sum(x1)
        if not (FIVE <= x2 <= 12):
            continue
        x3 = unifint(diff_lb, diff_ub, (SEVEN, 14))
        x4 = max(TWO, min(subtract(x3, THREE), add(divide(x3, TWO), choice((NEG_ONE, ZERO, ONE)))))
        x5 = tuple(sample(FG_COLORS_E21A174A, x0))
        x6 = tuple(_object_spec_e21a174a(diff_lb, diff_ub, x3, x4, h) for h in x1)
        x7 = add(x2, TWO)
        x8 = canvas(ZERO, (x7, x3))
        x9 = canvas(ZERO, (x7, x3))
        x10 = ONE
        for color_value, spec in pair(x5, x6):
            left, _, rows = spec
            x8 = _place_object_e21a174a(x8, color_value, x10, left, rows)
            x10 = add(x10, len(rows))
        x11 = ONE
        for color_value, spec in pair(x5[::-1], x6[::-1]):
            left, _, rows = spec
            x9 = _place_object_e21a174a(x9, color_value, x11, left, rows)
            x11 = add(x11, len(rows))
        return {"input": x8, "output": x9}
