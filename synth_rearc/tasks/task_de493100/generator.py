from synth_rearc.core import *

from .helpers import (
    AVAILABLE_COLORS_DE493100,
    MASK_COLOR_DE493100,
    build_complete_grid_de493100,
    choose_mask_box_de493100,
    make_seed_de493100,
    rect_patch_de493100,
)
from .verifier import verify_de493100


def generate_de493100(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        palette_size = unifint(diff_lb, diff_ub, (5, 8))
        palette_values = tuple(sample(AVAILABLE_COLORS_DE493100, palette_size))
        bg = choice(palette_values)
        seed = make_seed_de493100(diff_lb, diff_ub, palette_values, bg)
        corner = tuple(tuple(choice(palette_values) for _ in range(TWO)) for _ in range(TWO))
        go = build_complete_grid_de493100(seed, corner)
        if numcolors(go) < FOUR:
            continue

        for _ in range(64):
            top, left, height, width = choose_mask_box_de493100(diff_lb, diff_ub)
            patch = rect_patch_de493100(top, left, height, width)
            out = crop(go, (top, left), (height, width))
            if MASK_COLOR_DE493100 in palette(out):
                continue
            if numcolors(out) < TWO:
                continue
            gi = fill(go, MASK_COLOR_DE493100, patch)
            if verify_de493100(gi) != out:
                continue
            return {"input": gi, "output": out}
