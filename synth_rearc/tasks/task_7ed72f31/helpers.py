from synth_rearc.core import *


def nearest_axis_7ed72f31(
    obj: Patch,
    axes: Objects,
) -> Object:
    x0 = lbind(manhattan, obj)
    x1 = argmin(axes, x0)
    return x1


def mirror_patch_7ed72f31(
    patch: Patch,
    axis: Patch,
) -> Patch:
    if size(axis) == ONE:
        x0 = ulcorner(axis)
        x1 = add(ulcorner(patch), lrcorner(patch))
        x2 = subtract(double(x0), x1)
        x3 = vmirror(patch)
        x4 = hmirror(x3)
        x5 = shift(x4, x2)
        return x5
    if vline(axis):
        x0 = leftmost(axis)
        x1 = add(leftmost(patch), rightmost(patch))
        x2 = subtract(double(x0), x1)
        x3 = vmirror(patch)
        x4 = astuple(ZERO, x2)
        x5 = shift(x3, x4)
        return x5
    x0 = uppermost(axis)
    x1 = add(uppermost(patch), lowermost(patch))
    x2 = subtract(double(x0), x1)
    x3 = hmirror(patch)
    x4 = astuple(x2, ZERO)
    x5 = shift(x3, x4)
    return x5


def mirror_object_7ed72f31(
    obj: Object,
    axis: Patch,
) -> Object:
    x0 = mirror_patch_7ed72f31(obj, axis)
    return x0
