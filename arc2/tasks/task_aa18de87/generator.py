from arc2.core import *


MARKER_COLORS_AA18DE87 = remove(TWO, remove(ZERO, interval(ZERO, TEN, ONE)))
MAIN_LEN_BOUNDS_AA18DE87 = (THREE, FIVE)
TOP_PAD_CHOICES_AA18DE87 = (ZERO,)
LEFT_PAD_CHOICES_AA18DE87 = (ZERO, ZERO, ONE, TWO)
BOTTOM_PAD_CHOICES_AA18DE87 = (ZERO,)
RIGHT_PAD_CHOICES_AA18DE87 = (ZERO, ZERO, ONE, TWO)


def _segment_union_aa18de87(
    segments,
):
    x0 = frozenset()
    for x1, x2 in segments:
        x0 = combine(x0, connect(x1, x2))
    return x0


def _render_output_aa18de87(
    gi: Grid,
) -> Grid:
    x0 = ofcolor(gi, ZERO)
    x1 = difference(asindices(gi), x0)
    x2 = order({x3[0] for x3 in x1}, identity)
    x3 = gi
    for x4 in x2:
        x5 = tuple(x6[1] for x6 in x1 if x6[0] == x4)
        if greater(size(x5), ONE):
            x6 = connect((x4, minimum(x5)), (x4, maximum(x5)))
            x7 = intersection(x6, x0)
            x3 = fill(x3, TWO, x7)
    return x3


def _converging_patch_aa18de87(
    diff_lb: float,
    diff_ub: float,
):
    x0 = unifint(diff_lb, diff_ub, MAIN_LEN_BOUNDS_AA18DE87)
    x1 = unifint(diff_lb, diff_ub, MAIN_LEN_BOUNDS_AA18DE87)
    x2 = ZERO
    x3 = ZERO
    if greater(x0, THREE) and choice((T, F)) == T:
        x2 = randint(TWO, min(THREE, subtract(x0, ONE)))
    if greater(x1, THREE) and choice((T, F)) == T:
        x3 = randint(TWO, min(THREE, subtract(x1, ONE)))
    x4 = max(subtract(x0, ONE), subtract(x1, ONE))
    x5 = subtract(x2, ONE) if positive(x2) else ZERO
    x6 = subtract(x3, ONE) if positive(x3) else ZERO
    x7 = add(subtract(x0, ONE), x5)
    x8 = (x4, x7)
    x9 = (subtract(x4, subtract(x0, ONE)), x5)
    x10 = (subtract(x4, subtract(x1, ONE)), add(x7, subtract(x1, ONE)))
    x11 = [(x9, x8), (x10, x8)]
    if positive(x2):
        x12 = (add(x9[ZERO], x5), ZERO)
        x11.append((x9, x12))
    if positive(x3):
        x13 = (add(x10[ZERO], x6), add(x10[ONE], x6))
        x11.append((x10, x13))
    return _segment_union_aa18de87(tuple(x11))


def _diverging_patch_aa18de87(
    diff_lb: float,
    diff_ub: float,
):
    x0 = unifint(diff_lb, diff_ub, MAIN_LEN_BOUNDS_AA18DE87)
    x1 = unifint(diff_lb, diff_ub, MAIN_LEN_BOUNDS_AA18DE87)
    x2 = (ZERO, subtract(x0, ONE))
    x3 = (subtract(x0, ONE), ZERO)
    x4 = (subtract(x1, ONE), add(subtract(x0, ONE), subtract(x1, ONE)))
    return _segment_union_aa18de87(((x2, x3), (x2, x4)))


def generate_aa18de87(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(MARKER_COLORS_AA18DE87)
        x1 = choice(("converge", "converge", "converge", "diverge"))
        x2 = _converging_patch_aa18de87(diff_lb, diff_ub) if x1 == "converge" else _diverging_patch_aa18de87(diff_lb, diff_ub)
        x3 = shape(x2)
        x4 = choice(TOP_PAD_CHOICES_AA18DE87)
        x5 = choice(LEFT_PAD_CHOICES_AA18DE87)
        x6 = choice(BOTTOM_PAD_CHOICES_AA18DE87)
        x7 = choice(RIGHT_PAD_CHOICES_AA18DE87)
        x8 = add(x3, (add(x4, x6), add(x5, x7)))
        x9 = shift(x2, (x4, x5))
        gi = fill(canvas(ZERO, x8), x0, x9)
        go = _render_output_aa18de87(gi)
        if width(gi) < EIGHT:
            continue
        if width(gi) > 12:
            continue
        x10 = tuple(
            x11
            for x11 in order({x12[0] for x12 in x9}, identity)
            if greater(size(tuple(x13[1] for x13 in x9 if x13[0] == x11)), ONE)
        )
        if size(x10) < TWO:
            continue
        if colorcount(go, TWO) < TWO:
            continue
        return {"input": gi, "output": go}
