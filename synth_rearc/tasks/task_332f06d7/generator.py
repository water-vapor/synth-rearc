from __future__ import annotations

from synth_rearc.core import *


Node332F06D7 = tuple[int, int]


def _path_332f06d7(a: Node332F06D7, b: Node332F06D7) -> frozenset[Node332F06D7]:
    x0, x1 = a
    x2, x3 = b
    if x0 == x2:
        x4 = ONE if x3 >= x1 else NEG_ONE
        return frozenset((x0, x5) for x5 in range(x1, x3 + x4, x4))
    if x1 == x3:
        x4 = ONE if x2 >= x0 else NEG_ONE
        return frozenset((x5, x1) for x5 in range(x0, x2 + x4, x4))
    raise ValueError((a, b))


def _square_patch_332f06d7(topleft: Node332F06D7, size: int) -> frozenset[Node332F06D7]:
    x0 = interval(topleft[0], topleft[0] + size, ONE)
    x1 = interval(topleft[1], topleft[1] + size, ONE)
    return product(x0, x1)


def _cells_from_nodes_332f06d7(
    nodes: frozenset[Node332F06D7],
    size: int,
) -> frozenset[Node332F06D7]:
    x0 = set()
    for x1 in nodes:
        x0 |= _square_patch_332f06d7(x1, size)
    return frozenset(x0)


def _fill_patch_332f06d7(grid: Grid, patch: frozenset[Node332F06D7], value: int) -> Grid:
    return fill(grid, value, patch)


def _leaves_332f06d7(nodes: frozenset[Node332F06D7]) -> tuple[Node332F06D7, ...]:
    x0 = []
    x1 = ((ONE, ZERO), (NEG_ONE, ZERO), (ZERO, ONE), (ZERO, NEG_ONE))
    for x2 in nodes:
        x3 = ZERO
        for x4 in x1:
            if add(x2, x4) in nodes:
                x3 = increment(x3)
        if x3 == ONE:
            x0.append(x2)
    return tuple(sorted(x0))


def _target_leaf_332f06d7(I: Grid) -> tuple[Node332F06D7, Node332F06D7, tuple[int, int]] | None:
    x0 = ofcolor(I, ZERO)
    x1 = ofcolor(I, TWO)
    if len(x0) == ZERO or len(x1) == ZERO:
        return None
    x2 = ulcorner(x0)
    x3 = shape(x1)
    x4 = replace(I, ZERO, ONE)
    x5 = replace(x4, TWO, ONE)
    x6 = set()
    x7 = height(I) - x3[0] + ONE
    x8 = width(I) - x3[1] + ONE
    for x9 in range(x7):
        for x10 in range(x8):
            x11 = crop(x5, (x9, x10), x3)
            if palette(x11) == initset(ONE):
                x6.add((x9, x10))
    if x2 not in x6:
        return None
    x12 = {x2}
    x13 = [x2]
    x14 = ((ONE, ZERO), (NEG_ONE, ZERO), (ZERO, ONE), (ZERO, NEG_ONE))
    while len(x13) > ZERO:
        x15 = x13.pop()
        for x16 in x14:
            x17 = add(x15, x16)
            if x17 in x6 and x17 not in x12:
                x12.add(x17)
                x13.append(x17)
    x18 = []
    for x19 in x12:
        if x19 == x2:
            continue
        x20 = ZERO
        for x21 in x14:
            if add(x19, x21) in x12:
                x20 = increment(x20)
        if x20 == ONE:
            x18.append(x19)
    if len(x18) == ZERO:
        return None
    x22 = min(x18)
    return (x2, x22, x3)


