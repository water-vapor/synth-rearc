from synth_rearc.core import *

from .helpers import (
    apply_layers_to_rectangle_40f6cd08,
    base_color_40f6cd08,
    decorated_rectangle_40f6cd08,
    full_rectangle_components_40f6cd08,
    layer_specs_40f6cd08,
)


def verify_40f6cd08(I: Grid) -> Grid:
    x0 = full_rectangle_components_40f6cd08(I)
    x1 = base_color_40f6cd08(x0)
    x2 = decorated_rectangle_40f6cd08(x0)
    x3 = layer_specs_40f6cd08(x2, I, x1)
    x4 = I
    for x5 in x0:
        x6 = index(I, ulcorner(x5))
        if x6 != x1:
            continue
        x4 = apply_layers_to_rectangle_40f6cd08(x4, x5, x3)
    return x4
