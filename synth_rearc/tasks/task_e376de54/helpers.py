from __future__ import annotations

from synth_rearc.core import *


STEP_BY_ORIENTATION_E376DE54 = {
    "horizontal": RIGHT,
    "vertical": DOWN,
    "diag_main": UNITY,
    "diag_anti": DOWN_LEFT,
}


def segment_orientation_e376de54(
    patch: Patch,
) -> str:
    x0 = toindices(patch)
    x1 = frozenset(x2 for x2, _ in x0)
    x2 = frozenset(x3 for _, x3 in x0)
    x3 = frozenset(x4 - x5 for x4, x5 in x0)
    x4 = frozenset(x6 + x7 for x6, x7 in x0)
    if len(x1) == ONE:
        return "horizontal"
    if len(x2) == ONE:
        return "vertical"
    if len(x3) == ONE:
        return "diag_main"
    if len(x4) == ONE:
        return "diag_anti"
    raise ValueError("expected a straight segment")


def segment_endpoints_e376de54(
    patch: Patch,
    orientation: str,
) -> tuple[IntegerTuple, IntegerTuple]:
    if orientation == "horizontal":
        x0 = uppermost(patch)
        return (x0, leftmost(patch)), (x0, rightmost(patch))
    if orientation == "vertical":
        x0 = leftmost(patch)
        return (uppermost(patch), x0), (lowermost(patch), x0)
    if orientation == "diag_main":
        return ulcorner(patch), lrcorner(patch)
    if orientation == "diag_anti":
        return urcorner(patch), llcorner(patch)
    raise ValueError(f"unsupported orientation: {orientation}")


def perpendicular_invariant_e376de54(
    loc: IntegerTuple,
    orientation: str,
) -> Integer:
    x0, x1 = loc
    if orientation == "horizontal":
        return x1
    if orientation == "vertical":
        return x0
    if orientation == "diag_main":
        return x0 + x1
    if orientation == "diag_anti":
        return x0 - x1
    raise ValueError(f"unsupported orientation: {orientation}")


def segment_patch_e376de54(
    anchor: IntegerTuple,
    orientation: str,
    length_value: Integer,
    anchor_side: str,
) -> Indices:
    x0 = STEP_BY_ORIENTATION_E376DE54[orientation]
    x1 = decrement(length_value)
    x2 = multiply(x0, x1)
    if anchor_side == "start":
        x3 = anchor
        x4 = add(anchor, x2)
    else:
        x3 = subtract(anchor, x2)
        x4 = anchor
    return connect(x3, x4)
