from synth_rearc.core import *


THREE_BY_THREE_E133D23D = astuple(THREE, THREE)
ALL_CELLS_E133D23D = tuple(sorted(product(interval(ZERO, THREE, ONE), interval(ZERO, THREE, ONE))))
SEPARATOR_E133D23D = connect((ZERO, THREE), (TWO, THREE))


def generate_e133d23d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        left_count = unifint(diff_lb, diff_ub, (TWO, SEVEN))
        right_count = unifint(diff_lb, diff_ub, (THREE, FIVE))
        overlap_lb = max(ONE, left_count + right_count - EIGHT)
        overlap_ub = min(THREE, left_count, right_count)
        if overlap_lb > overlap_ub:
            continue
        overlap_count = randint(overlap_lb, overlap_ub)
        if overlap_count == left_count == right_count:
            continue
        union_count = left_count + right_count - overlap_count
        if not (FOUR <= union_count <= EIGHT):
            continue
        union_cells = tuple(sample(ALL_CELLS_E133D23D, union_count))
        overlap_cells = frozenset(sample(union_cells, overlap_count))
        residual_cells = tuple(cell for cell in union_cells if cell not in overlap_cells)
        left_only_count = left_count - overlap_count
        left_only_cells = (
            frozenset(sample(residual_cells, left_only_count))
            if left_only_count > ZERO
            else frozenset()
        )
        right_only_cells = frozenset(cell for cell in residual_cells if cell not in left_only_cells)
        left_patch = combine(overlap_cells, left_only_cells)
        right_patch = combine(overlap_cells, right_only_cells)
        gi = canvas(ZERO, (THREE, SEVEN))
        gi = fill(gi, FOUR, SEPARATOR_E133D23D)
        gi = fill(gi, SIX, left_patch)
        gi = fill(gi, EIGHT, shift(right_patch, astuple(ZERO, FOUR)))
        go = fill(canvas(ZERO, THREE_BY_THREE_E133D23D), TWO, combine(left_patch, right_patch))
        return {"input": gi, "output": go}
