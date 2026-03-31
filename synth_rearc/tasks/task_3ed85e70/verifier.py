from synth_rearc.core import *

from .helpers import extract_outside_objects_3ed85e70
from .helpers import extract_panel_patterns_3ed85e70, find_panel_bbox_3ed85e70
from .helpers import fragment_variants_3ed85e70, match_variant_3ed85e70


def verify_3ed85e70(I: Grid) -> Grid:
    x0 = find_panel_bbox_3ed85e70(I)
    x1 = extract_panel_patterns_3ed85e70(I, x0)
    x2 = tuple((x3, fragment_variants_3ed85e70(x3)) for x3 in x1)
    x3 = extract_outside_objects_3ed85e70(I, x0)
    x4 = I
    for x5 in x3:
        x6 = None
        for x7, x8 in x2:
            x9 = next((x10 for x10 in x8 if match_variant_3ed85e70(I, x5, x10)), None)
            if x9 is None:
                continue
            x6 = (x7, x9)
            break
        if x6 is None:
            continue
        x7, x8 = x6
        x9 = tuple(i for i, _ in x5)
        x10 = tuple(j for _, j in x5)
        x11 = (min(x9), min(x10))
        x12 = subtract(x11, x8[1])
        x13 = shift(x7, x12)
        x4 = paint(x4, frozenset((value, loc) for value, loc in x13 if index(x4, loc) in (ZERO, index(I, loc))))
    return x4
