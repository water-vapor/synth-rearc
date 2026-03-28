from synth_rearc.core import *

from .helpers import (
    FRAME_COLORS_93C31FBE,
    TALL_93C31FBE,
    WIDE_93C31FBE,
    box_orientation_93c31fbe,
    find_boxes_93c31fbe,
    paint_boxes_93c31fbe,
    reflect_points_93c31fbe,
)


GRID_HEIGHT_BOUNDS_93C31FBE = (20, 28)
GRID_WIDTH_BOUNDS_93C31FBE = (20, 28)
BOX_COUNT_BOUNDS_93C31FBE = (TWO, THREE)
BOX_SIDE_BOUNDS_93C31FBE = (FIVE, EIGHT)
LONG_BOX_MAX_93C31FBE = 14
MAX_LAYOUT_ATTEMPTS_93C31FBE = 128
MAX_BOX_ATTEMPTS_93C31FBE = 96
MAX_CLUSTER_SIZE_93C31FBE = SIX


def _boxes_separate_93c31fbe(
    box_a: Tuple,
    box_b: Tuple,
) -> bool:
    ar0, ac0, ar1, ac1 = box_a
    br0, bc0, br1, bc1 = box_b
    return (
        ar1 + ONE < br0
        or br1 + ONE < ar0
        or ac1 + ONE < bc0
        or bc1 + ONE < ac0
    )


