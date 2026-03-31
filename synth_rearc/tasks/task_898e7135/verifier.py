from collections import Counter, defaultdict

from synth_rearc.core import *

from .helpers import canonical_patch_898e7135, scaled_local_patch_898e7135


def verify_898e7135(
    I: Grid,
) -> Grid:
    x0 = tuple(objects(I, T, F, T))
    x1 = max(x0, key=lambda x2: (size(backdrop(x2)), size(x2), -uppermost(x2), -leftmost(x2)))
    x2 = shift(delta(x1), invert(ulcorner(x1)))
    x3 = fill(canvas(ZERO, shape(x1)), ONE, x2)
    x4 = tuple(sorted(objects(x3, T, F, T), key=lambda x5: (uppermost(x5), leftmost(x5), size(x5))))
    x5 = tuple(x6 for x6 in x0 if x6 != x1)
    x6 = defaultdict(list)
    for x7 in x5:
        x8 = canonical_patch_898e7135(x7)
        x6[x8].append(x7)
    for x9 in x6.values():
        x9.sort(key=lambda x10: (color(x10), uppermost(x10), leftmost(x10), size(x10)))
    x10 = None
    x11 = None
    for x12 in range(TWO, EIGHT):
        x13 = []
        x14 = Counter()
        for x15 in x4:
            x16 = canonical_patch_898e7135(upscale(normalize(x15), x12))
            x13.append(x16)
            x14[x16] += ONE
        if not all(len(x6[x17]) >= x18 for x17, x18 in x14.items()):
            continue
        x19 = (sum(size(x20) * x21 for x20, x21 in x14.items()), len(x14), x12)
        if x10 is None or x19 > x10:
            x10 = x19
            x11 = (x12, tuple(x13))
    if x11 is None:
        raise ValueError("failed to infer common scale factor")
    x12, x13 = x11
    x14 = {x15: list(x16) for x15, x16 in x6.items()}
    x17 = canvas(color(x1), multiply(shape(x1), x12))
    for x18, x19 in zip(x4, x13):
        x20 = x14[x19].pop(ZERO)
        x21 = recolor(color(x20), scaled_local_patch_898e7135(x18, x12))
        x17 = paint(x17, x21)
    return x17
