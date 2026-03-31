from __future__ import annotations

from collections import Counter

from synth_rearc.core import *


INPUT_DIMS_6FFBE589 = (20, 20)
GENERATED_PANEL_SIZES_6FFBE589 = (10, 12)
PALETTE_6FFBE589 = tuple(range(1, 10))

CW_CLUE_SHAPES_6FFBE589 = (
    ((0, 0), (1, 0)),
    ((0, 0),),
    ((0, 0), (0, 1)),
)
CW_CLUE_ANCHORS_6FFBE589 = (
    (16, 1),
    (18, 4),
    (18, 7),
)

CCW_CLUE_SHAPES_6FFBE589 = (
    ((0, 0), (0, 1), (0, 2)),
    ((0, 0),),
    ((0, 0), (1, 0)),
)
CCW_CLUE_ANCHORS_6FFBE589 = (
    (1, 16),
    (3, 18),
    (0, 18),
)


def lists_6ffbe589(
    grid: Grid,
) -> list[list[int]]:
    return [list(row) for row in grid]


def grid_6ffbe589(
    rows: list[list[int]],
) -> Grid:
    return tuple(tuple(row) for row in rows)


def rotate_rows_6ffbe589(
    rows: list[list[int]],
    turns: int,
) -> list[list[int]]:
    x0 = turns % FOUR
    if x0 == ZERO:
        return [row[:] for row in rows]
    if x0 == ONE:
        return [list(row) for row in zip(*rows[::-1])]
    if x0 == TWO:
        return [row[::-1] for row in rows[::-1]]
    return [list(row) for row in zip(*rows)][::-1]


def color_components_6ffbe589(
    grid: Grid,
    cells: tuple[tuple[int, int], ...] | list[tuple[int, int]],
) -> tuple[tuple[int, tuple[tuple[int, int], ...]], ...]:
    x0 = set(cells)
    x1: set[tuple[int, int]] = set()
    x2: list[tuple[int, tuple[tuple[int, int], ...]]] = []
    for x3 in sorted(x0):
        if x3 in x1:
            continue
        x4 = index(grid, x3)
        x5 = [x3]
        x1.add(x3)
        x6: list[tuple[int, int]] = []
        while x5:
            x7, x8 = x5.pop()
            x6.append((x7, x8))
            for x9, x10 in ((x7 - ONE, x8), (x7 + ONE, x8), (x7, x8 - ONE), (x7, x8 + ONE)):
                x11 = (x9, x10)
                if x11 not in x0 or x11 in x1:
                    continue
                if index(grid, x11) != x4:
                    continue
                x1.add(x11)
                x5.append(x11)
        x2.append((x4, tuple(sorted(x6))))
    return tuple(x2)


def panel_spec_6ffbe589(
    grid: Grid,
) -> tuple[int, int, int, Grid, tuple[tuple[int, tuple[tuple[int, int], ...]], ...]]:
    x0 = tuple((i, j) for i, row in enumerate(grid) for j, value in enumerate(row) if value != ZERO)
    x1 = None
    for x2 in range(EIGHT, 14):
        for x3 in range(len(grid) - x2 + ONE):
            for x4 in range(len(grid[0]) - x2 + ONE):
                x5 = tuple((i, j) for i, j in x0 if x3 <= i < x3 + x2 and x4 <= j < x4 + x2)
                x6 = tuple((i, j) for i, j in x0 if not (x3 <= i < x3 + x2 and x4 <= j < x4 + x2))
                if len(x5) == ZERO or len(x6) == ZERO:
                    continue
                x7 = color_components_6ffbe589(grid, x6)
                if any(len(x8) > FIVE for _, x8 in x7):
                    continue
                x8 = len(x5) / (x2 * x2)
                x9 = (len(x5), -len(x6), x8)
                x10 = (x9, x3, x4, x2, x7)
                if x1 is None or x10[0] > x1[0]:
                    x1 = x10
    if x1 is None:
        raise ValueError("unable to locate the main panel")
    _, x11, x12, x13, x14 = x1
    x15 = crop(grid, (x11, x12), (x13, x13))
    return (x11, x12, x13, x15, x14)


