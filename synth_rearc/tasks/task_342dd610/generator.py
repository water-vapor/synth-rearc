from synth_rearc.core import *


GRID_SIZE_RANGE_342DD610 = (TEN, 18)
COLOR_COUNT_OPTIONS_342DD610 = (ONE, ONE, TWO, TWO, THREE, FOUR)
EXTRA_MARKER_CAPS_342DD610 = {
    ONE: TWO,
    TWO: FOUR,
    THREE: FIVE,
    FOUR: SIX,
}
TASK_COLORS_342DD610 = (ONE, TWO, SEVEN, NINE)
OFFSETS_342DD610 = {
    ONE: RIGHT,
    TWO: double(LEFT),
    SEVEN: double(UP),
    NINE: double(DOWN),
}


def _clear_of_neighbors_342dd610(
    cell: IntegerTuple,
    occupied: set[IntegerTuple],
) -> Boolean:
    return all(abs(cell[0] - i) > ONE or abs(cell[1] - j) > ONE for i, j in occupied)


def _candidate_pairs_342dd610(
    h: Integer,
    w: Integer,
    color: Integer,
    input_cells: set[IntegerTuple],
    output_cells: set[IntegerTuple],
) -> list[tuple[IntegerTuple, IntegerTuple]]:
    di, dj = OFFSETS_342DD610[color]
    candidates = []
    for i in interval(ZERO, h, ONE):
        oi = i + di
        if not 0 <= oi < h:
            continue
        for j in interval(ZERO, w, ONE):
            oj = j + dj
            if not 0 <= oj < w:
                continue
            src = (i, j)
            dst = (oi, oj)
            if src in input_cells or dst in output_cells:
                continue
            if not _clear_of_neighbors_342dd610(src, input_cells):
                continue
            if not _clear_of_neighbors_342dd610(dst, output_cells):
                continue
            candidates.append((src, dst))
    return candidates


def _marker_colors_342dd610(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, ...]:
    ncolors = choice(COLOR_COUNT_OPTIONS_342DD610)
    colors = list(sample(TASK_COLORS_342DD610, ncolors))
    markers = list(colors)
    nextra = unifint(diff_lb, diff_ub, (ZERO, EXTRA_MARKER_CAPS_342DD610[ncolors]))
    for _ in interval(ZERO, nextra, ONE):
        markers.append(choice(colors))
    shuffle(markers)
    return tuple(markers)


def generate_342dd610(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        side = unifint(diff_lb, diff_ub, GRID_SIZE_RANGE_342DD610)
        colors = _marker_colors_342dd610(diff_lb, diff_ub)
        gi = canvas(EIGHT, (side, side))
        go = canvas(EIGHT, (side, side))
        input_cells = set()
        output_cells = set()
        success = True
        for color in colors:
            candidates = _candidate_pairs_342dd610(side, side, color, input_cells, output_cells)
            if len(candidates) == ZERO:
                success = False
                break
            src, dst = choice(candidates)
            input_cells.add(src)
            output_cells.add(dst)
            gi = fill(gi, color, frozenset((src,)))
            go = fill(go, color, frozenset((dst,)))
        if not success:
            continue
        if gi == go:
            continue
        if len(input_cells) != len(colors):
            continue
        if len(output_cells) != len(colors):
            continue
        return {"input": gi, "output": go}
