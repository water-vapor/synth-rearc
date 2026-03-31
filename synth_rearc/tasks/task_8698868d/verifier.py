from synth_rearc.core import *

from .helpers import background_component_count_8698868d
from .helpers import compose_block_8698868d
from .helpers import extract_square_panels_8698868d


def verify_8698868d(
    I: Grid,
) -> Grid:
    x0, x1, x2 = extract_square_panels_8698868d(I)
    x3 = {background_component_count_8698868d(x4["grid"], x0): x4 for x4 in x2}
    x4 = {}
    for x5 in x1:
        x6 = x5["top_left"][0]
        x4.setdefault(x6, []).append(x5)
    x5 = []
    for x6 in sorted(x4):
        x7 = sorted(x4[x6], key=lambda x8: x8["top_left"][1])
        x8 = x7[0]["side"]
        x9 = [[] for _ in range(x8)]
        for x10 in x7:
            x11 = background_component_count_8698868d(x10["grid"], x0)
            x12 = x3[x11]
            x13 = compose_block_8698868d(x10["color"], x12["grid"], x0)
            for x14, x15 in enumerate(x13):
                x9[x14].extend(x15)
        x5.extend(tuple(x16) for x16 in x9)
    return tuple(x5)
