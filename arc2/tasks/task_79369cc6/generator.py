from arc2.core import *

from .verifier import verify_79369cc6


BACKGROUND_BAGS_79369CC6 = (
    (ZERO, ONE, EIGHT),
    (ZERO, ZERO, ONE, EIGHT),
    (ZERO, ONE, ONE, EIGHT),
    (ZERO, ONE, EIGHT, EIGHT),
    (ZERO, ZERO, ONE, ONE, EIGHT, EIGHT),
)

TEMPLATE_LIBRARY_79369CC6 = (
    (
        (SIX, FOUR, SIX),
        (FOUR, SIX, SIX),
        (FOUR, SIX, FOUR),
    ),
    (
        (FOUR, SIX, SIX),
        (FOUR, FOUR, SIX),
        (SIX, FOUR, FOUR),
    ),
    (
        (ZERO, ZERO, ZERO),
        (FOUR, SIX, SIX),
        (SIX, FOUR, FOUR),
    ),
    (
        (FOUR, FOUR, FOUR),
        (SIX, FOUR, FOUR),
        (SIX, SIX, FOUR),
    ),
)

TEMPLATE_POOL_79369CC6 = (
    TEMPLATE_LIBRARY_79369CC6[ZERO],
    TEMPLATE_LIBRARY_79369CC6[ZERO],
    TEMPLATE_LIBRARY_79369CC6[ONE],
    TEMPLATE_LIBRARY_79369CC6[ONE],
    TEMPLATE_LIBRARY_79369CC6[TWO],
    TEMPLATE_LIBRARY_79369CC6[THREE],
    TEMPLATE_LIBRARY_79369CC6[THREE],
)

TEMPLATE_TRANSFORMS_79369CC6 = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
)


def _variant_grids_79369cc6(window: Grid) -> tuple[Grid, ...]:
    variants = []
    seen = set()
    for transform in TEMPLATE_TRANSFORMS_79369CC6:
        transformed = transform(window)
        if transformed in seen:
            continue
        seen.add(transformed)
        variants.append(transformed)
    return tuple(variants)


def _template_score_79369cc6(
    gi: Grid,
    anchor: IntegerTuple,
    window: Grid,
) -> tuple[int, int, int, int] | None:
    height_value = height(gi)
    width_value = width(gi)
    scan_rows = interval(ZERO, subtract(height_value, TWO), ONE)
    scan_cols = interval(ZERO, subtract(width_value, TWO), ONE)
    variants = []
    seen = set()
    for transformed in _variant_grids_79369cc6(window):
        sixes = ofcolor(transformed, SIX)
        key = tuple(sorted(sixes))
        if key in seen:
            continue
        seen.add(key)
        variants.append((sixes, ofcolor(transformed, FOUR)))
    change_windows = ZERO
    for i in scan_rows:
        for j in scan_cols:
            patch = crop(gi, astuple(i, j), astuple(THREE, THREE))
            sixes = ofcolor(patch, SIX)
            for variant_sixes, variant_fours in variants:
                if sixes != variant_sixes:
                    continue
                changed = any(index(patch, loc) != FOUR for loc in variant_fours)
                if changed:
                    change_windows += ONE
                break
    if change_windows == ZERO:
        return None
    four_count = colorcount(window, FOUR)
    six_count = colorcount(window, SIX)
    return (min(four_count, six_count), -anchor[ZERO], four_count, -anchor[ONE])


def _apply_template_79369cc6(
    gi: Grid,
    window: Grid,
) -> Grid:
    height_value = height(gi)
    width_value = width(gi)
    scan_rows = interval(ZERO, subtract(height_value, TWO), ONE)
    scan_cols = interval(ZERO, subtract(width_value, TWO), ONE)
    variants = []
    seen = set()
    for transformed in _variant_grids_79369cc6(window):
        sixes = ofcolor(transformed, SIX)
        key = tuple(sorted(sixes))
        if key in seen:
            continue
        seen.add(key)
        variants.append((sixes, ofcolor(transformed, FOUR)))
    go = gi
    for i in scan_rows:
        for j in scan_cols:
            patch = crop(gi, astuple(i, j), astuple(THREE, THREE))
            sixes = ofcolor(patch, SIX)
            for variant_sixes, variant_fours in variants:
                if sixes != variant_sixes:
                    continue
                go = fill(go, FOUR, shift(variant_fours, astuple(i, j)))
                break
    return go


