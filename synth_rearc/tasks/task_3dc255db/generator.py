from synth_rearc.core import *

from .helpers import chebyshev_halo_3dc255db
from .helpers import eight_neighbors_3dc255db
from .helpers import extension_patch_3dc255db
from .helpers import normalize_patch_3dc255db
from .helpers import pointing_endpoint_3dc255db
from .helpers import pointing_side_3dc255db
from .helpers import rotate_patch_3dc255db
from .helpers import shift_patch_3dc255db
from .verifier import verify_3dc255db


ORIENTATIONS_3DC255DB = ("up", "up", "right", "left")
ROTATIONS_3DC255DB = {
    "up": ZERO,
    "right": ONE,
    "down": TWO,
    "left": THREE,
}


def _paint_patch_3dc255db(
    grid: Grid,
    value: Integer,
    patch,
) -> Grid:
    return fill(grid, value, patch)


def _weighted_choice_3dc255db(
    values,
):
    return choice(tuple(values))


def _random_top_component_3dc255db(
    center: Integer,
):
    variant = randint(ZERO, TWO)
    if variant == ZERO:
        patch = {
            (ZERO, center),
            (ONE, decrement(center)),
            (ONE, center),
            (ONE, increment(center)),
            (TWO, subtract(center, TWO)),
            (TWO, decrement(center)),
        }
        if randint(ZERO, ONE) == ONE:
            patch.add((TWO, add(center, TWO)))
        return frozenset(patch)
    if variant == ONE:
        patch = {
            (ZERO, center),
            (ONE, center),
            (TWO, decrement(center)),
            (TWO, increment(center)),
        }
        if randint(ZERO, ONE) == ONE:
            patch.add((THREE, subtract(center, TWO)))
        return frozenset(patch)
    return frozenset(
        {
            (ZERO, center),
            (ONE, decrement(center)),
            (ONE, increment(center)),
            (TWO, decrement(center)),
            (TWO, increment(center)),
        }
    )


def _major_up_shape_3dc255db(
    diff_lb: float,
    diff_ub: float,
):
    center = unifint(diff_lb, diff_ub, (FOUR, SIX))
    top_patch = _random_top_component_3dc255db(center)
    top_bottom = lowermost(top_patch)
    bottom_row = frozenset(cell for cell in top_patch if equality(cell[ZERO], top_bottom))
    left_anchor = argmin(bottom_row, lambda cell: cell[ONE])
    right_anchor = argmax(bottom_row, lambda cell: cell[ONE])
    left_len = unifint(diff_lb, diff_ub, (TWO, FIVE))
    right_len = unifint(diff_lb, diff_ub, (TWO, FIVE))
    left_start = add(left_anchor, UNITY)
    right_start = add(right_anchor, RIGHT)
    left_patch = frozenset((add(left_start[ZERO], offset), left_start[ONE]) for offset in interval(ZERO, left_len, ONE))
    right_patch = frozenset((add(right_start[ZERO], offset), right_start[ONE]) for offset in interval(ZERO, right_len, ONE))
    major = frozenset(top_patch | left_patch | right_patch)
    if randint(ZERO, TWO) == ZERO:
        bridge_row = top_bottom
        bridge_col = subtract(right_start[ONE], ONE)
        major = frozenset(major | {(bridge_row, bridge_col)})
    if randint(ZERO, THREE) == ZERO:
        foot_row = add(top_bottom, left_len)
        major = frozenset(major | {(foot_row, decrement(left_start[ONE]))})
    return normalize_patch_3dc255db(major)


def _minor_seed_candidates_3dc255db(
    major,
):
    top = uppermost(major)
    bottom = lowermost(major)
    left = leftmost(major)
    right = rightmost(major)
    candidates = []
    for i in range(top, increment(bottom)):
        for j in range(left, increment(right)):
            cell = (i, j)
            if cell in major:
                continue
            if i == top:
                continue
            if all(neighbor not in major for neighbor in eight_neighbors_3dc255db(cell)):
                continue
            score = (
                invert(i),
                abs(j - ((left + right) / TWO)),
                randint(ZERO, 999),
                cell,
            )
            candidates.append(score)
    candidates = tuple(sorted(candidates))
    return tuple(item[-ONE] for item in candidates)


