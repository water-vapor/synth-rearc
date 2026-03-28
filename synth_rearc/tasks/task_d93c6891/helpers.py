from synth_rearc.core import *


def rectangle_patch_d93c6891(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = loc
    x2, x3 = dims
    x4 = interval(x0, x0 + x2, ONE)
    x5 = interval(x1, x1 + x3, ONE)
    x6 = product(x4, x5)
    return x6


def attachment_patch_d93c6891(
    seven: Patch,
    side: str,
    depth: Integer,
    split: Integer,
) -> Indices:
    x0 = uppermost(seven)
    x1 = lowermost(seven)
    x2 = leftmost(seven)
    x3 = rightmost(seven)
    x4 = height(seven)
    x5 = width(seven)
    if side in ("top", "bottom"):
        x6 = multiply(depth, x5)
        x7 = subtract(x6, split)
        x8 = x0 if side == "top" else x1
        x9 = frozenset() if split == ZERO else connect((x8, x2 - split), (x8, x2 - ONE))
        x10 = frozenset() if x7 == ZERO else connect((x8, x3 + ONE), (x8, x3 + x7))
        x11 = combine(x9, x10)
        return x11
    x6 = multiply(depth, x4)
    x7 = subtract(x6, split)
    x8 = x2 if side == "left" else x3
    x9 = frozenset() if split == ZERO else connect((x0 - split, x8), (x0 - ONE, x8))
    x10 = frozenset() if x7 == ZERO else connect((x1 + ONE, x8), (x1 + x7, x8))
    x11 = combine(x9, x10)
    return x11


def projected_strip_d93c6891(
    seven: Patch,
    five: Patch,
) -> Indices:
    x0 = toindices(five)
    if size(x0) == ZERO:
        return frozenset()
    x1 = apply(first, x0)
    x2 = apply(last, x0)
    x3 = uppermost(seven)
    x4 = lowermost(seven)
    x5 = leftmost(seven)
    x6 = rightmost(seven)
    x7 = height(seven)
    x8 = width(seven)
    x9 = size(x0)
    if contained(x3, x1):
        x10 = divide(x9, x8)
        x11 = interval(x3, x3 + x10, ONE)
        x12 = interval(x5, x6 + ONE, ONE)
        x13 = product(x11, x12)
        return x13
    if contained(x4, x1):
        x10 = divide(x9, x8)
        x11 = interval(x4 - x10 + ONE, x4 + ONE, ONE)
        x12 = interval(x5, x6 + ONE, ONE)
        x13 = product(x11, x12)
        return x13
    if contained(x5, x2):
        x10 = divide(x9, x7)
        x11 = interval(x3, x4 + ONE, ONE)
        x12 = interval(x5, x5 + x10, ONE)
        x13 = product(x11, x12)
        return x13
    x10 = divide(x9, x7)
    x11 = interval(x3, x4 + ONE, ONE)
    x12 = interval(x6 - x10 + ONE, x6 + ONE, ONE)
    x13 = product(x11, x12)
    return x13


def component_patches_d93c6891(
    loc: IntegerTuple,
    dims: IntegerTuple,
    side: str | None = None,
    depth: Integer = ZERO,
    split: Integer = ZERO,
) -> tuple[Indices, Indices, Indices]:
    x0 = rectangle_patch_d93c6891(loc, dims)
    if side is None:
        return x0, frozenset(), frozenset()
    x1 = attachment_patch_d93c6891(x0, side, depth, split)
    x2 = projected_strip_d93c6891(x0, x1)
    return x0, x1, x2
