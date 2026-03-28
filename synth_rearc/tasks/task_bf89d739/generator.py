from synth_rearc.core import *


def _render_bf89d739(
    dims: IntegerTuple,
    spine_a: IntegerTuple,
    spine_b: IntegerTuple,
    branches: tuple[IntegerTuple, ...],
) -> dict:
    gi = canvas(ZERO, dims)
    gi = fill(gi, TWO, initset(spine_a))
    gi = fill(gi, TWO, initset(spine_b))
    for loc in branches:
        gi = fill(gi, TWO, initset(loc))
    path = connect(spine_a, spine_b)
    horizontal = equality(spine_a[0], spine_b[0])
    for loc in branches:
        foot = (spine_a[0], loc[1]) if horizontal else (loc[0], spine_a[1])
        path = combine(path, connect(loc, foot))
    go = underfill(gi, THREE, path)
    return {"input": gi, "output": go}


def _sample_horizontal_bf89d739(
    h: int,
    w: int,
    branch_count: int,
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    max_span = min(w - THREE, 11)
    min_span = max(FOUR, branch_count + TWO)
    if max_span < min_span:
        return None
    span = unifint(diff_lb, diff_ub, (min_span, max_span))
    start_max = subtract(w - TWO, span)
    if start_max < ONE:
        return None
    row = randint(ONE, h - TWO)
    rows = [i for i in range(ONE, h - ONE) if i != row]
    if len(rows) < branch_count:
        return None
    left = randint(ONE, start_max)
    right = add(left, span)
    anchors = list(range(left + ONE, right))
    if len(anchors) < branch_count:
        return None
    anchor_cols = sorted(sample(anchors, branch_count))
    branch_rows = sorted(sample(rows, branch_count))
    spine_a = (row, left)
    spine_b = (row, right)
    branches = tuple((i, j) for i, j in zip(branch_rows, anchor_cols))
    return _render_bf89d739((h, w), spine_a, spine_b, branches)


def _sample_vertical_bf89d739(
    h: int,
    w: int,
    branch_count: int,
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    max_span = min(h - THREE, 11)
    min_span = max(FOUR, branch_count + TWO)
    if max_span < min_span:
        return None
    span = unifint(diff_lb, diff_ub, (min_span, max_span))
    start_max = subtract(h - TWO, span)
    if start_max < ONE:
        return None
    col = randint(ONE, w - TWO)
    cols = [j for j in range(ONE, w - ONE) if j != col]
    if len(cols) < branch_count:
        return None
    top = randint(ONE, start_max)
    bottom = add(top, span)
    anchors = list(range(top + ONE, bottom))
    if len(anchors) < branch_count:
        return None
    anchor_rows = sorted(sample(anchors, branch_count))
    branch_cols = sorted(sample(cols, branch_count))
    spine_a = (top, col)
    spine_b = (bottom, col)
    branches = tuple((i, j) for i, j in zip(anchor_rows, branch_cols))
    return _render_bf89d739((h, w), spine_a, spine_b, branches)


def generate_bf89d739(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (12, 22))
        w = unifint(diff_lb, diff_ub, (10, 20))
        orientation = choice((ZERO, ONE))
        if equality(orientation, ZERO):
            max_branches = min(FIVE, h - THREE, w - FOUR)
            if max_branches < TWO:
                continue
            branch_count = unifint(diff_lb, diff_ub, (TWO, max_branches))
            example = _sample_horizontal_bf89d739(h, w, branch_count, diff_lb, diff_ub)
        else:
            max_branches = min(FIVE, h - FOUR, w - THREE)
            if max_branches < TWO:
                continue
            branch_count = unifint(diff_lb, diff_ub, (TWO, max_branches))
            example = _sample_vertical_bf89d739(h, w, branch_count, diff_lb, diff_ub)
        if example is None:
            continue
        if equality(example["input"], example["output"]):
            continue
        return example
