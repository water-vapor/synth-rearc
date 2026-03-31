from __future__ import annotations

from synth_rearc.core import *


SIDES = ("top", "left", "right", "bottom")
SIDE_TO_CONNECTOR_OFFSET = {
    "top": (-ONE, ZERO),
    "left": (ZERO, -ONE),
    "right": (ZERO, TWO),
    "bottom": (TWO, ZERO),
}


def _mask_from_indices(indices: Indices) -> Grid:
    x0 = normalize(indices)
    x1 = canvas(ZERO, shape(x0))
    x2 = fill(x1, ONE, x0)
    return x2


def _indices_from_mask(mask: Grid) -> Indices:
    x0 = ofcolor(mask, ONE)
    return x0


def rotate_indices(indices: Indices, turns: int) -> Indices:
    x0 = turns % FOUR
    x1 = _mask_from_indices(indices)
    if x0 == ZERO:
        return _indices_from_mask(x1)
    if x0 == ONE:
        return _indices_from_mask(rot90(x1))
    if x0 == TWO:
        return _indices_from_mask(rot180(x1))
    return _indices_from_mask(rot270(x1))


def is_connector_candidate(obj: Object) -> bool:
    return both(equality(size(obj), TWO), either(hline(obj), vline(obj)))


def find_connectors_2c181942(objs: Objects) -> dict[str, Object]:
    x0 = tuple(obj for obj in objs if is_connector_candidate(obj))
    x1 = {ulcorner(obj): obj for obj in x0 if hline(obj)}
    x2 = {ulcorner(obj): obj for obj in x0 if vline(obj)}
    x3 = []
    for x4 in x1.values():
        x5 = ulcorner(x4)
        x6 = x2.get(add(x5, DOWN_LEFT))
        x7 = x2.get(add(x5, astuple(ONE, TWO)))
        x8 = x1.get(add(x5, toivec(THREE)))
        if all((x6, x7, x8)):
            x3.append({"top": x4, "left": x6, "right": x7, "bottom": x8})
    if len(x3) != ONE:
        raise ValueError("expected exactly one connector hub")
    return x3[ZERO]


def payload_indices_for_color(
    objs: Objects,
    value: int,
    connector: Object,
) -> Indices:
    x0 = frozenset()
    for x1 in objs:
        if both(equality(color(x1), value), x1 != connector):
            x0 = combine(x0, toindices(x1))
    return normalize(x0) if len(x0) > ZERO else x0


def expected_border_indices(dims: tuple[int, int], side: str) -> Indices:
    x0, x1 = dims
    if side == "top":
        return frozenset({(x0 - ONE, x1 // TWO - ONE), (x0 - ONE, x1 // TWO)})
    if side == "bottom":
        return frozenset({(ZERO, x1 // TWO - ONE), (ZERO, x1 // TWO)})
    if side == "left":
        return frozenset({(x0 // TWO - ONE, x1 - ONE), (x0 // TWO, x1 - ONE)})
    return frozenset({(x0 // TWO - ONE, ZERO), (x0 // TWO, ZERO)})


def actual_border_indices(indices: Indices, side: str) -> Indices:
    x0 = shape(indices)
    if side == "top":
        return frozenset((i, j) for i, j in indices if i == x0[ZERO] - ONE)
    if side == "bottom":
        return frozenset((i, j) for i, j in indices if i == ZERO)
    if side == "left":
        return frozenset((i, j) for i, j in indices if j == x0[ONE] - ONE)
    return frozenset((i, j) for i, j in indices if j == ZERO)


def matching_payload_rotations(indices: Indices, side: str) -> tuple[Indices, ...]:
    x0 = normalize(indices)
    x1 = []
    for x2 in range(FOUR):
        x3 = rotate_indices(x0, x2)
        x4 = shape(x3)
        if side in ("top", "bottom") and flip(even(x4[ONE])):
            continue
        if side in ("left", "right") and flip(even(x4[ZERO])):
            continue
        x5 = expected_border_indices(x4, side)
        x6 = actual_border_indices(x3, side)
        if x6 == x5:
            x1.append(x3)
    x7 = []
    x8 = set()
    for x9 in x1:
        x10 = tuple(sorted(x9))
        if x10 in x8:
            continue
        x8.add(x10)
        x7.append(x9)
    return tuple(x7)


def orient_payload_for_side(indices: Indices, side: str) -> Indices:
    x0 = matching_payload_rotations(indices, side)
    if len(x0) != ONE:
        raise ValueError(f"expected exactly one payload orientation for {side}, got {len(x0)}")
    return x0[ZERO]


def place_payload_for_connector(
    indices: Indices,
    connector: Object,
    side: str,
) -> Indices:
    x0, x1 = shape(indices)
    x2, x3 = ulcorner(connector)
    if side == "top":
        return shift(indices, (x2 - x0, x3 - (x1 // TWO - ONE)))
    if side == "bottom":
        return shift(indices, (x2 + ONE, x3 - (x1 // TWO - ONE)))
    if side == "left":
        return shift(indices, (x2 - (x0 // TWO - ONE), x3 - x1))
    return shift(indices, (x2 - (x0 // TWO - ONE), x3 + ONE))


def connector_object(side: str, value: int, gap_ul: tuple[int, int]) -> Object:
    x0 = SIDE_TO_CONNECTOR_OFFSET[side]
    x1 = add(gap_ul, x0)
    if side in ("top", "bottom"):
        x2 = frozenset({x1, add(x1, RIGHT)})
    else:
        x2 = frozenset({x1, add(x1, DOWN)})
    return recolor(value, x2)


def assemble_output_indices(
    side: str,
    connector: Object,
    payload: Indices | None,
) -> Indices:
    x0 = toindices(connector)
    if payload is None or len(payload) == ZERO:
        return x0
    x1 = orient_payload_for_side(payload, side)
    x2 = place_payload_for_connector(x1, connector, side)
    return combine(x0, x2)
