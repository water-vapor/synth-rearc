from synth_rearc.core import *

from .helpers import (
    CROP_HEIGHT_BOUNDS_269E22FB,
    CROP_WIDTH_BOUNDS_269E22FB,
    binary_variants_269e22fb,
    colorize_binary_grid_269e22fb,
    unique_crop_specs_269e22fb,
)


def generate_269e22fb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(range(TEN))
    x1 = binary_variants_269e22fb()
    x2 = unique_crop_specs_269e22fb()
    while True:
        x3, x4 = sample(x0, TWO)
        x5 = randint(ZERO, subtract(len(x1), ONE))
        x6 = choice((F, T))
        x7 = x1[x5]
        x8 = colorize_binary_grid_269e22fb(x7, x4, x3) if x6 else colorize_binary_grid_269e22fb(x7, x3, x4)
        x9 = unifint(diff_lb, diff_ub, CROP_HEIGHT_BOUNDS_269E22FB)
        x10 = unifint(diff_lb, diff_ub, CROP_WIDTH_BOUNDS_269E22FB)
        x11 = tuple(x12 for x12 in x2[x5] if x12[2] == x9 and x12[3] == x10)
        if len(x11) == ZERO:
            continue
        x13 = choice(x11)
        x14 = crop(x8, (x13[0], x13[1]), (x13[2], x13[3]))
        return {"input": x14, "output": x8}
