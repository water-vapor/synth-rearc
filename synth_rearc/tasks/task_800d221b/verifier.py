from collections import Counter

from synth_rearc.core import *

from .helpers import adjacent_component_ids_800d221b
from .helpers import branch_components_800d221b
from .helpers import component_index_800d221b
from .helpers import dominant_color_for_cells_800d221b
from .helpers import foreground_components_800d221b
from .helpers import separator_center_800d221b
from .helpers import separator_color_800d221b


def verify_800d221b(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = separator_color_800d221b(I, x0)
    x2 = separator_center_800d221b(I, x1)
    x3 = foreground_components_800d221b(I, x0, x1)
    x4 = component_index_800d221b(x3)
    x5 = tuple(dominant_color_for_cells_800d221b(I, x6) for x6 in x3)
    x6 = Counter()
    x7 = Counter()
    x8 = Counter()
    x9 = Counter()
    x10 = Counter()
    for x11, x12 in pair(x3, x5):
        x13 = len(x11)
        x10[x12] += x13
        x14 = sum(i for i, _ in x11) / x13
        x15 = sum(j for _, j in x11) / x13
        x16 = x14 < x2[ZERO]
        x17 = x15 < x2[ONE]
        if both(x16, x17):
            x6[x12] += x13
        elif both(x16, flip(x17)):
            x7[x12] += x13
        elif both(flip(x16), x17):
            x8[x12] += x13
        else:
            x9[x12] += x13
    x18 = max(x6, key=lambda x19: (x6[x19], invert(x19))) if x6 else None
    x19 = max(x8, key=lambda x20: (x8[x20], invert(x20))) if x8 else None
    x20 = max(x7, key=lambda x21: (x7[x21], invert(x21))) if x7 else None
    x21 = max(x9, key=lambda x22: (x9[x22], invert(x22))) if x9 else None
    if both(x18 is not None, x18 == x19):
        x22 = x18
    elif both(x20 is not None, x20 == x21):
        x22 = x20
    else:
        x22 = max(x10, key=lambda x23: (x10[x23], invert(x23)))
    x23 = branch_components_800d221b(I, x1, x2)
    x24 = I
    x25 = shape(I)
    for x26 in x23:
        x27 = adjacent_component_ids_800d221b(x26, x4, x25)
        x28 = Counter(x27).most_common(ONE)[ZERO][ZERO]
        x29 = x5[x28]
        x24 = fill(x24, x29, x26)
    x30 = initset(x2)
    x31 = fill(x24, x22, x30)
    return x31
