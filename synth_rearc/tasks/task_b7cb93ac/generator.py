from __future__ import annotations

from synth_rearc.core import *

from .helpers import OUTPUT_DIMS_B7CB93AC, extract_components_b7cb93ac, normalized_shape_b7cb93ac, shape_rotations_b7cb93ac
from .verifier import verify_b7cb93ac


PACKED_TEMPLATES_B7CB93AC = (
    (
        (ONE, TWO, TWO, TWO),
        (ONE, ONE, ONE, TWO),
        (ONE, THREE, TWO, TWO),
    ),
    (
        (TWO, TWO, TWO, ONE),
        (ONE, ONE, ONE, ONE),
        (ONE, THREE, THREE, ONE),
    ),
    (
        (THREE, ONE, TWO, TWO),
        (ONE, ONE, ONE, ONE),
        (THREE, ONE, TWO, TWO),
    ),
    (
        (ONE, ONE, ONE, ONE),
        (ONE, TWO, THREE, ONE),
        (TWO, TWO, THREE, THREE),
    ),
)

PACKED_TRANSFORMS_B7CB93AC = (identity, hmirror, vmirror, rot180)


def _relabel_grid_b7cb93ac(
    grid: Grid,
    colors: tuple[Integer, Integer, Integer],
) -> Grid:
    x0 = {ONE: colors[ZERO], TWO: colors[ONE], THREE: colors[TWO]}
    return tuple(tuple(x0[x1] for x1 in x2) for x2 in grid)


def _bbox_margin_b7cb93ac(
    patch: Patch,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    x2 = max(ZERO, subtract(uppermost(patch), ONE))
    x3 = max(ZERO, subtract(leftmost(patch), ONE))
    x4 = min(subtract(x0, ONE), add(lowermost(patch), ONE))
    x5 = min(subtract(x1, ONE), add(rightmost(patch), ONE))
    return frozenset((x6, x7) for x6 in range(x2, add(x4, ONE)) for x7 in range(x3, add(x5, ONE)))


def _place_objects_b7cb93ac(
    objs: tuple[Object, ...],
    dims: IntegerTuple,
) -> Grid | None:
    x0 = canvas(ZERO, dims)
    x1 = frozenset()
    x2 = x0
    for x3 in objs:
        x4 = height(x3)
        x5 = width(x3)
        x6 = []
        for x7 in range(subtract(subtract(first(dims), x4), NEG_ONE)):
            for x8 in range(subtract(subtract(last(dims), x5), NEG_ONE)):
                x9 = shift(x3, (x7, x8))
                x10 = _bbox_margin_b7cb93ac(x9, dims)
                if len(intersection(x1, x10)) != ZERO:
                    continue
                x6.append(x9)
        if len(x6) == ZERO:
            return None
        shuffle(x6)
        x11 = first(x6)
        x2 = paint(x2, x11)
        x1 = combine(x1, _bbox_margin_b7cb93ac(x11, dims))
    return x2


def generate_b7cb93ac(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(remove(ZERO, interval(ZERO, TEN, ONE)))
    while True:
        x1 = choice(PACKED_TEMPLATES_B7CB93AC)
        x2 = choice(PACKED_TRANSFORMS_B7CB93AC)(x1)
        x3 = tuple(sample(x0, THREE))
        go = _relabel_grid_b7cb93ac(x2, x3)
        x4 = extract_components_b7cb93ac(go, F)
        x5 = tuple(sorted(x4, key=lambda x6: (-size(x6), uppermost(x6), leftmost(x6), color(x6))))
        x6 = first(x5)
        x7 = tuple(x5[ONE:])
        x8 = recolor(color(x6), normalized_shape_b7cb93ac(x6))
        x9 = []
        for x10 in x7:
            x11 = choice(shape_rotations_b7cb93ac(x10))
            x12 = recolor(color(x10), x11)
            x9.append(x12)
        shuffle(x9)
        x13 = (x8,) + tuple(x9)
        x14 = (TEN, unifint(diff_lb, diff_ub, (TEN, 13)))
        gi = _place_objects_b7cb93ac(x13, x14)
        if gi is None:
            continue
        if verify_b7cb93ac(gi) != go:
            continue
        return {"input": gi, "output": go}

