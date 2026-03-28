from arc2.core import *

from .helpers import (
    boundary_cells_4b6b68e5,
    enclosed_cells_4b6b68e5,
    rectangle_region_4b6b68e5,
)
from .verifier import verify_4b6b68e5


PALETTE_4B6B68E5 = tuple(range(ONE, TEN))


def _rectangle_outline_4b6b68e5(
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return box(
        frozenset(
            {
                ORIGIN,
                (height_value - ONE, width_value - ONE),
            }
        )
    )


def _open_outline_4b6b68e5() -> Indices:
    while True:
        x0 = randint(FIVE, TEN)
        x1 = randint(FIVE, TEN)
        x2 = set(_rectangle_outline_4b6b68e5(x0, x1))
        x3 = choice(("top", "bottom", "left", "right"))
        if x3 in ("top", "bottom"):
            x4 = ZERO if x3 == "top" else x0 - ONE
            x5 = randint(ONE, x1 - THREE)
            x6 = randint(ONE, x1 - x5 - TWO)
            for x7 in range(x5, x5 + x6):
                x2.discard((x4, x7))
        else:
            x4 = ZERO if x3 == "left" else x1 - ONE
            x5 = randint(ONE, x0 - THREE)
            x6 = randint(ONE, x0 - x5 - TWO)
            for x7 in range(x5, x5 + x6):
                x2.discard((x7, x4))
        x8 = frozenset(x2)
        if len(x8) <= ONE:
            continue
        if len(enclosed_cells_4b6b68e5(x8)) != ZERO:
            continue
        return x8


def _coarse_shape_4b6b68e5() -> frozenset[tuple[int, int]]:
    while True:
        x0 = randint(TWO, FOUR)
        x1 = randint(TWO, FOUR)
        x2 = randint(THREE, min(SIX, multiply(x0, x1)))
        x3 = {(randint(ZERO, x0 - ONE), randint(ZERO, x1 - ONE))}
        x4 = ZERO
        while len(x3) < x2 and x4 < 200:
            x4 += ONE
            x5 = choice(tuple(x3))
            x6 = tuple(
                x7
                for x7 in dneighbors(x5)
                if 0 <= x7[0] < x0 and 0 <= x7[1] < x1 and x7 not in x3
            )
            if len(x6) == ZERO:
                continue
            x3.add(choice(x6))
        if len(x3) != x2:
            continue
        x8 = rectangle_region_4b6b68e5(
            minimum(tuple(x9[0] for x9 in x3)),
            minimum(tuple(x10[1] for x10 in x3)),
            subtract(
                maximum(tuple(x11[0] for x11 in x3)),
                minimum(tuple(x12[0] for x12 in x3)),
            )
            + ONE,
            subtract(
                maximum(tuple(x13[1] for x13 in x3)),
                minimum(tuple(x14[1] for x14 in x3)),
            )
            + ONE,
        )
        if len(x3) == len(x8):
            continue
        return frozenset(x3)


def _closed_outline_4b6b68e5() -> tuple[Indices, Indices]:
    while True:
        x0 = choice(("rectangle", "rectangle", "irregular"))
        if x0 == "rectangle":
            x1 = randint(FIVE, TEN)
            x2 = randint(FIVE, TEN)
            x3 = _rectangle_outline_4b6b68e5(x1, x2)
        else:
            x1 = randint(THREE, FIVE)
            x2 = _coarse_shape_4b6b68e5()
            x3 = set()
            for x4, x5 in x2:
                x6 = rectangle_region_4b6b68e5(
                    multiply(x4, x1),
                    multiply(x5, x1),
                    x1,
                    x1,
                )
                x3.update(x6)
            x3 = boundary_cells_4b6b68e5(frozenset(x3))
        x7 = enclosed_cells_4b6b68e5(x3)
        if len(x7) < SIX:
            continue
        return x3, x7


def _place_patch_4b6b68e5(
    patch: Indices,
    grid_shape: tuple[int, int],
    reserved: set[tuple[int, int]],
) -> tuple[Indices, set[tuple[int, int]]] | tuple[None, None]:
    x0, x1 = grid_shape
    x2 = height(patch)
    x3 = width(patch)
    if x2 > x0 or x3 > x1:
        return None, None
    x4 = {
        (x5, x6)
        for x5 in range(x0)
        for x6 in range(x1)
    }
    for _ in range(300):
        x5 = randint(ZERO, x0 - x2)
        x6 = randint(ZERO, x1 - x3)
        x7 = shift(patch, (x5, x6))
        x8 = backdrop(x7)
        x9 = set(x8) | set(intersection(outbox(x8), x4))
        if x9 & reserved:
            continue
        return x7, reserved | x9
    return None, None


def _scatter_isolated_4b6b68e5(
    grid: Grid,
    cells: Indices,
    colors: tuple[int, ...],
    count: Integer,
) -> tuple[Grid, tuple[tuple[int, int], ...]]:
    x0 = list(cells)
    shuffle(x0)
    x1 = grid
    x2 = []
    x3 = list(colors)
    if len(x3) == count:
        shuffle(x3)
    for x4 in x0:
        if len(x2) == count:
            break
        if index(x1, x4) != ZERO:
            continue
        if any(index(x1, x5) != ZERO for x5 in neighbors(x4)):
            continue
        x5 = x3[len(x2)] if len(x3) == count else choice(colors)
        x1 = fill(x1, x5, initset(x4))
        x2.append(x4)
    return x1, tuple(x2)


def _build_output_4b6b68e5(
    grid_shape: tuple[int, int],
    structures: tuple[dict, ...],
) -> Grid:
    x0 = canvas(ZERO, grid_shape)
    for x1 in structures:
        x0 = fill(x0, x1["outline_color"], x1["outline"])
    for x2 in structures:
        if x2["fill_color"] is None:
            continue
        x0 = fill(x0, x2["fill_color"], x2["interior"])
    return x0


def generate_4b6b68e5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (16, 30))
        x1 = unifint(diff_lb, diff_ub, (16, 30))
        x2 = randint(ONE, THREE)
        x3 = randint(ZERO, min(TWO, FOUR - x2))
        x4 = sample(PALETTE_4B6B68E5, x2 + x3)
        x5 = []
        x6 = set()
        x7 = set()
        for x8 in range(x2):
            x9, x10 = _closed_outline_4b6b68e5()
            x11, x6 = _place_patch_4b6b68e5(x9, (x0, x1), x6)
            if x11 is None:
                break
            x12 = shift(x10, ulcorner(x11))
            x13 = x4[x8]
            x14 = choice(tuple(x15 for x15 in PALETTE_4B6B68E5 if x15 != x13))
            x16 = tuple(
                x17
                for x17 in PALETTE_4B6B68E5
                if x17 not in (x13, x14)
            )
            x18 = randint(ZERO, min(TWO, len(x16)))
            x19 = sample(x16, x18)
            x20 = {
                "outline": x11,
                "interior": x12,
                "outline_color": x13,
                "fill_color": x14,
                "secondary_colors": x19,
            }
            x5.append(x20)
            x7.update(x11)
            x7.update(x12)
        else:
            for x8 in range(x3):
                x9 = _open_outline_4b6b68e5()
                x10, x6 = _place_patch_4b6b68e5(x9, (x0, x1), x6)
                if x10 is None:
                    break
                x11 = x4[x2 + x8]
                x12 = {
                    "outline": x10,
                    "interior": frozenset(),
                    "outline_color": x11,
                    "fill_color": None,
                    "secondary_colors": tuple(),
                }
                x5.append(x12)
                x7.update(x10)
            else:
                shuffle(x5)
                gi = canvas(ZERO, (x0, x1))
                for x8 in x5:
                    gi = fill(gi, x8["outline_color"], x8["outline"])
                okay = T
                for x8 in x5:
                    if x8["fill_color"] is None:
                        continue
                    x9 = len(x8["interior"])
                    x10 = min(randint(TWO, FOUR), max(TWO, x9 // FOUR))
                    x11 = list(repeat(x8["fill_color"], x10))
                    for x12 in x8["secondary_colors"]:
                        x11.extend(repeat(x12, randint(ONE, TWO)))
                    gi, x13 = _scatter_isolated_4b6b68e5(
                        gi,
                        x8["interior"],
                        tuple(x11),
                        len(x11),
                    )
                    x14 = tuple(index(gi, x15) for x15 in x8["interior"] if index(gi, x15) != ZERO)
                    if len(x13) != len(x11) or mostcommon(x14) != x8["fill_color"]:
                        okay = F
                        break
                if not okay:
                    continue
                x15 = {
                    (x16, x17)
                    for x16 in range(x0)
                    for x17 in range(x1)
                    if (x16, x17) not in x7
                }
                x18 = randint(x2 + x3, max(x2 + x3 + TWO, multiply(TWO, x2 + x3 + ONE)))
                x19 = tuple(PALETTE_4B6B68E5)
                gi, _ = _scatter_isolated_4b6b68e5(
                    gi,
                    frozenset(x15),
                    x19,
                    x18,
                )
                go = _build_output_4b6b68e5((x0, x1), tuple(x5))
                if gi == go:
                    continue
                if verify_4b6b68e5(gi) != go:
                    continue
                return {"input": gi, "output": go}
        continue
