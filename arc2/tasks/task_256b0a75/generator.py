from arc2.core import *

from .verifier import verify_256b0a75


COLORS_256B0A75 = tuple(x0 for x0 in range(ONE, TEN) if x0 != EIGHT)
CORNER_OFFSETS_256B0A75 = {
    "ul": ((ZERO, ZERO), (ZERO, ONE), (ONE, ZERO)),
    "ur": ((ZERO, NEG_ONE), (ZERO, ZERO), (ONE, ZERO)),
    "ll": ((NEG_ONE, ZERO), (ZERO, ZERO), (ZERO, ONE)),
    "lr": ((NEG_ONE, ZERO), (ZERO, NEG_ONE), (ZERO, ZERO)),
}


def _corner_loc_256b0a75(
    corner: str,
    top: Integer,
    left: Integer,
    bottom: Integer,
    right: Integer,
) -> IntegerTuple:
    if corner == "ul":
        return (top, left)
    if corner == "ur":
        return (top, right)
    if corner == "ll":
        return (bottom, left)
    return (bottom, right)


def _corner_cells_256b0a75(
    corner: str,
    top: Integer,
    left: Integer,
    bottom: Integer,
    right: Integer,
) -> Indices:
    x0, x1 = _corner_loc_256b0a75(corner, top, left, bottom, right)
    return frozenset((x0 + x2, x1 + x3) for x2, x3 in CORNER_OFFSETS_256B0A75[corner])


def _paint_segments_256b0a75(
    grid: Grid,
    left_groups: dict,
    right_groups: dict,
    up_groups: dict,
    down_groups: dict,
) -> Grid:
    x0 = width(grid)
    x1 = height(grid)
    x2 = grid
    for x3, x4 in left_groups.items():
        x5 = sorted(x4, reverse=True)
        x6 = len(x5)
        for x7 in range(x6):
            x8, x9 = x5[x7]
            x10 = x5[x7 + 1][0] if x7 + 1 < x6 else -1
            x11 = connect((x3, x10 + 1), (x3, x8))
            x2 = fill(x2, x9, x11)
    for x12, x13 in right_groups.items():
        x14 = sorted(x13)
        x15 = len(x14)
        for x16 in range(x15):
            x17, x18 = x14[x16]
            x19 = x14[x16 + 1][0] if x16 + 1 < x15 else x0
            x20 = connect((x12, x17), (x12, x19 - 1))
            x2 = fill(x2, x18, x20)
    for x21, x22 in up_groups.items():
        x23 = sorted(x22, reverse=True)
        x24 = len(x23)
        for x25 in range(x24):
            x26, x27 = x23[x25]
            x28 = x23[x25 + 1][0] if x25 + 1 < x24 else -1
            x29 = connect((x28 + 1, x21), (x26, x21))
            x2 = fill(x2, x27, x29)
    for x30, x31 in down_groups.items():
        x32 = sorted(x31)
        x33 = len(x32)
        for x34 in range(x33):
            x35, x36 = x32[x34]
            x37 = x32[x34 + 1][0] if x34 + 1 < x33 else x1
            x38 = connect((x35, x30), (x37 - 1, x30))
            x2 = fill(x2, x36, x38)
    return x2


def _sample_horizontal_markers_256b0a75(
    lines: tuple,
    positions: tuple,
    total: Integer,
    occupied: set,
) -> tuple | None:
    x0 = []
    for _ in range(300):
        if len(x0) == total:
            return tuple(x0)
        x1 = choice(lines)
        x2 = tuple(x3 for x3 in positions if (x1, x3) not in occupied)
        if len(x2) == ZERO:
            continue
        x3 = choice(x2)
        occupied.add((x1, x3))
        x0.append((x1, x3, choice(COLORS_256B0A75)))
    return None


def _sample_vertical_markers_256b0a75(
    lines: tuple,
    positions: tuple,
    total: Integer,
    occupied: set,
) -> tuple | None:
    x0 = []
    for _ in range(300):
        if len(x0) == total:
            return tuple(x0)
        x1 = choice(lines)
        x2 = tuple(x3 for x3 in positions if (x3, x1) not in occupied)
        if len(x2) == ZERO:
            continue
        x3 = choice(x2)
        occupied.add((x3, x1))
        x0.append((x3, x1, choice(COLORS_256B0A75)))
    return None


