from synth_rearc.core import *

from .helpers import assemble_output_indices, find_connectors_2c181942, payload_indices_for_color


def verify_2c181942(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = find_connectors_2c181942(x0)
    x2 = mostcolor(I)
    x3 = canvas(x2, shape(I))
    for x4 in ("top", "left", "right", "bottom"):
        x5 = x1[x4]
        x6 = color(x5)
        x7 = payload_indices_for_color(x0, x6, x5)
        x8 = assemble_output_indices(x4, x5, x7 if len(x7) > ZERO else None)
        x9 = fill(x3, x6, x8)
        x3 = x9
    return x3
