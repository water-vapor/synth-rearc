from arc2.core import *

from .helpers import (
    FRAME_PATCH_4DF5B0AE,
    GRID_SHAPE_4DF5B0AE,
    frame_color_4df5b0ae,
    pack_objects_4df5b0ae,
    place_objects_4df5b0ae,
    sample_object_colors_4df5b0ae,
    sample_object_shapes_4df5b0ae,
)
from .verifier import verify_4df5b0ae


def generate_4df5b0ae(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = sample_object_shapes_4df5b0ae(diff_lb, diff_ub)
        if len(x0) == ZERO:
            continue
        x1 = sample_object_colors_4df5b0ae(len(x0))
        x2 = choice((F, F, T))
        x3 = canvas(SEVEN, GRID_SHAPE_4DF5B0AE)
        if x2:
            x4 = frame_color_4df5b0ae(x1)
            x3 = fill(x3, x4, FRAME_PATCH_4DF5B0AE)
        x5 = place_objects_4df5b0ae(x0, x1, x2)
        if len(x5) == ZERO:
            continue
        x6 = x3
        for x7 in x5:
            x6 = paint(x6, x7)
        x8 = pack_objects_4df5b0ae(x5)
        if verify_4df5b0ae(x6) != x8:
            continue
        return {"input": x6, "output": x8}
