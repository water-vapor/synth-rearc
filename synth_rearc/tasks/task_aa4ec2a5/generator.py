from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    connected_patch_aa4ec2a5,
    enclosed_cells_aa4ec2a5,
    halo8_aa4ec2a5,
    rectangle_region_aa4ec2a5,
)


BG_AA4EC2A5 = FOUR
FG_AA4EC2A5 = ONE


def _normalize_patch_aa4ec2a5(
    patch: Patch,
) -> Indices:
    return frozenset(normalize(patch))


def _touches_patch_aa4ec2a5(
    a: Patch,
    b: Patch,
) -> Boolean:
    x0 = toindices(a)
    x1 = toindices(b)
    if positive(size(intersection(x0, x1))):
        return True
    return any(
        positive(size(intersection(dneighbors(x2), x1)))
        for x2 in x0
    )


def _tiny_plain_patch_aa4ec2a5() -> Indices:
    x0 = choice(("cell", "domino_h", "domino_v", "square", "el"))
    if x0 == "cell":
        return frozenset({ORIGIN})
    if x0 == "domino_h":
        return frozenset({ORIGIN, RIGHT})
    if x0 == "domino_v":
        return frozenset({ORIGIN, DOWN})
    if x0 == "square":
        return rectangle_region_aa4ec2a5(ZERO, ZERO, TWO, TWO)
    return frozenset({ORIGIN, RIGHT, DOWN})


def _plain_union_patch_aa4ec2a5() -> Indices:
    for _ in range(300):
        x0 = randint(THREE, TEN)
        x1 = randint(THREE, TEN)
        x2 = choice((TWO, TWO, THREE, THREE, FOUR))
        x3 = frozenset()
        for x4 in range(x2):
            x5 = None
            for _ in range(80):
                x6 = randint(ONE, x0)
                x7 = randint(ONE, x1)
                x8 = randint(ZERO, x0 - x6)
                x9 = randint(ZERO, x1 - x7)
                x10 = rectangle_region_aa4ec2a5(x8, x9, x6, x7)
                if equality(x4, ZERO) or _touches_patch_aa4ec2a5(x10, x3):
                    x5 = x10
                    break
            if x5 is None:
                x3 = frozenset()
                break
            x3 = frozenset(set(x3) | set(x5))
        if len(x3) <= ONE:
            continue
        x11 = _normalize_patch_aa4ec2a5(x3)
        if not connected_patch_aa4ec2a5(x11):
            continue
        if len(enclosed_cells_aa4ec2a5(x11)) != ZERO:
            continue
        return x11
    return rectangle_region_aa4ec2a5(ZERO, ZERO, randint(ONE, SIX), randint(ONE, EIGHT))


def _sample_plain_patch_aa4ec2a5() -> Indices:
    x0 = choice(("tiny", "rect", "rect", "union", "union", "union"))
    if x0 == "tiny":
        return _tiny_plain_patch_aa4ec2a5()
    if x0 == "rect":
        return rectangle_region_aa4ec2a5(
            ZERO,
            ZERO,
            randint(ONE, EIGHT),
            randint(ONE, TEN),
        )
    return _plain_union_patch_aa4ec2a5()


