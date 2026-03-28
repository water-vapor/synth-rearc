from synth_rearc.core import *

from .verifier import verify_668eec9a


GRID_SHAPE_668EEC9A = (16, 16)
TRACE_COLORS_668EEC9A = tuple(x0 for x0 in interval(ONE, TEN, ONE) if x0 != SEVEN)
DIAGONAL_TOP_RANGES_668EEC9A = (
    (TWO, SIX),
    (SEVEN, TEN),
    (TEN, 12),
    (12, 12),
)
TRACE_TEMPLATES_668EEC9A = {
    THREE: (
        ("dr_long", "dl_long", "dr_mid"),
        ("dl_long", "dr_long", "dl_mid"),
        ("dr_long", "dr_mid", "dl_short"),
    ),
    FOUR: (
        ("dr_long", "dr_mid", "dl_short", "bar"),
        ("dl_long", "dr_mid", "dr_short", "bar"),
        ("dr_long", "dl_mid", "dr_short", "bar"),
    ),
    FIVE: (
        ("dr_long", "dr_mid", "dl_short", "dr_short", "bar"),
        ("dl_long", "dr_mid", "dr_short", "dl_short", "bar"),
    ),
}
TRACE_SPECS_668EEC9A = {
    "dr_long": {"dir": "dr", "col_bounds": (THREE, SIX), "len_bounds": (EIGHT, 13)},
    "dl_long": {"dir": "dl", "col_bounds": (EIGHT, 11), "len_bounds": (EIGHT, 13)},
    "dr_mid": {"dir": "dr", "col_bounds": (FIVE, SEVEN), "len_bounds": (FIVE, EIGHT)},
    "dl_mid": {"dir": "dl", "col_bounds": (SEVEN, NINE), "len_bounds": (FIVE, EIGHT)},
    "dr_short": {"dir": "dr", "col_bounds": (SIX, EIGHT), "len_bounds": (THREE, FIVE)},
    "dl_short": {"dir": "dl", "col_bounds": (SIX, EIGHT), "len_bounds": (THREE, FIVE)},
}


def _sample_top_rows_668eec9a(
    n_diagonals: int,
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, ...]:
    x0: list[int] = []
    x1 = NEG_ONE
    for x2, x3 in DIAGONAL_TOP_RANGES_668EEC9A[:n_diagonals]:
        x4 = max(x2, x1 + ONE)
        x5 = max(x4, unifint(diff_lb, diff_ub, (x4, x3)))
        x0.append(x5)
        x1 = x5
    return tuple(x0)


def _sample_diagonal_patch_668eec9a(
    kind: str,
    top_row: int,
    occupied: frozenset[tuple[int, int]],
    diff_lb: float,
    diff_ub: float,
) -> frozenset[tuple[int, int]]:
    x0 = TRACE_SPECS_668EEC9A[kind]
    x1 = GRID_SHAPE_668EEC9A[ONE]
    x2 = GRID_SHAPE_668EEC9A[ZERO]
    x3, x4 = x0["col_bounds"]
    x5, x6 = x0["len_bounds"]
    for _ in range(200):
        x7 = randint(x3, x4)
        if x0["dir"] == "dr":
            x8 = min(x2 - top_row, x1 - x7)
            x9 = (top_row, x7)
        else:
            x8 = min(x2 - top_row, x7 + ONE)
            x9 = (top_row, x7)
        x11 = min(x8, x6)
        if x11 < x5:
            continue
        x12 = unifint(diff_lb, diff_ub, (x5, x11))
        if x0["dir"] == "dr":
            x13 = connect(x9, (top_row + x12 - ONE, x7 + x12 - ONE))
        else:
            x13 = connect(x9, (top_row + x12 - ONE, x7 - x12 + ONE))
        if all(x14 not in occupied for x14 in x13):
            return x13
    raise RuntimeError(f"failed to place {kind}")


def _sample_bar_patch_668eec9a(
    occupied: frozenset[tuple[int, int]],
    diff_lb: float,
    diff_ub: float,
) -> frozenset[tuple[int, int]]:
    x0 = GRID_SHAPE_668EEC9A[ZERO] - ONE
    x1 = set(x2[ONE] for x2 in occupied if x2[ZERO] == x0)
    x2: list[tuple[int, int]] = []
    x3 = GRID_SHAPE_668EEC9A[ONE]
    x4 = ZERO
    while x4 < x3:
        if x4 in x1:
            x4 += ONE
            continue
        x5 = x4
        while x4 < x3 and x4 not in x1:
            x4 += ONE
        x6 = decrement(x4)
        if x6 - x5 + ONE >= SEVEN:
            x2.append((x5, x6))
    if not x2:
        raise RuntimeError("failed to place bottom bar")
    x7 = choice(x2)
    x8 = x7[ONE] - x7[ZERO] + ONE
    x9 = max(SEVEN, x8 - FOUR)
    x10 = unifint(diff_lb, diff_ub, (x9, x8))
    x11 = randint(x7[ZERO], x7[ONE] - x10 + ONE)
    x12 = x11 + x10 - ONE
    return connect((x0, x11), (x0, x12))


def generate_668eec9a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        try:
            x0 = choice((THREE, FOUR, FOUR, FIVE))
            x1 = choice(TRACE_TEMPLATES_668EEC9A[x0])
            x2 = sample(TRACE_COLORS_668EEC9A, x0)
            x3 = canvas(SEVEN, GRID_SHAPE_668EEC9A)
            x4: set[tuple[int, int]] = set()
            x5 = x1[-ONE] == "bar"
            x6 = subtract(x0, branch(x5, ONE, ZERO))
            x7 = _sample_top_rows_668eec9a(x6, diff_lb, diff_ub)
            for x8, x9, x10 in zip(x2[:x6], x1[:x6], x7):
                x11 = _sample_diagonal_patch_668eec9a(x9, x10, frozenset(x4), diff_lb, diff_ub)
                x3 = fill(x3, x8, x11)
                x4 |= set(x11)
            if x5:
                x12 = _sample_bar_patch_668eec9a(frozenset(x4), diff_lb, diff_ub)
                x3 = fill(x3, x2[-ONE], x12)
                x4 |= set(x12)
            x13 = repeat(SEVEN, subtract(FIVE, x0))
            x14 = combine(x13, x2)
            x15 = tuple(repeat(x16, THREE) for x16 in x14)
            if verify_668eec9a(x3) != x15:
                continue
            return {"input": x3, "output": x15}
        except RuntimeError:
            continue
