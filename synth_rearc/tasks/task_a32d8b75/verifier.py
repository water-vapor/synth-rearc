from synth_rearc.core import *

from .helpers import apply_stamp_a32d8b75
from .helpers import cue_corner_a32d8b75
from .helpers import cue_turn_a32d8b75
from .helpers import main_and_cues_a32d8b75
from .helpers import split_pieces_a32d8b75
from .helpers import stencil_mask_a32d8b75
from .helpers import swap_motif_a32d8b75


def verify_a32d8b75(I: Grid) -> Grid:
    x0, x1 = main_and_cues_a32d8b75(I)
    x2 = size(x1)
    x3 = x0
    for x4 in x1:
        x5 = split_pieces_a32d8b75(x4)
        x6 = swap_motif_a32d8b75(x5[ZERO][ONE])
        x7 = stencil_mask_a32d8b75(x5[ONE][ONE])
        x8 = cue_corner_a32d8b75(x5[-TWO:])
        x9 = cue_turn_a32d8b75(x8, x2)
        x3 = apply_stamp_a32d8b75(x3, x6, x7, x8, x9)
    return x3
