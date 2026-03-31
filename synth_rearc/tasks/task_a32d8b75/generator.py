from synth_rearc.core import *

from .helpers import apply_stamp_a32d8b75
from .helpers import cue_turn_a32d8b75
from .helpers import stamp_bounds_a32d8b75
from .helpers import stamp_dims_a32d8b75
from .helpers import stencil_mask_a32d8b75
from .helpers import swap_motif_a32d8b75
from .verifier import verify_a32d8b75


MAIN_HEIGHT_SINGLE_A32D8B75 = (20, 30)
MAIN_WIDTH_SINGLE_A32D8B75 = (20, 22, 24)
MAIN_HEIGHT_MULTI_A32D8B75 = (30,)
MAIN_WIDTH_MULTI_A32D8B75 = (20,)
MOTIF_SIDE_RANGE_A32D8B75 = (2, 5)
STENCIL_HEIGHT_RANGE_A32D8B75 = (4, 8)
STENCIL_WIDTH_RANGE_A32D8B75 = (3, 5)
SINGLE_CORNERS_A32D8B75 = (ZERO, ONE, TWO, THREE)
MULTI_CORNERS_A32D8B75 = (TWO, ZERO)


def _random_motif_a32d8b75(
    colors: tuple[Integer, Integer],
    *,
    max_side: Integer = FIVE,
) -> Grid:
    a, b = colors
    h = randint(TWO, max_side)
    w = randint(TWO, max_side)
    accent_count = randint(ONE, max(TWO, (h * w) // THREE))
    accent_locs = set(sample(list(product(range(h), range(w))), accent_count))
    return tuple(
        tuple(b if (i, j) in accent_locs else a for j in range(w))
        for i in range(h)
    )


def _random_stencil_mask_a32d8b75(
    *,
    h_bounds: tuple[Integer, Integer] = STENCIL_HEIGHT_RANGE_A32D8B75,
    w_bounds: tuple[Integer, Integer] = STENCIL_WIDTH_RANGE_A32D8B75,
) -> Grid:
    h = randint(h_bounds[ZERO], h_bounds[ONE])
    w = randint(w_bounds[ZERO], w_bounds[ONE])
    target = randint(max(FOUR, (h * w) // THREE), max(FIVE, (2 * h * w) // THREE))
    cells = {(randint(ZERO, h - ONE), randint(ZERO, w - ONE))}
    while len(cells) < target:
        ci, cj = choice(tuple(cells))
        di, dj = choice(((ONE, ZERO), (NEG_ONE, ZERO), (ZERO, ONE), (ZERO, NEG_ONE)))
        ni = ci + di
        nj = cj + dj
        if ZERO <= ni < h and ZERO <= nj < w:
            cells.add((ni, nj))
    extra_segments = randint(ONE, TWO)
    for _ in range(extra_segments):
        ci, cj = choice(tuple(cells))
        if choice((T, F)):
            start = randint(ZERO, cj)
            stop = randint(cj, w - ONE)
            for nj in range(start, stop + ONE):
                cells.add((ci, nj))
        else:
            start = randint(ZERO, ci)
            stop = randint(ci, h - ONE)
            for ni in range(start, stop + ONE):
                cells.add((ni, cj))
    min_i = min(i for i, _ in cells)
    max_i = max(i for i, _ in cells)
    min_j = min(j for _, j in cells)
    max_j = max(j for _, j in cells)
    h2 = max_i - min_i + ONE
    w2 = max_j - min_j + ONE
    shifted = {(i - min_i, j - min_j) for i, j in cells}
    return tuple(
        tuple(ONE if (i, j) in shifted else ZERO for j in range(w2))
        for i in range(h2)
    )


def _colorize_stencil_a32d8b75(
    mask: Grid,
    color_value: Integer,
) -> Grid:
    return tuple(
        tuple(color_value if value != ZERO else ZERO for value in row)
        for row in mask
    )


def _vertical_background_a32d8b75(
    dims: IntegerTuple,
    colors: tuple[Integer, Integer],
) -> Grid:
    h, w = dims
    band = randint(FOUR, SIX)
    return tuple(
        tuple(colors[(j // band) % TWO] for j in range(w))
        for _ in range(h)
    )


def _horizontal_background_a32d8b75(
    dims: IntegerTuple,
    colors: tuple[Integer, Integer],
) -> Grid:
    h, w = dims
    band = randint(FOUR, SIX)
    return tuple(
        tuple(colors[(i // band) % TWO] for _ in range(w))
        for i in range(h)
    )


def _diagonal_background_a32d8b75(
    dims: IntegerTuple,
    colors: tuple[Integer, Integer, Integer],
) -> Grid:
    h, w = dims
    lo = randint(THREE, FIVE)
    hi = lo + randint(FOUR, SIX)
    return tuple(
        tuple(
            colors[ZERO]
            if min(i + j, (h - ONE - i) + (w - ONE - j)) < lo
            else colors[ONE]
            if min(i + j, (h - ONE - i) + (w - ONE - j)) < hi
            else colors[TWO]
            for j in range(w)
        )
        for i in range(h)
    )


def _cross_background_a32d8b75(
    dims: IntegerTuple,
    color_value: Integer,
) -> Grid:
    h, w = dims
    grid = canvas(color_value, dims)
    gap_h = randint(FOUR, FIVE)
    gap_w = randint(THREE, FOUR)
    top = (h - gap_h) // TWO
    left = (w - gap_w) // TWO
    grid = fill(grid, ZERO, product(interval(top, top + gap_h, ONE), interval(ZERO, w, ONE)))
    grid = fill(grid, ZERO, product(interval(ZERO, h, ONE), interval(left, left + gap_w, ONE)))
    return grid


def _main_background_a32d8b75(
    dims: IntegerTuple,
    mode: str,
    colors: tuple[Integer, ...],
) -> Grid:
    if mode == "vertical":
        return _vertical_background_a32d8b75(dims, (colors[ZERO], colors[ONE]))
    if mode == "horizontal":
        return _horizontal_background_a32d8b75(dims, (colors[ZERO], colors[ONE]))
    if mode == "cross":
        return _cross_background_a32d8b75(dims, colors[ZERO])
    return _diagonal_background_a32d8b75(dims, (colors[ZERO], colors[ONE], colors[TWO]))


def _icon_columns_a32d8b75(
    corner: Integer,
) -> tuple[Integer, tuple[Integer, ...]]:
    if corner == ZERO:
        return ZERO, (ONE, ONE)
    if corner == ONE:
        return ONE, (ZERO, ONE)
    if corner == TWO:
        return ONE, (ZERO, ZERO)
    return ZERO, (ZERO, ONE)


def _place_cue_panel_a32d8b75(
    dims: IntegerTuple,
    motif: Grid,
    stencil: Grid,
    corner: Integer,
    *,
    decorate: bool,
) -> Grid | None:
    h, w = dims
    grid = canvas(ZERO, dims)
    motif_left = randint(ZERO, w - width(motif))
    motif_top = ONE
    grid = paint(grid, shift(asobject(motif), (motif_top, motif_left)))
    stencil_top = motif_top + height(motif) + randint(TWO, THREE)
    stencil_left = randint(ZERO, w - width(stencil))
    min_cue_rows = FOUR if corner in (ZERO, TWO) else THREE
    cue_gap = randint(TWO, FOUR)
    cue_rows = cue_gap + min_cue_rows
    cue_top = h - cue_rows - randint(ONE, TWO)
    if cue_top <= stencil_top + height(stencil) + ONE:
        return None
    grid = paint(grid, shift(asobject(stencil), (stencil_top, stencil_left)))
    four_col, seven_cols = _icon_columns_a32d8b75(corner)
    four_obj = frozenset({(FOUR, (cue_top, four_col))})
    grid = paint(grid, four_obj)
    if corner in (ZERO, TWO):
        seven_obj = frozenset({(SEVEN, (cue_top + cue_gap, seven_cols[ZERO])), (SEVEN, (cue_top + cue_gap + ONE, seven_cols[ONE]))})
    else:
        seven_obj = frozenset({(SEVEN, (cue_top + cue_gap, seven_cols[ZERO])), (SEVEN, (cue_top + cue_gap, seven_cols[ONE]))})
    grid = paint(grid, seven_obj)
    if decorate:
        divider = stencil_top + height(stencil) + ONE
        if divider < cue_top - ONE:
            grid = fill(grid, SIX, hfrontier((divider, ZERO)) & asindices(grid))
        if cue_top > TWO and cue_top + cue_rows + ONE < h:
            box_rows = interval(cue_top - ONE, min(h, cue_top + cue_rows + ONE), ONE)
            frame = product(box_rows, initset(ZERO)) | product(box_rows, initset(w - ONE))
            grid = fill(grid, SIX, frame)
    return grid


def _available_palette_a32d8b75(
    forbidden: tuple[Integer, ...],
    *,
    allow_zero: bool = F,
) -> tuple[Integer, ...]:
    base = tuple(range(TEN)) if allow_zero else tuple(range(ONE, TEN))
    return tuple(value for value in base if value not in forbidden)


def _non_overlapping_a32d8b75(
    bounds_a: tuple[Integer, Integer, Integer, Integer],
    bounds_b: tuple[Integer, Integer, Integer, Integer],
) -> Boolean:
    top_a, left_a, bottom_a, right_a = bounds_a
    top_b, left_b, bottom_b, right_b = bounds_b
    return either(bottom_a <= top_b, either(bottom_b <= top_a, either(right_a <= left_b, right_b <= left_a)))


def _single_example_a32d8b75(
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    corner = choice(SINGLE_CORNERS_A32D8B75)
    main_h = choice(MAIN_HEIGHT_SINGLE_A32D8B75)
    main_w = choice(MAIN_WIDTH_SINGLE_A32D8B75)
    mode = {ZERO: "vertical", ONE: "horizontal", TWO: "diagonal", THREE: "horizontal"}[corner]
    all_palette = sample(tuple(value for value in range(ONE, TEN) if value not in (FOUR, SIX, SEVEN)), SIX)
    motif_colors = (all_palette[ZERO], all_palette[ONE])
    stencil_color = all_palette[TWO]
    bg_colors = all_palette[THREE:]
    motif = _random_motif_a32d8b75(
        motif_colors,
        max_side=unifint(diff_lb, diff_ub, MOTIF_SIDE_RANGE_A32D8B75),
    )
    stencil_mask = _random_stencil_mask_a32d8b75()
    turn = cue_turn_a32d8b75(corner, ONE)
    stamp_h, stamp_w = stamp_dims_a32d8b75(motif, stencil_mask, turn)
    if either(stamp_h > main_h, stamp_w > main_w):
        return None
    main = _main_background_a32d8b75((main_h, main_w), mode, bg_colors)
    stencil = _colorize_stencil_a32d8b75(stencil_mask, stencil_color)
    panel_w = max(width(motif), width(stencil), TWO)
    if panel_w + ONE + main_w > 30:
        return None
    cue_panel = _place_cue_panel_a32d8b75((main_h, panel_w), motif, stencil, corner, decorate=T)
    if equality(cue_panel, None):
        return None
    gi = hconcat(cue_panel, hconcat(canvas(SIX, (main_h, ONE)), main))
    go = apply_stamp_a32d8b75(main, swap_motif_a32d8b75(motif), stencil_mask, corner, turn)
    if equality(main, go):
        return None
    return {"input": gi, "output": go}


def _multi_example_a32d8b75() -> dict | None:
    main_h = choice(MAIN_HEIGHT_MULTI_A32D8B75)
    main_w = choice(MAIN_WIDTH_MULTI_A32D8B75)
    palette = sample(tuple(value for value in range(ONE, TEN) if value not in (FOUR, SIX, SEVEN)), SIX)
    left_motif_colors = (palette[ZERO], palette[ONE])
    right_motif_colors = (palette[TWO], palette[THREE])
    left_stencil_color = palette[FOUR]
    right_stencil_color = palette[FIVE]
    main = _main_background_a32d8b75((main_h, main_w), "cross", (choice((left_stencil_color, right_stencil_color)),))
    left_corner, right_corner = MULTI_CORNERS_A32D8B75
    left_motif = _random_motif_a32d8b75(left_motif_colors, max_side=THREE)
    right_motif = _random_motif_a32d8b75(right_motif_colors, max_side=THREE)
    left_mask = _random_stencil_mask_a32d8b75(w_bounds=(THREE, FOUR))
    right_mask = _random_stencil_mask_a32d8b75(w_bounds=(THREE, FOUR))
    left_turn = cue_turn_a32d8b75(left_corner, TWO)
    right_turn = cue_turn_a32d8b75(right_corner, TWO)
    left_bounds = stamp_bounds_a32d8b75(main, left_motif, left_mask, left_corner, left_turn)
    right_bounds = stamp_bounds_a32d8b75(main, right_motif, right_mask, right_corner, right_turn)
    if either(left_bounds[TWO] > main_h, left_bounds[THREE] > main_w):
        return None
    if either(right_bounds[TWO] > main_h, right_bounds[THREE] > main_w):
        return None
    if flip(_non_overlapping_a32d8b75(left_bounds, right_bounds)):
        return None
    left_stencil = _colorize_stencil_a32d8b75(left_mask, left_stencil_color)
    right_stencil = _colorize_stencil_a32d8b75(right_mask, right_stencil_color)
    left_panel_w = max(width(left_motif), width(left_stencil), TWO)
    right_panel_w = max(width(right_motif), width(right_stencil), TWO)
    if left_panel_w + right_panel_w + TWO + main_w > 30:
        return None
    left_panel = _place_cue_panel_a32d8b75((main_h, left_panel_w), left_motif, left_stencil, left_corner, decorate=F)
    right_panel = _place_cue_panel_a32d8b75((main_h, right_panel_w), right_motif, right_stencil, right_corner, decorate=F)
    if either(equality(left_panel, None), equality(right_panel, None)):
        return None
    left_swapped = swap_motif_a32d8b75(left_motif)
    right_swapped = swap_motif_a32d8b75(right_motif)
    go = apply_stamp_a32d8b75(main, left_swapped, left_mask, left_corner, left_turn)
    go = apply_stamp_a32d8b75(go, right_swapped, right_mask, right_corner, right_turn)
    if equality(main, go):
        return None
    gi = hconcat(left_panel, hconcat(canvas(SIX, (main_h, ONE)), hconcat(main, hconcat(canvas(SIX, (main_h, ONE)), right_panel))))
    return {"input": gi, "output": go}


def generate_a32d8b75(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        example = _multi_example_a32d8b75() if uniform(0.0, 1.0) < 0.2 else _single_example_a32d8b75(diff_lb, diff_ub)
        if equality(example, None):
            continue
        gi = example["input"]
        go = example["output"]
        if equality(gi, go):
            continue
        if verify_a32d8b75(gi) != go:
            continue
        return example