def _best_template_anchor_79369cc6(gi: Grid) -> IntegerTuple | None:
    height_value = height(gi)
    width_value = width(gi)
    scan_rows = interval(ZERO, subtract(height_value, TWO), ONE)
    scan_cols = interval(ZERO, subtract(width_value, TWO), ONE)
    best_anchor = None
    best_score = None
    for i in scan_rows:
        for j in scan_cols:
            window = crop(gi, astuple(i, j), astuple(THREE, THREE))
            values = palette(window)
            if FOUR not in values or SIX not in values:
                continue
            score = _template_score_79369cc6(gi, astuple(i, j), window)
            if score is None:
                continue
            if best_score is None or score > best_score:
                best_anchor = astuple(i, j)
                best_score = score
    return best_anchor


def _reserve_box_79369cc6(
    anchor: IntegerTuple,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    top, left = anchor
    return frozenset(
        (i, j)
        for i in range(max(ZERO, top - ONE), min(height_value, top + FOUR))
        for j in range(max(ZERO, left - ONE), min(width_value, left + FOUR))
    )


def _sample_anchors_79369cc6(
    height_value: Integer,
    width_value: Integer,
    count: Integer,
) -> tuple[IntegerTuple, ...] | None:
    reserved = frozenset()
    anchors = []
    for _ in range(500):
        candidate = astuple(randint(ZERO, subtract(height_value, THREE)), randint(ZERO, subtract(width_value, THREE)))
        blocked = _reserve_box_79369cc6(candidate, height_value, width_value)
        if len(intersection(blocked, reserved)) > ZERO:
            continue
        anchors.append(candidate)
        reserved = combine(reserved, blocked)
        if len(anchors) == count:
            return tuple(anchors)
    return None


def _random_background_grid_79369cc6(
    height_value: Integer,
    width_value: Integer,
) -> Grid:
    bag = choice(BACKGROUND_BAGS_79369CC6)
    return tuple(tuple(choice(bag) for _ in range(width_value)) for _ in range(height_value))


def generate_79369cc6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        height_value = unifint(diff_lb, diff_ub, (12, 20))
        width_value = unifint(diff_lb, diff_ub, (12, 20))
        area = height_value * width_value
        source_template = choice(TEMPLATE_POOL_79369CC6)
        source_template = choice(_variant_grids_79369cc6(source_template))
        target_count = unifint(diff_lb, diff_ub, (ONE, FOUR))
        anchors = _sample_anchors_79369cc6(height_value, width_value, add(target_count, ONE))
        if anchors is None:
            continue
        source_anchor = first(anchors)
        target_anchors = anchors[ONE:]
        gi = _random_background_grid_79369cc6(height_value, width_value)
        four_source = ofcolor(source_template, FOUR)
        six_source = ofcolor(source_template, SIX)
        gi = fill(gi, FOUR, shift(four_source, source_anchor))
        gi = fill(gi, SIX, shift(six_source, source_anchor))
        source_variants = _variant_grids_79369cc6(source_template)
        for anchor in target_anchors:
            variant = choice(source_variants)
            four_patch = ofcolor(variant, FOUR)
            six_patch = ofcolor(variant, SIX)
            gi = fill(gi, SIX, shift(six_patch, anchor))
        reserved = frozenset()
        for anchor in anchors:
            reserved = combine(reserved, _reserve_box_79369cc6(anchor, height_value, width_value))
        free_cells = tuple(sorted(difference(asindices(gi), reserved)))
        extra_sixes = unifint(
            diff_lb,
            diff_ub,
            (max(2, area // 40), max(6, area // 24)),
        )
        extra_sixes = min(extra_sixes, len(free_cells))
        if extra_sixes > ZERO:
            gi = fill(gi, SIX, frozenset(sample(free_cells, extra_sixes)))
        best_anchor = _best_template_anchor_79369cc6(gi)
        if best_anchor != source_anchor:
            continue
        go = _apply_template_79369cc6(gi, source_template)
        if verify_79369cc6(gi) != go:
            continue
        return {"input": gi, "output": go}
