from synth_rearc.core import *


RIGHT_MARKER_9BEBAE7A = frozenset({
    (ZERO, ZERO),
    (ZERO, ONE),
    (ZERO, TWO),
    (ONE, ONE),
    (TWO, ONE),
})
LEFT_MARKER_9BEBAE7A = frozenset({
    (ZERO, ONE),
    (ONE, ONE),
    (TWO, ZERO),
    (TWO, ONE),
    (TWO, TWO),
})
UP_MARKER_9BEBAE7A = frozenset({
    (ZERO, ONE),
    (ONE, ZERO),
    (ONE, ONE),
    (ONE, TWO),
    (ONE, THREE),
    (TWO, ONE),
})
DOWN_MARKER_9BEBAE7A = frozenset({
    (ZERO, TWO),
    (ONE, ZERO),
    (ONE, ONE),
    (ONE, TWO),
    (ONE, THREE),
    (TWO, TWO),
})

MARKERS_9BEBAE7A = {
    "right": RIGHT_MARKER_9BEBAE7A,
    "left": LEFT_MARKER_9BEBAE7A,
    "up": UP_MARKER_9BEBAE7A,
    "down": DOWN_MARKER_9BEBAE7A,
}


def _connected_patch_9bebae7a(
    patch: frozenset[tuple[int, int]] | set[tuple[int, int]],
) -> bool:
    if len(patch) == ZERO:
        return F
    x0 = next(iter(patch))
    x1 = {x0}
    x2 = [x0]
    while len(x2) > ZERO:
        x3 = x2.pop()
        x4 = {
            x5 for x5 in neighbors(x3)
            if x5 in patch and x5 not in x1
        }
        x1.update(x4)
        x2.extend(x4)
    return len(x1) == len(patch)


def _covers_bbox_9bebae7a(
    patch: frozenset[tuple[int, int]] | set[tuple[int, int]],
    height_: Integer,
    width_: Integer,
) -> bool:
    x0 = {i for i, _ in patch}
    x1 = {j for _, j in patch}
    return len(x0) == height_ and len(x1) == width_


def _has_hole_9bebae7a(
    patch: frozenset[tuple[int, int]] | set[tuple[int, int]],
    height_: Integer,
    width_: Integer,
) -> bool:
    x0 = {(i, j) for i in range(height_) for j in range(width_)}
    x1 = x0 - set(patch)
    if len(x1) == ZERO:
        return F
    x2 = {
        x3 for x3 in x1
        if x3[0] == ZERO or x3[0] == height_ - ONE or x3[1] == ZERO or x3[1] == width_ - ONE
    }
    x4 = set(x2)
    x5 = list(x2)
    while len(x5) > ZERO:
        x6 = x5.pop()
        x7 = {
            x8 for x8 in dneighbors(x6)
            if x8 in x1 and x8 not in x4
        }
        x4.update(x7)
        x5.extend(x7)
    return len(x4) != len(x1)


def _carve_patch_9bebae7a(
    height_: Integer,
    width_: Integer,
    target: Integer,
) -> frozenset[tuple[int, int]]:
    x0 = {(i, j) for i in range(height_) for j in range(width_)}
    x1 = list(x0)
    shuffle(x1)
    x2 = set(x0)
    for x3 in x1:
        if len(x2) <= target:
            break
        x4 = x2 - {x3}
        if not _covers_bbox_9bebae7a(x4, height_, width_):
            continue
        if not _connected_patch_9bebae7a(x4):
            continue
        x2 = x4
    return frozenset(x2)


def _body_dims_9bebae7a(
    diff_lb: float,
    diff_ub: float,
    direction: str,
) -> tuple[int, int]:
    if direction in ("left", "right"):
        x0 = unifint(diff_lb, diff_ub, (FOUR, FIVE))
        x1 = unifint(diff_lb, diff_ub, (THREE, FOUR))
    else:
        x0 = unifint(diff_lb, diff_ub, (THREE, FOUR))
        x1 = unifint(diff_lb, diff_ub, (FOUR, SIX))
    return x0, x1


def _make_body_9bebae7a(
    diff_lb: float,
    diff_ub: float,
    direction: str,
) -> frozenset[tuple[int, int]]:
    while True:
        x0, x1 = _body_dims_9bebae7a(diff_lb, diff_ub, direction)
        x2 = x0 * x1
        x3 = max(SIX, x0 + x1 - ONE, divide(x2, TWO))
        x4 = min(x2 - ONE, maximum((x3, divide(multiply(x2, TWO), THREE))))
        x5 = unifint(diff_lb, diff_ub, (x3, x4))
        x6 = _carve_patch_9bebae7a(x0, x1, x5)
        if len(x6) != x5:
            continue
        if _has_hole_9bebae7a(x6, x0, x1):
            continue
        if direction in ("left", "right") and x6 == vmirror(x6):
            continue
        if direction in ("up", "down") and x6 == hmirror(x6):
            continue
        return x6


def _mirror_copy_9bebae7a(
    body: Object,
    direction: str,
) -> Object:
    if direction == "right":
        x0 = vmirror(body)
        return shift(x0, (ZERO, width(body)))
    if direction == "left":
        x0 = vmirror(body)
        return shift(x0, (ZERO, -width(body)))
    if direction == "up":
        x0 = hmirror(body)
        return shift(x0, (-height(body), ZERO))
    x0 = hmirror(body)
    return shift(x0, (height(body), ZERO))


def generate_9bebae7a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("right", "left", "up", "down"))
        x1 = _make_body_9bebae7a(diff_lb, diff_ub, x0)
        x2 = recolor(FOUR, x1)
        x3 = height(x2)
        x4 = width(x2)
        if x0 in ("left", "right"):
            x5 = unifint(diff_lb, diff_ub, (max(SIX, x3 + THREE), 14))
            x6 = unifint(diff_lb, diff_ub, (max(EIGHT, double(x4)), 15))
            x7 = randint(ZERO, x5 - x3 - THREE)
            if x0 == "right":
                x8 = randint(ZERO, x6 - double(x4))
            else:
                x8 = randint(x4, x6 - x4)
        elif x0 == "up":
            x5 = unifint(diff_lb, diff_ub, (max(SIX, double(x3) + THREE), 15))
            x6 = unifint(diff_lb, diff_ub, (max(EIGHT, x4), 15))
            x7 = randint(x3, x5 - x3 - THREE)
            x8 = randint(ZERO, x6 - x4)
        else:
            x5 = unifint(diff_lb, diff_ub, (max(SIX, double(x3)), 14))
            x6 = unifint(diff_lb, diff_ub, (max(EIGHT, x4), 15))
            x7 = randint(ZERO, x5 - double(x3))
            x8 = randint(ZERO, x6 - x4)
        x9 = shift(x2, (x7, x8))
        x10 = MARKERS_9BEBAE7A[x0]
        x11 = height(x10)
        x12 = width(x10)
        x13 = randint(x7 + x3, x5 - x11)
        x14 = max(ZERO, x8 - TWO)
        x15 = min(x6 - x12, x8 + x4 - ONE)
        x16 = randint(x14, x15)
        x17 = recolor(SIX, shift(x10, (x13, x16)))
        x18 = canvas(ZERO, (x5, x6))
        x19 = paint(x18, x9)
        x20 = paint(x19, x17)
        x21 = _mirror_copy_9bebae7a(x9, x0)
        x22 = paint(cover(x20, x17), x21)
        x23 = objects(x20, T, T, T)
        if len(colorfilter(x23, FOUR)) != ONE:
            continue
        if len(colorfilter(x23, SIX)) != ONE:
            continue
        return {"input": x20, "output": x22}
