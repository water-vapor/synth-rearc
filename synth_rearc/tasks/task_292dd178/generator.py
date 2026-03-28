from synth_rearc.core import *

from .verifier import verify_292dd178


BACKGROUND_COLORS_292dd178 = (FOUR, FIVE, EIGHT, NINE)
HEIGHT_BOUNDS_292dd178 = (SEVEN, 15)
WIDTH_BOUNDS_292dd178 = (NINE, 15)
OBJECT_COUNT_CHOICES_292dd178 = (ONE, TWO, TWO, THREE)


def _frame_box_292dd178(
    top: Integer,
    left: Integer,
) -> frozenset[tuple[Integer, Integer]]:
    bottom = add(top, THREE)
    right = add(left, THREE)
    cells = {
        (top, col_index) for col_index in range(left, increment(right))
    }
    cells |= {
        (bottom, col_index) for col_index in range(left, increment(right))
    }
    cells |= {
        (row_index, left) for row_index in range(top, increment(bottom))
    }
    cells |= {
        (row_index, right) for row_index in range(top, increment(bottom))
    }
    return frozenset(cells)


def _interior_292dd178(
    top: Integer,
    left: Integer,
) -> frozenset[tuple[Integer, Integer]]:
    return frozenset(
        {
            (add(top, ONE), add(left, ONE)),
            (add(top, ONE), add(left, TWO)),
            (add(top, TWO), add(left, ONE)),
            (add(top, TWO), add(left, TWO)),
        }
    )


def _gap_options_292dd178(
    top: Integer,
    left: Integer,
) -> tuple[tuple[Integer, Integer], ...]:
    bottom = add(top, THREE)
    right = add(left, THREE)
    return (
        (top, add(left, ONE)),
        (top, add(left, TWO)),
        (bottom, add(left, ONE)),
        (bottom, add(left, TWO)),
        (add(top, ONE), left),
        (add(top, TWO), left),
        (add(top, ONE), right),
        (add(top, TWO), right),
    )


def _edge_endpoint_292dd178(
    gap: tuple[Integer, Integer],
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> tuple[Integer, Integer]:
    row_index, col_index = gap
    bottom = add(top, THREE)
    right = add(left, THREE)
    if row_index == top:
        return (ZERO, col_index)
    if row_index == bottom:
        return (decrement(height_value), col_index)
    if col_index == left:
        return (row_index, ZERO)
    return (row_index, decrement(width_value))


def _candidate_specs_292dd178(
    height_value: Integer,
    width_value: Integer,
) -> tuple[tuple[frozenset[tuple[Integer, Integer]], frozenset[tuple[Integer, Integer]]], ...]:
    candidates = []
    top_limit = subtract(height_value, THREE)
    left_limit = subtract(width_value, THREE)
    for top in range(top_limit):
        for left in range(left_limit):
            frame_box = _frame_box_292dd178(top, left)
            interior = _interior_292dd178(top, left)
            for gap in _gap_options_292dd178(top, left):
                frame = difference(frame_box, initset(gap))
                endpoint = _edge_endpoint_292dd178(gap, top, left, height_value, width_value)
                ray = connect(gap, endpoint)
                output = combine(interior, ray)
                candidates.append((frame, output))
    return tuple(candidates)


def _choose_specs_292dd178(
    candidates: tuple[tuple[frozenset[tuple[Integer, Integer]], frozenset[tuple[Integer, Integer]]], ...],
    target_count: Integer,
) -> tuple[tuple[frozenset[tuple[Integer, Integer]], frozenset[tuple[Integer, Integer]]], ...]:
    specs = list(candidates)
    shuffle(specs)
    chosen = []
    occupied_input = frozenset({})
    blocked_input = frozenset({})
    occupied_output = frozenset({})
    for frame, output in specs:
        if len(intersection(frame, blocked_input)) > ZERO:
            continue
        if len(intersection(frame, occupied_output)) > ZERO:
            continue
        if len(intersection(output, occupied_input)) > ZERO:
            continue
        if len(intersection(output, occupied_output)) > ZERO:
            continue
        chosen.append((frame, output))
        occupied_input = combine(occupied_input, frame)
        blocked_input = combine(blocked_input, frame)
        blocked_input = combine(blocked_input, mapply(dneighbors, frame))
        occupied_output = combine(occupied_output, output)
        if len(chosen) == target_count:
            return tuple(chosen)
    return ()


def generate_292dd178(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        height_value = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_292dd178)
        width_value = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_292dd178)
        background = choice(BACKGROUND_COLORS_292dd178)
        target_count = choice(OBJECT_COUNT_CHOICES_292dd178)
        candidates = _candidate_specs_292dd178(height_value, width_value)
        specs = _choose_specs_292dd178(candidates, target_count)
        if len(specs) != target_count:
            continue
        gi = canvas(background, (height_value, width_value))
        go = canvas(background, (height_value, width_value))
        for frame, output in specs:
            gi = fill(gi, ONE, frame)
            go = fill(go, ONE, frame)
            go = fill(go, TWO, output)
        if gi == go:
            continue
        if verify_292dd178(gi) != go:
            continue
        return {"input": gi, "output": go}
