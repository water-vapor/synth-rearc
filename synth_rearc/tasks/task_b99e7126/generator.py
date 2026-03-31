from synth_rearc.core import *

from .helpers import (
    make_background_tile_b99e7126,
    make_special_tile_b99e7126,
    mask_indices_b99e7126,
    random_background_mask_b99e7126,
    random_special_mask_and_seed_b99e7126,
    render_grid_b99e7126,
    shift_indices_b99e7126,
)


def generate_b99e7126(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = sample(interval(ONE, TEN, ONE), FOUR)
    x1, x2, x3, x4 = x0
    x5 = random_background_mask_b99e7126()
    x6, x7 = random_special_mask_and_seed_b99e7126()
    x8 = make_background_tile_b99e7126(x5, x2, x3)
    x9 = make_special_tile_b99e7126(x6, x2, x4)
    x10 = astuple(randint(ZERO, FOUR), randint(ZERO, FOUR))
    x11 = shift_indices_b99e7126(x7, x10)
    x12 = shift_indices_b99e7126(mask_indices_b99e7126(x6), x10)
    x13 = render_grid_b99e7126(x1, x8, x9, x11)
    x14 = render_grid_b99e7126(x1, x8, x9, x12)
    return {"input": x13, "output": x14}
