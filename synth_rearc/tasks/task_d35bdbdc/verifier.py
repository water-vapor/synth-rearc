from synth_rearc.core import *

from .helpers import extract_motifs_d35bdbdc
from .helpers import paint_motif_d35bdbdc
from .helpers import select_terminal_motif_indices_d35bdbdc


def verify_d35bdbdc(I: Grid) -> Grid:
    x0 = frozenset((i, j) for i, row in enumerate(I) for j, value in enumerate(row) if equality(value, FIVE))
    x1 = extract_motifs_d35bdbdc(I)
    x2 = select_terminal_motif_indices_d35bdbdc(x1, x0)
    x3 = {x4["outer_color"]: x4["center_color"] for x4 in x1}
    x4 = canvas(ZERO, (len(I), len(I[ZERO])))
    x4 = fill(x4, FIVE, x0)
    for x5 in x2:
        x6 = x1[x5]
        x7 = x3.get(x6["center_color"], x6["center_color"])
        x4 = paint_motif_d35bdbdc(x4, x6["patch"], x6["outer_color"], x7)
    return x4
