from synth_rearc.core import *

from .verifier import verify_2697da3f


MARGIN_BOUNDS_2697da3f = (ONE, THREE)


def _neighbors_2697da3f(
    loc: IntegerTuple,
    height_value: Integer,
    width_value: Integer,
) -> tuple[IntegerTuple, ...]:
    i, j = loc
    out = []
    if positive(i):
        out.append((decrement(i), j))
    if i < decrement(height_value):
        out.append((increment(i), j))
    if positive(j):
        out.append((i, decrement(j)))
    if j < decrement(width_value):
        out.append((i, increment(j)))
    return tuple(out)


def _connected_2697da3f(
    patch: frozenset[IntegerTuple],
    height_value: Integer,
    width_value: Integer,
) -> Boolean:
    frontier = [next(iter(patch))]
    seen = {frontier[ZERO]}
    while len(frontier) > ZERO:
        loc = frontier.pop()
        for neighbor in _neighbors_2697da3f(loc, height_value, width_value):
            if neighbor in patch and neighbor not in seen:
                seen.add(neighbor)
                frontier.append(neighbor)
    return len(seen) == len(patch)


def _profile_ok_2697da3f(
    patch: frozenset[IntegerTuple],
    height_value: Integer,
    width_value: Integer,
) -> Boolean:
    area = multiply(height_value, width_value)
    lo = max(add(height_value, ONE), divide(area, THREE))
    hi = subtract(area, ONE)
    row_counts = [sum((i, j) in patch for j in range(width_value)) for i in range(height_value)]
    col_counts = [sum((i, j) in patch for i in range(height_value)) for j in range(width_value)]
    degrees = [
        sum(neighbor in patch for neighbor in _neighbors_2697da3f(loc, height_value, width_value))
        for loc in patch
    ]
    interior = sum(
        ZERO < i < decrement(height_value) and ZERO < j < decrement(width_value)
        for i, j in patch
    )
    return (
        lo <= len(patch) <= hi
        and min(row_counts) >= ONE
        and min(col_counts) >= ONE
        and max(row_counts) >= TWO
        and max(col_counts) >= TWO
        and interior >= ONE
        and max(degrees) >= THREE
        and _connected_2697da3f(patch, height_value, width_value)
    )


def _frontier_bag_2697da3f(
    patch: frozenset[IntegerTuple],
    height_value: Integer,
    width_value: Integer,
) -> tuple[IntegerTuple, ...]:
    rows = {i for i, _ in patch}
    cols = {j for _, j in patch}
    bag = []
    frontier = {
        neighbor
        for loc in patch
        for neighbor in _neighbors_2697da3f(loc, height_value, width_value)
        if neighbor not in patch
    }
    for loc in frontier:
        i, j = loc
        weight = ONE
        if i not in rows:
            weight = add(weight, TWO)
        if j not in cols:
            weight = add(weight, TWO)
        weight = add(
            weight,
            sum(neighbor in patch for neighbor in _neighbors_2697da3f(loc, height_value, width_value)),
        )
        bag.extend([loc] * weight)
    return tuple(bag)


def _make_patch_2697da3f(
    diff_lb: float,
    diff_ub: float,
    height_value: Integer,
    width_value: Integer,
) -> frozenset[IntegerTuple] | None:
    area = multiply(height_value, width_value)
    lo = max(add(height_value, ONE), divide(area, THREE))
    hi = min(subtract(area, ONE), add(divide(multiply(area, TWO), THREE), ONE))
    for _ in range(240):
        target = unifint(diff_lb, diff_ub, (lo, hi))
        seed = (
            randint(ZERO, decrement(height_value)),
            randint(ZERO, decrement(width_value)),
        )
        patch = {seed}
        while len(patch) < target:
            bag = _frontier_bag_2697da3f(frozenset(patch), height_value, width_value)
            if len(bag) == ZERO:
                break
            patch.add(choice(bag))
        patch = frozenset(patch)
        if len(patch) != target:
            continue
        if _profile_ok_2697da3f(patch, height_value, width_value):
            return patch
    return None


def _shape_dims_2697da3f(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Integer]:
    height_value = unifint(diff_lb, diff_ub, (THREE, FIVE))
    if height_value == THREE:
        width_value = FOUR
    else:
        width_value = add(height_value, choice((ZERO, ZERO, ONE)))
    return height_value, width_value


def generate_2697da3f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        height_value, width_value = _shape_dims_2697da3f(diff_lb, diff_ub)
        patch = _make_patch_2697da3f(diff_lb, diff_ub, height_value, width_value)
        if patch is None:
            continue
        top = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_2697da3f)
        bottom = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_2697da3f)
        left = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_2697da3f)
        right = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_2697da3f)
        input_height = add(height_value, add(top, bottom))
        input_width = add(width_value, add(left, right))
        shifted_patch = shift(patch, (top, left))
        gi = fill(canvas(ZERO, (input_height, input_width)), FOUR, shifted_patch)
        go = verify_2697da3f(gi)
        if verify_2697da3f(gi) != go:
            continue
        return {"input": gi, "output": go}
