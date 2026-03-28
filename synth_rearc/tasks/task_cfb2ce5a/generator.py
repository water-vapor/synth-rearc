from synth_rearc.core import *


NONZERO_COLORS = remove(ZERO, interval(ZERO, TEN, ONE))
QUADRANT_SHAPE = (FOUR, FOUR)
GRID_SHAPE = (TEN, TEN)
TR_ORIGIN = (ONE, FIVE)
BL_ORIGIN = (FIVE, ONE)
BR_ORIGIN = (FIVE, FIVE)


def _place(grid: Grid, piece: Grid, origin: tuple[int, int]) -> Grid:
    return paint(grid, shift(asobject(piece), origin))


def _recolor(pattern: Grid, mapping: dict[int, int]) -> Grid:
    return tuple(tuple(mapping[value] for value in row) for row in pattern)


def _sample_template(diff_lb: float, diff_ub: float) -> tuple[Grid, tuple[int, int]]:
    colors = tuple(sample(NONZERO_COLORS, TWO))
    count = unifint(diff_lb, diff_ub, (SIX, EIGHT))
    cells = tuple(product(interval(ZERO, FOUR, ONE), interval(ZERO, FOUR, ONE)))
    while True:
        accent = frozenset(sample(cells, count))
        grid = tuple(
            tuple(colors[ONE] if (i, j) in accent else colors[ZERO] for j in range(FOUR))
            for i in range(FOUR)
        )
        mixed_rows = sum(len(set(row)) > ONE for row in grid)
        mixed_cols = sum(len({row[j] for row in grid}) > ONE for j in range(FOUR))
        if mixed_rows + mixed_cols < TWO:
            continue
        return grid, colors


def _sample_pair(pool: tuple[int, ...]) -> tuple[tuple[int, int], tuple[int, ...]]:
    chosen = tuple(sample(pool, TWO))
    rest = tuple(value for value in pool if value not in chosen)
    return chosen, rest


def _sample_mapping(
    source_colors: tuple[int, int],
    pool: tuple[int, ...],
    allow_background: bool,
) -> tuple[dict[int, int], tuple[int, ...]]:
    if allow_background and choice((T, F)):
        color_ = choice(pool)
        rest = tuple(value for value in pool if value != color_)
        zero_color = choice(source_colors)
        live_color = other(source_colors, zero_color)
        mapping = {zero_color: ZERO, live_color: color_}
        return mapping, rest
    chosen, rest = _sample_pair(pool)
    targets = tuple(sample(chosen, TWO))
    mapping = {source_colors[ZERO]: targets[ZERO], source_colors[ONE]: targets[ONE]}
    return mapping, rest


def _sample_clues(quadrant: Grid) -> Grid:
    clues = canvas(ZERO, QUADRANT_SHAPE)
    for color_ in palette(quadrant) - {ZERO}:
        loc = choice(tuple(ofcolor(quadrant, color_)))
        clues = fill(clues, color_, initset(loc))
    return clues


def generate_cfb2ce5a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    template, source_colors = _sample_template(diff_lb, diff_ub)
    top_right_pattern = vmirror(template)
    bottom_left_pattern = hmirror(template)
    bottom_right_pattern = rot180(template)

    pool = tuple(value for value in NONZERO_COLORS if value not in source_colors)
    top_right_mapping, pool = _sample_mapping(source_colors, pool, F)
    bottom_left_mapping, pool = _sample_mapping(source_colors, pool, F)
    bottom_right_mapping, pool = _sample_mapping(source_colors, pool, T)

    top_right = _recolor(top_right_pattern, top_right_mapping)
    bottom_left = _recolor(bottom_left_pattern, bottom_left_mapping)
    bottom_right = _recolor(bottom_right_pattern, bottom_right_mapping)

    gi = canvas(ZERO, GRID_SHAPE)
    gi = _place(gi, template, UNITY)
    gi = _place(gi, _sample_clues(top_right), TR_ORIGIN)
    gi = _place(gi, _sample_clues(bottom_left), BL_ORIGIN)
    gi = _place(gi, _sample_clues(bottom_right), BR_ORIGIN)

    go = canvas(ZERO, GRID_SHAPE)
    go = _place(go, template, UNITY)
    go = _place(go, top_right, TR_ORIGIN)
    go = _place(go, bottom_left, BL_ORIGIN)
    go = _place(go, bottom_right, BR_ORIGIN)

    return {"input": gi, "output": go}
