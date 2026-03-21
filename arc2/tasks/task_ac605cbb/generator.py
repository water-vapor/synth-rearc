from arc2.core import *


ALL_COLORS_AC605CBB = (ONE, TWO, THREE, SIX)
INTERSECTION_PAIRS_AC605CBB = ((TWO, THREE), (TWO, SIX))
OFFSET_BY_COLOR_AC605CBB = {
    ONE: add(UP_RIGHT, RIGHT),
    TWO: multiply(FOUR, LEFT),
    THREE: multiply(THREE, DOWN),
    SIX: multiply(SIX, UP),
}


def _valid_positions_ac605cbb(
    h: Integer,
    w: Integer,
    color_value: Integer,
) -> tuple[IntegerTuple, ...]:
    if color_value == ONE:
        rows = range(ONE, h)
        cols = range(ZERO, w - TWO)
    elif color_value == TWO:
        rows = range(ZERO, h)
        cols = range(FOUR, w)
    elif color_value == THREE:
        rows = range(ZERO, h - THREE)
        cols = range(ZERO, w)
    else:
        rows = range(SIX, h)
        cols = range(ZERO, w)
    return tuple((i, j) for i in rows for j in cols)


def _motif_parts_ac605cbb(
    color_value: Integer,
    loc: IntegerTuple,
) -> tuple[Indices, Object]:
    offset = OFFSET_BY_COLOR_AC605CBB[color_value]
    endpoint = add(loc, offset)
    colored = frozenset({loc, endpoint})
    if color_value == ONE:
        gray = frozenset({
            add(loc, RIGHT),
            add(loc, ZERO_BY_TWO),
        })
    else:
        segment = connect(loc, endpoint)
        gray = difference(segment, colored)
    obj = frozenset({(color_value, loc), (color_value, endpoint)})
    return gray, obj


def _render_ac605cbb(
    h: Integer,
    w: Integer,
    seeds: tuple[tuple[Integer, IntegerTuple], ...],
) -> tuple[Grid, Grid, Indices, tuple[tuple[Integer, Integer], ...], Indices, Indices]:
    gi = canvas(ZERO, (h, w))
    gray_parts = []
    colored = frozenset()
    for color_value, loc in seeds:
        gi = fill(gi, color_value, frozenset({loc}))
        gray, obj = _motif_parts_ac605cbb(color_value, loc)
        gray_parts.append((color_value, gray))
        colored = combine(colored, obj)
    gray_union = frozenset()
    intersections = frozenset()
    intersect_pairs = []
    for idx, (color_a, gray_a) in enumerate(gray_parts):
        gray_union = combine(gray_union, gray_a)
        for color_b, gray_b in gray_parts[:idx]:
            overlap = intersection(gray_a, gray_b)
            if len(overlap) > ZERO:
                intersections = combine(intersections, overlap)
                intersect_pairs.append((min(color_a, color_b), max(color_a, color_b)))
    diagonals = frozenset()
    for loc in intersections:
        diagonals = combine(diagonals, shoot(loc, DOWN_LEFT))
    go = fill(gi, FIVE, difference(gray_union, intersections))
    go = fill(go, FOUR, diagonals)
    go = paint(go, colored)
    return gi, go, intersections, tuple(intersect_pairs), gray_union, toindices(colored)


def _sample_intersection_pair_ac605cbb(
    h: Integer,
    w: Integer,
    pair: tuple[Integer, Integer],
) -> tuple[tuple[Integer, IntegerTuple], ...] | None:
    for _ in range(200):
        row2 = randint(ZERO, h - ONE)
        col2 = randint(FOUR, w - ONE)
        step_h = randint(ONE, THREE)
        cross_col = col2 - step_h
        if pair == (TWO, THREE):
            step_v = randint(ONE, TWO)
            row3 = row2 - step_v
            if ZERO <= row3 <= h - FOUR:
                return ((TWO, (row2, col2)), (THREE, (row3, cross_col)))
        else:
            step_v = randint(ONE, FIVE)
            row6 = row2 + step_v
            if SIX <= row6 < h:
                return ((TWO, (row2, col2)), (SIX, (row6, cross_col)))
    return None


def _seed_spacing_ok_ac605cbb(
    seeds: tuple[tuple[Integer, IntegerTuple], ...],
) -> Boolean:
    locs = [loc for _, loc in seeds]
    for idx, (i0, j0) in enumerate(locs):
        for i1, j1 in locs[idx + ONE:]:
            if abs(i0 - i1) + abs(j0 - j1) <= TWO:
                return False
    return True


def _sample_colors_ac605cbb() -> tuple[Integer, ...]:
    ncolors = choice((ONE, TWO, TWO, THREE, THREE, THREE, FOUR))
    if ncolors == ONE:
        return (choice((ONE, TWO, THREE, SIX, SIX)),)
    return tuple(sample(ALL_COLORS_AC605CBB, ncolors))


def generate_ac605cbb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(1000):
        h = unifint(diff_lb, diff_ub, (NINE, 11))
        w = unifint(diff_lb, diff_ub, (NINE, 11))
        colors = _sample_colors_ac605cbb()
        available_pairs = tuple(
            pair for pair in INTERSECTION_PAIRS_AC605CBB
            if pair[ZERO] in colors and pair[ONE] in colors
        )
        want_intersection = len(available_pairs) > ZERO and choice((True, False, False))
        seeds = []
        used = set()
        if want_intersection:
            pair = choice(available_pairs)
            pair_seeds = _sample_intersection_pair_ac605cbb(h, w, pair)
            if pair_seeds is None:
                continue
            seeds.extend(pair_seeds)
            used |= {color_value for color_value, _ in pair_seeds}
        for color_value in colors:
            if color_value in used:
                continue
            candidates = [loc for loc in _valid_positions_ac605cbb(h, w, color_value) if loc not in {loc0 for _, loc0 in seeds}]
            if len(candidates) == ZERO:
                break
            seeds.append((color_value, choice(candidates)))
        if len(seeds) != len(colors):
            continue
        seeds = tuple(sorted(seeds))
        if not _seed_spacing_ok_ac605cbb(seeds):
            continue
        gi, go, intersections, intersect_pairs, gray_union, colored = _render_ac605cbb(h, w, seeds)
        diagonals = difference(ofcolor(go, FOUR), intersections)
        if len(colored) != TWO * len(seeds):
            continue
        if len(intersections) > ONE:
            continue
        if len(intersections) == ONE and len(intersect_pairs) != ONE:
            continue
        if any(pair not in INTERSECTION_PAIRS_AC605CBB for pair in intersect_pairs):
            continue
        if len(intersection(gray_union, colored)) > ZERO:
            continue
        if len(intersection(diagonals, colored)) > ZERO:
            continue
        if len(intersection(diagonals, difference(gray_union, intersections))) > ZERO:
            continue
        if gi == go:
            continue
        return {"input": gi, "output": go}
    raise RuntimeError("failed to generate ac605cbb example")