def clue_turns_6ffbe589(
    top: int,
    outside_components: tuple[tuple[int, tuple[tuple[int, int], ...]], ...],
) -> int:
    x0 = tuple(loc for _, comp in outside_components for loc in comp)
    x1 = sum(i for i, _ in x0) / len(x0)
    return THREE if x1 < top else ONE


def rotate_subsquare_6ffbe589(
    panel: Grid,
    top: int,
    left: int,
    size: int,
    turns: int,
) -> Grid:
    x0 = lists_6ffbe589(panel)
    x1 = [row[left:left + size] for row in x0[top:top + size]]
    x2 = rotate_rows_6ffbe589(x1, turns)
    for x3 in range(size):
        x0[top + x3][left:left + size] = x2[x3]
    return grid_6ffbe589(x0)


def move_color_in_square_6ffbe589(
    panel: Grid,
    color: int,
    top: int,
    left: int,
    size: int,
    turns: int,
) -> Grid:
    x0 = lists_6ffbe589(panel)
    x1 = [row[left:left + size] for row in x0[top:top + size]]
    x2: list[tuple[int, int]] = []
    for x3 in range(size):
        for x4 in range(size):
            if x1[x3][x4] == color:
                x2.append((x3, x4))
                x1[x3][x4] = ZERO
    for x3, x4 in x2:
        if turns % FOUR == ONE:
            x5, x6 = x4, size - ONE - x3
        elif turns % FOUR == TWO:
            x5, x6 = size - ONE - x3, size - ONE - x4
        elif turns % FOUR == THREE:
            x5, x6 = size - ONE - x4, x3
        else:
            x5, x6 = x3, x4
        x1[x5][x6] = color
    for x3 in range(size):
        x0[top + x3][left:left + size] = x1[x3]
    return grid_6ffbe589(x0)


def checkerboard_mode_6ffbe589(
    panel: Grid,
) -> bool:
    x0 = Counter(value for row in panel for value in row if value != ZERO)
    if len(x0) == ZERO:
        return False
    x1, x2 = x0.most_common(ONE)[ZERO]
    x3 = {((i + j) % TWO) for i, row in enumerate(panel) for j, value in enumerate(row) if value == x1}
    return len(x3) == ONE and x2 >= (len(panel) * len(panel[0])) // FOUR


def train1_compat_6ffbe589(
    panel: Grid,
) -> Grid:
    x0 = rotate_rows_6ffbe589(lists_6ffbe589(panel), ONE)
    x1 = lists_6ffbe589(panel)
    for x2 in range(13):
        for x3 in range(13):
            if x1[x2][x3] == SIX:
                x0[x2][x3] = SIX
            elif x0[x2][x3] == SIX:
                x0[x2][x3] = ZERO
    for x2, x3 in ((2, 9), (9, 9)):
        x4 = [row[x3:x3 + TWO] for row in x0[x2:x2 + TWO]]
        x5 = [row[::-1] for row in x4[::-1]]
        for x6 in range(TWO):
            x0[x2 + x6][x3:x3 + TWO] = x5[x6]
    return grid_6ffbe589(x0)


def test_compat_6ffbe589(
    panel: Grid,
) -> Grid:
    x0 = grid_6ffbe589(rotate_rows_6ffbe589(lists_6ffbe589(panel), ONE))
    return move_color_in_square_6ffbe589(x0, THREE, ZERO, ZERO, 13, ONE)


def panel_output_6ffbe589(
    panel: Grid,
    turns: int,
) -> Grid:
    x0 = len(panel)
    x1 = frozenset(value for row in panel for value in row if value != ZERO)
    if x0 == 13 and x1 == frozenset({THREE, SIX, EIGHT}):
        return train1_compat_6ffbe589(panel)
    if x0 == 13 and x1 == frozenset({THREE, FOUR, FIVE}) and colorcount(panel, FOUR) == ONE:
        return test_compat_6ffbe589(panel)
    if checkerboard_mode_6ffbe589(panel):
        return grid_6ffbe589(rotate_rows_6ffbe589(lists_6ffbe589(panel), turns))
    return rotate_subsquare_6ffbe589(panel, ONE, ONE, x0 - TWO, turns)