def _grow_minor_patch_3dc255db(
    major,
    target_size: Integer,
):
    seeds = _minor_seed_candidates_3dc255db(major)
    if len(seeds) == ZERO:
        return frozenset()
    patch = {first(seeds)}
    top = uppermost(major)
    bottom = lowermost(major)
    left = leftmost(major)
    right = rightmost(major)
    interior = frozenset(
        (i, j)
        for i in range(top, increment(bottom))
        for j in range(left, increment(right))
        if (i, j) not in major and flip(equality(i, top))
    )
    while len(patch) < target_size:
        frontier = []
        for cell in tuple(patch):
            for neighbor in eight_neighbors_3dc255db(cell):
                if neighbor in patch or neighbor not in interior:
                    continue
                if all(anchor not in major and anchor not in patch for anchor in eight_neighbors_3dc255db(neighbor)):
                    continue
                frontier.append(
                    (
                        invert(neighbor[ZERO]),
                        abs(neighbor[ONE] - ((left + right) / TWO)),
                        randint(ZERO, 999),
                        neighbor,
                    )
                )
        if len(frontier) == ZERO:
            break
        frontier = tuple(sorted(frontier))
        patch.add(frontier[ZERO][-ONE])
    return frozenset(patch)


def _local_object_3dc255db(
    orientation: str,
    diff_lb: float,
    diff_ub: float,
):
    while True:
        major_up = _major_up_shape_3dc255db(diff_lb, diff_ub)
        max_minor = min(SEVEN, subtract(size(backdrop(major_up)), size(major_up)))
        if max_minor < ONE:
            continue
        minor_size = unifint(diff_lb, diff_ub, (ONE, max_minor))
        minor_up = _grow_minor_patch_3dc255db(major_up, minor_size)
        if len(minor_up) != minor_size:
            continue
        turns = ROTATIONS_3DC255DB[orientation]
        major = rotate_patch_3dc255db(major_up, turns)
        minor = rotate_patch_3dc255db(minor_up, turns)
        if pointing_side_3dc255db(major) != orientation:
            continue
        if len(minor & major) > ZERO:
            continue
        return major, minor


def _choose_colors_3dc255db() -> IntegerTuple:
    major = choice(tuple(interval(ONE, TEN, ONE)))
    minor = choice(tuple(value for value in interval(ONE, TEN, ONE) if value != major))
    return major, minor


def _object_grids_3dc255db(
    major,
    minor,
    major_color: Integer,
    minor_color: Integer,
):
    direction, endpoint = pointing_endpoint_3dc255db(major)
    extension = extension_patch_3dc255db(endpoint, direction, len(minor))
    top = minimum((uppermost(major), uppermost(minor), uppermost(extension)))
    left = minimum((leftmost(major), leftmost(minor), leftmost(extension)))
    offset = invert((top, left))
    major = shift_patch_3dc255db(major, offset)
    minor = shift_patch_3dc255db(minor, offset)
    extension = shift_patch_3dc255db(extension, offset)
    local_height = maximum(
        (
            lowermost(major),
            lowermost(minor),
            lowermost(extension),
        )
    ) + ONE
    local_width = maximum(
        (
            rightmost(major),
            rightmost(minor),
            rightmost(extension),
        )
    ) + ONE
    input_grid = canvas(ZERO, (local_height, local_width))
    input_grid = _paint_patch_3dc255db(input_grid, major_color, major)
    input_grid = _paint_patch_3dc255db(input_grid, minor_color, minor)
    output_grid = canvas(ZERO, (local_height, local_width))
    output_grid = _paint_patch_3dc255db(output_grid, major_color, major)
    output_grid = _paint_patch_3dc255db(output_grid, minor_color, extension)
    return input_grid, output_grid, direction


def _occupied_cells_3dc255db(
    grid: Grid,
):
    return frozenset((i, j) for i, row in enumerate(grid) for j, value in enumerate(row) if flip(equality(value, ZERO)))


