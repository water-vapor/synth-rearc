from arc2.core import *


_MOTIF_COLORS_B4A43F3B = tuple(x0 for x0 in interval(ONE, TEN, ONE) if x0 != FIVE)
_NEIGHBORS8_B4A43F3B = (
    UP,
    DOWN,
    LEFT,
    RIGHT,
    UP_RIGHT,
    DOWN_LEFT,
    NEG_UNITY,
    UNITY,
)


def _in_bounds_b4a43f3b(
    loc: IntegerTuple,
) -> bool:
    i, j = loc
    return 0 <= i < SIX and 0 <= j < SIX


def _stroke_b4a43f3b(
    start: IntegerTuple,
    direction: IntegerTuple,
    length: int,
) -> tuple[IntegerTuple, ...]:
    cells = []
    loc = start
    for _ in range(length):
        if not _in_bounds_b4a43f3b(loc):
            return tuple()
        cells.append(loc)
        loc = add(loc, direction)
    return tuple(cells)


def _max_length_b4a43f3b(
    start: IntegerTuple,
    direction: IntegerTuple,
) -> int:
    length = ZERO
    loc = start
    while _in_bounds_b4a43f3b(loc):
        length = increment(length)
        loc = add(loc, direction)
    return length


def _good_markers_b4a43f3b(
    cells: set[IntegerTuple],
) -> bool:
    if not 4 <= len(cells) <= 12:
        return False
    rows = {i for i, _ in cells}
    cols = {j for _, j in cells}
    return len(rows) >= TWO and len(cols) >= TWO


def _cross_markers_b4a43f3b(
    diff_lb: float,
    diff_ub: float,
) -> frozenset[IntegerTuple]:
    while True:
        i = unifint(diff_lb, diff_ub, (ZERO, FIVE))
        j = unifint(diff_lb, diff_ub, (ZERO, FIVE))
        cells = set()
        if choice((T, T, F)):
            left = unifint(diff_lb, diff_ub, (ZERO, j))
            right = unifint(diff_lb, diff_ub, (ZERO, FIVE - j))
            if left + right < TWO:
                continue
            up = unifint(diff_lb, diff_ub, (ZERO, i))
            down = unifint(diff_lb, diff_ub, (ZERO, FIVE - i))
            if both(equality(up, ZERO), equality(down, ZERO)):
                if i == ZERO:
                    down = ONE
                elif i == FIVE:
                    up = ONE
                elif choice((T, F)):
                    up = ONE
                else:
                    down = ONE
            for x0 in range(j - left, j + right + ONE):
                cells.add((i, x0))
            for x1 in range(i - up, i + down + ONE):
                cells.add((x1, j))
        else:
            up = unifint(diff_lb, diff_ub, (ZERO, i))
            down = unifint(diff_lb, diff_ub, (ZERO, FIVE - i))
            if up + down < TWO:
                continue
            left = unifint(diff_lb, diff_ub, (ZERO, j))
            right = unifint(diff_lb, diff_ub, (ZERO, FIVE - j))
            if both(equality(left, ZERO), equality(right, ZERO)):
                if j == ZERO:
                    right = ONE
                elif j == FIVE:
                    left = ONE
                elif choice((T, F)):
                    left = ONE
                else:
                    right = ONE
            for x2 in range(i - up, i + down + ONE):
                cells.add((x2, j))
            for x3 in range(j - left, j + right + ONE):
                cells.add((i, x3))
        if choice((T, F, F)):
            extras = []
            for x4 in ((i - ONE, j - ONE), (i - ONE, j + ONE), (i + ONE, j - ONE), (i + ONE, j + ONE)):
                if _in_bounds_b4a43f3b(x4):
                    extras.append(x4)
            if len(extras) > ZERO:
                cells.add(choice(tuple(extras)))
        if _good_markers_b4a43f3b(cells):
            return frozenset(cells)


def _stair_markers_b4a43f3b(
    diff_lb: float,
    diff_ub: float,
) -> frozenset[IntegerTuple]:
    while True:
        length = unifint(diff_lb, diff_ub, (THREE, FIVE))
        step = choice((ONE, NEG_ONE))
        start_i = unifint(diff_lb, diff_ub, (ZERO, SIX - length))
        if equality(step, ONE):
            start_j = unifint(diff_lb, diff_ub, (ZERO, SIX - length))
        else:
            start_j = unifint(diff_lb, diff_ub, (length - ONE, FIVE))
        cells = {
            (start_i + x0, start_j + step * x0)
            for x0 in range(length)
        }
        head = (start_i, start_j)
        if choice((T, T, F)):
            for x1 in ((head[0] + ONE, head[1]), (head[0], head[1] + step)):
                if _in_bounds_b4a43f3b(x1):
                    cells.add(x1)
        tail = (start_i + length - ONE, start_j + step * (length - ONE))
        if choice((T, F)):
            span_max = FIVE - tail[1] if equality(step, ONE) else tail[1]
            if span_max > ZERO:
                span = unifint(diff_lb, diff_ub, (ONE, min(TWO, span_max)))
                for x2 in range(ONE, span + ONE):
                    cells.add((tail[0], tail[1] + step * x2))
        if _good_markers_b4a43f3b(cells):
            return frozenset(cells)


