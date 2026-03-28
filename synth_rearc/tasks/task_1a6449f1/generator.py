from synth_rearc.core import *

from .verifier import verify_1a6449f1


FRAME_COUNT_POOL_1A6449F1 = (TWO, TWO, THREE)
INTERIOR_MOTIFS_1A6449F1 = (
    frozenset({ORIGIN}),
    frozenset({ORIGIN}),
    frozenset({ORIGIN, RIGHT}),
    frozenset({ORIGIN, DOWN}),
    frozenset({ORIGIN, RIGHT, add(RIGHT, RIGHT)}),
    frozenset({ORIGIN, DOWN, add(DOWN, DOWN)}),
    frozenset({ORIGIN, RIGHT, DOWN}),
)
OUTER_MOTIFS_1A6449F1 = (
    frozenset({ORIGIN}),
    frozenset({ORIGIN}),
    frozenset({ORIGIN}),
    frozenset({ORIGIN, RIGHT}),
    frozenset({ORIGIN, DOWN}),
    frozenset({ORIGIN, RIGHT, add(RIGHT, RIGHT)}),
    frozenset({ORIGIN, DOWN, add(DOWN, DOWN)}),
)


def _frame_patch_1a6449f1(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    x0 = frozenset({(top, left), (top + height_value - ONE, left + width_value - ONE)})
    return box(x0)


def _bbox_patch_1a6449f1(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
    dims: IntegerTuple,
    pad: Integer = ZERO,
) -> Indices:
    x0, x1 = dims
    x2 = max(ZERO, top - pad)
    x3 = max(ZERO, left - pad)
    x4 = min(x0 - ONE, top + height_value - ONE + pad)
    x5 = min(x1 - ONE, left + width_value - ONE + pad)
    return frozenset((i, j) for i in range(x2, x4 + ONE) for j in range(x3, x5 + ONE))


def _paint_patch_grid_1a6449f1(
    grid: Grid,
    patch_grid: Grid,
    offset: IntegerTuple,
) -> Grid:
    x0 = frozenset(
        (value, (offset[0] + i, offset[1] + j))
        for i, row in enumerate(patch_grid)
        for j, value in enumerate(row)
        if value != ZERO
    )
    return paint(grid, x0)


def _scatter_motifs_1a6449f1(
    grid: Grid,
    blocked: Indices,
    motif_pool,
    target_cells: Integer,
) -> Grid:
    x0, x1 = shape(grid)
    x2 = grid
    x3 = set()
    x4 = ZERO
    while len(x3) < target_cells and x4 < 400:
        x4 = add(x4, ONE)
        x5 = choice(motif_pool)
        x6 = add(max(i for i, _ in x5), ONE)
        x7 = add(max(j for _, j in x5), ONE)
        if greater(x6, x0) or greater(x7, x1):
            continue
        x8 = randint(ZERO, x0 - x6)
        x9 = randint(ZERO, x1 - x7)
        x10 = frozenset((x8 + i, x9 + j) for i, j in x5)
        if len(intersection(x10, blocked)) > ZERO:
            continue
        if any(cell in x3 for cell in x10):
            continue
        x11 = randint(ONE, NINE)
        x2 = fill(x2, x11, x10)
        x3 |= set(x10)
    return x2


def _sample_inner_grid_1a6449f1(
    diff_lb: float,
    diff_ub: float,
    dims: IntegerTuple,
) -> Grid:
    x0, x1 = dims
    x2 = multiply(x0, x1)
    x3 = min(x2, max(TWO, x2 // FIVE))
    x4 = min(x2, max(x3, x2 * 2 // FIVE))
    x5 = unifint(diff_lb, diff_ub, (x3, x4))
    x6 = canvas(ZERO, dims)
    return _scatter_motifs_1a6449f1(x6, frozenset(), INTERIOR_MOTIFS_1A6449F1, x5)


def _attachment_candidates_1a6449f1(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
    dims: IntegerTuple,
):
    x0, x1 = dims
    x2 = top + height_value - ONE
    x3 = left + width_value - ONE
    x4 = []
    for x5 in range(left + ONE, x3):
        if top >= ONE:
            x4.append(frozenset({(top - ONE, x5)}))
        if top >= TWO:
            x4.append(frozenset({(top - ONE, x5), (top - TWO, x5)}))
        if x2 <= x0 - TWO:
            x4.append(frozenset({(x2 + ONE, x5)}))
        if x2 <= x0 - THREE:
            x4.append(frozenset({(x2 + ONE, x5), (x2 + TWO, x5)}))
    for x5 in range(top + ONE, x2):
        if left >= ONE:
            x4.append(frozenset({(x5, left - ONE)}))
        if left >= TWO:
            x4.append(frozenset({(x5, left - ONE), (x5, left - TWO)}))
        if x3 <= x1 - TWO:
            x4.append(frozenset({(x5, x3 + ONE)}))
        if x3 <= x1 - THREE:
            x4.append(frozenset({(x5, x3 + ONE), (x5, x3 + TWO)}))
    return x4


def _add_attachments_1a6449f1(
    grid: Grid,
    color_value: Integer,
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
    dims: IntegerTuple,
    is_target: Boolean,
) -> tuple[Grid, Indices]:
    x0 = _attachment_candidates_1a6449f1(top, left, height_value, width_value, dims)
    shuffle(x0)
    x1 = branch(is_target, choice((ZERO, ONE, ONE, TWO)), choice((ZERO, ZERO, ONE)))
    x2 = grid
    x3 = frozenset()
    for x4 in x0:
        if equality(x1, ZERO):
            break
        if len(intersection(x4, x3)) > ZERO:
            continue
        x2 = fill(x2, color_value, x4)
        x3 = combine(x3, x4)
        x1 = subtract(x1, ONE)
    return x2, x3


def generate_1a6449f1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(FRAME_COUNT_POOL_1A6449F1)
        x1 = unifint(diff_lb, diff_ub, (18, 29))
        x2 = unifint(diff_lb, diff_ub, (13, 29))
        x3 = (x1, x2)
        x4 = min(12, x1 - FIVE)
        x5 = min(13, x2 - FIVE)
        if x4 < SIX or x5 < SEVEN:
            continue
        x6 = unifint(diff_lb, diff_ub, (SIX, x4))
        x7 = unifint(diff_lb, diff_ub, (SEVEN, x5))
        x8 = multiply(x6, x7)
        x9 = sample(tuple(interval(ONE, TEN, ONE)), x0)
        x10 = [{"height": x6, "width": x7, "color": x9[0], "target": T}]
        x11 = T
        for x12 in range(x0 - ONE):
            x13 = min(x6 - ONE, x1 - FIVE)
            x14 = min(x7 - ONE, x2 - FIVE)
            if x13 < FOUR or x14 < FOUR:
                x11 = F
                break
            x15 = F
            for _ in range(80):
                x16 = unifint(diff_lb, diff_ub, (FOUR, x13))
                x17 = unifint(diff_lb, diff_ub, (FOUR, x14))
                x18 = multiply(x16, x17)
                if x18 >= subtract(x8, EIGHT):
                    continue
                x10.append({"height": x16, "width": x17, "color": x9[x12 + ONE], "target": F})
                x15 = T
                break
            if not x15:
                x11 = F
                break
        if not x11:
            continue
        x19 = canvas(ZERO, x3)
        x20 = frozenset()
        x21 = frozenset()
        x22 = None
        shuffle(x10)
        x23 = T
        for x24 in x10:
            x25 = x24["height"]
            x26 = x24["width"]
            x27 = x1 - x25 - TWO
            x28 = x2 - x26 - TWO
            if x27 < TWO or x28 < TWO:
                x23 = F
                break
            x29 = F
            for _ in range(160):
                x30 = randint(TWO, x27)
                x31 = randint(TWO, x28)
                x32 = _bbox_patch_1a6449f1(x30, x31, x25, x26, x3, TWO)
                if len(intersection(x32, x20)) > ZERO:
                    continue
                x33 = _frame_patch_1a6449f1(x30, x31, x25, x26)
                x34 = subtract((x25, x26), TWO_BY_TWO)
                x35 = _sample_inner_grid_1a6449f1(diff_lb, diff_ub, x34)
                x36 = fill(x19, x24["color"], x33)
                x36 = _paint_patch_grid_1a6449f1(x36, x35, (x30 + ONE, x31 + ONE))
                x36, x37 = _add_attachments_1a6449f1(
                    x36,
                    x24["color"],
                    x30,
                    x31,
                    x25,
                    x26,
                    x3,
                    x24["target"],
                )
                x19 = x36
                x20 = combine(x20, x32)
                x38 = _bbox_patch_1a6449f1(x30, x31, x25, x26, x3, ONE)
                x21 = combine(x21, combine(x38, x37))
                if x24["target"]:
                    x22 = (x30, x31, x25, x26)
                x29 = T
                break
            if not x29:
                x23 = F
                break
        if not x23 or x22 is None:
            continue
        x39 = multiply(x1, x2)
        x40 = unifint(diff_lb, diff_ub, (max(FIVE, x39 // 24), max(SEVEN, x39 // 10)))
        x19 = _scatter_motifs_1a6449f1(x19, x21, OUTER_MOTIFS_1A6449F1, x40)
        x41 = (x22[0] + ONE, x22[1] + ONE)
        x42 = subtract((x22[2], x22[3]), TWO_BY_TWO)
        x43 = crop(x19, x41, x42)
        x44 = remove(ZERO, palette(x43))
        if len(x44) < THREE:
            continue
        if verify_1a6449f1(x19) != x43:
            continue
        return {"input": x19, "output": x43}
