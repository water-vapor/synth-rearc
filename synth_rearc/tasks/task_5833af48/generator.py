from synth_rearc.core import *


COLOR_OPTIONS_5833AF48 = remove(EIGHT, remove(TWO, interval(ONE, TEN, ONE)))
STAMP_DIM_BOUNDS_5833AF48 = (THREE, FIVE)
MAP_DIM_BOUNDS_5833AF48 = (TWO, SIX)
MAP_SCALE_OPTIONS_5833AF48 = (ONE, TWO)
TOP_MARGIN_OPTIONS_5833AF48 = (ZERO, ONE)
LEFT_MARGIN_OPTIONS_5833AF48 = (ZERO, ONE)
RECT_SHIFT_OPTIONS_5833AF48 = (ZERO, ONE, TWO)
OUTER_MARGIN_OPTIONS_5833AF48 = (ONE, TWO, THREE)


def _grid_to_object_5833af48(grid: Grid) -> Object:
    return frozenset(
        (value, (i, j))
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value != ZERO
    )


def _embed_grid_5833af48(
    grid: Grid,
    patch: Grid,
    offset: IntegerTuple,
) -> Grid:
    return paint(grid, shift(_grid_to_object_5833af48(patch), offset))


def _connected_cells_5833af48(
    dims: IntegerTuple,
    count: Integer,
) -> Indices:
    h, w = dims
    cells = {choice(totuple(asindices(canvas(ZERO, dims))))}
    while len(cells) < count:
        frontier = set()
        for cell in cells:
            frontier.update(
                nbr
                for nbr in dneighbors(cell)
                if 0 <= nbr[0] < h and 0 <= nbr[1] < w and nbr not in cells
            )
        cells.add(choice(totuple(frontier)))
    return frozenset(cells)


def _sample_stamp_5833af48(
    diff_lb: float,
    diff_ub: float,
    dims: IntegerTuple,
) -> Grid:
    area = multiply(*dims)
    lower = branch(greater(area, NINE), THREE, TWO)
    upper = decrement(area)
    count = unifint(diff_lb, diff_ub, (lower, upper))
    motif = _connected_cells_5833af48(dims, count)
    stamp = canvas(TWO, dims)
    return fill(stamp, EIGHT, motif)


def _sample_map_5833af48(
    diff_lb: float,
    diff_ub: float,
    dims: IntegerTuple,
    fill_color: Integer,
) -> Grid:
    area = multiply(*dims)
    lower = branch(greater(area, FOUR), TWO, ONE)
    upper = decrement(area)
    count = unifint(diff_lb, diff_ub, (lower, upper))
    active = frozenset(sample(totuple(asindices(canvas(ZERO, dims))), count))
    coarse = canvas(fill_color, dims)
    return fill(coarse, EIGHT, active)


def _render_output_5833af48(
    stamp: Grid,
    coarse_map: Grid,
    fill_color: Integer,
) -> Grid:
    stamp_dims = shape(stamp)
    map_dims = shape(coarse_map)
    output_dims = multiply(stamp_dims, map_dims)
    output = canvas(fill_color, output_dims)
    motif = ofcolor(stamp, EIGHT)
    for loc in ofcolor(coarse_map, EIGHT):
        output = fill(output, EIGHT, shift(motif, multiply(stamp_dims, loc)))
    return output


def generate_5833af48(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        fill_color = choice(COLOR_OPTIONS_5833AF48)
        stamp_h = unifint(diff_lb, diff_ub, STAMP_DIM_BOUNDS_5833AF48)
        stamp_w = unifint(diff_lb, diff_ub, STAMP_DIM_BOUNDS_5833AF48)
        map_h = unifint(diff_lb, diff_ub, MAP_DIM_BOUNDS_5833AF48)
        map_w = unifint(diff_lb, diff_ub, MAP_DIM_BOUNDS_5833AF48)
        map_scale = choice(MAP_SCALE_OPTIONS_5833AF48)

        rect_h = multiply(stamp_h, map_h)
        rect_w = multiply(stamp_w, map_w)
        display_h = multiply(map_h, map_scale)
        display_w = multiply(map_w, map_scale)

        top_margin = choice(TOP_MARGIN_OPTIONS_5833AF48)
        left_margin = choice(LEFT_MARGIN_OPTIONS_5833AF48)
        rect_left = add(left_margin, choice(RECT_SHIFT_OPTIONS_5833AF48))
        rect_top = add(add(top_margin, max(stamp_h, display_h)), ONE)
        input_h = add(add(rect_top, rect_h), choice(OUTER_MARGIN_OPTIONS_5833AF48))
        instruction_w = add(add(left_margin, stamp_w), add(ONE, display_w))
        input_w = add(
            max(instruction_w, add(rect_left, rect_w)),
            choice(OUTER_MARGIN_OPTIONS_5833AF48),
        )
        top_nonzero = add(multiply(stamp_h, stamp_w), multiply(display_h, display_w))
        if input_h > 30 or input_w > 30:
            continue
        if multiply(rect_top, input_w) <= double(top_nonzero):
            continue

        stamp = _sample_stamp_5833af48(diff_lb, diff_ub, (stamp_h, stamp_w))
        coarse_map = _sample_map_5833af48(diff_lb, diff_ub, (map_h, map_w), fill_color)
        display_map = branch(
            equality(map_scale, ONE),
            coarse_map,
            upscale(coarse_map, map_scale),
        )

        output = _render_output_5833af48(stamp, coarse_map, fill_color)
        rect = canvas(fill_color, (rect_h, rect_w))
        input_grid = canvas(ZERO, (input_h, input_w))
        input_grid = _embed_grid_5833af48(input_grid, stamp, (top_margin, left_margin))
        input_grid = _embed_grid_5833af48(
            input_grid,
            display_map,
            (top_margin, add(add(left_margin, stamp_w), ONE)),
        )
        input_grid = _embed_grid_5833af48(input_grid, rect, (rect_top, rect_left))
        return {"input": input_grid, "output": output}