def _marker_options_332f06d7(
    anchor: Node332F06D7,
    size: int,
    cells: frozenset[Node332F06D7],
) -> tuple[tuple[Node332F06D7, frozenset[Node332F06D7]], ...]:
    x0, x1 = anchor
    x2 = (
        ("up", (x0 - size - TWO, x1 - size // TWO)),
        ("down", (x0 + TWO, x1 - size // TWO)),
        ("left", (x0 - size // TWO, x1 - size - TWO)),
        ("right", (x0 - size // TWO, x1 + TWO)),
    )
    x3 = []
    for x4, x5 in x2:
        x6 = _square_patch_332f06d7(x5, size)
        if minimum(apply(first, x6)) < ZERO or minimum(apply(last, x6)) < ZERO:
            continue
        if len(intersection(x6, cells)) > ZERO:
            continue
        if x4 == "up":
            x7 = frozenset((x8, x5[1] + size // TWO) for x8 in range(x5[0] + size, x0))
        elif x4 == "down":
            x7 = frozenset((x8, x1 + size // TWO) for x8 in range(x0 + size, x5[0]))
        elif x4 == "left":
            x7 = frozenset((x0 + size // TWO, x8) for x8 in range(x5[1] + size, x1))
        else:
            x7 = frozenset((x0 + size // TWO, x8) for x8 in range(x1 + size, x5[1]))
        if len(intersection(x7, cells)) > ZERO:
            continue
        x3.append((x5, x7))
    return tuple(x3)


def generate_332f06d7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x1 = x0 == ONE or choice((True, False))
        x2 = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        x3 = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
        x4 = randint(ZERO, x2 - ONE)
        x5 = x3 + choice((-FOUR, -THREE, NEG_TWO, NEG_ONE, ONE, TWO, THREE, FOUR))
        x6 = x2 + unifint(diff_lb, diff_ub, (THREE, SEVEN))
        x7 = x3 + choice((-FOUR, -THREE, NEG_TWO, TWO, THREE, FOUR))
        x8 = set()
        x9 = (x4, x3)
        x8 |= _path_332f06d7((x4, x5), x9)
        x8 |= _path_332f06d7(x9, (x2, x3))
        x10 = (x6, x3)
        x8 |= _path_332f06d7((x2, x3), x10)
        x8 |= _path_332f06d7(x10, (x6, x7))
        if choice((True, False, True)):
            x11 = x2 + unifint(diff_lb, diff_ub, (ONE, FOUR))
            x12 = x3 + choice((-FIVE, -FOUR, -THREE, THREE, FOUR, FIVE))
            x13 = (x11, x3)
            x8 |= _path_332f06d7((x2, x3), x13)
            x8 |= _path_332f06d7(x13, (x11, x12))
        x14 = minimum(apply(first, x8))
        x15 = minimum(apply(last, x8))
        x16 = frozenset((x17 - x14, x18 - x15) for x17, x18 in x8)
        x19 = _leaves_332f06d7(x16)
        if len(x19) < TWO:
            continue
        x20 = max(x19)
        x21 = min(tuple(x22 for x22 in x19 if x22 != x20))
        x23 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x24 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x25 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x26 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x27 = (x23, x24)
        x28 = frozenset((x29 + x27[0], x30 + x27[1]) for x29, x30 in x16)
        x31 = _cells_from_nodes_332f06d7(x28, x0)
        x32 = add(x20, x27)
        x33 = add(x21, x27)
        if x1:
            x34 = x33
            x35 = frozenset()
        else:
            x36 = add((x2 - x14, x3 - x15), x27)
            x37 = _marker_options_332f06d7(x36, x0, x31)
            if len(x37) == ZERO:
                continue
            x34, x35 = choice(x37)
            x31 = combine(x31, combine(_square_patch_332f06d7(x34, x0), x35))
        x38 = maximum(apply(first, x31)) + ONE + x25
        x39 = maximum(apply(last, x31)) + ONE + x26
        if x38 > 30 or x39 > 30:
            continue
        x40 = canvas(THREE, (x38, x39))
        x41 = _fill_patch_332f06d7(x40, x31, ONE)
        x42 = _square_patch_332f06d7(x32, x0)
        x43 = _square_patch_332f06d7(x33, x0)
        x44 = _square_patch_332f06d7(x34, x0)
        x45 = _fill_patch_332f06d7(x41, x42, ZERO)
        x46 = _fill_patch_332f06d7(x45, x44, TWO)
        x47 = _fill_patch_332f06d7(_fill_patch_332f06d7(x46, x42, ONE), x43, ZERO)
        x48 = _target_leaf_332f06d7(x46)
        if x48 is None:
            continue
        x49, x50, x51 = x48
        if x49 != x32 or x50 != x33 or x51 != (x0, x0):
            continue
        if x46 == x47:
            continue
        return {"input": x46, "output": x47}
