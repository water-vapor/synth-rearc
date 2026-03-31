from synth_rearc.core import *

from .verifier import verify_c663677b


GRID_SIZE_C663677B = 27
TILE_PERIOD_C663677B = 8
FRONTIER_OPTIONS_C663677B = (
    (SEVEN,),
    (SEVEN,),
    (FOUR, SEVEN),
    (ONE, SEVEN),
)
STATE_MODULI_C663677B = (FIVE, SIX, SEVEN, EIGHT, NINE)
FORMULA_FAMILIES_C663677B = ("add", "add", "mix", "mul")
PALETTE_POOLS_C663677B = (
    (TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE),
    (THREE, FIVE, SEVEN, NINE),
    (TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE),
)
PROTECTED_ORIGINS_C663677B = (ZERO, EIGHT, 16)


def _exact_vertical_period_c663677b(
    grid: Grid,
) -> Integer:
    x0 = height(grid)
    x1 = width(grid)
    for x2 in range(ONE, x0 + ONE):
        x3 = T
        for x4 in range(x0 - x2):
            for x5 in range(x1):
                if grid[x4][x5] != grid[x4 + x2][x5]:
                    x3 = F
                    break
            if not x3:
                break
        if x3:
            return x2
    return x0


def _exact_horizontal_period_c663677b(
    grid: Grid,
) -> Integer:
    x0 = height(grid)
    x1 = width(grid)
    for x2 in range(ONE, x1 + ONE):
        x3 = T
        for x4 in range(x0):
            for x5 in range(x1 - x2):
                if grid[x4][x5] != grid[x4][x5 + x2]:
                    x3 = F
                    break
            if not x3:
                break
        if x3:
            return x2
    return x1


def _repeat_tile_c663677b(
    tile: Grid,
) -> Grid:
    return tuple(
        tuple(tile[x0 % TILE_PERIOD_C663677B][x1 % TILE_PERIOD_C663677B] for x1 in range(GRID_SIZE_C663677B))
        for x0 in range(GRID_SIZE_C663677B)
    )


def _state_sequence_c663677b(
    length: Integer,
    modulus: Integer,
) -> tuple[int, ...]:
    x0 = choice(("pal", "pal", "repeat", "cycle"))
    if x0 == "pal":
        x1 = tuple(randint(ZERO, modulus - ONE) for _ in range((length + ONE) // TWO))
        if length % TWO == ONE:
            return x1 + x1[:-ONE][::-ONE]
        return x1 + x1[::-ONE]
    if x0 == "repeat":
        x1 = min(length, choice((TWO, THREE, FOUR)))
        x2 = tuple(randint(ZERO, modulus - ONE) for _ in range(x1))
        return tuple(x2[x3 % x1] for x3 in range(length))
    x1 = randint(ZERO, modulus - ONE)
    x2 = randint(ONE, modulus - ONE)
    return tuple((x1 + x2 * x3) % modulus for x3 in range(length))


def _color_map_c663677b(
    modulus: Integer,
) -> tuple[int, ...]:
    x0 = choice(PALETTE_POOLS_C663677B)
    x1 = min(len(x0), choice((THREE, FOUR, FIVE, SIX)))
    x2 = tuple(sample(x0, x1))
    x3 = choice((ZERO, ZERO, ONE, ONE, TWO))
    x4 = tuple(sample(tuple(range(modulus)), x3))
    x5 = []
    for x6 in range(modulus):
        if x6 in x4:
            x5.append(ONE)
        else:
            x5.append(x2[x6 % len(x2)])
    return tuple(x5)


def _residue_c663677b(
    left: Integer,
    right: Integer,
    modulus: Integer,
    family: str,
) -> Integer:
    if family == "add":
        return (left + right) % modulus
    if family == "mix":
        return (left * right + left + right) % modulus
    return (left * right) % modulus


def _build_tile_c663677b() -> Grid:
    x0 = set(choice(FRONTIER_OPTIONS_C663677B))
    x1 = tuple(x2 for x2 in range(TILE_PERIOD_C663677B) if x2 not in x0)
    x2 = choice(STATE_MODULI_C663677B)
    x3 = _state_sequence_c663677b(len(x1), x2)
    x4 = dict(zip(x1, x3))
    x5 = _color_map_c663677b(x2)
    x6 = choice(FORMULA_FAMILIES_C663677B)
    x7 = []
    for x8 in range(TILE_PERIOD_C663677B):
        x9 = []
        for x10 in range(TILE_PERIOD_C663677B):
            if x8 in x0 or x10 in x0:
                x11 = ONE
            else:
                x12 = _residue_c663677b(x4[x8], x4[x10], x2, x6)
                x11 = x5[x12]
            x9.append(x11)
        x7.append(tuple(x9))
    return tuple(x7)


def _rectangle_patch_c663677b(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return frozenset(
        (x0, x1)
        for x0 in range(top, top + height_value)
        for x1 in range(left, left + width_value)
    )


def _protected_patch_c663677b() -> Indices:
    x0 = choice(PROTECTED_ORIGINS_C663677B)
    x1 = choice(PROTECTED_ORIGINS_C663677B)
    return _rectangle_patch_c663677b(x0, x1, TILE_PERIOD_C663677B, TILE_PERIOD_C663677B)


def generate_c663677b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _build_tile_c663677b()
        x1 = tuple(x2 for x2, x3 in enumerate(x0) if all(x4 == ONE for x4 in x3))
        x2 = tuple(x3 for x3 in range(TILE_PERIOD_C663677B) if all(x0[x4][x3] == ONE for x4 in range(TILE_PERIOD_C663677B)))
        if x1 not in FRONTIER_OPTIONS_C663677B:
            continue
        if x1 != x2:
            continue
        x1 = _repeat_tile_c663677b(x0)
        if _exact_vertical_period_c663677b(x1) != TILE_PERIOD_C663677B:
            continue
        if _exact_horizontal_period_c663677b(x1) != TILE_PERIOD_C663677B:
            continue
        if len(palette(x1)) < THREE:
            continue
        x3 = tuple(x0[x4] for x4 in range(TILE_PERIOD_C663677B))
        if len(set(x3)) < THREE:
            continue
        x4 = _protected_patch_c663677b()
        x5 = x1
        x6 = unifint(diff_lb, diff_ub, (FOUR, SIX))
        for _ in range(x6):
            x7 = unifint(diff_lb, diff_ub, (TWO, SEVEN))
            x8 = unifint(diff_lb, diff_ub, (TWO, SEVEN))
            x9 = randint(ZERO, GRID_SIZE_C663677B - x7)
            x10 = randint(ZERO, GRID_SIZE_C663677B - x8)
            x11 = difference(_rectangle_patch_c663677b(x9, x10, x7, x8), x4)
            if len(x11) == ZERO:
                continue
            x5 = fill(x5, ZERO, x11)
        x12 = colorcount(x5, ZERO)
        if x12 < 45 or x12 > 110:
            continue
        x13 = frozenset(
            (x14 % TILE_PERIOD_C663677B, x15 % TILE_PERIOD_C663677B)
            for x14 in range(GRID_SIZE_C663677B)
            for x15 in range(GRID_SIZE_C663677B)
            if x5[x14][x15] != ZERO
        )
        if size(x13) != 64:
            continue
        if verify_c663677b(x5) != x1:
            continue
        return {"input": x5, "output": x1}
