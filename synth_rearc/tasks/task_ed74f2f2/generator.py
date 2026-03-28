from itertools import combinations

from synth_rearc.core import *


SELECTOR_PATCHES_ED74F2F2 = (
    (ONE, frozenset({(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)})),
    (TWO, frozenset({(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)})),
    (THREE, frozenset({(0, 1), (0, 2), (1, 1), (2, 0), (2, 1)})),
)

SELECTOR_PATCH_SET_ED74F2F2 = frozenset(
    x1 for _, x1 in SELECTOR_PATCHES_ED74F2F2
)


def _motif_grid_ed74f2f2(
    patch: Indices,
) -> Grid:
    return fill(canvas(ZERO, THREE_BY_THREE), FIVE, patch)


def _right_motifs_ed74f2f2() -> tuple[Indices, ...]:
    x0 = []
    x1 = tuple((i, j) for i in range(THREE) for j in range(THREE))
    for x2 in range(FOUR, EIGHT):
        for x3 in combinations(x1, x2):
            x4 = frozenset(x3)
            if ORIGIN not in x4:
                continue
            if height(x4) != THREE or width(x4) != THREE:
                continue
            x5 = colorfilter(objects(_motif_grid_ed74f2f2(x4), T, T, F), FIVE)
            if size(x5) != ONE:
                continue
            if x4 in SELECTOR_PATCH_SET_ED74F2F2:
                continue
            x0.append(x4)
    x6 = lambda x7: (size(x7), tuple(sorted(x7)))
    return tuple(sorted(x0, key=x6))


RIGHT_MOTIFS_ED74F2F2 = _right_motifs_ed74f2f2()


def generate_ed74f2f2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0, x1 = choice(SELECTOR_PATCHES_ED74F2F2)
    x2 = choice(RIGHT_MOTIFS_ED74F2F2)
    x3 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x4 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x5 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x6 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x7 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x8 = astuple(add(add(x3, THREE), x4), add(add(add(add(x5, THREE), x6), THREE), x7))
    x9 = astuple(x3, x5)
    x10 = astuple(x3, add(add(x5, THREE), x6))
    gi = canvas(ZERO, x8)
    gi = fill(gi, FIVE, shift(x1, x9))
    gi = fill(gi, FIVE, shift(x2, x10))
    go = fill(canvas(ZERO, THREE_BY_THREE), x0, x2)
    return {"input": gi, "output": go}
