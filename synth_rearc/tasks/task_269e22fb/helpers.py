from functools import lru_cache

from synth_rearc.core import *


TARGET_SIZE_269E22FB = 20
CROP_HEIGHT_BOUNDS_269E22FB = (EIGHT, 16)
CROP_WIDTH_BOUNDS_269E22FB = (EIGHT, 12)

MASTER_TEMPLATE_269E22FB = (
    "00111111111111100111",
    "00000011111111100111",
    "00000001111111100011",
    "00111000111111100011",
    "11111100011111000001",
    "11111110001111011001",
    "11111111001100011001",
    "11111111101101011001",
    "11111111100001011001",
    "10000000001001011001",
    "10111111100001011001",
    "10000000001101011001",
    "10101111101100011001",
    "00010000001111011001",
    "10100111101111000001",
    "00010111101110010011",
    "10100111101110111001",
    "00010111101110011100",
    "10100111010111010001",
    "00011110111011000111",
)

SYMMETRIES_269E22FB = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
)


def _binary_master_269e22fb() -> Grid:
    return tuple(
        tuple(ONE if value == "1" else ZERO for value in row)
        for row in MASTER_TEMPLATE_269E22FB
    )


def colorize_binary_grid_269e22fb(
    grid: Grid,
    zero_color: Integer,
    one_color: Integer,
) -> Grid:
    return tuple(
        tuple(one_color if value == ONE else zero_color for value in row)
        for row in grid
    )


@lru_cache(maxsize=1)
def binary_variants_269e22fb() -> tuple[Grid, ...]:
    x0 = _binary_master_269e22fb()
    return tuple(x1(x0) for x1 in SYMMETRIES_269E22FB)


def candidate_outputs_269e22fb(
    zero_color: Integer,
    one_color: Integer,
) -> tuple[Grid, ...]:
    x0 = []
    for x1 in binary_variants_269e22fb():
        x0.append(colorize_binary_grid_269e22fb(x1, zero_color, one_color))
        x0.append(colorize_binary_grid_269e22fb(x1, one_color, zero_color))
    return tuple(x0)


@lru_cache(maxsize=1)
def unique_crop_specs_269e22fb() -> tuple[tuple[tuple[int, int, int, int], ...], ...]:
    x0: dict[tuple[int, int, Grid], set[int]] = {}
    x1 = [[] for _ in binary_variants_269e22fb()]
    x2, x3 = CROP_HEIGHT_BOUNDS_269E22FB
    x4, x5 = CROP_WIDTH_BOUNDS_269E22FB
    for x6, x7 in enumerate(binary_variants_269e22fb()):
        for x8 in range(x2, add(x3, ONE)):
            for x9 in range(x4, add(x5, ONE)):
                x10 = subtract(TARGET_SIZE_269E22FB, x8)
                x11 = subtract(TARGET_SIZE_269E22FB, x9)
                for x12 in range(add(x10, ONE)):
                    for x13 in range(add(x11, ONE)):
                        x14 = crop(x7, (x12, x13), (x8, x9))
                        if numcolors(x14) != TWO:
                            continue
                        x15 = (x8, x9, x14)
                        x1[x6].append((x12, x13, x8, x9, x15))
                        x0.setdefault(x15, set()).add(x6)
    x16 = []
    for x17, x18 in enumerate(x1):
        x19 = []
        for x20, x21, x22, x23, x24 in x18:
            if x0[x24] == {x17}:
                x19.append((x20, x21, x22, x23))
        x16.append(tuple(x19))
    return tuple(x16)
