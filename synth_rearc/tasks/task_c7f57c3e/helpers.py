from __future__ import annotations

from synth_rearc.core import *


SignatureC7F57C3E = tuple[tuple[Integer, IntegerTuple], ...]
ScaffoldC7F57C3E = tuple[IntegerTuple, ...]


def object_grid_c7f57c3e(
    obj: Object,
) -> Grid:
    x0 = normalize(obj)
    x1 = canvas(ZERO, shape(x0))
    x2 = paint(x1, x0)
    return x2


def block_scale_c7f57c3e(
    grid: Grid,
) -> Integer:
    x0, x1 = shape(grid)
    for x2 in range(min(x0, x1), ZERO, -ONE):
        if x0 % x2 != ZERO or x1 % x2 != ZERO:
            continue
        x3 = downscale(grid, x2)
        if upscale(x3, x2) == grid:
            return x2
    raise ValueError("expected an exactly block-upscaled motif")


def build_object_c7f57c3e(
    scaffold: ScaffoldC7F57C3E,
    signature: SignatureC7F57C3E,
    scale: Integer,
    anchor: IntegerTuple,
) -> Object:
    x0, x1 = anchor
    x2 = set()
    for x3, x4 in scaffold:
        x5 = add(x0, multiply(x3, scale))
        x6 = add(x1, multiply(x4, scale))
        for x7 in range(scale):
            for x8 in range(scale):
                x2.add((ONE, (add(x5, x7), add(x6, x8))))
    for x9, (x10, x11) in signature:
        x12 = add(x0, multiply(x10, scale))
        x13 = add(x1, multiply(x11, scale))
        for x14 in range(scale):
            for x15 in range(scale):
                x2.add((x9, (add(x12, x14), add(x13, x15))))
    return frozenset(x2)


def footprint_bounds_c7f57c3e(
    scaffold: ScaffoldC7F57C3E,
    signatures: tuple[SignatureC7F57C3E, ...],
) -> tuple[Integer, Integer, Integer, Integer]:
    x0 = list(scaffold)
    for x1 in signatures:
        x0.extend(x2 for _, x2 in x1)
    x3 = tuple(x4 for x4, _ in x0)
    x5 = tuple(x6 for _, x6 in x0)
    return (minimum(x3), minimum(x5), maximum(x3), maximum(x5))


def describe_object_c7f57c3e(
    obj: Object,
) -> dict[str, object]:
    x0 = object_grid_c7f57c3e(obj)
    x1 = block_scale_c7f57c3e(x0)
    x2 = downscale(x0, x1)
    x3 = ofcolor(x2, ONE)
    if size(x3) == ZERO:
        raise ValueError("expected a color-1 scaffold")
    x4 = ulcorner(x3)
    x5 = tuple(sorted((subtract(x6, x4[0]), subtract(x7, x4[1])) for x6, x7 in x3))
    x8 = tuple(
        sorted(
            (
                x9,
                (subtract(x10, x4[0]), subtract(x11, x4[1])),
            )
            for x10, x12 in enumerate(x2)
            for x11, x9 in enumerate(x12)
            if x9 not in (ZERO, ONE)
        )
    )
    x13 = frozenset(x14 for x15, x14 in obj if x15 == ONE)
    x16 = ulcorner(x13)
    return {
        "anchor": x16,
        "scale": x1,
        "scaffold": x5,
        "signature": x8,
    }


def describe_objects_c7f57c3e(
    grid: Grid,
) -> tuple[dict[str, object], ...]:
    x0 = tuple(sorted(objects(grid, F, T, T), key=ulcorner))
    return tuple(describe_object_c7f57c3e(x1) for x1 in x0)


def render_signature_c7f57c3e(
    descriptor: dict[str, object],
    signature: SignatureC7F57C3E,
) -> Object:
    x0 = descriptor["scaffold"]
    x1 = descriptor["scale"]
    x2 = descriptor["anchor"]
    return build_object_c7f57c3e(x0, signature, x1, x2)
