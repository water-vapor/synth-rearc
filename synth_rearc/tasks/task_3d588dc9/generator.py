from synth_rearc.core import *


BG_3D588DC9 = SEVEN
GRAY_3D588DC9 = FIVE
BLACK_3D588DC9 = ZERO
MARK_3D588DC9 = SIX
DIM_3D588DC9 = 16
TRI_HEIGHT_3D588DC9 = FOUR
WEDGE_H_RIGHT_3D588DC9 = frozenset(
    {
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
    }
)
WEDGE_H_LEFT_3D588DC9 = frozenset((i, 5 - j) for i, j in WEDGE_H_RIGHT_3D588DC9)
WEDGE_V_UP_3D588DC9 = frozenset(
    {
        (0, 1),
        (1, 1),
        (2, 0),
        (2, 1),
        (2, 2),
        (3, 0),
        (3, 1),
        (3, 2),
        (4, 0),
        (4, 1),
        (4, 2),
        (5, 0),
        (5, 1),
        (5, 2),
    }
)
WEDGE_V_DOWN_3D588DC9 = frozenset(
    {
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
        (3, 0),
        (3, 1),
        (3, 2),
        (4, 1),
        (5, 1),
    }
)
WEDGES_3D588DC9 = {
    "h_right": WEDGE_H_RIGHT_3D588DC9,
    "h_left": WEDGE_H_LEFT_3D588DC9,
    "v_up": WEDGE_V_UP_3D588DC9,
    "v_down": WEDGE_V_DOWN_3D588DC9,
}
OBJECT_COLORS_3D588DC9 = tuple(
    x0 for x0 in interval(ONE, TEN, ONE) if x0 not in (GRAY_3D588DC9, MARK_3D588DC9, BG_3D588DC9)
)


def _triangle_patch_3d588dc9(
    length: Integer,
    right_aligned: Boolean,
    height: Integer = TRI_HEIGHT_3D588DC9,
) -> Indices:
    if right_aligned:
        return frozenset((i, j) for i in range(height) for j in range(i, length))
    return frozenset((i, j) for i in range(height) for j in range(length - i))


def _row_overlap_3d588dc9(x0: Patch, x1: Patch) -> Integer:
    y0 = {i for i, _ in toindices(x0)}
    y1 = {i for i, _ in toindices(x1)}
    return len(y0 & y1)


def _horizontal_gap_3d588dc9(x0: Patch, x1: Patch) -> Integer:
    y0 = rightmost(x0)
    y1 = leftmost(x0)
    y2 = rightmost(x1)
    y3 = leftmost(x1)
    if y0 < y3:
        return y3 - y0 - ONE
    if y2 < y1:
        return y1 - y2 - ONE
    return ZERO


def _halo_3d588dc9(x0: Indices) -> Indices:
    y0 = set(x0)
    for y1 in tuple(x0):
        for y2 in neighbors(y1):
            if 0 <= y2[0] < DIM_3D588DC9 and 0 <= y2[1] < DIM_3D588DC9:
                y0.add(y2)
    return frozenset(y0)


def _contact_and_tail_3d588dc9(
    x0: Indices,
    x1: Boolean,
) -> tuple[Indices, Indices]:
    y0 = normalize(x0)
    y1 = tuple(sum(1 for i, _ in y0 if i == k) for k in range(height(y0)))
    y2 = tuple(sum(1 for _, j in y0 if j == k) for k in range(width(y0)))
    y3 = ulcorner(x0)
    if height(y0) == THREE:
        y4 = tuple(k for k, v in enumerate(y2) if v == THREE)
        y5 = tuple(k for k, v in enumerate(y2) if v == ONE)
        y6 = min(y4) if x1 else max(y4)
        y7 = frozenset((i, j) for i, j in y0 if j == y6)
        y8 = frozenset((i, j) for i, j in y0 if j in y5)
        return shift(y7, y3), shift(y8, y3)
    y4 = tuple(k for k, v in enumerate(y1) if v == THREE)
    y5 = tuple(k for k, v in enumerate(y1) if v == ONE)
    y6 = min(j for i, j in y0 if i in y4) if x1 else max(j for i, j in y0 if i in y4)
    y7 = frozenset((i, j) for i, j in y0 if i in y4 and j == y6)
    y8 = frozenset((i, j) for i, j in y0 if i in y5)
    return shift(y7, y3), shift(y8, y3)


def _place_ok_3d588dc9(
    x0: Indices,
    x1: set[IntegerTuple],
) -> Boolean:
    if any(not (0 <= i < DIM_3D588DC9 and 0 <= j < DIM_3D588DC9) for i, j in x0):
        return F
    return len(intersection(x0, frozenset(x1))) == ZERO