def _sample_box_93c31fbe(
    grid_shape: Tuple,
    orientation: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Tuple:
    gh, gw = grid_shape
    x0 = unifint(diff_lb, diff_ub, BOX_SIDE_BOUNDS_93C31FBE)
    x1 = min(LONG_BOX_MAX_93C31FBE, gh if orientation == TALL_93C31FBE else gw)
    x2 = max(x0 + TWO, SEVEN)
    if orientation == WIDE_93C31FBE:
        x3 = x0
        x4 = randint(x2, x1)
        return (x3, x4)
    x3 = randint(x2, x1)
    x4 = x0
    return (x3, x4)


def _place_boxes_93c31fbe(
    grid_shape: Tuple,
    diff_lb: float,
    diff_ub: float,
) -> Tuple:
    gh, gw = grid_shape
    x0 = unifint(diff_lb, diff_ub, BOX_COUNT_BOUNDS_93C31FBE)
    x1 = [choice((WIDE_93C31FBE, TALL_93C31FBE)) for _ in range(x0)]
    if x0 > ONE and len(set(x1)) == ONE:
        x1[-ONE] = other((WIDE_93C31FBE, TALL_93C31FBE), x1[ZERO])
    x2 = []
    x3 = set()
    x4 = set()
    for x5 in x1:
        x6 = F
        for _ in range(MAX_BOX_ATTEMPTS_93C31FBE):
            bh, bw = _sample_box_93c31fbe(grid_shape, x5, diff_lb, diff_ub)
            if bh >= gh or bw >= gw:
                continue
            r0 = randint(ZERO, gh - bh)
            c0 = randint(ZERO, gw - bw)
            x7 = (r0, c0, r0 + bh - ONE, c0 + bw - ONE)
            if x7[ZERO] in x3 or x7[TWO] in x3 or x7[ONE] in x4 or x7[THREE] in x4:
                continue
            if any(not _boxes_separate_93c31fbe(x7, x8) for x8 in x2):
                continue
            x2.append(x7)
            x3.add(x7[ZERO])
            x3.add(x7[TWO])
            x4.add(x7[ONE])
            x4.add(x7[THREE])
            x6 = T
            break
        if not x6:
            return tuple()
    return tuple(sorted(x2))


def _half_candidates_93c31fbe(
    box: Tuple,
    side: Integer,
) -> Tuple:
    r0, c0, r1, c1 = box
    x0 = box_orientation_93c31fbe(box)
    x1 = []
    if x0 == WIDE_93C31FBE:
        x2 = (c0 + c1) / TWO
        for i in range(r0 + ONE, r1):
            for j in range(c0 + ONE, c1):
                if side == NEG_ONE and j < x2:
                    x1.append((i, j))
                elif side == ONE and j > x2:
                    x1.append((i, j))
    else:
        x2 = (r0 + r1) / TWO
        for i in range(r0 + ONE, r1):
            for j in range(c0 + ONE, c1):
                if side == NEG_ONE and i < x2:
                    x1.append((i, j))
                elif side == ONE and i > x2:
                    x1.append((i, j))
    return tuple(x1)


def _grow_cluster_93c31fbe(
    candidates: Tuple,
    target: Integer,
) -> Indices:
    x0 = set(candidates)
    x1 = {choice(candidates)}
    while len(x1) < target:
        x2 = set()
        for x3 in x1:
            x2 |= {x4 for x4 in neighbors(x3) if x4 in x0 and x4 not in x1}
        if len(x2) == ZERO:
            x2 = x0 - x1
        x1.add(choice(tuple(x2)))
    return frozenset(x1)


def _sample_seed_93c31fbe(
    box: Tuple,
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = choice((NEG_ONE, ONE))
    x1 = _half_candidates_93c31fbe(box, x0)
    x2 = len(x1)
    x3 = max(ONE, min(MAX_CLUSTER_SIZE_93C31FBE, x2 // TWO))
    x4 = unifint(diff_lb, diff_ub, (ONE, x3))
    return _grow_cluster_93c31fbe(x1, x4)


def _stray_cells_93c31fbe(
    grid_shape: Tuple,
    boxes: Tuple,
) -> Indices:
    gh, gw = grid_shape
    x0 = frozenset(
        (i, j)
        for i in range(gh)
        for j in range(gw)
        if all(not (r0 <= i <= r1 and c0 <= j <= c1) for r0, c0, r1, c1 in boxes)
    )
    x1 = set()
    x2 = randint(ONE, TWO)
    for _ in range(x2):
        x3 = tuple(x0 - x1)
        if len(x3) == ZERO:
            break
        x4 = {choice(x3)}
        x5 = randint(ONE, THREE)
        while len(x4) < x5:
            x6 = set()
            for x7 in x4:
                x6 |= {x8 for x8 in neighbors(x7) if x8 in x0 and x8 not in x1 and x8 not in x4}
            if len(x6) == ZERO:
                x6 = set(x0 - x1 - x4)
            x4.add(choice(tuple(x6)))
        x1 |= x4
    return frozenset(x1)


def _render_pair_93c31fbe(
    grid_shape: Tuple,
    boxes: Tuple,
    seeds: Tuple,
    stray: Indices,
    frame_color: Integer,
) -> Tuple:
    x0 = canvas(ZERO, grid_shape)
    x1 = paint_boxes_93c31fbe(x0, boxes, frame_color)
    x2 = merge(seeds)
    x3 = combine(x2, stray)
    x4 = fill(x1, ONE, x3)
    x5 = frozenset()
    for x6, x7 in zip(boxes, seeds):
        x8 = reflect_points_93c31fbe(x7, x6)
        x5 = combine(x5, x7)
        x5 = combine(x5, x8)
    x6 = fill(x1, ONE, x5)
    return (x4, x6)


def generate_93c31fbe(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = (
            unifint(diff_lb, diff_ub, GRID_HEIGHT_BOUNDS_93C31FBE),
            unifint(diff_lb, diff_ub, GRID_WIDTH_BOUNDS_93C31FBE),
        )
        x1 = _place_boxes_93c31fbe(x0, diff_lb, diff_ub)
        if len(x1) == ZERO:
            continue
        x2 = tuple(_sample_seed_93c31fbe(x3, diff_lb, diff_ub) for x3 in x1)
        x3 = _stray_cells_93c31fbe(x0, x1)
        x4 = choice(FRAME_COLORS_93C31FBE)
        x5, x6 = _render_pair_93c31fbe(x0, x1, x2, x3, x4)
        if x5 == x6:
            continue
        if len(find_boxes_93c31fbe(x5)) != len(x1):
            continue
        return {"input": x5, "output": x6}
