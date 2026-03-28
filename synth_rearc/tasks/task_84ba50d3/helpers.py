from synth_rearc.core import *


def make_line_patch_84ba50d3(
    obj_height: Integer,
) -> Indices:
    return frozenset((i, ZERO) for i in range(obj_height))


def make_bar_stem_patch_84ba50d3(
    bar_width: Integer,
    stem_up: Integer,
    stem_down: Integer,
    stem_col: Integer,
) -> Indices:
    x0 = {(stem_up, j) for j in range(bar_width)}
    x1 = {(i, stem_col) for i in range(stem_up)}
    x2 = {(i, stem_col) for i in range(add(stem_up, ONE), add(add(stem_up, stem_down), ONE))}
    return frozenset(x0 | x1 | x2)


def place_patch_84ba50d3(
    patch: Patch,
    top: Integer,
    left: Integer,
    value: Integer = ONE,
) -> Object:
    return recolor(value, shift(patch, (top, left)))
