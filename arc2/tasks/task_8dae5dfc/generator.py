from arc2.core import *


PALETTE_8DAE5DFC = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT)
OBJECT_COUNTS_8DAE5DFC = (ONE, TWO, TWO, TWO, THREE)
OBJECT_BOUNDS_8DAE5DFC = {
    ONE: ((SIX, 13), (SIX, 13)),
    TWO: ((SIX, 12), (SIX, 13)),
    THREE: ((SIX, 10), (SIX, 12)),
}


def _sample_layer_thicknesses_8dae5dfc(
    diff_lb: float,
    diff_ub: float,
    shells: int,
) -> tuple[int, ...]:
    x0 = tuple(x1 for x1 in (THREE, FOUR, FOUR, FIVE) if x1 <= shells)
    x1 = choice(x0)
    if x1 == ONE:
        return (shells,)
    x2 = sorted(sample(range(ONE, shells), x1 - ONE))
    x3 = []
    x4 = ZERO
    for x5 in x2:
        x3.append(x5 - x4)
        x4 = x5
    x3.append(shells - x4)
    return tuple(x3)


def _render_layers_8dae5dfc(
    dims: tuple[int, int],
    colors: tuple[int, ...],
    thicknesses: tuple[int, ...],
) -> Grid:
    x0 = canvas(ZERO, dims)
    x1 = ZERO
    for x2, x3 in zip(colors, thicknesses):
        for x4 in range(x1, x1 + x3):
            x5 = frozenset(
                (i, j)
                for i in range(x4, dims[0] - x4)
                for j in range(x4, dims[1] - x4)
                if i in (x4, dims[0] - x4 - ONE) or j in (x4, dims[1] - x4 - ONE)
            )
            x0 = fill(x0, x2, x5)
        x1 += x3
    return x0


def _sample_object_8dae5dfc(
    diff_lb: float,
    diff_ub: float,
    bounds: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[Grid, Grid]:
    x0 = unifint(diff_lb, diff_ub, bounds[0])
    x1 = unifint(diff_lb, diff_ub, bounds[1])
    x2 = (min(x0, x1) + ONE) // TWO
    x3 = _sample_layer_thicknesses_8dae5dfc(diff_lb, diff_ub, x2)
    x4 = tuple(sample(PALETTE_8DAE5DFC, len(x3)))
    x5 = _render_layers_8dae5dfc((x0, x1), x4, x3)
    x6 = _render_layers_8dae5dfc((x0, x1), tuple(reversed(x4)), x3)
    return x5, x6


def _separated_bbox_8dae5dfc(
    bbox: tuple[int, int, int, int],
    placed: list[tuple[int, int, int, int]],
) -> bool:
    for x0 in placed:
        x1 = bbox[2] + ONE < x0[0]
        x2 = x0[2] + ONE < bbox[0]
        x3 = bbox[3] + ONE < x0[1]
        x4 = x0[3] + ONE < bbox[1]
        if not (x1 or x2 or x3 or x4):
            return F
    return T


def _place_objects_8dae5dfc(
    objects_io: list[tuple[Grid, Grid]],
    dims: tuple[int, int],
) -> list[tuple[int, int]] | None:
    x0 = sorted(
        range(len(objects_io)),
        key=lambda x1: height(objects_io[x1][0]) * width(objects_io[x1][0]),
        reverse=T,
    )
    x1 = [None] * len(objects_io)
    x2: list[tuple[int, int, int, int]] = []
    for x3 in x0:
        x4 = objects_io[x3][0]
        x5 = height(x4)
        x6 = width(x4)
        x7 = [(i, j) for i in range(dims[0] - x5 + ONE) for j in range(dims[1] - x6 + ONE)]
        shuffle(x7)
        for x8 in x7:
            x9 = (x8[0], x8[1], x8[0] + x5 - ONE, x8[1] + x6 - ONE)
            if _separated_bbox_8dae5dfc(x9, x2):
                x1[x3] = x8
                x2.append(x9)
                break
        if x1[x3] is None:
            return None
    return x1


def generate_8dae5dfc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (16, 20))
        x1 = unifint(diff_lb, diff_ub, (16, 20))
        x2 = choice(OBJECT_COUNTS_8DAE5DFC)
        x3 = [_sample_object_8dae5dfc(diff_lb, diff_ub, OBJECT_BOUNDS_8DAE5DFC[x2]) for _ in range(x2)]
        x4 = _place_objects_8dae5dfc(x3, (x0, x1))
        if x4 is None:
            continue
        x5 = canvas(ZERO, (x0, x1))
        x6 = canvas(ZERO, (x0, x1))
        for x7, x8 in zip(x3, x4):
            x9 = shift(asobject(x7[0]), x8)
            x10 = shift(asobject(x7[1]), x8)
            x5 = paint(x5, x9)
            x6 = paint(x6, x10)
        x11 = colorcount(x5, ZERO)
        x12 = multiply(x0, x1)
        if x11 * TWO < x12:
            continue
        return {"input": x5, "output": x6}
