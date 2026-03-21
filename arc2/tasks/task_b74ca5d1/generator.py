from arc2.core import *

from .helpers import align_to_corner_b74ca5d1, expand_bbox_b74ca5d1
from .verifier import verify_b74ca5d1


GRID_SHAPE_B74CA5D1 = (30, 30)
PLACEMENT_MARGIN_B74CA5D1 = 3
TEMPLATE_LIBRARY_B74CA5D1 = (
    {"dims": (5, 5), "base": frozenset({(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (3, 2), (3, 3), (3, 4), (4, 2), (4, 4)}), "marker": (2, 2)},
    {"dims": (5, 5), "base": frozenset({(0, 2), (1, 0), (1, 1), (1, 3), (1, 4), (2, 2), (3, 2), (4, 2)}), "marker": (1, 2)},
    {"dims": (5, 5), "base": frozenset({(0, 4), (1, 4), (2, 4), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)}), "marker": (3, 3)},
    {"dims": (5, 5), "base": frozenset({(0, 2), (0, 3), (0, 4), (1, 4), (2, 2), (2, 4), (3, 1), (4, 0)}), "marker": (1, 3)},
    {"dims": (5, 5), "base": frozenset({(0, 2), (2, 1), (2, 3), (3, 1), (3, 3), (4, 0), (4, 4)}), "marker": (1, 2)},
    {"dims": (5, 5), "base": frozenset({(0, 0), (0, 4), (1, 3), (2, 4), (3, 3), (4, 0), (4, 4)}), "marker": (2, 3)},
    {"dims": (1, 5), "base": frozenset({(0, 0), (0, 1), (0, 3), (0, 4)}), "marker": (0, 2)},
    {"dims": (5, 5), "base": frozenset({(0, 0), (1, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (4, 0)}), "marker": (2, 0)},
    {"dims": (2, 2), "base": frozenset({(0, 0), (1, 1)}), "marker": (0, 1)},
    {"dims": (5, 5), "base": frozenset({(0, 0), (1, 1), (2, 0), (2, 2), (3, 3), (4, 0), (4, 2), (4, 4)}), "marker": (3, 1)},
    {"dims": (5, 5), "base": frozenset({(0, 0), (0, 4), (1, 1), (1, 3), (3, 1), (3, 3), (4, 0), (4, 4)}), "marker": (2, 2)},
    {"dims": (5, 5), "base": frozenset({(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 4), (2, 0), (2, 1), (2, 3), (2, 4), (3, 2), (4, 2)}), "marker": (2, 2)},
    {"dims": (5, 5), "base": frozenset({(0, 2), (1, 1), (1, 3), (2, 0), (2, 4), (3, 2), (4, 2)}), "marker": (2, 2)},
    {"dims": (5, 5), "base": frozenset({(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (2, 0), (2, 1), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)}), "marker": (2, 2)},
)

def _shape_counts_b74ca5d1(
    n_corners: int,
) -> tuple[int, ...]:
    if n_corners == TWO:
        return choice(((TWO, TWO), (TWO, THREE)))
    return choice(((TWO, TWO, ONE), (TWO, ONE, TWO), (ONE, TWO, TWO)))


def generate_b74ca5d1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ZERO, TEN, ONE)
    x1 = (
        (ZERO, ZERO),
        (ZERO, GRID_SHAPE_B74CA5D1[1] - ONE),
        (GRID_SHAPE_B74CA5D1[0] - ONE, ZERO),
        (GRID_SHAPE_B74CA5D1[0] - ONE, GRID_SHAPE_B74CA5D1[1] - ONE),
    )
    while True:
        x2 = choice((TWO, TWO, THREE))
        x3 = sample(x1, x2)
        x4 = _shape_counts_b74ca5d1(x2)
        x5 = sum(x4)
        x6 = choice(x0)
        x7 = sample(remove(x6, x0), x2 + x5)
        x8 = x7[:x2]
        x9 = x7[x2:]
        x10 = canvas(x6, GRID_SHAPE_B74CA5D1)
        for x11, x12 in zip(x3, x8):
            x10 = fill(x10, x12, initset(x11))
        x13 = sample(TEMPLATE_LIBRARY_B74CA5D1, x5)
        x14 = set()
        x15 = []
        x16 = T
        x17 = ZERO
        for x18, x19, x20 in zip(x3, x8, x4):
            for _ in range(x20):
                x21 = x9[x17]
                x17 += ONE
                x22 = x13[len(x15)]
                x23, x24 = x22["dims"]
                x25 = F
                x26 = shift(x22["base"], (ZERO, ZERO))
                x27 = x22["marker"]
                for _ in range(100):
                    x28 = randint(PLACEMENT_MARGIN_B74CA5D1, GRID_SHAPE_B74CA5D1[0] - x23 - PLACEMENT_MARGIN_B74CA5D1)
                    x29 = randint(PLACEMENT_MARGIN_B74CA5D1, GRID_SHAPE_B74CA5D1[1] - x24 - PLACEMENT_MARGIN_B74CA5D1)
                    x30 = shift(x26, (x28, x29))
                    x31 = add(x27, (x28, x29))
                    x32 = combine(x30, initset(x31))
                    x33 = expand_bbox_b74ca5d1(x32, ONE, GRID_SHAPE_B74CA5D1)
                    if any(x34 in x14 for x34 in x33):
                        continue
                    x10 = fill(x10, x21, x30)
                    x10 = fill(x10, x19, initset(x31))
                    x14 |= set(x33)
                    x15.append((x30, x31, x21, x19, x18))
                    x25 = T
                    break
                if not x25:
                    x16 = F
                    break
            if not x16:
                break
        if not x16:
            continue
        x34 = x10
        for x35, x36, x37, x38, x39 in x15:
            x34 = fill(x34, x38, x35)
            x34 = fill(x34, x37, initset(x36))
            x40 = combine(x35, initset(x36))
            x41 = align_to_corner_b74ca5d1(x40, x39, GRID_SHAPE_B74CA5D1)
            x34 = fill(x34, x38, x41)
        if verify_b74ca5d1(x10) != x34:
            continue
        return {"input": x10, "output": x34}
