from arc2.core import *


PALETTE_3EE1011A = (ONE, TWO, THREE, FOUR, SIX, SEVEN, EIGHT)


def _line_patch_3ee1011a(
    start: IntegerTuple,
    length: Integer,
    vertical: Boolean,
) -> Indices:
    end = add(start, (subtract(length, ONE), ZERO) if vertical else (ZERO, subtract(length, ONE)))
    return connect(start, end)


def _padded_patch_3ee1011a(
    patch: Indices,
    dims: tuple[Integer, Integer],
) -> Indices:
    height_, width_ = dims
    top = max(ZERO, uppermost(patch) - ONE)
    left = max(ZERO, leftmost(patch) - ONE)
    bottom = min(height_ - ONE, lowermost(patch) + ONE)
    right = min(width_ - ONE, rightmost(patch) + ONE)
    return frozenset((i, j) for i in range(top, bottom + ONE) for j in range(left, right + ONE))


def _lengths_3ee1011a(
    nobjs: Integer,
    outer: Integer,
) -> tuple[Integer, ...]:
    if nobjs == THREE and outer == FIVE:
        return (FIVE, FOUR, ONE)
    return tuple(outer - TWO * idx for idx in range(nobjs))


def _output_3ee1011a(
    colors: tuple[Integer, ...],
    outer: Integer,
) -> Grid:
    go = canvas(ZERO, (outer, outer))
    for depth, color_value in enumerate(colors):
        corner = outer - depth - ONE
        patch = backdrop(frozenset({(depth, depth), (corner, corner)}))
        go = fill(go, color_value, patch)
    return go


def generate_3ee1011a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        nobjs = unifint(diff_lb, diff_ub, (THREE, FOUR))
        outer = unifint(diff_lb, diff_ub, (FIVE, SIX)) if nobjs == THREE else unifint(diff_lb, diff_ub, (SEVEN, EIGHT))
        lengths = _lengths_3ee1011a(nobjs, outer)
        colors = tuple(sample(PALETTE_3EE1011A, nobjs))
        specs = [{"length": length, "color": color_value} for length, color_value in zip(lengths, colors)]

        height_ = unifint(diff_lb, diff_ub, (20, 25))
        width_ = unifint(diff_lb, diff_ub, (20, 29))
        gi = canvas(ZERO, (height_, width_))
        blocked: Indices = frozenset({})
        placed = True

        place_specs = list(specs)
        shuffle(place_specs)
        for spec in place_specs:
            length = spec["length"]
            found = False
            for _ in range(200):
                vertical = False if length == ONE else choice((T, F))
                max_i = height_ - (length if vertical else ONE)
                max_j = width_ - (ONE if vertical else length)
                start = (randint(ZERO, max_i), randint(ZERO, max_j))
                patch = _line_patch_3ee1011a(start, length, vertical)
                if patch & blocked:
                    continue
                gi = fill(gi, spec["color"], patch)
                blocked = blocked | _padded_patch_3ee1011a(patch, (height_, width_))
                found = True
                break
            if not found:
                placed = False
                break

        if not placed:
            continue

        go = _output_3ee1011a(colors, outer)
        if gi != go:
            return {"input": gi, "output": go}
