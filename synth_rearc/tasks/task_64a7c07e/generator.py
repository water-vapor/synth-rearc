from synth_rearc.core import *


BACKGROUND_64A7C07E = ZERO
OBJECT_COLOR_64A7C07E = EIGHT
MIN_GRID_SIZE_64A7C07E = FIVE
MAX_GRID_SIZE_64A7C07E = 18
MAX_OBJECT_SPAN_64A7C07E = SIX
MAX_OBJECTS_64A7C07E = THREE


def _neighbors8_64a7c07e(cell):
    i, j = cell
    return {
        (i + di, j + dj)
        for di in (-1, ZERO, ONE)
        for dj in (-1, ZERO, ONE)
        if not (di == ZERO and dj == ZERO)
    }


def _is_connected_64a7c07e(indices):
    if not indices:
        return False
    seen = {next(iter(indices))}
    frontier = list(seen)
    while frontier:
        cell = frontier.pop()
        for neighbor in _neighbors8_64a7c07e(cell):
            if neighbor in indices and neighbor not in seen:
                seen.add(neighbor)
                frontier.append(neighbor)
    return len(seen) == len(indices)


def _spans_box_64a7c07e(indices, height, width):
    rows = {i for i, _ in indices}
    cols = {j for _, j in indices}
    return rows == set(range(height)) and cols == set(range(width))


def _sample_shape_64a7c07e(height, width, diff_lb, diff_ub):
    cells = {(i, j) for i in range(height) for j in range(width)}
    if len(cells) == ONE:
        return frozenset(cells)
    target_lb = max(max(height, width), (height * width + ONE) // THREE)
    target = unifint(diff_lb, diff_ub, (target_lb, height * width))
    removable = list(cells)
    shuffle(removable)
    for cell in removable:
        if len(cells) <= target:
            break
        candidate = cells - {cell}
        if not _spans_box_64a7c07e(candidate, height, width):
            continue
        if not _is_connected_64a7c07e(candidate):
            continue
        cells = candidate
    return frozenset(cells)


def _expand_64a7c07e(indices):
    expanded = set(indices)
    for cell in indices:
        expanded |= _neighbors8_64a7c07e(cell)
    return expanded


def _choose_object_count_64a7c07e(grid_size):
    if grid_size < EIGHT:
        return ONE
    if grid_size < 13:
        return choice((ONE, TWO))
    return choice((ONE, TWO, TWO, THREE))


def generate_64a7c07e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        grid_size = unifint(diff_lb, diff_ub, (MIN_GRID_SIZE_64A7C07E, MAX_GRID_SIZE_64A7C07E))
        object_count = _choose_object_count_64a7c07e(grid_size)
        input_grid = canvas(BACKGROUND_64A7C07E, (grid_size, grid_size))
        output_grid = canvas(BACKGROUND_64A7C07E, (grid_size, grid_size))
        blocked_input = set()
        blocked_output = set()
        success = True
        for object_index in range(object_count):
            placed = False
            for _ in range(200):
                min_span = TWO if object_index == ZERO and grid_size > FIVE else ONE
                max_width = min(MAX_OBJECT_SPAN_64A7C07E, grid_size // TWO)
                if max_width < min_span:
                    max_width = min_span
                object_width = randint(min_span, max_width)
                max_height = min(MAX_OBJECT_SPAN_64A7C07E, max(min_span, grid_size - TWO))
                object_height = randint(min_span, max_height)
                shape = _sample_shape_64a7c07e(object_height, object_width, diff_lb, diff_ub)
                top = randint(ZERO, grid_size - object_height)
                left = randint(ZERO, grid_size - (object_width * TWO))
                input_patch = shift(shape, (top, left))
                output_patch = shift(input_patch, tojvec(object_width))
                input_indices = toindices(input_patch)
                output_indices = toindices(output_patch)
                if input_indices & blocked_input:
                    continue
                if output_indices & blocked_output:
                    continue
                input_object = recolor(OBJECT_COLOR_64A7C07E, input_patch)
                output_object = recolor(OBJECT_COLOR_64A7C07E, output_patch)
                input_grid = paint(input_grid, input_object)
                output_grid = paint(output_grid, output_object)
                blocked_input |= _expand_64a7c07e(input_indices)
                blocked_output |= _expand_64a7c07e(output_indices)
                placed = True
                break
            if not placed:
                success = False
                break
        foreground_cells = colorcount(input_grid, OBJECT_COLOR_64A7C07E)
        total_cells = grid_size * grid_size
        if success and input_grid != output_grid and foreground_cells * FOUR <= total_cells:
            return {"input": input_grid, "output": output_grid}
