from synth_rearc.core import *


GRID_SIZES_9F41BD9C = interval(15, 31, ONE)
TOP_OFFSETS_9F41BD9C = interval(TWO, 13, ONE)
MAGENTA_HEIGHTS_9F41BD9C = (FOUR, FIVE, SIX, SEVEN, EIGHT)


def _band_patch_9f41bd9c(size: Integer, band_top: Integer) -> Indices:
    return frozenset((i, j) for i in range(band_top, size) for j in range(size))


def _solid_patch_9f41bd9c(row: Integer, left: Integer) -> Indices:
    return frozenset((row, j) for j in range(left, add(left, FIVE)))


def _stripe_patch_9f41bd9c(row: Integer, left: Integer) -> Indices:
    return frozenset((row, j) for j in range(left, add(left, FIVE), TWO))


def _canonical_input_9f41bd9c(size: Integer, top: Integer, stripes: Integer) -> Grid:
    x0 = add(add(top, TWO), stripes)
    x1 = canvas(ONE, (size, size))
    x2 = fill(x1, SIX, _band_patch_9f41bd9c(size, x0))
    x3 = subtract(size, FIVE)
    for x4 in range(top, add(top, TWO)):
        x2 = fill(x2, FIVE, _solid_patch_9f41bd9c(x4, x3))
    for x4 in range(stripes):
        x5 = add(add(top, TWO), x4)
        x2 = fill(x2, FIVE, _stripe_patch_9f41bd9c(x5, x3))
    return x2


def _canonical_output_9f41bd9c(size: Integer, top: Integer, stripes: Integer) -> Grid:
    x0 = add(add(top, TWO), stripes)
    x1 = canvas(ONE, (size, size))
    x2 = fill(x1, SIX, _band_patch_9f41bd9c(size, x0))
    x3 = frozenset((x0, j) for j in range(stripes, size))
    x4 = fill(x2, NINE, x3)
    for x5 in range(top, add(top, TWO)):
        x4 = fill(x4, FIVE, _solid_patch_9f41bd9c(x5, ZERO))
    for x5 in range(stripes):
        x6 = add(add(top, TWO), x5)
        x4 = fill(x4, FIVE, _stripe_patch_9f41bd9c(x6, x5))
    return x4


def generate_9f41bd9c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(GRID_SIZES_9F41BD9C)
        x1 = choice(TOP_OFFSETS_9F41BD9C)
        x2 = choice(MAGENTA_HEIGHTS_9F41BD9C)
        x3 = subtract(subtract(subtract(x0, x1), TWO), x2)
        if x3 < THREE:
            continue
        gi = _canonical_input_9f41bd9c(x0, x1, x3)
        go = _canonical_output_9f41bd9c(x0, x1, x3)
        if choice((T, F)):
            gi = vmirror(gi)
            go = vmirror(go)
        return {"input": gi, "output": go}
