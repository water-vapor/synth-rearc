from synth_rearc.core import *

from .verifier import verify_a416fc5b


RING_DIRS_A416FC5B = (
    (-ONE, -ONE),
    (-ONE, ZERO),
    (-ONE, ONE),
    (ZERO, ONE),
    (ONE, ONE),
    (ONE, ZERO),
    (ONE, -ONE),
    (ZERO, -ONE),
)
BOARD_SIDE_A416FC5B = add(TEN, ONE)
BOARD_CENTERS_A416FC5B = (ONE, FIVE, NINE)


def _board_a416fc5b() -> Grid:
    gi = canvas(SEVEN, (BOARD_SIDE_A416FC5B, BOARD_SIDE_A416FC5B))
    gi = fill(gi, SIX, connect((THREE, ZERO), (THREE, TEN)))
    gi = fill(gi, SIX, connect((SEVEN, ZERO), (SEVEN, TEN)))
    gi = fill(gi, SIX, connect((ZERO, THREE), (TEN, THREE)))
    gi = fill(gi, SIX, connect((ZERO, SEVEN), (TEN, SEVEN)))
    return gi


def _cross_patch_a416fc5b(
    row_idx: Integer,
    col_idx: Integer,
) -> Indices:
    row_center = BOARD_CENTERS_A416FC5B[row_idx]
    col_center = BOARD_CENTERS_A416FC5B[col_idx]
    return dneighbors((row_center, col_center))


def generate_a416fc5b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        ring_idx = randint(ZERO, SEVEN)
        special = equality(unifint(diff_lb, diff_ub, (ZERO, TWO)), ZERO)
        ring_dir = RING_DIRS_A416FC5B[ring_idx]
        eight_dir = RING_DIRS_A416FC5B[(ring_idx - THREE) % EIGHT]
        five_dir = RING_DIRS_A416FC5B[(ring_idx + THREE) % EIGHT]
        center_patch = _cross_patch_a416fc5b(ONE, ONE)
        ring_patch = _cross_patch_a416fc5b(
            increment(ring_dir[ZERO]),
            increment(ring_dir[ONE]),
        )
        eight_patch = _cross_patch_a416fc5b(
            increment(eight_dir[ZERO]),
            increment(eight_dir[ONE]),
        )
        five_patch = _cross_patch_a416fc5b(
            increment(five_dir[ZERO]),
            increment(five_dir[ONE]),
        )
        gi = _board_a416fc5b()
        gi = fill(gi, TWO, center_patch)
        gi = fill(gi, TWO, ring_patch)
        if special:
            gi = fill(gi, EIGHT, eight_patch)
            gi = fill(gi, FIVE, five_patch)
            side = add(colorcount(gi, TWO), add(colorcount(gi, FIVE), colorcount(gi, EIGHT)))
            go = canvas(SEVEN, (side, side))
        else:
            go = fill(gi, EIGHT, eight_patch)
            go = fill(go, FIVE, five_patch)
        if verify_a416fc5b(gi) != go:
            raise ValueError("generated example does not satisfy verify_a416fc5b")
        return {"input": gi, "output": go}
