from synth_rearc.core import *

from .verifier import verify_f3e14006


FG_COLORS_F3E14006 = remove(ZERO, interval(ZERO, TEN, ONE))


def _render_output_f3e14006(
    dims: IntegerTuple,
    left: Integer,
    right: Integer,
    top: Integer,
    bottom: Integer,
    near: Integer,
    above: Boolean,
    row_major: Integer,
    row_accent: Integer,
    col_major: Integer,
    col_accent: Integer,
    intersection: Integer,
) -> Grid:
    x0 = canvas(ZERO, dims)
    x1 = tuple(j for j in range(left, right + ONE) if even(j - left))
    x2 = tuple(j for j in range(left, right + ONE) if not even(j - left))
    x3 = tuple(i for i in range(top, bottom + ONE) if even(i - top))
    x4 = tuple(i for i in range(top, bottom + ONE) if not even(i - top))
    if above:
        x5 = tuple(i for i in x3 if i > near)
        x6 = tuple(i for i in x3 if i < near)
    else:
        x5 = tuple(i for i in x3 if i < near)
        x6 = tuple(i for i in x3 if i > near)
    x7 = initset(near) if near in x3 else frozenset()
    x8 = fill(x0, row_major, product(x4, x1))
    x9 = fill(x8, intersection, product(x4, x2))
    x10 = fill(x9, row_accent, product(x5, x1))
    x11 = fill(x10, col_major, product(x5, x2))
    x12 = fill(x11, col_accent, product(x6, x1))
    x13 = fill(x12, col_major, product(x6, x2))
    x14 = fill(x13, col_accent, product(x7, x1))
    x15 = fill(x14, intersection, product(x7, x2))
    return x15


def _choose_row_span_f3e14006(
    row_start: Integer,
    row_end: Integer,
    col: Integer,
) -> tuple[Integer, Integer]:
    span_max = min(EIGHT, row_end - row_start + ONE)
    modes = []
    if col - row_start >= THREE:
        modes.append("left")
    if row_end - col >= THREE:
        modes.append("right")
    if row_start < col < row_end:
        modes.append("straddle")
    while True:
        mode = choice(tuple(modes))
        span = randint(THREE, span_max)
        if mode == "left":
            hi = col - ONE
            lo = row_start + span - ONE
            if lo > hi:
                continue
            right = randint(lo, hi)
            left = right - span + ONE
            return left, right
        if mode == "right":
            lo = col + ONE
            hi = row_end - span + ONE
            if lo > hi:
                continue
            left = randint(lo, hi)
            right = left + span - ONE
            return left, right
        lo = max(row_start, col - span + TWO)
        hi = min(col - ONE, row_end - span + ONE)
        if lo > hi:
            continue
        left = randint(lo, hi)
        right = left + span - ONE
        if left < col < right:
            return left, right


def _sample_structure_f3e14006(
    diff_lb: float,
    diff_ub: float,
) -> dict[str, object]:
    h = unifint(diff_lb, diff_ub, (TEN, 24))
    w = unifint(diff_lb, diff_ub, (TEN, 24))
    row_start = randint(ZERO, min(TWO, w - 7))
    row_end = randint(max(row_start + 6, w - 3), w - ONE)
    col_start = randint(ZERO, min(TWO, h - 9))
    col_end = randint(max(col_start + 8, h - 3), h - ONE)
    side = choice(("above", "below"))
    if side == "above":
        row = randint(col_start + THREE, col_end)
    else:
        row = randint(col_start, col_end - THREE)
    col = randint(row_start + ONE, row_end - ONE)
    left, right = _choose_row_span_f3e14006(row_start, row_end, col)
    if side == "above":
        far_gap = randint(TWO, row - col_start)
        near_gap = randint(ONE, far_gap - ONE)
        far = row - far_gap
        near = row - near_gap
    else:
        far_gap = randint(TWO, col_end - row)
        near_gap = randint(ONE, far_gap - ONE)
        far = row + far_gap
        near = row + near_gap
    row_major, row_accent, col_major, col_accent = sample(FG_COLORS_F3E14006, FOUR)
    intersection = choice((row_major, row_major, row_major, col_major))
    return {
        "dims": (h, w),
        "row_start": row_start,
        "row_end": row_end,
        "col_start": col_start,
        "col_end": col_end,
        "row": row,
        "col": col,
        "left": left,
        "right": right,
        "far": far,
        "near": near,
        "above": side == "above",
        "row_major": row_major,
        "row_accent": row_accent,
        "col_major": col_major,
        "col_accent": col_accent,
        "intersection": intersection,
    }


def _render_input_f3e14006(structure: dict[str, object]) -> Grid:
    h, w = structure["dims"]
    row = structure["row"]
    col = structure["col"]
    row_patch = product(
        initset(row),
        interval(structure["row_start"], structure["row_end"] + ONE, ONE),
    )
    col_patch = product(
        interval(structure["col_start"], structure["col_end"] + ONE, ONE),
        initset(col),
    )
    x0 = canvas(ZERO, (h, w))
    x1 = fill(x0, structure["row_major"], row_patch)
    x2 = fill(x1, structure["col_major"], col_patch)
    x3 = fill(
        x2,
        structure["row_accent"],
        frozenset({(row, structure["left"]), (row, structure["right"])}),
    )
    x4 = fill(
        x3,
        structure["col_accent"],
        frozenset({(structure["far"], col), (structure["near"], col)}),
    )
    x5 = fill(x4, structure["intersection"], frozenset({(row, col)}))
    return x5


def generate_f3e14006(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_structure_f3e14006(diff_lb, diff_ub)
        x1 = _render_input_f3e14006(x0)
        x2 = _render_output_f3e14006(
            x0["dims"],
            x0["left"],
            x0["right"],
            branch(x0["above"], x0["far"], x0["row"]),
            branch(x0["above"], x0["row"], x0["far"]),
            x0["near"],
            x0["above"],
            x0["row_major"],
            x0["row_accent"],
            x0["col_major"],
            x0["col_accent"],
            x0["intersection"],
        )
        if verify_f3e14006(x1) != x2:
            continue
        return {"input": x1, "output": x2}
