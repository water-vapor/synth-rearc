from synth_rearc.core import *


COLORS_538B439F = remove(ZERO, interval(ZERO, TEN, ONE))
SINGLETON_NOISE_538B439F = frozenset({ORIGIN})
DOMINO_NOISE_SHAPES_538B439F = (
    frozenset({ORIGIN, RIGHT}),
    frozenset({ORIGIN, DOWN}),
)
TROMINO_NOISE_SHAPES_538B439F = (
    frozenset({ORIGIN, RIGHT, DOWN}),
    frozenset({ORIGIN, RIGHT, add(DOWN, RIGHT)}),
    frozenset({ORIGIN, DOWN, add(DOWN, RIGHT)}),
    frozenset({RIGHT, DOWN, add(DOWN, RIGHT)}),
)


def _intervals_separated_538b439f(
    candidate: tuple[int, int],
    placed: tuple[tuple[int, int], ...],
) -> Boolean:
    x0, x1 = candidate
    for x2, x3 in placed:
        if not (x1 < x2 - ONE or x3 < x0 - ONE):
            return F
    return T


def _make_rectangle_538b439f(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> frozenset[tuple[int, int]]:
    return frozenset(
        (i, j)
        for i in range(top, top + height_)
        for j in range(left, left + width_)
    )


def _reflect_rectangle_538b439f(
    rect: frozenset[tuple[int, int]],
    orientation: str,
    axis: Integer,
) -> frozenset[tuple[int, int]]:
    if orientation == "vertical":
        return frozenset((i, subtract(multiply(TWO, axis), j)) for i, j in rect)
    return frozenset((subtract(multiply(TWO, axis), i), j) for i, j in rect)


def _transform_538b439f(
    gi: Grid,
    rectangles: tuple[frozenset[tuple[int, int]], ...],
    orientation: str,
    axis: Integer,
    line_color: Integer,
    rect_color: Integer,
) -> Grid:
    x0 = gi
    for x1 in rectangles:
        x2 = _reflect_rectangle_538b439f(x1, orientation, axis)
        x3 = combine(x1, x2)
        x4 = backdrop(x3)
        x0 = fill(x0, line_color, x4)
        x0 = fill(x0, rect_color, x1)
        x0 = fill(x0, rect_color, x2)
    return x0


def _sample_vertical_rectangles_538b439f(
    h: Integer,
    w: Integer,
    axis: Integer,
    nrects: Integer,
) -> tuple[frozenset[tuple[int, int]], ...]:
    x0 = min(FIVE, subtract(axis, TWO), subtract(subtract(w, axis), TWO))
    if x0 < TWO:
        raise RuntimeError("insufficient width for vertical layout")
    for _ in range(200):
        x1 = []
        x2 = []
        x3 = T
        for _ in range(nrects):
            x4 = randint(TWO, min(FIVE, subtract(h, add(nrects, TWO))))
            x5 = randint(ONE, subtract(subtract(h, x4), ONE))
            x6 = add(x5, subtract(x4, ONE))
            x7 = (x5, x6)
            if not _intervals_separated_538b439f(x7, tuple(x2)):
                x3 = F
                break
            x8 = randint(TWO, x0)
            x9 = max(ONE, subtract(multiply(TWO, axis), subtract(w, TWO)))
            x10 = subtract(subtract(axis, x8), ONE)
            if x10 < x9:
                x3 = F
                break
            x11 = randint(x9, x10)
            x12 = _make_rectangle_538b439f(x5, x11, x4, x8)
            x1.append(x12)
            x2.append(x7)
        if x3 and len(x1) == nrects:
            return tuple(x1)
    raise RuntimeError("failed to place vertical rectangles")


def _sample_horizontal_rectangles_538b439f(
    h: Integer,
    w: Integer,
    axis: Integer,
    nrects: Integer,
) -> tuple[frozenset[tuple[int, int]], ...]:
    x0 = min(FIVE, subtract(axis, TWO), subtract(subtract(h, axis), TWO))
    if x0 < TWO:
        raise RuntimeError("insufficient height for horizontal layout")
    for _ in range(200):
        x1 = []
        x2 = []
        x3 = T
        for _ in range(nrects):
            x4 = randint(TWO, min(FIVE, subtract(w, add(nrects, TWO))))
            x5 = randint(ONE, subtract(subtract(w, x4), ONE))
            x6 = add(x5, subtract(x4, ONE))
            x7 = (x5, x6)
            if not _intervals_separated_538b439f(x7, tuple(x2)):
                x3 = F
                break
            x8 = randint(TWO, x0)
            x9 = add(axis, TWO)
            x10 = min(subtract(subtract(h, x8), ONE), subtract(multiply(TWO, axis), x8))
            if x10 < x9:
                x3 = F
                break
            x11 = randint(x9, x10)
            x12 = _make_rectangle_538b439f(x11, x5, x8, x4)
            x1.append(x12)
            x2.append(x7)
        if x3 and len(x1) == nrects:
            return tuple(x1)
    raise RuntimeError("failed to place horizontal rectangles")


def _can_place_noise_538b439f(
    shape: frozenset[tuple[int, int]],
    blocked: frozenset[tuple[int, int]],
    occupied: frozenset[tuple[int, int]],
    dims: tuple[int, int],
) -> Boolean:
    x0, x1 = dims
    for x2 in shape:
        if x2 in blocked or x2 in occupied:
            return F
        if not (ZERO <= x2[ZERO] < x0 and ZERO <= x2[ONE] < x1):
            return F
        for x3 in dneighbors(x2):
            if x3 in occupied and x3 not in shape:
                return F
    return T


def _add_noise_538b439f(
    gi: Grid,
    rectangles: tuple[frozenset[tuple[int, int]], ...],
    line_patch: frozenset[tuple[int, int]],
    noise_color: Integer,
    nnoise: Integer,
) -> Grid:
    x0 = shape(gi)
    x1 = combine(line_patch, merge(rectangles))
    x2 = frozenset()
    x3 = gi
    x4 = ZERO
    if nnoise >= 12 and randint(ZERO, TWO) == ZERO:
        x4 = ONE
        if nnoise >= 20 and randint(ZERO, FOUR) == ZERO:
            x4 = add(x4, ONE)
        if nnoise >= 30 and randint(ZERO, SIX) == ZERO:
            x4 = add(x4, ONE)
    x5 = ZERO
    if nnoise >= 14 and randint(ZERO, SIX) == ZERO:
        x5 = ONE

    for _ in range(x4):
        for _ in range(200):
            x6 = choice(DOMINO_NOISE_SHAPES_538B439F)
            x7 = randint(ZERO, subtract(x0[ZERO], ONE))
            x8 = randint(ZERO, subtract(x0[ONE], ONE))
            x9 = shift(x6, (x7, x8))
            if not _can_place_noise_538b439f(x9, x1, x2, x0):
                continue
            x3 = fill(x3, noise_color, x9)
            x2 = combine(x2, x9)
            break

    for _ in range(x5):
        if add(size(x2), THREE) > nnoise:
            break
        for _ in range(200):
            x6 = choice(TROMINO_NOISE_SHAPES_538B439F)
            x7 = randint(ZERO, subtract(x0[ZERO], ONE))
            x8 = randint(ZERO, subtract(x0[ONE], ONE))
            x9 = shift(x6, (x7, x8))
            if not _can_place_noise_538b439f(x9, x1, x2, x0):
                continue
            x3 = fill(x3, noise_color, x9)
            x2 = combine(x2, x9)
            break

    for _ in range(2000):
        if size(x2) >= nnoise:
            break
        x6 = randint(ZERO, subtract(x0[ZERO], ONE))
        x7 = randint(ZERO, subtract(x0[ONE], ONE))
        x8 = shift(SINGLETON_NOISE_538B439F, (x6, x7))
        if not _can_place_noise_538b439f(x8, x1, x2, x0):
            continue
        x3 = fill(x3, noise_color, x8)
        x2 = combine(x2, x8)
    if size(x2) < nnoise:
        raise RuntimeError("failed to place enough noise")
    return x3


def generate_538b439f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("vertical", "horizontal"))
        x1 = unifint(diff_lb, diff_ub, (18, 24))
        x2 = unifint(diff_lb, diff_ub, (18, 24))
        x3, x4, x5, x6 = sample(COLORS_538B439F, FOUR)
        x7 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        if x0 == "vertical":
            x8 = randint(SIX, subtract(x2, SEVEN))
            x9 = vfrontier((ZERO, x8))
            try:
                x10 = _sample_vertical_rectangles_538b439f(x1, x2, x8, x7)
            except RuntimeError:
                continue
        else:
            x8 = randint(SIX, subtract(x1, SEVEN))
            x9 = hfrontier((x8, ZERO))
            try:
                x10 = _sample_horizontal_rectangles_538b439f(x1, x2, x8, x7)
            except RuntimeError:
                continue
        gi = canvas(x3, (x1, x2))
        gi = fill(gi, x4, x9)
        for x11 in x10:
            gi = fill(gi, x5, x11)
        x12 = unifint(diff_lb, diff_ub, (14, 32))
        try:
            gi = _add_noise_538b439f(gi, x10, x9, x6, x12)
        except RuntimeError:
            continue
        go = _transform_538b439f(gi, x10, x0, x8, x4, x5)
        if gi == go:
            continue
        if mostcolor(gi) != x3:
            continue
        if size(palette(gi)) != FOUR:
            continue
        return {"input": gi, "output": go}