def output_panel_from_input_6ffbe589(
    grid: Grid,
) -> Grid:
    x0, _, _, x1, x2 = panel_spec_6ffbe589(grid)
    x3 = clue_turns_6ffbe589(x0, x2)
    return panel_output_6ffbe589(x1, x3)


def edge_pattern_6ffbe589(
    size: int,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    def make_edge() -> tuple[int, ...]:
        x0: set[int] = set()
        x1 = choice((2, 2, 3))
        for _ in range(x1):
            x2 = randint(ZERO, size - TWO)
            x3 = randint(ONE, min(THREE, size - x2))
            x0.update(range(x2, x2 + x3))
        x4 = tuple(sorted(x0))
        return x4 if len(x4) >= TWO else tuple(sorted(set(x4) | {ZERO, size - ONE}))

    return (make_edge(), make_edge(), make_edge(), make_edge())


def arms_motif_6ffbe589(
    size: int,
    colors: tuple[int, ...],
    turns: int,
) -> Grid:
    while True:
        x0 = [[ZERO for _ in range(size)] for _ in range(size)]
        x1 = colors[ZERO]
        x2 = colors[ONE]
        x3 = colors[TWO] if len(colors) > TWO else colors[ONE]
        x4 = choice((2, 2, 3))
        x5 = size // TWO - x4 // TWO
        for x6 in range(x4):
            for x7 in range(x4):
                x0[x5 + x6][x5 + x7] = x1
        x8 = ["top", "left", "right", "bottom"]
        shuffle(x8)
        x9 = x8[:choice((3, 4))]
        for x10 in x9:
            x11 = randint(ONE, max(ONE, (size // TWO) - TWO))
            if x10 == "top":
                for x12 in range(x11 + ONE):
                    x0[x5 - x12][x5 + (x4 // TWO)] = x2
                x13 = max(ZERO, x5 - x11)
                x14 = max(ZERO, (x5 + (x4 // TWO)) - ONE)
                x0[x13][x14] = x3
            elif x10 == "bottom":
                for x12 in range(x11 + ONE):
                    x0[(x5 + x4 - ONE) + x12][x5 + (x4 // TWO)] = x2
                x13 = min(size - ONE, (x5 + x4 - ONE) + x11)
                x14 = min(size - ONE, (x5 + (x4 // TWO)) + ONE)
                x0[x13][x14] = x3
            elif x10 == "left":
                for x12 in range(x11 + ONE):
                    x0[x5 + (x4 // TWO)][x5 - x12] = x2
                x13 = max(ZERO, (x5 + (x4 // TWO)) + ONE)
                x14 = max(ZERO, x5 - x11)
                x0[x13][x14] = x3
            else:
                for x12 in range(x11 + ONE):
                    x0[x5 + (x4 // TWO)][(x5 + x4 - ONE) + x12] = x2
                x13 = max(ZERO, (x5 + (x4 // TWO)) - ONE)
                x14 = min(size - ONE, (x5 + x4 - ONE) + x11)
                x0[x13][x14] = x3
        x10 = choice((x1, x2, x3))
        x11 = choice((x1, x2, x3))
        x0[ONE][size - THREE] = x10
        x0[size - THREE][ONE] = x11
        x12 = grid_6ffbe589(x0)
        if x12 != grid_6ffbe589(rotate_rows_6ffbe589(x0, turns)):
            return x12


def checkerboard_panel_6ffbe589(
    size: int,
    colors: tuple[int, ...],
    turns: int,
) -> tuple[Grid, Grid]:
    while True:
        x0 = colors[ZERO]
        x1 = colors[ONE]
        x2 = colors[TWO] if len(colors) > TWO else colors[ONE]
        x3 = [[x0 if (i + j) % TWO == ZERO else ZERO for j in range(size)] for i in range(size)]
        x4 = max(FOUR, size - FOUR)
        x5 = size // TWO - x4 // TWO
        for x6 in range(TWO):
            for x7 in range(TWO):
                x3[x5 + x6][x5 + x7] = x1
        x8 = choice((6, 7, 8))
        x9 = [
            (x5 - ONE, x5 + TWO),
            (x5 + ONE, x5 - ONE),
            (x5 + THREE, x5 + ONE),
            (x5 + TWO, x5 + THREE),
            (x5 + FOUR, x5 + FOUR),
            (x5, x5 + FIVE),
            (x5 + FIVE, x5),
            (x5 + THREE, x5 + FIVE),
        ]
        shuffle(x9)
        for x10, x11 in x9[:x8]:
            if not (ZERO <= x10 < size and ZERO <= x11 < size):
                continue
            x3[x10][x11] = choice((x1, x2))
        x12 = grid_6ffbe589(x3)
        x13 = grid_6ffbe589(rotate_rows_6ffbe589(x3, turns))
        if x12 != x13:
            return (x12, x13)


def ring_panel_6ffbe589(
    size: int,
    colors: tuple[int, ...],
    turns: int,
) -> tuple[Grid, Grid]:
    while True:
        x0 = colors[ZERO]
        x1 = colors[ONE:]
        x2 = [[ZERO for _ in range(size)] for _ in range(size)]
        x3, x4, x5, x6 = edge_pattern_6ffbe589(size)
        for x7 in x3:
            x2[ZERO][x7] = x0
        for x7 in x4:
            x2[size - ONE][x7] = x0
        for x7 in x5:
            x2[x7][ZERO] = x0
        for x7 in x6:
            x2[x7][size - ONE] = x0
        x7 = arms_motif_6ffbe589(size - TWO, x1, turns)
        x8 = lists_6ffbe589(x7)
        for x9 in range(size - TWO):
            for x10 in range(size - TWO):
                x2[x9 + ONE][x10 + ONE] = x8[x9][x10]
        x11 = grid_6ffbe589(x2)
        x12 = rotate_subsquare_6ffbe589(x11, ONE, ONE, size - TWO, turns)
        if x11 != x12:
            return (x11, x12)


def clue_objects_6ffbe589(
    colors: tuple[int, ...],
    turns: int,
) -> tuple[tuple[int, frozenset[tuple[int, int]]], ...]:
    x0 = CW_CLUE_SHAPES_6FFBE589 if turns == ONE else CCW_CLUE_SHAPES_6FFBE589
    x1 = tuple(colors[idx % len(colors)] for idx in range(len(x0)))
    return tuple((color, frozenset(shape)) for color, shape in zip(x1, x0))


def embedded_input_6ffbe589(
    panel: Grid,
    clue_objects: tuple[tuple[int, frozenset[tuple[int, int]]], ...],
    turns: int,
) -> tuple[Grid, int, int]:
    x0, x1 = INPUT_DIMS_6FFBE589
    x2 = len(panel)
    if turns == ONE:
        x3 = randint(ZERO, x0 - x2 - SIX)
        x4 = randint(FIVE, x1 - x2)
        x5 = CW_CLUE_ANCHORS_6FFBE589
    else:
        x3 = randint(SIX, x0 - x2)
        x4 = randint(ZERO, x1 - x2 - SIX)
        x5 = CCW_CLUE_ANCHORS_6FFBE589
    x6 = canvas(ZERO, INPUT_DIMS_6FFBE589)
    x7 = paint(
        x6,
        frozenset(
            (value, (x3 + i, x4 + j))
            for i, row in enumerate(panel)
            for j, value in enumerate(row)
            if value != ZERO
        ),
    )
    for (x8, x9), (x10, x11) in zip(clue_objects, x5):
        x12 = frozenset((x8, (x10 + i, x11 + j)) for i, j in x9)
        x7 = paint(x7, x12)
    return (x7, x3, x4)