def _trim_holey_patch_aa4ec2a5(
    patch: Patch,
) -> Indices:
    x0 = frozenset(toindices(patch))
    x1 = randint(ZERO, THREE)
    for _ in range(x1):
        x2 = []
        x3 = height(x0)
        x4 = width(x0)
        if x3 <= FOUR and x4 <= FOUR:
            break
        for x5 in ("top", "bottom"):
            x6 = randint(ONE, max(ONE, x3 // THREE))
            x7 = randint(ONE, max(ONE, x4 - ONE))
            x8 = randint(ZERO, x4 - x7)
            x9 = ZERO if x5 == "top" else x3 - x6
            x2.append(rectangle_region_aa4ec2a5(x9, x8, x6, x7))
        for x5 in ("left", "right"):
            x6 = randint(ONE, max(ONE, x3 - ONE))
            x7 = randint(ONE, max(ONE, x4 // THREE))
            x8 = randint(ZERO, x3 - x6)
            x9 = ZERO if x5 == "left" else x4 - x7
            x2.append(rectangle_region_aa4ec2a5(x8, x9, x6, x7))
        shuffle(x2)
        for x10 in x2:
            x11 = frozenset(set(x0) - set(x10))
            if len(x11) <= ONE:
                continue
            if not connected_patch_aa4ec2a5(x11):
                continue
            if len(enclosed_cells_aa4ec2a5(x11)) == ZERO:
                continue
            x0 = _normalize_patch_aa4ec2a5(x11)
            break
    return x0


def _sample_holey_patch_aa4ec2a5() -> Indices:
    for _ in range(300):
        x0 = randint(FOUR, TEN)
        x1 = randint(FOUR, TEN)
        x2 = rectangle_region_aa4ec2a5(ZERO, ZERO, x0, x1)
        x3 = randint(ONE, max(ONE, x0 - THREE))
        x4 = randint(ONE, max(ONE, x1 - THREE))
        x5 = randint(ONE, x0 - x3 - ONE)
        x6 = randint(ONE, x1 - x4 - ONE)
        x7 = rectangle_region_aa4ec2a5(x5, x6, x3, x4)
        x8 = frozenset(set(x2) - set(x7))
        x8 = _trim_holey_patch_aa4ec2a5(x8)
        if not connected_patch_aa4ec2a5(x8):
            continue
        x9 = enclosed_cells_aa4ec2a5(x8)
        if len(x9) == ZERO:
            continue
        return x8
    return frozenset(set(rectangle_region_aa4ec2a5(ZERO, ZERO, FIVE, FIVE)) - set(initset((TWO, TWO))))


def _place_patch_aa4ec2a5(
    patch: Patch,
    grid_shape: IntegerTuple,
    reserved: set[IntegerTuple],
) -> tuple[Indices | None, set[IntegerTuple] | None]:
    x0, x1 = grid_shape
    x2 = height(patch)
    x3 = width(patch)
    if x2 + TWO > x0 or x3 + TWO > x1:
        return None, None
    for _ in range(400):
        x4 = randint(ONE, x0 - x2 - ONE)
        x5 = randint(ONE, x1 - x3 - ONE)
        x6 = shift(patch, (x4, x5))
        x7 = set(x6) | set(halo8_aa4ec2a5(x6, grid_shape))
        if x7 & reserved:
            continue
        return x6, reserved | x7
    return None, None


def _render_input_aa4ec2a5(
    grid_shape: IntegerTuple,
    patches: tuple[Patch, ...],
) -> Grid:
    x0 = canvas(BG_AA4EC2A5, grid_shape)
    for x1 in patches:
        x0 = fill(x0, FG_AA4EC2A5, x1)
    return x0


def _render_output_aa4ec2a5(
    grid_shape: IntegerTuple,
    patches: tuple[Patch, ...],
) -> Grid:
    x0 = tuple((x1, enclosed_cells_aa4ec2a5(x1)) for x1 in patches)
    x1 = canvas(BG_AA4EC2A5, grid_shape)
    x2 = fill(
        x1,
        TWO,
        merge(tuple(halo8_aa4ec2a5(x3, grid_shape) for x3, _ in x0)),
    )
    x3 = fill(x2, SIX, merge(tuple(x4 for _, x4 in x0)))
    x4 = tuple(
        recolor(EIGHT if len(x5) > ZERO else FG_AA4EC2A5, x6)
        for x6, x5 in x0
    )
    return paint(x3, merge(x4))


def generate_aa4ec2a5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (16, 30))
        x1 = unifint(diff_lb, diff_ub, (16, 30))
        x2 = (x0, x1)
        x3 = choice((ONE, ONE, TWO))
        x4 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x5 = []
        x6: set[IntegerTuple] = set()
        x7 = True
        for _ in range(x3):
            x8 = _sample_holey_patch_aa4ec2a5()
            x9, x6 = _place_patch_aa4ec2a5(x8, x2, x6)
            if x9 is None:
                x7 = False
                break
            x5.append(x9)
        if not x7:
            continue
        for _ in range(x4):
            x8 = _sample_plain_patch_aa4ec2a5()
            x9, x6 = _place_patch_aa4ec2a5(x8, x2, x6)
            if x9 is None:
                x7 = False
                break
            x5.append(x9)
        if not x7:
            continue
        shuffle(x5)
        x10 = tuple(x5)
        gi = _render_input_aa4ec2a5(x2, x10)
        go = _render_output_aa4ec2a5(x2, x10)
        if colorcount(go, SIX) == ZERO:
            continue
        if colorcount(go, ONE) == ZERO:
            continue
        if colorcount(go, TWO) < EIGHT:
            continue
        return {
            "input": gi,
            "output": go,
        }
