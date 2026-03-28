from synth_rearc.core import *


GRID_SHAPE_4ACC7107 = (TEN, TEN)
NONZERO_COLORS_4ACC7107 = remove(ZERO, interval(ZERO, TEN, ONE))
FOUR_OBJECTS_4ACC7107 = FOUR


def _sample_shape_4acc7107(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    target = unifint(diff_lb, diff_ub, (THREE, EIGHT))
    for _ in range(200):
        height_ = choice((ONE, TWO, TWO, THREE, THREE, THREE))
        width_choices = (THREE, FOUR, FIVE) if height_ == ONE else (TWO, THREE, THREE, FOUR, FOUR, FIVE)
        width_ = choice(width_choices)
        runs = []
        prev_start = None
        prev_stop = None
        for _ in range(height_):
            min_len = max(ONE, width_ - TWO)
            if height_ == ONE:
                min_len = max(TWO, min_len)
            run_len = randint(min_len, width_)
            if prev_start is None:
                start = randint(ZERO, width_ - run_len)
            else:
                options = tuple(
                    candidate
                    for candidate in range(width_ - run_len + ONE)
                    if candidate < prev_stop and prev_start < candidate + run_len
                )
                if len(options) == ZERO:
                    break
                start = choice(options)
            runs.append((start, run_len))
            prev_start = start
            prev_stop = start + run_len
        if len(runs) != height_:
            continue
        patch = frozenset(
            (i, j)
            for i, (start, run_len) in enumerate(runs)
            for j in range(start, start + run_len)
        )
        if not (THREE <= len(patch) <= EIGHT):
            continue
        if abs(len(patch) - target) > TWO:
            continue
        return normalize(patch)
    return frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)})


def _stack_width_4acc7107(
    bottom_patch: Indices,
    top_patch: Indices,
) -> Integer:
    return maximum((width(bottom_patch), width(top_patch)))


def _stack_height_4acc7107(
    bottom_patch: Indices,
    top_patch: Indices,
) -> Integer:
    return add(height(bottom_patch), increment(height(top_patch)))


def _paint_patch_4acc7107(
    grid: Grid,
    patch: Indices,
    color_: Integer,
    anchor: IntegerTuple,
) -> Grid:
    return paint(grid, recolor(color_, shift(patch, anchor)))


def _build_output_4acc7107(
    left_color: Integer,
    left_bottom: Indices,
    left_top: Indices,
    right_color: Integer,
    right_bottom: Indices,
    right_top: Indices,
) -> Grid:
    grid = canvas(ZERO, GRID_SHAPE_4ACC7107)
    cursor = ZERO
    for color_, bottom_patch, top_patch in (
        (left_color, left_bottom, left_top),
        (right_color, right_bottom, right_top),
    ):
        bottom_row = subtract(TEN, height(bottom_patch))
        top_row = subtract(bottom_row, increment(height(top_patch)))
        grid = _paint_patch_4acc7107(grid, top_patch, color_, astuple(top_row, cursor))
        grid = _paint_patch_4acc7107(grid, bottom_patch, color_, astuple(bottom_row, cursor))
        cursor = add(cursor, increment(_stack_width_4acc7107(bottom_patch, top_patch)))
    return grid


def _separated_4acc7107(
    patches: tuple[Indices, ...],
) -> Boolean:
    for i, patch_a in enumerate(patches):
        for patch_b in patches[i + ONE:]:
            if manhattan(patch_a, patch_b) <= ONE:
                return False
    return True


def _build_input_4acc7107(
    left_color: Integer,
    left_bottom: Indices,
    left_top: Indices,
    right_color: Integer,
    right_bottom: Indices,
    right_top: Indices,
) -> Grid | None:
    for _ in range(800):
        left_bottom_col = randint(ZERO, max(ZERO, subtract(SIX, width(left_bottom))))
        left_top_min = increment(left_bottom_col)
        left_top_max = subtract(TEN, width(left_top))
        if left_top_min > left_top_max:
            continue
        left_top_col = randint(left_top_min, left_top_max)
        right_bottom_min = max(TWO, increment(left_bottom_col))
        right_bottom_max = subtract(NINE, width(right_bottom))
        if right_bottom_min > right_bottom_max:
            continue
        right_bottom_col = randint(right_bottom_min, right_bottom_max)
        right_top_min = increment(right_bottom_col)
        right_top_max = subtract(TEN, width(right_top))
        if right_top_min > right_top_max:
            continue
        right_top_col = randint(right_top_min, right_top_max)
        left_bottom_row = randint(ZERO, subtract(TEN, height(left_bottom)))
        left_top_row = randint(ZERO, subtract(TEN, height(left_top)))
        right_bottom_row = randint(ZERO, subtract(TEN, height(right_bottom)))
        right_top_row = randint(ZERO, subtract(TEN, height(right_top)))
        placed_patches = (
            shift(left_bottom, astuple(left_bottom_row, left_bottom_col)),
            shift(left_top, astuple(left_top_row, left_top_col)),
            shift(right_bottom, astuple(right_bottom_row, right_bottom_col)),
            shift(right_top, astuple(right_top_row, right_top_col)),
        )
        if not _separated_4acc7107(placed_patches):
            continue
        grid = canvas(ZERO, GRID_SHAPE_4ACC7107)
        grid = _paint_patch_4acc7107(grid, placed_patches[ZERO], left_color, ORIGIN)
        grid = _paint_patch_4acc7107(grid, placed_patches[ONE], left_color, ORIGIN)
        grid = _paint_patch_4acc7107(grid, placed_patches[TWO], right_color, ORIGIN)
        grid = _paint_patch_4acc7107(grid, placed_patches[THREE], right_color, ORIGIN)
        if size(objects(grid, T, F, T)) != FOUR_OBJECTS_4ACC7107:
            continue
        return grid
    return None


def generate_4acc7107(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        left_color, right_color = sample(NONZERO_COLORS_4ACC7107, TWO)
        left_bottom = _sample_shape_4acc7107(diff_lb, diff_ub)
        left_top = _sample_shape_4acc7107(diff_lb, diff_ub)
        right_bottom = _sample_shape_4acc7107(diff_lb, diff_ub)
        right_top = _sample_shape_4acc7107(diff_lb, diff_ub)
        left_width = _stack_width_4acc7107(left_bottom, left_top)
        right_width = _stack_width_4acc7107(right_bottom, right_top)
        if add(add(left_width, right_width), ONE) > TEN:
            continue
        if _stack_height_4acc7107(left_bottom, left_top) > TEN:
            continue
        if _stack_height_4acc7107(right_bottom, right_top) > TEN:
            continue
        gi = _build_input_4acc7107(
            left_color,
            left_bottom,
            left_top,
            right_color,
            right_bottom,
            right_top,
        )
        if gi is None:
            continue
        go = _build_output_4acc7107(
            left_color,
            left_bottom,
            left_top,
            right_color,
            right_bottom,
            right_top,
        )
        if equality(gi, go):
            continue
        return {"input": gi, "output": go}
