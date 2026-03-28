from arc2.core import *


GRID_SIZE_BOUNDS_52FD389E = (25, 30)
RECT_COUNT_BOUNDS_52FD389E = (2, 3)
HEIGHT_BOUNDS_52FD389E = (3, 8)
WIDTH_BOUNDS_52FD389E = (3, 10)
MARKER_COUNT_BOUNDS_52FD389E = (1, 4)
MARKER_COLORS_52FD389E = remove(FOUR, remove(ZERO, interval(ZERO, TEN, ONE)))


def _rectangle_patch(height: int, width: int, loc: tuple[int, int]) -> Indices:
    x0 = canvas(ZERO, (height, width))
    x1 = asindices(x0)
    x2 = shift(x1, loc)
    return x2


def _expanded_patch(rect: Indices, margin: int) -> Indices:
    x0 = astuple(margin, margin)
    x1 = subtract(ulcorner(rect), x0)
    x2 = add(lrcorner(rect), x0)
    x3 = frozenset({x1, x2})
    return backdrop(x3)


def _reserve_patch(frame: Indices, cells: Indices) -> Indices:
    x0 = astuple(ONE, ONE)
    x1 = subtract(ulcorner(frame), x0)
    x2 = add(lrcorner(frame), x0)
    x3 = backdrop(frozenset({x1, x2}))
    x4 = intersection(x3, cells)
    return x4


def _touches_border(frame: Indices, bounds: tuple[int, int]) -> bool:
    h, w = bounds
    x0 = equality(uppermost(frame), ZERO)
    x1 = equality(leftmost(frame), ZERO)
    x2 = equality(lowermost(frame), h - ONE)
    x3 = equality(rightmost(frame), w - ONE)
    return either(either(x0, x1), either(x2, x3))


def _marker_patch(interior: Indices, count: int) -> Indices:
    x0 = totuple(interior)
    for _ in range(6):
        x1 = frozenset(sample(x0, count))
        x2 = frozenset(i for i, _ in x1)
        x3 = frozenset(j for _, j in x1)
        if count == ONE or both(greater(size(x2), ONE), greater(size(x3), ONE)):
            return x1
    return frozenset(sample(x0, count))


def _placement_candidates(
    bounds: tuple[int, int],
    height: int,
    width: int,
    margin: int,
    reserved: Indices,
    cells: Indices,
) -> list[tuple[Indices, Indices, Indices]]:
    h, w = bounds
    cands = []
    for i in range(h - height + ONE):
        for j in range(w - width + ONE):
            rect = _rectangle_patch(height, width, (i, j))
            frame = intersection(_expanded_patch(rect, margin), cells)
            if len(intersection(frame, reserved)) != ZERO:
                continue
            reserve = _reserve_patch(frame, cells)
            cands.append((rect, frame, reserve))
    return cands


def generate_52fd389e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        side = unifint(diff_lb, diff_ub, GRID_SIZE_BOUNDS_52FD389E)
        bounds = (side, side)
        gi = canvas(ZERO, bounds)
        go = canvas(ZERO, bounds)
        cells = asindices(gi)
        reserved = frozenset({})
        placements = []
        nrects = unifint(diff_lb, diff_ub, RECT_COUNT_BOUNDS_52FD389E)
        colors = sample(MARKER_COLORS_52FD389E, nrects)
        specs = []
        for color in colors:
            for _ in range(20):
                marker_count = unifint(diff_lb, diff_ub, MARKER_COUNT_BOUNDS_52FD389E)
                height = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_52FD389E)
                width = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_52FD389E)
                if (height - TWO) * (width - TWO) < marker_count:
                    continue
                specs.append((marker_count, height, width, color))
                break
            else:
                specs = []
                break
        if len(specs) != nrects:
            continue
        specs = sorted(specs, key=lambda x0: (x0[0], x0[1] * x0[2]), reverse=True)
        failed = F
        for marker_count, height, width, color in specs:
            cands = _placement_candidates(bounds, height, width, marker_count, reserved, cells)
            if len(cands) == ZERO:
                failed = T
                break
            if choice((T, F, F)):
                edge_cands = [cand for cand in cands if _touches_border(cand[1], bounds)]
                if len(edge_cands) != ZERO:
                    cands = edge_cands
            rect, frame, reserve = choice(cands)
            placements.append((rect, frame, marker_count, color))
            reserved = combine(reserved, reserve)
        if failed:
            continue
        for rect, frame, marker_count, color in placements:
            inner = difference(rect, box(rect))
            markers = _marker_patch(inner, marker_count)
            gi = fill(gi, FOUR, rect)
            gi = fill(gi, color, markers)
            go = fill(go, color, frame)
            go = fill(go, FOUR, rect)
            go = fill(go, color, markers)
        if gi == go:
            continue
        if mostcolor(gi) != ZERO:
            continue
        return {"input": gi, "output": go}
