from arc2.core import *


HEIGHT_BAG_3d6c6e23 = (
    TWO,
    TWO,
    THREE,
    THREE,
    THREE,
    FOUR,
)

NCOLORS_BY_HEIGHT_3d6c6e23 = {
    TWO: (ONE, ONE, TWO),
    THREE: (ONE, TWO, TWO, THREE),
    FOUR: (ONE, TWO, TWO, THREE, THREE),
}

PALETTE_3d6c6e23 = remove(ZERO, interval(ZERO, TEN, ONE))


def _split_extra_3d6c6e23(total: Integer, parts: Integer) -> tuple[Integer, ...]:
    x0 = [ZERO for _ in range(parts)]
    for _ in range(total):
        x1 = randint(ZERO, parts - ONE)
        x0[x1] += ONE
    return tuple(x0)


def _segment_lengths_3d6c6e23(height_value: Integer, ncolors: Integer) -> tuple[Integer, ...]:
    if ncolors == ONE:
        return (height_value,)
    x0 = tuple(sorted(sample(interval(ONE, height_value, ONE), ncolors - ONE)))
    x1 = []
    x2 = ZERO
    for x3 in x0 + (height_value,):
        x1.append(x3 - x2)
        x2 = x3
    return tuple(x1)


def _build_column_spec_3d6c6e23(
    height_value: Integer,
    colors: tuple[Integer, ...],
) -> dict:
    x0 = _segment_lengths_3d6c6e23(height_value, len(colors))
    x1 = []
    x2 = []
    x3 = ZERO
    for x4, x5 in zip(x0, colors):
        x6 = ZERO
        for _ in range(x4):
            x1.append(x5)
            x6 += x3 * TWO + ONE
            x3 += ONE
        x2.append(x6)
    return {
        "height": height_value,
        "segment_lengths": x0,
        "colors": tuple(colors),
        "counts": tuple(x2),
        "layer_colors": tuple(x1),
        "total": height_value * height_value,
    }


def _column_centers_3d6c6e23(
    specs: tuple[dict, ...],
    width_value: Integer,
    gap_value: Integer,
) -> tuple[Integer, ...]:
    x0 = tuple(spec["height"] * TWO - ONE for spec in specs)
    x1 = sum(x0) + gap_value * (len(x0) - ONE)
    x2 = width_value - x1
    x3 = _split_extra_3d6c6e23(x2, len(x0) + ONE)
    x4 = []
    x5 = x3[ZERO]
    for x6, x7 in enumerate(x0):
        x8 = x5 + x7 // TWO
        x4.append(x8)
        x5 += x7
        if x6 < len(x0) - ONE:
            x5 += gap_value + x3[x6 + ONE]
    return tuple(x4)


def _paint_output_column_3d6c6e23(
    grid: Grid,
    center_value: Integer,
    layer_colors: tuple[Integer, ...],
) -> Grid:
    x0 = height(grid)
    x1 = len(layer_colors)
    x2 = x0 - x1
    x3 = grid
    for x4, x5 in enumerate(layer_colors):
        x6 = x2 + x4
        x7 = connect((x6, center_value - x4), (x6, center_value + x4))
        x3 = fill(x3, x5, x7)
    return x3


def generate_3d6c6e23(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, TWO))
        x1 = [choice(HEIGHT_BAG_3d6c6e23) for _ in range(x0)]
        x2 = [choice(NCOLORS_BY_HEIGHT_3d6c6e23[x3]) for x3 in x1]
        x3 = sum(x2)
        if x3 > len(PALETTE_3d6c6e23):
            continue
        x4 = list(sample(PALETTE_3d6c6e23, x3))
        shuffle(x4)
        x5 = []
        x6 = ZERO
        for x7, x8 in zip(x1, x2):
            x9 = tuple(x4[x6:x6 + x8])
            x5.append(_build_column_spec_3d6c6e23(x7, x9))
            x6 += x8
        shuffle(x5)
        x10 = tuple(spec["height"] for spec in x5)
        x11 = maximum(x10)
        x12 = maximum(tuple(spec["total"] for spec in x5))
        x13 = max(16, x11 + x12 + ONE)
        x14 = min(30, x13 + 10)
        if x13 > 30:
            continue
        x15 = choice((ONE, TWO))
        x16 = tuple(spec["height"] * TWO - ONE for spec in x5)
        x17 = max(NINE, sum(x16) + x15 * (x0 - ONE) + ONE)
        x18 = min(30, x17 + 10)
        if x17 > 30:
            continue
        x19 = unifint(diff_lb, diff_ub, (x13, x14))
        x20 = unifint(diff_lb, diff_ub, (x17, x18))
        x21 = _column_centers_3d6c6e23(tuple(x5), x20, x15)
        x22 = canvas(ZERO, (x19, x20))
        x23 = canvas(ZERO, (x19, x20))
        x24 = interval(ZERO, x19 - x11, ONE)
        if len(x24) == ZERO:
            continue
        for x25, x26 in zip(x5, x21):
            x27 = sample(x24, x25["total"])
            x28 = tuple(sorted(x27))
            x29 = ZERO
            for x30, x31 in zip(x25["colors"], x25["counts"]):
                x32 = frozenset((x33, x26) for x33 in x28[x29:x29 + x31])
                x22 = fill(x22, x30, x32)
                x29 += x31
            x23 = _paint_output_column_3d6c6e23(x23, x26, x25["layer_colors"])
        return {"input": x22, "output": x23}
