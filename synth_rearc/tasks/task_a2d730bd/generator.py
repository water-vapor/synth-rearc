from synth_rearc.core import *


NCOLORS_OPTIONS_A2D730BD = (ONE, ONE, TWO, TWO, TWO, THREE)
MARKER_COUNT_OPTIONS_A2D730BD = (ONE, ONE, TWO, TWO, THREE)
VERTICAL_RECT_SHAPES_A2D730BD = (
    (SIX, THREE),
    (SEVEN, THREE),
    (SEVEN, FOUR),
    (EIGHT, THREE),
    (EIGHT, FOUR),
    (NINE, THREE),
)
HORIZONTAL_RECT_SHAPES_A2D730BD = (
    (TWO, SEVEN),
    (TWO, EIGHT),
    (THREE, EIGHT),
    (THREE, NINE),
    (THREE, TEN),
    (THREE, 11),
    (FOUR, TEN),
    (FOUR, 12),
)
MAX_GAP_A2D730BD = EIGHT


def _rectangle_patch_a2d730bd(
    shape_: tuple[int, int],
    loc: tuple[int, int],
) -> Indices:
    x0 = asindices(canvas(ZERO, shape_))
    x1 = shift(x0, loc)
    return x1


def _halo_a2d730bd(patch: Indices) -> Indices:
    x0 = mapply(dneighbors, patch)
    x1 = combine(patch, x0)
    return x1


def _in_bounds_a2d730bd(
    patch: Indices,
    dims: tuple[int, int],
) -> bool:
    return all(ZERO <= i < dims[0] and ZERO <= j < dims[1] for i, j in patch)


def _connector_anchor_a2d730bd(
    rect: Indices,
    marker: tuple[int, int],
) -> tuple[int, int]:
    x0 = uppermost(rect)
    x1 = lowermost(rect)
    x2 = leftmost(rect)
    x3 = rightmost(rect)
    if x0 <= marker[0] <= x1:
        if marker[1] < x2:
            return (marker[0], x2 - ONE)
        return (marker[0], x3 + ONE)
    if marker[0] < x0:
        return (x0 - ONE, marker[1])
    return (x1 + ONE, marker[1])


def _connector_patch_a2d730bd(
    rect: Indices,
    marker: tuple[int, int],
) -> Indices:
    x0 = _connector_anchor_a2d730bd(rect, marker)
    x1 = connect(marker, x0)
    x2 = combine(x1, dneighbors(marker))
    x3 = combine(x2, dneighbors(x0))
    x4 = remove(marker, x3)
    return x4


def _rectangle_candidates_a2d730bd(
    dims: tuple[int, int],
    blocked_output: set[tuple[int, int]],
) -> list[Indices]:
    candidates = []
    shapes = choice((VERTICAL_RECT_SHAPES_A2D730BD, HORIZONTAL_RECT_SHAPES_A2D730BD))
    shape_ = choice(shapes)
    for i in range(ONE, dims[0] - shape_[0]):
        for j in range(ONE, dims[1] - shape_[1]):
            rect = _rectangle_patch_a2d730bd(shape_, (i, j))
            if len(intersection(_halo_a2d730bd(rect), frozenset(blocked_output))) == ZERO:
                candidates.append(rect)
    return candidates


