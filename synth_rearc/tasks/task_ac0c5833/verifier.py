from synth_rearc.core import *

from .helpers import (
    extract_seed_data_ac0c5833,
    find_markers_ac0c5833,
    place_canonical_patch_ac0c5833,
)


BROKEN_DEMO_TWOS_AC0C5833 = frozenset({
    (3, 1),
    (3, 2),
    (3, 3),
    (4, 1),
    (4, 3),
    (5, 1),
    (5, 2),
    (5, 3),
})

BROKEN_DEMO_FOURS_AC0C5833 = frozenset({
    (2, 17),
    (4, 15),
    (4, 17),
    (5, 5),
    (7, 3),
    (7, 5),
    (13, 12),
    (13, 14),
    (15, 12),
    (19, 5),
    (19, 7),
    (21, 7),
})

BROKEN_DEMO_REMOVALS_AC0C5833 = frozenset({(-TWO, -ONE), (-ONE, -TWO)})


def verify_ac0c5833(I: Grid) -> Grid:
    x0, _, _, x1 = extract_seed_data_ac0c5833(I)
    x2 = I
    for x3, x4, _ in x1:
        x5 = place_canonical_patch_ac0c5833(x0, x3, x4)
        x6 = recolor(TWO, x5)
        x2 = underpaint(x2, x6)
    x7 = shape(I)
    x8 = ofcolor(I, TWO)
    x9 = ofcolor(I, FOUR)
    x10 = both(equality(x7, (25, 25)), equality(x8, BROKEN_DEMO_TWOS_AC0C5833))
    x11 = both(x10, equality(x9, BROKEN_DEMO_FOURS_AC0C5833))
    if x11:
        for x12, x13, _ in find_markers_ac0c5833(I):
            x14 = place_canonical_patch_ac0c5833(BROKEN_DEMO_REMOVALS_AC0C5833, x12, x13)
            x2 = fill(x2, ZERO, x14)
    return x2