def generate_3d588dc9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = canvas(BG_3D588DC9, (DIM_3D588DC9, DIM_3D588DC9))
        x1 = {}
        x2 = set()

        x3 = choice(("left", "right"))
        x4 = unifint(diff_lb, diff_ub, (FIVE, EIGHT))
        x5 = _triangle_patch_3d588dc9(x4, x3 == "right")
        x6 = choice(("v_up", "v_down", "h_right") if x3 == "left" else ("v_up", "v_down", "h_left"))
        x7 = WEDGES_3D588DC9[x6]
        x8 = height(x7)
        x9 = width(x7)
        x10 = [y0 for y0 in range(DIM_3D588DC9 - x8 + ONE)]
        x11 = []
        for y0 in x10:
            y1 = shift(x5, (y0, ZERO))
            if x3 == "left":
                y2 = list(range(DIM_3D588DC9 - x9 + ONE))
            else:
                y2 = list(range(DIM_3D588DC9 - x9 + ONE))
            for y3 in y2:
                if x3 == "left":
                    y4 = shift(x5, (y0, randint(ZERO, TWO)))
                    y5 = randint(ONE, FOUR)
                    y6 = shift(x7, (randint(ZERO, DIM_3D588DC9 - x8), rightmost(y4) + y5 + ONE))
                else:
                    y4 = shift(x5, (y0, DIM_3D588DC9 - width(x5) - randint(ZERO, TWO)))
                    y5 = randint(ONE, FOUR)
                    y6 = shift(x7, (randint(ZERO, DIM_3D588DC9 - x8), leftmost(y4) - y5 - x9))
                if not _place_ok_3d588dc9(y4, x2):
                    continue
                if not _place_ok_3d588dc9(y6, x2 | set(_halo_3d588dc9(y4))):
                    continue
                y7 = _row_overlap_3d588dc9(y4, y6)
                if y7 == ZERO:
                    continue
                y8 = _horizontal_gap_3d588dc9(y4, y6)
                x11.append((y7, -y8, y4, y6))
        if len(x11) == ZERO:
            continue
        x12, x13, x14, x15 = choice(tuple(x11))
        x1["gray"] = x14
        x1["target"] = x15
        x2 |= set(_halo_3d588dc9(x14))
        x2 |= set(_halo_3d588dc9(x15))

        x16 = choice(OBJECT_COLORS_3D588DC9)
        x17 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x18 = unifint(diff_lb, diff_ub, (x17, min(EIGHT, add(x17, TWO))))
        x19 = _triangle_patch_3d588dc9(x18, choice((T, F)), x17)
        x20 = False
        for _ in range(200):
            y0 = shift(
                x19,
                (
                    randint(ZERO, DIM_3D588DC9 - height(x19)),
                    randint(ZERO, DIM_3D588DC9 - width(x19)),
                ),
            )
            if not _place_ok_3d588dc9(y0, x2):
                continue
            x1["other_color"] = (x16, y0)
            x2 |= set(_halo_3d588dc9(y0))
            x20 = True
            break
        if not x20:
            continue

        x21 = False
        for _ in range(300):
            y0 = choice(tuple(WEDGES_3D588DC9.values()))
            y1 = shift(
                y0,
                (
                    randint(ZERO, DIM_3D588DC9 - height(y0)),
                    randint(ZERO, DIM_3D588DC9 - width(y0)),
                ),
            )
            y2 = (_row_overlap_3d588dc9(y1, x14), -_horizontal_gap_3d588dc9(y1, x14))
            if y2 >= (x12, x13):
                continue
            if not _place_ok_3d588dc9(y1, x2):
                continue
            x1["other_black"] = y1
            x2 |= set(_halo_3d588dc9(y1))
            x21 = True
            break
        if not x21:
            continue

        if choice((T, T, F)):
            x22 = choice((frozenset({(0, 0)}), frozenset({(0, 0), (0, 1), (1, 0), (1, 1)})))
            for _ in range(120):
                y0 = shift(
                    x22,
                    (
                        randint(ZERO, DIM_3D588DC9 - height(x22)),
                        randint(ZERO, DIM_3D588DC9 - width(x22)),
                    ),
                )
                if not _place_ok_3d588dc9(y0, x2):
                    continue
                x1["small_black"] = y0
                x2 |= set(_halo_3d588dc9(y0))
                break

        x23 = tuple(x24 for x24 in OBJECT_COLORS_3D588DC9 if x24 != x16)
        x24 = randint(ONE, TWO)
        x25 = []
        for _ in range(200):
            y0 = []
            y1 = set()
            for _ in range(x24):
                y2 = choice(x23)
                y3 = (randint(ZERO, DIM_3D588DC9 - ONE), randint(ZERO, DIM_3D588DC9 - ONE))
                if y3 in x2 or y3 in y1:
                    break
                y0.append((y2, y3))
                y1.add(y3)
            else:
                x25 = y0
                x2 |= y1
                break
        if x24 > ZERO and len(x25) != x24:
            continue

        x0 = fill(x0, GRAY_3D588DC9, x14)
        x0 = fill(x0, BLACK_3D588DC9, x15)
        x0 = fill(x0, x16, x1["other_color"][ONE])
        x0 = fill(x0, BLACK_3D588DC9, x1["other_black"])
        if "small_black" in x1:
            x0 = fill(x0, BLACK_3D588DC9, x1["small_black"])
        for y0, y1 in x25:
            x0 = fill(x0, y0, initset(y1))

        x26 = greater(leftmost(x15), rightmost(x14))
        x27, x28 = _contact_and_tail_3d588dc9(x15, x26)
        x29 = fill(x0, BG_3D588DC9, x28)
        x30 = fill(x29, MARK_3D588DC9, x27)
        return {"input": x0, "output": x30}
