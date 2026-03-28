from synth_rearc.core import *


BOARD_SIZE_E84FEF15 = 29
STRIDE_E84FEF15 = 6
ACTIVE_COLORS_E84FEF15 = (ZERO, TWO, FOUR, SIX)


def _touching_e84fef15(
    a: IntegerTuple,
    b: IntegerTuple,
) -> Boolean:
    return abs(subtract(a[0], b[0])) + abs(subtract(a[1], b[1])) == ONE


def _neighbor_cells_e84fef15(
    cell: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0 = cell
    x1 = (
        (subtract(x0[0], ONE), x0[1]),
        (add(x0[0], ONE), x0[1]),
        (x0[0], subtract(x0[1], ONE)),
        (x0[0], add(x0[1], ONE)),
    )
    return tuple(ij for ij in x1 if ZERO <= ij[0] < FIVE and ZERO <= ij[1] < FIVE)


def _connected_cluster_e84fef15(
    size_: int,
) -> tuple[IntegerTuple, ...]:
    x0 = {(randint(ZERO, FOUR), randint(ZERO, FOUR))}
    while len(x0) < size_:
        x1 = tuple(
            ij
            for cell in x0
            for ij in _neighbor_cells_e84fef15(cell)
            if ij not in x0
        )
        x0.add(choice(x1))
    return tuple(sorted(x0))


def _motif_cells_e84fef15(
    count: int,
    cluster_size: int,
) -> tuple[IntegerTuple, ...]:
    x0 = tuple((i, j) for i in range(FIVE) for j in range(FIVE))
    while True:
        x1 = set(_connected_cluster_e84fef15(cluster_size))
        while len(x1) < count:
            x2 = tuple(
                ij
                for ij in x0
                if ij not in x1
                and all(not _touching_e84fef15(ij, x3) for x3 in x1)
            )
            if len(x2) == ZERO:
                break
            x1.add(choice(x2))
        if len(x1) != count:
            continue
        x3 = {i for i, _ in x1}
        x4 = {j for _, j in x1}
        if len(x3) < THREE or len(x4) < THREE:
            continue
        return tuple(sorted(x1))


def _base_tile_e84fef15(
    cells: tuple[IntegerTuple, ...],
    colors: tuple[int, ...],
) -> Grid:
    x0 = canvas(EIGHT, (FIVE, FIVE))
    x1 = list(colors)
    shuffle(x1)
    for x2, x3 in zip(cells, x1):
        x0 = fill(x0, x3, initset(x2))
    return x0


def _corrupted_tile_e84fef15(
    tile: Grid,
    cells: tuple[IntegerTuple, ...],
    count: int,
) -> Grid:
    x0 = sample(cells, count)
    return fill(tile, EIGHT, x0)


def _assembled_input_e84fef15(
    base_tile: Grid,
    odd_tile: Grid,
    odd_loc: IntegerTuple,
) -> Grid:
    x0 = canvas(THREE, (BOARD_SIZE_E84FEF15, BOARD_SIZE_E84FEF15))
    x1 = asobject(base_tile)
    x2 = asobject(odd_tile)
    for x3 in range(FIVE):
        for x4 in range(FIVE):
            x5 = multiply(STRIDE_E84FEF15, (x3, x4))
            x6 = branch(equality((x3, x4), odd_loc), x2, x1)
            x0 = paint(x0, shift(x6, x5))
    return x0


def generate_e84fef15(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((THREE, FOUR))
        x1 = [TWO, TWO, TWO]
        if x0 == FOUR:
            x1.append(ONE)
        if choice((T, F)):
            x1[choice(interval(ZERO, x0, ONE))] = THREE
        shuffle(x1)
        x2 = tuple(x1)
        x3 = sum(x2)
        x4 = choice((ONE, TWO, TWO, THREE))
        if x4 > x3:
            continue
        x5 = _motif_cells_e84fef15(x3, x4)
        x6 = (ZERO,) + tuple(sample(remove(ZERO, ACTIVE_COLORS_E84FEF15), subtract(x0, ONE)))
        x7 = []
        for x8, x9 in zip(x6, x2):
            x7.extend(repeat(x8, x9))
        x10 = tuple(x7)
        x11 = _base_tile_e84fef15(x5, x10)
        x12 = min(unifint(diff_lb, diff_ub, (TWO, FOUR)), subtract(x3, ONE))
        x13 = _corrupted_tile_e84fef15(x11, x5, x12)
        x14 = (randint(ZERO, FOUR), randint(ZERO, FOUR))
        x15 = _assembled_input_e84fef15(x11, x13, x14)
        x16 = cellwise(x11, x13, ONE)
        return {"input": x15, "output": x16}
