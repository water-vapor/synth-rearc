from synth_rearc.core import *

from .helpers import perpendicular_invariant_e376de54
from .helpers import segment_endpoints_e376de54
from .helpers import segment_orientation_e376de54
from .helpers import segment_patch_e376de54


def verify_e376de54(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, T, T)
    x2 = tuple(
        {
            "color": color(x3),
            "patch": toindices(x3),
            "orientation": segment_orientation_e376de54(x3),
            "endpoints": segment_endpoints_e376de54(
                x3,
                segment_orientation_e376de54(x3),
            ),
            "length": size(x3),
        }
        for x3 in x1
    )
    x3 = tuple(x4["orientation"] for x4 in x2)
    x4 = mostcommon(x3)
    x5 = tuple(x6 for x6 in x2 if x6["orientation"] == x4)
    x6 = tuple(
        perpendicular_invariant_e376de54(
            x7["endpoints"][ZERO],
            x4,
        )
        for x7 in x5
    )
    x7 = tuple(
        perpendicular_invariant_e376de54(
            x8["endpoints"][ONE],
            x4,
        )
        for x8 in x5
    )
    x8 = ZERO if len(set(x6)) <= len(set(x7)) else ONE
    x9 = tuple(sorted(x5, key=lambda x10: x10["endpoints"][x8]))
    x10 = x9[len(x9) // TWO]["length"]
    x11 = fill(I, x0, merge(x1))
    x12 = "start" if x8 == ZERO else "end"
    for x13 in x9:
        x14 = segment_patch_e376de54(
            x13["endpoints"][x8],
            x4,
            x10,
            x12,
        )
        x11 = fill(x11, x13["color"], x14)
    return x11