def _branch_directions_b4a43f3b(
    direction: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    if equality(direction, RIGHT):
        return (UP, DOWN, UP_RIGHT, UNITY)
    if equality(direction, DOWN):
        return (LEFT, RIGHT, DOWN_LEFT, UNITY)
    if equality(direction, UNITY):
        return (RIGHT, DOWN, LEFT, UP)
    return (LEFT, DOWN, RIGHT, UP)


def _polyline_markers_b4a43f3b(
    diff_lb: float,
    diff_ub: float,
) -> frozenset[IntegerTuple]:
    while True:
        start = (
            unifint(diff_lb, diff_ub, (ZERO, FIVE)),
            unifint(diff_lb, diff_ub, (ZERO, FIVE)),
        )
        direction = choice((RIGHT, DOWN, UNITY, DOWN_LEFT))
        max_length = _max_length_b4a43f3b(start, direction)
        if max_length < THREE:
            continue
        length = unifint(diff_lb, diff_ub, (THREE, min(SIX, max_length)))
        stem = _stroke_b4a43f3b(start, direction, length)
        anchor = choice(stem)
        turn = choice(_branch_directions_b4a43f3b(direction))
        branch_max = _max_length_b4a43f3b(anchor, turn)
        if branch_max < TWO:
            continue
        branch_length = unifint(diff_lb, diff_ub, (TWO, min(FOUR, branch_max)))
        branch = _stroke_b4a43f3b(anchor, turn, branch_length)
        cells = set(stem) | set(branch)
        if choice((T, F, F)):
            fringe = []
            for x0 in tuple(cells):
                for x1 in _NEIGHBORS8_B4A43F3B:
                    x2 = add(x0, x1)
                    if _in_bounds_b4a43f3b(x2) and x2 not in cells:
                        fringe.append(x2)
            if len(fringe) > ZERO:
                cells.add(choice(tuple(fringe)))
        if _good_markers_b4a43f3b(cells):
            return frozenset(cells)


def _make_markers_b4a43f3b(
    diff_lb: float,
    diff_ub: float,
) -> frozenset[IntegerTuple]:
    x0 = choice((
        _cross_markers_b4a43f3b,
        _cross_markers_b4a43f3b,
        _stair_markers_b4a43f3b,
        _polyline_markers_b4a43f3b,
    ))
    return x0(diff_lb, diff_ub)


def _make_motif_b4a43f3b(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    while True:
        count = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        cells = {(x0, x1) for x0, x1 in zip(interval(ZERO, THREE, ONE), sample(interval(ZERO, THREE, ONE), THREE))}
        remaining = [(x2, x3) for x2 in range(THREE) for x3 in range(THREE) if (x2, x3) not in cells]
        shuffle(remaining)
        while len(cells) < count:
            cells.add(remaining.pop())
        palette_size = unifint(diff_lb, diff_ub, (TWO, min(FOUR, len(cells))))
        colors = tuple(sample(_MOTIF_COLORS_B4A43F3B, palette_size))
        grid = canvas(ZERO, THREE_BY_THREE)
        for x4 in cells:
            grid = fill(grid, choice(colors), initset(x4))
        used = difference(palette(grid), initset(ZERO))
        if len(used) >= TWO:
            return grid


def _stamp_output_b4a43f3b(
    motif: Grid,
    markers: Indices,
) -> Grid:
    x0 = apply(rbind(multiply, THREE), markers)
    x1 = canvas(ZERO, multiply((SIX, SIX), THREE))
    x2 = difference(palette(motif), initset(ZERO))
    for x3 in x2:
        x4 = ofcolor(motif, x3)
        x5 = lbind(shift, x4)
        x6 = mapply(x5, x0)
        x1 = fill(x1, x3, x6)
    return x1


def generate_b4a43f3b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        motif = _make_motif_b4a43f3b(diff_lb, diff_ub)
        markers = _make_markers_b4a43f3b(diff_lb, diff_ub)
        top = upscale(motif, TWO)
        sep = canvas(FIVE, (ONE, SIX))
        bottom = fill(canvas(ZERO, (SIX, SIX)), TWO, markers)
        gi = top + sep + bottom
        go = _stamp_output_b4a43f3b(motif, markers)
        if equality(gi, go):
            continue
        from .verifier import verify_b4a43f3b

        if verify_b4a43f3b(gi) != go:
            continue
        return {"input": gi, "output": go}