def _sample_corner_noise_256b0a75(
    diff_lb: float,
    diff_ub: float,
    top: Integer,
    left: Integer,
    bottom: Integer,
    right: Integer,
    height_value: Integer,
    width_value: Integer,
    occupied: set,
) -> tuple | None:
    x0 = tuple(
        (x1, x2)
        for x1 in range(height_value)
        for x2 in range(width_value)
        if (x1 < top or x1 > bottom) and (x2 < left or x2 > right) and (x1, x2) not in occupied
    )
    x1 = min(len(x0), unifint(diff_lb, diff_ub, (THREE, 12)))
    if x1 < THREE:
        return None
    x2 = sample(x0, x1)
    return tuple((x3, x4, choice(COLORS_256B0A75)) for x3, x4 in x2)


def generate_256b0a75(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (20, 28))
        x1 = unifint(diff_lb, diff_ub, (20, 28))
        x2 = min(10, x0 - EIGHT)
        x3 = min(10, x1 - EIGHT)
        x4 = unifint(diff_lb, diff_ub, (SEVEN, x2))
        x5 = unifint(diff_lb, diff_ub, (SIX, x3))
        x6 = randint(THREE, x0 - x4 - FOUR)
        x7 = randint(THREE, x1 - x5 - FOUR)
        x8 = x6 + x4 - ONE
        x9 = x7 + x5 - ONE
        x10 = choice(("ul", "ur", "ll", "lr"))
        x11 = choice(COLORS_256B0A75)
        x12 = canvas(ZERO, (x0, x1))
        x13 = frozenset()
        for x14 in ("ul", "ur", "ll", "lr"):
            x15 = _corner_cells_256b0a75(x14, x6, x7, x8, x9)
            x16 = branch(equality(x14, x10), x11, EIGHT)
            x13 = combine(x13, recolor(x16, x15))
        x17 = paint(x12, x13)
        x18 = {
            (x19, x20)
            for x19 in range(x6, x8 + ONE)
            for x20 in range(x7, x9 + ONE)
        }
        x19 = set(x18)
        x20 = tuple(range(x6, x8 + ONE))
        x21 = tuple(range(x7, x9 + ONE))
        x22 = tuple(range(x7))
        x23 = tuple(range(x9 + ONE, x1))
        x24 = tuple(range(x6))
        x25 = tuple(range(x8 + ONE, x0))
        if min(len(x22), len(x23), len(x24), len(x25)) == ZERO:
            continue
        x26 = unifint(diff_lb, diff_ub, (ONE, min(FIVE, len(x21) * len(x24))))
        x27 = unifint(diff_lb, diff_ub, (ONE, min(FIVE, len(x21) * len(x25))))
        x28 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, len(x20) * len(x22))))
        x29 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, len(x20) * len(x23))))
        x30 = _sample_vertical_markers_256b0a75(x21, x24, x26, x19)
        if x30 is None:
            continue
        x31 = _sample_vertical_markers_256b0a75(x21, x25, x27, x19)
        if x31 is None:
            continue
        x32 = _sample_horizontal_markers_256b0a75(x20, x22, x28, x19)
        if x32 is None:
            continue
        x33 = _sample_horizontal_markers_256b0a75(x20, x23, x29, x19)
        if x33 is None:
            continue
        x34 = _sample_corner_noise_256b0a75(diff_lb, diff_ub, x6, x7, x8, x9, x0, x1, x19)
        if x34 is None:
            continue
        x35 = {}
        x36 = {}
        x37 = {}
        x38 = {}
        x39 = frozenset()
        for x40, x41, x42 in x30:
            x39 = insert((x42, (x40, x41)), x39)
            x37.setdefault(x41, []).append((x40, x42))
        for x43, x44, x45 in x31:
            x39 = insert((x45, (x43, x44)), x39)
            x38.setdefault(x44, []).append((x43, x45))
        for x46, x47, x48 in x32:
            x39 = insert((x48, (x46, x47)), x39)
            x35.setdefault(x46, []).append((x47, x48))
        for x49, x50, x51 in x33:
            x39 = insert((x51, (x49, x50)), x39)
            x36.setdefault(x49, []).append((x50, x51))
        for x52, x53, x54 in x34:
            x39 = insert((x54, (x52, x53)), x39)
        x55 = paint(x17, x39)
        x56 = frozenset(
            (x57, x58)
            for x57 in range(x0)
            for x58 in range(x1)
            if x6 <= x57 <= x8 or x7 <= x58 <= x9
        )
        x57 = fill(x55, x11, x56)
        x58 = fill(x57, EIGHT, box(ofcolor(x55, EIGHT)))
        x59 = _paint_segments_256b0a75(x58, x35, x36, x37, x38)
        if verify_256b0a75(x55) != x59:
            continue
        return {"input": x55, "output": x59}
