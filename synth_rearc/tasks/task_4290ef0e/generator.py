from synth_rearc.core import *

from .verifier import verify_4290ef0e


def _build_quadrant_4290ef0e(
    depth: int,
    bgc: Integer,
    colors: tuple[int, ...],
) -> Grid:
    x0 = canvas(bgc, (depth + ONE, depth + ONE))
    x1 = x0
    for x2, x3 in enumerate(colors):
        x4 = randint(TWO, depth - x2 + ONE)
        x5 = connect((x2, x2), (x2 + x4 - ONE, x2))
        x6 = connect((x2, x2), (x2, x2 + x4 - ONE))
        x1 = fill(x1, x3, x5)
        x1 = fill(x1, x3, x6)
    return x1


def _build_output_4290ef0e(
    depth: int,
    bgc: Integer,
    colors: tuple[int, ...],
    center_color: Integer | None,
) -> Grid:
    x0 = _build_quadrant_4290ef0e(depth, bgc, colors)
    x1 = canvas(bgc, (depth + ONE, double(depth) + ONE))
    x2 = asobject(x0)
    x3 = shift(asobject(vmirror(x0)), (ZERO, depth))
    x4 = paint(x1, x2)
    x5 = paint(x4, x3)
    x6 = vconcat(x5, hmirror(x5)[ONE:])
    if center_color is None:
        return x6
    return fill(x6, center_color, {center(asindices(x6))})


def _scatter_parts_4290ef0e(
    output: Grid,
    fullh: int,
    fullw: int,
    bgc: Integer,
) -> Grid | None:
    x0 = canvas(bgc, (fullh, fullw))
    x1 = order(
        sfilter(partition(output), lambda x2: color(x2) != bgc),
        width,
    )
    x2 = asindices(x0)
    x3 = x2
    x4 = x0
    for x5 in x1:
        x6 = normalize(x5)
        x7 = toindices(x6)
        x8 = width(x5)
        x9 = max(ZERO, x8 // TWO - ONE)
        x10 = sfilter(x2, lambda x11: x11[ZERO] <= fullh - x8 and x11[ONE] <= fullw - x8)
        x10 = x10 | shift(x10, (-x9, ZERO)) | shift(x10, (ZERO, -x9)) | shift(x10, (x9, ZERO)) | shift(x10, (ZERO, x9))
        if len(x10) == ZERO:
            return None
        x11 = ZERO
        x12 = TEN
        x13 = False
        x14 = ORIGIN
        while x11 < x12 and not x13:
            x11 += ONE
            x14 = choice(totuple(x10))
            if (shift(x7, x14) & x2).issubset(x3):
                x13 = True
        if not x13:
            return None
        x4 = paint(x4, shift(x6, x14))
        x3 = x3 - shift(x7, x14)
    return x4


def generate_4290ef0e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ZERO, TEN, ONE)
    while True:
        x1 = unifint(diff_lb, diff_ub, (TWO, SEVEN))
        x2 = unifint(diff_lb, diff_ub, (multiply(FOUR, x1), 30))
        x3 = unifint(diff_lb, diff_ub, (multiply(FOUR, x1), 30))
        x4 = choice(x0)
        x5 = remove(x4, x0)
        x6 = sample(x5, x1)
        x7 = choice((T, F))
        x8 = branch(x7, choice(difference(x5, x6)), None)
        x9 = _build_output_4290ef0e(x1, x4, x6, x8)
        x10 = _scatter_parts_4290ef0e(x9, x2, x3, x4)
        if x10 is None:
            continue
        if verify_4290ef0e(x10) != x9:
            continue
        return {"input": x10, "output": x9}