def _marker_candidates_a2d730bd(
    rect: Indices,
    dims: tuple[int, int],
    blocked_input: set[tuple[int, int]],
    blocked_output: set[tuple[int, int]],
) -> list[tuple[tuple[int, int], Indices]]:
    candidates = []
    top = uppermost(rect)
    bottom = lowermost(rect)
    left = leftmost(rect)
    right = rightmost(rect)
    rect_set = set(rect)
    for j in range(left, right + ONE):
        for gap in range(TWO, min(MAX_GAP_A2D730BD, top - ONE) + ONE):
            marker = (top - gap, j)
            if marker in blocked_input:
                continue
            if any(neighbor in blocked_input for neighbor in dneighbors(marker)):
                continue
            patch = _connector_patch_a2d730bd(rect, marker)
            extra = set(patch) - rect_set
            if not _in_bounds_a2d730bd(frozenset(extra), dims):
                continue
            if any(cell in blocked_output for cell in extra):
                continue
            candidates.append((marker, patch))
        for gap in range(TWO, min(MAX_GAP_A2D730BD, dims[0] - bottom - TWO) + ONE):
            marker = (bottom + gap, j)
            if marker in blocked_input:
                continue
            if any(neighbor in blocked_input for neighbor in dneighbors(marker)):
                continue
            patch = _connector_patch_a2d730bd(rect, marker)
            extra = set(patch) - rect_set
            if not _in_bounds_a2d730bd(frozenset(extra), dims):
                continue
            if any(cell in blocked_output for cell in extra):
                continue
            candidates.append((marker, patch))
    for i in range(top, bottom + ONE):
        for gap in range(TWO, min(MAX_GAP_A2D730BD, left - ONE) + ONE):
            marker = (i, left - gap)
            if marker in blocked_input:
                continue
            if any(neighbor in blocked_input for neighbor in dneighbors(marker)):
                continue
            patch = _connector_patch_a2d730bd(rect, marker)
            extra = set(patch) - rect_set
            if not _in_bounds_a2d730bd(frozenset(extra), dims):
                continue
            if any(cell in blocked_output for cell in extra):
                continue
            candidates.append((marker, patch))
        for gap in range(TWO, min(MAX_GAP_A2D730BD, dims[1] - right - TWO) + ONE):
            marker = (i, right + gap)
            if marker in blocked_input:
                continue
            if any(neighbor in blocked_input for neighbor in dneighbors(marker)):
                continue
            patch = _connector_patch_a2d730bd(rect, marker)
            extra = set(patch) - rect_set
            if not _in_bounds_a2d730bd(frozenset(extra), dims):
                continue
            if any(cell in blocked_output for cell in extra):
                continue
            candidates.append((marker, patch))
    return candidates


def generate_a2d730bd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (16, 30))
        x1 = unifint(diff_lb, diff_ub, (16, 30))
        x2 = choice(interval(ZERO, TEN, ONE))
        x3 = canvas(x2, (x0, x1))
        x4 = x3
        x5 = [x6 for x6 in interval(ZERO, TEN, ONE) if x6 != x2]
        shuffle(x5)
        x6 = choice(NCOLORS_OPTIONS_A2D730BD)
        x7 = x5[:x6]
        occupied_input: set[tuple[int, int]] = set()
        occupied_output: set[tuple[int, int]] = set()
        failed = F
        for x8 in x7:
            placed = F
            for _ in range(80):
                rect_candidates = _rectangle_candidates_a2d730bd((x0, x1), occupied_output)
                if len(rect_candidates) == ZERO:
                    break
                x9 = choice(rect_candidates)
                x10 = set(x9)
                x11 = set(x10)
                x12 = set(x10)
                x13 = []
                x14 = choice(MARKER_COUNT_OPTIONS_A2D730BD)
                for x15 in range(x14):
                    x16 = occupied_input | x11
                    x17 = occupied_output | (x12 - x10)
                    x18 = _marker_candidates_a2d730bd(x9, (x0, x1), x16, x17)
                    if len(x18) == ZERO:
                        if x15 == ZERO:
                            x13 = []
                            break
                        break
                    x19, x20 = choice(x18)
                    x13.append((x19, x20))
                    x11.add(x19)
                    x12 |= set(x20)
                if len(x13) == ZERO:
                    continue
                x3 = fill(x3, x8, x9)
                x4 = fill(x4, x8, x9)
                for x19, x20 in x13:
                    x3 = fill(x3, x8, frozenset({x19}))
                    x4 = fill(x4, x8, x20)
                occupied_input |= x11
                occupied_output |= x12
                placed = T
                break
            if flip(placed):
                failed = T
                break
        if failed:
            continue
        if x3 == x4:
            continue
        if mostcolor(x3) != x2:
            continue
        return {"input": x3, "output": x4}
