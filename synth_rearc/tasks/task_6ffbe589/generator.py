from synth_rearc.core import *

from .helpers import (
    GENERATED_PANEL_SIZES_6FFBE589,
    PALETTE_6FFBE589,
    checkerboard_panel_6ffbe589,
    clue_objects_6ffbe589,
    embedded_input_6ffbe589,
    output_panel_from_input_6ffbe589,
    panel_spec_6ffbe589,
    ring_panel_6ffbe589,
)


def generate_6ffbe589(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("ring", "ring", "checker"))
        x1 = choice((ONE, ONE, THREE))
        x2 = choice(GENERATED_PANEL_SIZES_6FFBE589)
        x3 = tuple(sample(PALETTE_6FFBE589, choice((3, 4))))
        if x0 == "checker":
            x4, x5 = checkerboard_panel_6ffbe589(x2, x3, x1)
        else:
            x4, x5 = ring_panel_6ffbe589(x2, x3, x1)
        x6 = clue_objects_6ffbe589(tuple(v for v in x3 if v != ZERO), x1)
        x7, x8, x9 = embedded_input_6ffbe589(x4, x6, x1)
        x10, x11, x12, _, _ = panel_spec_6ffbe589(x7)
        if (x10, x11, x12) != (x8, x9, x2):
            continue
        if output_panel_from_input_6ffbe589(x7) != x5:
            continue
        return {"input": x7, "output": x5}
