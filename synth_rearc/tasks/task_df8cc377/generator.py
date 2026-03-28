from synth_rearc.core import *

from .verifier import verify_df8cc377


def _checker_patch_df8cc377(frame: Object) -> Indices:
    anchor = ulcorner(frame)
    return frozenset(
        ij for ij in delta(frame)
        if even(ij[0] + ij[1]) == even(anchor[0] + anchor[1])
    )


def _frame_df8cc377(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
    value: Integer,
) -> Object:
    lower = add(top, subtract(height_value, ONE))
    right = add(left, subtract(width_value, ONE))
    patch = box(frozenset({(top, left), (lower, right)}))
    return recolor(value, patch)


def _guard_df8cc377(frame: Object) -> Indices:
    return combine(backdrop(frame), outbox(frame))


def _fill_count_df8cc377(
    height_value: Integer,
    width_value: Integer,
) -> Integer:
    area = multiply(subtract(height_value, TWO), subtract(width_value, TWO))
    return divide(increment(area), TWO)


def _isolated_scatter_df8cc377(
    candidates: tuple[IntegerTuple, ...],
    needed: Integer,
) -> tuple[IntegerTuple, ...]:
    chosen = tuple()
    blocked = frozenset()
    pool = list(candidates)
    shuffle(pool)
    for loc in pool:
        if loc in blocked:
            continue
        chosen = chosen + (loc,)
        blocked = combine(blocked, insert(loc, neighbors(loc)))
        if len(chosen) == needed:
            return chosen
    return tuple()


def generate_df8cc377(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        height_value = unifint(diff_lb, diff_ub, (12, 30))
        width_value = unifint(diff_lb, diff_ub, (12, 30))
        shape_value = astuple(height_value, width_value)
        nframes = TWO if min(height_value, width_value) < 16 else choice((TWO, TWO, THREE))
        colors = sample(interval(ONE, TEN, ONE), add(nframes, nframes))
        frame_colors = colors[:nframes]
        fill_colors = colors[nframes:]
        frames = tuple()
        fill_counts = tuple()
        occupied = frozenset()
        attempts = ZERO
        max_frame_h = min(TEN, subtract(height_value, TWO))
        max_frame_w = min(12, subtract(width_value, TWO))
        if max_frame_h < THREE or max_frame_w < THREE:
            continue
        while len(frames) < nframes and attempts < 500:
            attempts = increment(attempts)
            frame_h = unifint(diff_lb, diff_ub, (THREE, max_frame_h))
            frame_w = unifint(diff_lb, diff_ub, (THREE, max_frame_w))
            fill_count = _fill_count_df8cc377(frame_h, frame_w)
            if contained(fill_count, fill_counts):
                continue
            top = randint(ZERO, subtract(height_value, frame_h))
            left = randint(ZERO, subtract(width_value, frame_w))
            frame = _frame_df8cc377(top, left, frame_h, frame_w, frame_colors[len(frames)])
            guard = _guard_df8cc377(frame)
            if len(intersection(guard, occupied)) > ZERO:
                continue
            frames = frames + (frame,)
            fill_counts = fill_counts + (fill_count,)
            occupied = combine(occupied, guard)
        if len(frames) != nframes:
            continue
        x0 = asindices(canvas(ZERO, shape_value))
        forbidden = merge(tuple(_guard_df8cc377(frame) for frame in frames))
        candidates = tuple(difference(x0, forbidden))
        needed = sum(fill_counts)
        scatters = _isolated_scatter_df8cc377(candidates, needed)
        if len(scatters) != needed:
            continue
        output_grid = canvas(ZERO, shape_value)
        input_grid = canvas(ZERO, shape_value)
        start = ZERO
        for frame, fill_color, fill_count in zip(frames, fill_colors, fill_counts):
            checker = _checker_patch_df8cc377(frame)
            output_grid = fill(output_grid, fill_color, checker)
            frame_cells = toindices(frame)
            output_grid = fill(output_grid, color(frame), frame_cells)
            input_grid = fill(input_grid, color(frame), frame_cells)
            scatter_patch = frozenset(scatters[start:add(start, fill_count)])
            input_grid = fill(input_grid, fill_color, scatter_patch)
            start = add(start, fill_count)
        if input_grid == output_grid:
            continue
        if verify_df8cc377(input_grid) != output_grid:
            continue
        return {"input": input_grid, "output": output_grid}
