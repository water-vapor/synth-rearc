from synth_rearc.core import *

from .helpers import OUTPUT_DIMS_B7CB93AC, extract_components_b7cb93ac, normalized_shape_b7cb93ac, shape_rotations_b7cb93ac


def verify_b7cb93ac(I: Grid) -> Grid:
    x0 = extract_components_b7cb93ac(I, T)
    x1 = tuple(sorted(x0, key=lambda x2: (-size(x2), uppermost(x2), leftmost(x2), color(x2))))
    x2 = first(x1)
    x3 = tuple(sorted(x1[ONE:], key=lambda x4: (leftmost(x4), uppermost(x4), size(x4), color(x4))))
    x4 = normalized_shape_b7cb93ac(x2)
    x5 = first(OUTPUT_DIMS_B7CB93AC)
    x6 = last(OUTPUT_DIMS_B7CB93AC)
    x7 = canvas(ZERO, OUTPUT_DIMS_B7CB93AC)
    x8 = multiply(x5, x6)
    x9 = color(x2)
    x10 = height(x4)
    x11 = width(x4)

    def x12(
        x13: tuple[Object, ...],
        x14: Indices,
        x15: Grid,
    ) -> Grid | None:
        if len(x13) == ZERO:
            return x15 if size(x14) == x8 else None
        x16 = first(x13)
        x17 = color(x16)
        x18 = shape_rotations_b7cb93ac(x16)
        for x19 in x18:
            x20 = height(x19)
            x21 = width(x19)
            for x22 in range(subtract(subtract(x5, x20), NEG_ONE)):
                for x23 in range(subtract(subtract(x6, x21), NEG_ONE)):
                    x24 = shift(x19, (x22, x23))
                    if len(intersection(x14, x24)) != ZERO:
                        continue
                    x25 = fill(x15, x17, x24)
                    x26 = x12(x13[ONE:], combine(x14, x24), x25)
                    if x26 is not None:
                        return x26
        return None

    for x13 in range(subtract(subtract(x5, x10), NEG_ONE)):
        for x14 in range(subtract(subtract(x6, x11), NEG_ONE)):
            x15 = shift(x4, (x13, x14))
            x16 = fill(x7, x9, x15)
            x17 = x12(x3, x15, x16)
            if x17 is not None:
                return x17
    raise ValueError("unable to pack components into the target rectangle")

