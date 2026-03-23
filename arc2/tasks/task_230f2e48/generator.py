from arc2.core import *
from .verifier import verify_230f2e48


MAIN_DIRECTIONS_230F2E48 = (UP, DOWN, LEFT, RIGHT)
STEM_LENGTHS_230F2E48 = (ONE, ONE, TWO, TWO, THREE, THREE, FOUR, FIVE)
TAIL_LENGTHS_230F2E48 = (ONE, TWO, TWO, THREE, THREE, FOUR, FIVE, SIX)
TOP_K_OPTIONS_230F2E48 = (THREE, FOUR, FIVE, SIX, SEVEN, EIGHT)


def _ray_230f2e48(
    start: IntegerTuple,
    direction: IntegerTuple,
    length: int,
) -> Indices:
    return frozenset(add(start, multiply(k, direction)) for k in range(length))


def _halo_230f2e48(patch: Indices) -> Indices:
    x0 = mapply(neighbors, patch)
    x1 = combine(patch, x0)
    return x1


def _turn_direction_230f2e48(
    zero_loc: IntegerTuple,
    main_direction: IntegerTuple,
    dims: IntegerTuple,
) -> IntegerTuple | None:
    if main_direction[1] == ZERO:
        left_gap = zero_loc[1]
        right_gap = dims[1] - ONE - zero_loc[1]
        if left_gap == right_gap:
            return None
        return RIGHT if left_gap < right_gap else LEFT
    top_gap = zero_loc[0]
    bottom_gap = dims[0] - ONE - zero_loc[0]
    if top_gap == bottom_gap:
        return None
    return DOWN if top_gap < bottom_gap else UP


def _arm_payload_230f2e48(
    dims: IntegerTuple,
    zero_loc: IntegerTuple,
    main_direction: IntegerTuple,
    stem_len: int,
    tail_len: int,
) -> dict | None:
    turn_direction = _turn_direction_230f2e48(zero_loc, main_direction, dims)
    if turn_direction is None:
        return None
    five_loc = add(zero_loc, multiply(-(stem_len + ONE), main_direction))
    stem_start = add(five_loc, main_direction)
    tail_start = add(zero_loc, main_direction)
    branch_start = add(zero_loc, turn_direction)
    stem_patch = _ray_230f2e48(stem_start, main_direction, stem_len)
    tail_patch = _ray_230f2e48(tail_start, main_direction, tail_len)
    branch_patch = _ray_230f2e48(branch_start, turn_direction, tail_len)
    input_patch = combine(
        combine(stem_patch, tail_patch),
        combine(initset(five_loc), initset(zero_loc)),
    )
    output_patch = combine(
        combine(stem_patch, branch_patch),
        combine(initset(five_loc), initset(zero_loc)),
    )
    if not all(ZERO <= i < dims[0] and ZERO <= j < dims[1] for i, j in input_patch):
        return None
    if not all(ZERO <= i < dims[0] and ZERO <= j < dims[1] for i, j in output_patch):
        return None
    x0 = recolor(TWO, combine(stem_patch, tail_patch))
    x1 = recolor(TWO, combine(stem_patch, branch_patch))
    x2 = recolor(FIVE, initset(five_loc))
    x3 = recolor(ZERO, initset(zero_loc))
    x4 = combine(combine(x0, x2), x3)
    x5 = combine(combine(x1, x2), x3)
    x6 = combine(input_patch, output_patch)
    if main_direction[1] == ZERO:
        edge_score = min(zero_loc[1], dims[1] - ONE - zero_loc[1])
    else:
        edge_score = min(zero_loc[0], dims[0] - ONE - zero_loc[0])
    return {
        "input_obj": x4,
        "output_obj": x5,
        "footprint": x6,
        "edge_score": edge_score,
    }


def _placement_candidates_230f2e48(
    dims: IntegerTuple,
    main_direction: IntegerTuple,
    stem_len: int,
    tail_len: int,
    forbidden: Indices,
) -> list[dict]:
    candidates = []
    for i in range(dims[0]):
        for j in range(dims[1]):
            payload = _arm_payload_230f2e48(dims, (i, j), main_direction, stem_len, tail_len)
            if payload is None:
                continue
            if len(intersection(payload["footprint"], forbidden)) != ZERO:
                continue
            candidates.append(payload)
    return candidates


def generate_230f2e48(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (EIGHT, 18))
        x1 = unifint(diff_lb, diff_ub, (EIGHT, 18))
        x2 = x0 * x1
        if x2 < 100:
            x3 = choice((ONE, TWO, TWO))
        elif x2 < 180:
            x3 = choice((ONE, TWO, TWO, THREE))
        else:
            x3 = choice((ONE, TWO, TWO, THREE, THREE, FOUR))
        x4 = canvas(SEVEN, (x0, x1))
        x5 = x4
        x6 = frozenset({})
        x7 = ZERO
        x8 = F
        for _ in range(x3):
            x9 = F
            for _ in range(120):
                x10 = choice(MAIN_DIRECTIONS_230F2E48)
                x11 = choice(STEM_LENGTHS_230F2E48)
                x12 = choice(TAIL_LENGTHS_230F2E48)
                x13 = _placement_candidates_230f2e48((x0, x1), x10, x11, x12, x6)
                if len(x13) == ZERO:
                    continue
                x14 = sorted(x13, key=lambda x: x["edge_score"])
                x15 = min(len(x14), choice(TOP_K_OPTIONS_230F2E48))
                x16 = choice(x14[:x15])
                x4 = paint(x4, x16["input_obj"])
                x5 = paint(x5, x16["output_obj"])
                x6 = combine(x6, _halo_230f2e48(x16["footprint"]))
                x7 = increment(x7)
                x9 = T
                break
            if flip(x9):
                x8 = T
                break
        if x8:
            continue
        if x7 == ZERO:
            continue
        if x4 == x5:
            continue
        if verify_230f2e48(x4) != x5:
            continue
        return {"input": x4, "output": x5}
