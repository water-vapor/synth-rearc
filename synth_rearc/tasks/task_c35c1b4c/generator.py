from synth_rearc.core import *


BOARD_SIZE_C35C1B4C = 10
HALF_WIDTH_C35C1B4C = 5
NONZERO_COLORS_C35C1B4C = tuple(range(1, 10))


def _mirror_cells_c35c1b4c(
    cells: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple]:
    x0 = {
        (i, subtract(BOARD_SIZE_C35C1B4C - 1, j))
        for i, j in cells
    }
    return frozenset(set(cells) | x0)


def _profile_c35c1b4c(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, int, dict[int, int]]:
    x0 = unifint(diff_lb, diff_ub, (5, 8))
    x1 = randint(1, BOARD_SIZE_C35C1B4C - x0 - 1)
    x2 = x1 + x0 - 1
    x3 = randint(x1 + 1, x2 - 1)
    x4 = unifint(diff_lb, diff_ub, (0, 2))
    x5 = choice((1, 1, 2))
    x6 = choice((0, 1))
    x7: dict[int, int] = {}
    for x8 in range(x1, x2 + 1):
        x9 = abs(x8 - x3)
        x10 = max(0, x9 - x6)
        x11 = min(4, x4 + (x10 + x5 - 1) // x5)
        if x9 > 0 and choice((T, F, F, F)):
            x11 += choice((-1, 1))
        x7[x8] = max(0, min(4, x11))
    for x12 in range(max(x1, x3 - 1), min(x2, x3 + 1) + 1):
        if choice((T, T, F)):
            x7[x12] = max(0, x7[x12] - choice((0, 1)))
    if x4 == 0 and choice((T, F, F)):
        x13 = randint(max(x1, x3 - 1), min(x2, x3 + 1))
        x7[x13] = 0
    x7[x1] = max(x7[x1], choice((2, 3, 4)))
    x7[x2] = max(x7[x2], choice((2, 3, 4)))
    return x1, x2, x7


def _shape_cells_c35c1b4c(
    starts: dict[int, int],
) -> frozenset[IntegerTuple]:
    x0 = {
        (i, j)
        for i, x1 in starts.items()
        for j in range(x1, HALF_WIDTH_C35C1B4C)
    }
    return _mirror_cells_c35c1b4c(frozenset(x0))


def _carve_holes_c35c1b4c(
    cells: frozenset[IntegerTuple],
    top: int,
    bottom: int,
    starts: dict[int, int],
) -> tuple[frozenset[IntegerTuple], frozenset[IntegerTuple]]:
    x0: set[IntegerTuple] = set()
    x1 = [i for i in range(top, bottom + 1) if starts[i] <= 2]
    if len(x1) >= 2 and choice((T, T, F)):
        x2 = randint(1, min(3, len(x1)))
        x3 = randint(0, len(x1) - x2)
        x4 = x1[x3:x3 + x2]
        x5 = max(starts[i] for i in x4) + 1
        if x5 <= 3:
            x6 = randint(x5, 3)
            for x7 in x4:
                x0.add((x7, x6))
                x0.add((x7, subtract(BOARD_SIZE_C35C1B4C - 1, x6)))
    x8 = [i for i in range(top, bottom + 1) if starts[i] <= 1]
    if x8 and choice((T, F, F)):
        x9 = choice(x8)
        x10 = starts[x9] + 1
        if x10 <= 3:
            x11 = randint(x10, 3)
            x0.add((x9, x11))
            x0.add((x9, subtract(BOARD_SIZE_C35C1B4C - 1, x11)))
    return frozenset(set(cells) - x0), frozenset(x0)


def _fragment_cells_c35c1b4c(
    start: IntegerTuple,
    horizontal: bool,
    length: int,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = start
    if horizontal:
        return tuple((x0, x1 + dj) for dj in range(length))
    return tuple((x0 + di, x1) for di in range(length))


def _noise_assignments_c35c1b4c(
    shape_cells: frozenset[IntegerTuple],
    hole_cells: frozenset[IntegerTuple],
    colors: tuple[int, int],
    diff_lb: float,
    diff_ub: float,
) -> dict[IntegerTuple, int]:
    x0: dict[IntegerTuple, int] = {}
    for x1 in hole_cells:
        if choice((T, T, F)):
            x0[x1] = choice(colors)
    x2 = set(shape_cells) | set(x0)
    x3 = unifint(diff_lb, diff_ub, (6, 10))
    x4 = 0
    while x3 > 0 and x4 < 300:
        x4 += 1
        x5 = choice((1, 1, 2, 2, 3, 3, 4))
        x6 = choice((T, T, T, F))
        x7 = (randint(0, 9), randint(0, 9))
        x8 = _fragment_cells_c35c1b4c(x7, x6, x5)
        if any(
            not (0 <= i < BOARD_SIZE_C35C1B4C and 0 <= j < BOARD_SIZE_C35C1B4C)
            for i, j in x8
        ):
            continue
        if any(x9 in x2 for x9 in x8):
            continue
        x10 = choice(colors)
        for x11 in x8:
            x0[x11] = x10
        x2.update(x8)
        x3 -= 1
    x12 = set(x0.values())
    x13 = [
        (i, j)
        for i in range(BOARD_SIZE_C35C1B4C)
        for j in range(BOARD_SIZE_C35C1B4C)
        if (i, j) not in x2
    ]
    shuffle(x13)
    for x14 in colors:
        if x14 in x12 or not x13:
            continue
        x15 = x13.pop()
        x0[x15] = x14
        x2.add(x15)
    return x0


def _paint_assignments_c35c1b4c(
    grid: Grid,
    assignments: dict[IntegerTuple, int],
) -> Grid:
    x0 = grid
    for x1 in sorted(set(assignments.values())):
        x2 = frozenset(x3 for x3, x4 in assignments.items() if x4 == x1)
        x0 = fill(x0, x1, x2)
    return x0


def _corrupted_input_c35c1b4c(
    output: Grid,
    shape_cells: frozenset[IntegerTuple],
    colors: tuple[int, int],
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0: dict[int, list[int]] = {}
    for i, j in shape_cells:
        if j >= 5:
            x0.setdefault(i, []).append(j)
    x1 = sorted(x0)
    shuffle(x1)
    x2 = max(1, min(len(x1), unifint(diff_lb, diff_ub, (2, max(2, len(x1))))))
    x3: set[IntegerTuple] = set()
    for x4 in x1[:x2]:
        x5 = sorted(x0[x4])
        if len(x5) >= 2 and choice((T, T, F)):
            x6 = randint(0, len(x5) - 2)
            x7 = randint(x6, len(x5) - 1)
            x3.update((x4, j) for j in x5[x6:x7 + 1])
        else:
            x8 = randint(1, min(2, len(x5)))
            x3.update((x4, j) for j in sample(x5, x8))
    if not x3:
        x9 = choice(x1)
        x3.add((x9, choice(x0[x9])))
    x10 = output
    x11 = (0,) + colors + colors
    for x12 in x3:
        x10 = fill(x10, choice(x11), initset(x12))
    return x10


def generate_c35c1b4c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(NONZERO_COLORS_C35C1B4C)
        x1 = tuple(sample(tuple(c for c in NONZERO_COLORS_C35C1B4C if c != x0), 2))
        x2, x3, x4 = _profile_c35c1b4c(diff_lb, diff_ub)
        x5 = _shape_cells_c35c1b4c(x4)
        x6, x7 = _carve_holes_c35c1b4c(x5, x2, x3, x4)
        if len(x6) < 18:
            continue
        x8 = canvas(0, (BOARD_SIZE_C35C1B4C, BOARD_SIZE_C35C1B4C))
        x9 = fill(x8, 1, x6)
        x10 = objects(x9, T, F, T)
        if len(x10) != 1:
            continue
        x11 = fill(x8, x0, x6)
        x12 = _noise_assignments_c35c1b4c(x6, x7, x1, diff_lb, diff_ub)
        x13 = _paint_assignments_c35c1b4c(x11, x12)
        x14 = _corrupted_input_c35c1b4c(x13, x6, x1, diff_lb, diff_ub)
        if mostcolor(x13) != x0 or mostcolor(x14) != x0:
            continue
        if x13 == x14:
            continue
        return {"input": x14, "output": x13}
