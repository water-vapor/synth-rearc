from synth_rearc.core import *

from .verifier import verify_38007db0


NONZERO_COLORS_38007DB0 = remove(ZERO, interval(ZERO, TEN, ONE))
BOX_SHAPES_38007DB0 = (
    (ONE, ONE),
    (ONE, TWO),
    (TWO, ONE),
    (TWO, TWO),
    (ONE, THREE),
    (THREE, ONE),
    (TWO, THREE),
    (THREE, TWO),
)


def _connected_patch_38007db0(
    patch: Indices,
    inner_size: Integer,
) -> Boolean:
    x0 = canvas(ZERO, (inner_size, inner_size))
    x1 = fill(x0, ONE, patch)
    x2 = objects(x1, T, F, F)
    x3 = colorfilter(x2, ONE)
    return equality(size(x3), ONE)


def _sample_inner_patch_38007db0(
    diff_lb: float,
    diff_ub: float,
    inner_size: Integer,
) -> Indices:
    x0 = multiply(inner_size, inner_size)
    x1 = subtract(inner_size, ONE)
    while True:
        x2 = {(randint(ZERO, x1), randint(ZERO, x1))}
        x3 = unifint(diff_lb, diff_ub, (TWO, add(inner_size, TWO)))
        for _ in range(x3):
            x4 = choice(tuple(x2))
            if choice((T, F)):
                x5 = (x4[0], randint(ZERO, x1))
            else:
                x5 = (randint(ZERO, x1), x4[1])
            x2 |= set(connect(x4, x5))
        x6 = frozenset(x2)
        if not (THREE <= size(x6) < x0):
            continue
        if height(x6) == ONE or width(x6) == ONE:
            continue
        if not _connected_patch_38007db0(x6, inner_size):
            continue
        return x6


def _mutate_inner_patch_38007db0(
    diff_lb: float,
    diff_ub: float,
    patch: Indices,
    inner_size: Integer,
) -> Indices:
    x0 = tuple(
        shape
        for shape in BOX_SHAPES_38007DB0
        if shape[0] <= inner_size and shape[1] <= inner_size
    )
    x1 = multiply(inner_size, inner_size)
    x2 = subtract(inner_size, ONE)
    for _ in range(200):
        x3, x4 = choice(x0)
        x5 = randint(ZERO, subtract(inner_size, x3))
        x6 = randint(ZERO, subtract(inner_size, x4))
        x7 = tuple((i, j) for i in range(x5, add(x5, x3)) for j in range(x6, add(x6, x4)))
        x8 = frozenset(x7)
        x9 = intersection(patch, x8)
        for _ in range(40):
            x10 = unifint(diff_lb, diff_ub, (ZERO, len(x7)))
            x11 = frozenset(sample(x7, x10))
            if x11 == x9:
                continue
            x12 = frozenset((loc for loc in patch if loc not in x8))
            x13 = frozenset(set(x12) | set(x11))
            if not (THREE <= size(x13) < x1):
                continue
            if height(x13) == ONE or width(x13) == ONE:
                continue
            if not _connected_patch_38007db0(x13, inner_size):
                continue
            return x13
    x14 = tuple((i, j) for i in range(inner_size) for j in range(inner_size))
    for x15 in x14:
        x16 = frozenset(set(patch) ^ {x15})
        if x16 == patch:
            continue
        if not (THREE <= size(x16) < x1):
            continue
        if height(x16) == ONE or width(x16) == ONE:
            continue
        if not _connected_patch_38007db0(x16, inner_size):
            continue
        return x16
    return patch


def _render_tile_38007db0(
    tile_size: Integer,
    tile_color: Integer,
    mark_color: Integer,
    patch: Indices,
) -> Grid:
    x0 = canvas(tile_color, (tile_size, tile_size))
    x1 = shift(patch, UNITY)
    return fill(x0, mark_color, x1)


def _assemble_input_38007db0(
    rows: tuple[tuple[Grid, ...], ...],
    border_color: Integer,
) -> Grid:
    x0 = len(rows)
    x1 = len(rows[ZERO][ZERO])
    x2 = len(rows[ZERO])
    x3 = add(multiply(add(x1, ONE), x0), ONE)
    x4 = add(multiply(add(x1, ONE), x2), ONE)
    x5 = canvas(border_color, (x3, x4))
    for i, row in enumerate(rows):
        for j, tile in enumerate(row):
            x6 = add(ONE, multiply(i, add(x1, ONE)))
            x7 = add(ONE, multiply(j, add(x1, ONE)))
            x8 = shift(asobject(tile), (x6, x7))
            x5 = paint(x5, x8)
    return x5


def _assemble_output_38007db0(
    tiles: tuple[Grid, ...],
    border_color: Integer,
) -> Grid:
    x0 = tuple((tile,) for tile in tiles)
    return _assemble_input_38007db0(x0, border_color)


def generate_38007db0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, FOUR))
        x1 = choice((THREE, FOUR)) if x0 == THREE else FOUR
        x2 = FIVE if x0 == THREE else unifint(diff_lb, diff_ub, (FIVE, SIX))
        x3 = subtract(x2, TWO)
        x4, x5, x6 = sample(NONZERO_COLORS_38007DB0, THREE)
        x7 = []
        x8 = []
        for _ in range(x0):
            x9 = _sample_inner_patch_38007db0(diff_lb, diff_ub, x3)
            x10 = _mutate_inner_patch_38007db0(diff_lb, diff_ub, x9, x3)
            if x10 == x9:
                break
            x11 = _render_tile_38007db0(x2, x5, x6, x9)
            x12 = _render_tile_38007db0(x2, x5, x6, x10)
            x13 = randint(ZERO, subtract(x1, ONE))
            x14 = [x11 for _ in range(x1)]
            x14[x13] = x12
            x7.append(tuple(x14))
            x8.append(x12)
        if len(x7) != x0:
            continue
        x15 = tuple(x8)
        if size(frozenset(x15)) == ONE:
            continue
        x16 = _assemble_input_38007db0(tuple(x7), x4)
        x17 = _assemble_output_38007db0(x15, x4)
        if verify_38007db0(x16) != x17:
            continue
        return {"input": x16, "output": x17}