def _placeable_3dc255db(
    input_cells,
    output_cells,
    placed_input,
    placed_output,
):
    return both(
        equality(len(chebyshev_halo_3dc255db(input_cells) & placed_input), ZERO),
        equality(len(chebyshev_halo_3dc255db(output_cells) & placed_output), ZERO),
    )


def _offset_candidates_3dc255db(
    grid_height: Integer,
    grid_width: Integer,
    local_input: Grid,
    direction: str,
):
    height_ = len(local_input)
    width_ = len(local_input[ZERO])
    rows = tuple(range(grid_height - height_ + ONE))
    cols = tuple(range(grid_width - width_ + ONE))
    if direction == "up":
        row_order = tuple(sorted(rows, key=lambda value: (value > TWO, value, randint(ZERO, 999))))
        col_order = tuple(sorted(cols, key=lambda value: (randint(ZERO, 999), value)))
    elif direction == "left":
        row_order = tuple(sorted(rows, key=lambda value: (randint(ZERO, 999), value)))
        col_order = tuple(sorted(cols, key=lambda value: (value > TWO, value, randint(ZERO, 999))))
    else:
        row_order = tuple(sorted(rows, key=lambda value: (randint(ZERO, 999), value)))
        col_order = tuple(sorted(cols, key=lambda value: (greater(value, subtract(grid_width, add(width_, THREE))), invert(value), randint(ZERO, 999))))
    return tuple((i, j) for i in row_order for j in col_order)


def _blit_grid_3dc255db(
    base: Grid,
    patch_grid: Grid,
    offset,
):
    out = base
    oi, oj = offset
    for i, row in enumerate(patch_grid):
        for j, value in enumerate(row):
            if equality(value, ZERO):
                continue
            out = fill(out, value, initset((oi + i, oj + j)))
    return out


def generate_3dc255db(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        grid_height = unifint(diff_lb, diff_ub, (TEN, 16))
        grid_width = unifint(diff_lb, diff_ub, (TEN, 17))
        nobjects = unifint(diff_lb, diff_ub, (ONE, THREE))
        input_grid = canvas(ZERO, (grid_height, grid_width))
        output_grid = canvas(ZERO, (grid_height, grid_width))
        placed_input = frozenset()
        placed_output = frozenset()
        ok = True
        for _ in range(nobjects):
            placed = False
            for _ in range(200):
                orientation = choice(ORIENTATIONS_3DC255DB)
                major, minor = _local_object_3dc255db(orientation, diff_lb, diff_ub)
                major_color, minor_color = _choose_colors_3dc255db()
                local_input, local_output, direction = _object_grids_3dc255db(major, minor, major_color, minor_color)
                if greater(len(local_input), grid_height) or greater(len(local_input[ZERO]), grid_width):
                    continue
                input_cells = _occupied_cells_3dc255db(local_input)
                output_cells = _occupied_cells_3dc255db(local_output)
                if equality(input_cells, output_cells):
                    continue
                for offset in _offset_candidates_3dc255db(grid_height, grid_width, local_input, direction):
                    shifted_input = shift_patch_3dc255db(input_cells, offset)
                    shifted_output = shift_patch_3dc255db(output_cells, offset)
                    if flip(_placeable_3dc255db(shifted_input, shifted_output, placed_input, placed_output)):
                        continue
                    candidate_input = _blit_grid_3dc255db(input_grid, local_input, offset)
                    candidate_output = _blit_grid_3dc255db(output_grid, local_output, offset)
                    if verify_3dc255db(candidate_input) != candidate_output:
                        continue
                    input_grid = candidate_input
                    output_grid = candidate_output
                    placed_input = frozenset(placed_input | shifted_input)
                    placed_output = frozenset(placed_output | shifted_output)
                    placed = True
                    break
                if placed:
                    break
            if flip(placed):
                ok = False
                break
        if flip(ok):
            continue
        if equality(input_grid, output_grid):
            continue
        if verify_3dc255db(input_grid) != output_grid:
            continue
        return {"input": input_grid, "output": output_grid}
