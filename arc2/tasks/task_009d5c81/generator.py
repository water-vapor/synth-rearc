from arc2.core import *

from .helpers import (
    MOTIFS_009d5c81,
    make_signal_patch_009d5c81,
    motif_patch_009d5c81,
    motif_to_color_009d5c81,
    signal_patch_is_valid_009d5c81,
)


def generate_009d5c81(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        gi = canvas(ZERO, (14, 14))
        signal_patch = make_signal_patch_009d5c81(diff_lb, diff_ub)
        if not signal_patch_is_valid_009d5c81(signal_patch):
            continue
        sig_h = height(signal_patch)
        sig_w = width(signal_patch)
        top = randint(ZERO, EIGHT - sig_h)
        left = randint(ZERO, 14 - sig_w)
        signal_patch = shift(signal_patch, (top, left))
        motif = choice(MOTIFS_009d5c81)
        motif_patch = motif_patch_009d5c81(motif, (randint(EIGHT, TEN), randint(ONE, SEVEN)))
        gi = fill(gi, EIGHT, signal_patch)
        gi = fill(gi, ONE, motif_patch)
        target_color = motif_to_color_009d5c81(motif)
        go = replace(gi, EIGHT, target_color)
        go = cover(go, motif_patch)
        return {"input": gi, "output": go}
