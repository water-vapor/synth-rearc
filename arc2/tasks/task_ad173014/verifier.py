import math

from arc2.core import *


def _frame_specs_ad173014(
    I: Grid,
) -> tuple[dict, ...]:
    x0 = objects(I, T, F, T)
    x1 = tuple(obj for obj in x0 if color(obj) == TWO)
    x2 = tuple(
        obj
        for obj in x1
        if size(obj) == size(box(obj))
    )
    x3 = tuple(
        (center(obj)[0], center(obj)[1], obj)
        for obj in x2
    )
    x4 = sum(item[0] for item in x3) / len(x3)
    x5 = sum(item[1] for item in x3) / len(x3)
    x6 = sorted(
        x3,
        key=lambda item: math.atan2(x5 - item[1], item[0] - x4),
        reverse=True,
    )
    specs = []
    for _, _, frame in x6:
        x7 = ulcorner(frame)
        x8 = subgrid(frame, I)
        x9 = tuple(sorted(palette(x8) - {ZERO, TWO}))
        x10 = first(x9)
        x11 = frozenset(
            (i, j)
            for i in range(x7[0], x7[0] + height(x8))
            for j in range(x7[1], x7[1] + width(x8))
            if index(I, (i, j)) == x10
        )
        specs.append({"frame": frame, "motif_color": x10, "motif_patch": x11})
    return tuple(specs)


def verify_ad173014(I: Grid) -> Grid:
    x0 = _frame_specs_ad173014(I)
    x1 = I
    for x2, x3 in enumerate(x0):
        x4 = x0[x2 - ONE]["motif_color"]
        x1 = fill(x1, x4, x3["motif_patch"])
    return x1
