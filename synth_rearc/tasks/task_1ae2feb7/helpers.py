from synth_rearc.core import *


def scan_blocks_1ae2feb7(
    values: tuple[int, ...],
) -> tuple[tuple[int, int], ...]:
    x0 = []
    x1 = ZERO
    x2 = len(values)
    while x1 < x2:
        x3 = values[x1]
        if x3 == ZERO:
            x1 = increment(x1)
            continue
        x4 = x1
        while x1 < x2 and values[x1] == x3:
            x1 = increment(x1)
        x5 = subtract(x1, x4)
        x0.append((x3, x5))
    return tuple(x0)


def project_values_1ae2feb7(
    blocks: tuple[tuple[int, int], ...],
    target_len: Integer,
) -> tuple[int, ...]:
    x0 = [ZERO] * target_len
    for x1, x2 in reversed(blocks):
        for x3 in range(ZERO, target_len, x2):
            x0[x3] = x1
    return tuple(x0)


def source_values_from_blocks_1ae2feb7(
    side_width: Integer,
    blocks: tuple[tuple[int, int], ...],
    near_pad: Integer,
    far_pad: Integer,
    source_on_left: bool,
) -> tuple[int, ...]:
    x0 = [ZERO] * near_pad
    for x1, x2 in blocks:
        x0.extend([x1] * x2)
    x0.extend([ZERO] * far_pad)
    x1 = tuple(x0)
    if len(x1) != side_width:
        raise ValueError("row width mismatch")
    return tuple(reversed(x1)) if source_on_left else x1


def projection_object_1ae2feb7(
    grid: Grid,
    sep_col: Integer,
) -> Object:
    x0 = height(grid)
    x1 = width(grid)
    x2 = sum(
        ONE
        for x3 in range(x0)
        for x4 in range(sep_col)
        if grid[x3][x4] != ZERO
    )
    x5 = sum(
        ONE
        for x6 in range(x0)
        for x7 in range(add(sep_col, ONE), x1)
        if grid[x6][x7] != ZERO
    )
    x8 = x2 >= x5
    x9 = subtract(subtract(x1, sep_col), ONE) if x8 else sep_col
    x10 = []
    for x11, x12 in enumerate(grid):
        x13 = tuple(reversed(x12[:sep_col])) if x8 else x12[add(sep_col, ONE):]
        x14 = scan_blocks_1ae2feb7(x13)
        x15 = project_values_1ae2feb7(x14, x9)
        for x16, x17 in enumerate(x15):
            if x17 == ZERO:
                continue
            x18 = add(sep_col, increment(x16)) if x8 else subtract(sep_col, increment(x16))
            x10.append((x17, (x11, x18)))
    return frozenset(x10)


def make_input_grid_1ae2feb7(
    height_value: Integer,
    width_value: Integer,
    sep_col: Integer,
    sep_color: Integer,
    divider_top: Integer,
    divider_bottom: Integer,
    source_rows: dict[int, tuple[int, ...]],
    source_on_left: bool,
) -> Grid:
    x0 = canvas(ZERO, (height_value, width_value))
    x1 = fill(x0, sep_color, connect((divider_top, sep_col), (divider_bottom, sep_col)))
    x2 = x1
    if source_on_left:
        x3 = ZERO
    else:
        x3 = add(sep_col, ONE)
    for x4, x5 in source_rows.items():
        x6 = frozenset(
            (x7, (x4, add(x3, x8)))
            for x8, x7 in enumerate(x5)
            if x7 != ZERO
        )
        x2 = paint(x2, x6)
    return x2
