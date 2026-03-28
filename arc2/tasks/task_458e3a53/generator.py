from arc2.core import *


LATTICE_OPTIONS_458E3A53 = (
    (FOUR, SIX, "toeplitz"),
    (FIVE, FIVE, "toeplitz"),
    (SIX, FOUR, "hankel"),
)
OUTPUT_SHAPES_458E3A53 = {
    FOUR: ((THREE, TWO), (THREE, THREE)),
    FIVE: ((TWO, TWO), (TWO, THREE), (THREE, TWO)),
    SIX: ((THREE, THREE), (THREE, TWO), (TWO, THREE)),
}
COLOR_POOL_458E3A53 = interval(ZERO, TEN, ONE)


def _sample_long_sequence(
    colors: tuple[int, ...],
    length: int,
) -> tuple[int, ...]:
    x0 = list(colors)
    shuffle(x0)
    while len(x0) < length:
        x1 = list(colors)
        shuffle(x1)
        if x1[ZERO] == x0[NEG_ONE]:
            x1 = x1[ONE:] + x1[:ONE]
        x0.extend(x1)
    return tuple(x0[:length])


def _make_toeplitz_tile(
    sequence: tuple[int, ...],
    offset: int,
    tile_size: int,
) -> Grid:
    x0 = tuple(sequence[offset + i] for i in range(tile_size))
    x1 = tuple(reversed(x0[ONE:])) + x0
    return tuple(
        tuple(x1[j - i + tile_size - ONE] for j in range(tile_size))
        for i in range(tile_size)
    )


def _make_hankel_tile(
    sequence: tuple[int, ...],
    offset: int,
    tile_size: int,
) -> Grid:
    x0 = sequence[offset:offset + TWO * tile_size - ONE]
    return tuple(
        tuple(x0[i + j] for j in range(tile_size))
        for i in range(tile_size)
    )


def generate_458e3a53(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    _ = diff_lb, diff_ub
    while True:
        x0 = choice(LATTICE_OPTIONS_458E3A53)
        x1, x2, x3 = x0
        x4 = choice(COLOR_POOL_458E3A53)
        x5 = tuple(color0 for color0 in COLOR_POOL_458E3A53 if color0 != x4)
        x6 = tuple(sample(x5, SIX))
        x7 = OUTPUT_SHAPES_458E3A53[x1]
        x8, x9 = choice(x7)
        x10 = randint(ZERO, x1 - x8)
        x11 = randint(ZERO, x1 - x9)
        x12 = tuple(tuple(choice(x5) for _ in range(x9)) for _ in range(x8))
        x13 = {value for row in x12 for value in row}
        if len(x13) == ONE:
            continue
        if x3 == "toeplitz":
            x14 = x1
            x15 = _sample_long_sequence(x6, x2 + x14 - ONE)
            x16 = tuple(_make_toeplitz_tile(x15, offset, x2) for offset in range(x14))
        else:
            x14 = TWO
            x15 = _sample_long_sequence(x6, TWO * x2 + x14 - TWO)
            x16 = tuple(_make_hankel_tile(x15, offset, x2) for offset in range(x14))
        if len(set(x16)) != x14:
            continue
        x17 = x1 * x2 + x1 - ONE
        x18 = [[x4 for _ in range(x17)] for _ in range(x17)]
        for i in range(x1):
            for j in range(x1):
                x19 = i * (x2 + ONE)
                x20 = j * (x2 + ONE)
                x21 = x10 <= i < x10 + x8 and x11 <= j < x11 + x9
                if x21:
                    x22 = x12[i - x10][j - x11]
                    x23 = tuple(tuple(x22 for _ in range(x2)) for _ in range(x2))
                else:
                    x24 = (j - i) % x14
                    x23 = x16[x24]
                for k, row in enumerate(x23):
                    for l, value in enumerate(row):
                        x18[x19 + k][x20 + l] = value
        x25 = format_grid(x18)
        return {"input": x25, "output": x12}
