from __future__ import annotations

from dataclasses import dataclass

from synth_rearc.core import *


ORIENTATION_POOL_B9E38DC0 = (
    ZERO,
    ZERO,
    ONE,
    ONE,
    TWO,
)


@dataclass(frozen=True)
class BeamComponentB9E38DC0:
    left: Integer
    right: Integer
    expand_left: Boolean
    expand_right: Boolean
    allow_left: Boolean
    allow_right: Boolean
    alternate_left: Boolean
    alternate_right: Boolean


def _segments_b9e38dc0(
    cols: Iterable[Integer],
) -> tuple[tuple[Integer, Integer], ...]:
    x0 = sorted(cols)
    if len(x0) == ZERO:
        return tuple()
    x1 = []
    x2 = x0[ZERO]
    x3 = x0[ZERO]
    for x4 in x0[ONE:]:
        if x4 == increment(x3):
            x3 = x4
        else:
            x1.append((x2, x3))
            x2 = x4
            x3 = x4
    x1.append((x2, x3))
    return tuple(x1)


def _rotate_grid_b9e38dc0(
    grid: Grid,
    turns: Integer,
) -> Grid:
    x0 = turns % FOUR
    if x0 == ZERO:
        return grid
    if x0 == ONE:
        return rot90(grid)
    if x0 == TWO:
        return rot180(grid)
    return rot270(grid)


def _unrotate_grid_b9e38dc0(
    grid: Grid,
    turns: Integer,
) -> Grid:
    return _rotate_grid_b9e38dc0(grid, subtract(FOUR, turns) % FOUR)


def _non_bg_counts_b9e38dc0(
    grid: Grid,
    bg: Integer,
) -> dict[Integer, Integer]:
    x0 = {}
    for x1 in grid:
        for x2 in x1:
            if x2 == bg:
                continue
            x0[x2] = add(x0.get(x2, ZERO), ONE)
    return x0


def _wall_color_b9e38dc0(
    grid: Grid,
    bg: Integer,
) -> Integer:
    x0 = _non_bg_counts_b9e38dc0(grid, bg)
    return max(x0, key=x0.get)


def _detect_bar_b9e38dc0(
    grid: Grid,
    wall_color: Integer,
) -> tuple[Integer, Integer, Integer]:
    x0 = None
    for x1, x2 in enumerate(grid):
        x3 = [x4 for x4, x5 in enumerate(x2) if x5 == wall_color]
        for x6, x7 in _segments_b9e38dc0(x3):
            x8 = (subtract(add(x7, ONE), x6), invert(x1))
            if both(x0 is None, T):
                x0 = (x8, (x1, x6, x7))
            elif x8 > x0[ZERO]:
                x0 = (x8, (x1, x6, x7))
    return x0[ONE]


def _detect_fill_color_b9e38dc0(
    grid: Grid,
    bg: Integer,
    wall_color: Integer,
    bar_row: Integer,
    bar_left: Integer,
    bar_right: Integer,
) -> Integer:
    x0 = tuple(
        x1
        for x1 in palette(grid)
        if x1 not in (bg, wall_color)
    )
    x2 = []
    for x3 in x0:
        x4 = [
            (x5, x6)
            for x5, x7 in enumerate(grid)
            for x6, x8 in enumerate(x7)
            if x8 == x3
        ]
        x9 = [
            (x10, x11)
            for x10, x11 in x4
            if both(x10 >= bar_row, both(x11 >= bar_left, x11 <= bar_right))
        ]
        if len(x9) > ZERO:
            x12 = (
                min(x13 for x13, _ in x9),
                invert(len(x9)),
                invert(len(x4)),
                x3,
            )
        else:
            x14 = min(
                add(
                    max(subtract(bar_row, x15), ZERO),
                    add(
                        max(subtract(bar_left, x16), ZERO),
                        max(subtract(x16, bar_right), ZERO),
                    ),
                )
                for x15, x16 in x4
            )
            x12 = (
                add(1000, x14),
                invert(len(x4)),
                invert(len(x4)),
                x3,
            )
        x2.append(x12)
    return min(x2)[THREE]


def normalize_projector_b9e38dc0(
    grid: Grid,
) -> dict[str, object]:
    x0 = mostcolor(grid)
    x1 = _wall_color_b9e38dc0(grid, x0)
    x2 = None
    for x3 in range(FOUR):
        x4 = _rotate_grid_b9e38dc0(grid, x3)
        x5, x6, x7 = _detect_bar_b9e38dc0(x4, x1)
        x8 = (subtract(add(x7, ONE), x6), invert(x5))
        if both(x2 is None, T):
            x2 = (x8, x3, x4, x5, x6, x7)
        elif x8 > x2[ZERO]:
            x2 = (x8, x3, x4, x5, x6, x7)
    _, x9, x10, x11, x12, x13 = x2
    x14 = _detect_fill_color_b9e38dc0(x10, x0, x1, x11, x12, x13)
    return {
        "bg": x0,
        "wall": x1,
        "fill": x14,
        "grid": x10,
        "turns": x9,
        "bar_row": x11,
        "bar_left": x12,
        "bar_right": x13,
    }


def _paint_normalized_b9e38dc0(
    grid: Grid,
    bg: Integer,
    wall_color: Integer,
    fill_color: Integer,
    bar_row: Integer,
    bar_left: Integer,
    bar_right: Integer,
) -> Grid:
    x0 = [list(x1) for x1 in grid]
    if bar_row >= subtract(len(grid), ONE):
        return grid
    x2 = []
    x3 = add(bar_row, ONE)
    x4 = {
        x5
        for x5 in range(bar_left, add(bar_right, ONE))
        if grid[x3][x5] in (bg, fill_color)
    }
    for x6, x7 in _segments_b9e38dc0(x4):
        x2.append(
            BeamComponentB9E38DC0(
                left=x6,
                right=x7,
                expand_left=T,
                expand_right=T,
                allow_left=T,
                allow_right=T,
                alternate_left=F,
                alternate_right=F,
            )
        )
        for x8 in range(x6, add(x7, ONE)):
            if grid[x3][x8] == bg:
                x0[x3][x8] = fill_color
    for x9 in range(add(bar_row, TWO), len(grid)):
        x10 = []
        x11 = any(x12 == wall_color for x12 in grid[x9])
        for x13 in x2:
            x14 = both(x13.expand_left, x13.allow_left)
            x15 = both(x13.expand_right, x13.allow_right)
            x16 = max(ZERO, subtract(x13.left, branch(x14, ONE, ZERO)))
            x17 = min(subtract(len(grid[ZERO]), ONE), add(x13.right, branch(x15, ONE, ZERO)))
            x18 = {
                x19
                for x19 in range(x16, add(x17, ONE))
                if grid[x9][x19] in (bg, fill_color)
            }
            x20 = tuple(
                (x21, x22)
                for x21, x22 in _segments_b9e38dc0(x18)
                if max(x21, x13.left) <= min(x22, x13.right)
            )
            if len(x20) == ZERO:
                continue
            if len(x20) == ONE:
                x23, x24 = x20[ZERO]
                x25 = x23 < x13.left
                x26 = x24 > x13.right
                x27 = x13.allow_left
                x28 = x13.allow_right
                if both(x13.expand_left, both(not x13.expand_right, x13.alternate_left)):
                    x27 = not x25
                if both(x13.expand_right, both(not x13.expand_left, x13.alternate_right)):
                    x28 = not x26
                x10.append(
                    BeamComponentB9E38DC0(
                        left=x23,
                        right=x24,
                        expand_left=x13.expand_left,
                        expand_right=x13.expand_right,
                        allow_left=x27,
                        allow_right=x28,
                        alternate_left=x13.alternate_left,
                        alternate_right=x13.alternate_right,
                    )
                )
                continue
            x29 = [
                subtract(subtract(x31, x30), ONE)
                for (_, x30), (x31, _) in zip(x20, x20[ONE:])
            ]
            for x32, (x33, x34) in enumerate(x20):
                if not both(x13.expand_left, x13.expand_right):
                    x33 = max(x33, x13.left)
                    x34 = min(x34, x13.right)
                    if x33 > x34:
                        continue
                x35 = both(equality(x32, ZERO), x13.expand_left)
                x36 = both(equality(x32, subtract(len(x20), ONE)), x13.expand_right)
                x37 = x29[ZERO] if both(x35, not x36) else (x29[-ONE] if both(x36, not x35) else None)
                if both(not x11, x37 == ONE):
                    if x35:
                        x33 = max(x33, x13.left)
                    if x36:
                        x34 = min(x34, x13.right)
                    if x33 > x34:
                        continue
                x38 = both(x35, x33 < x13.left)
                x39 = both(x36, x34 > x13.right)
                x40 = both(x35, x37 == ONE)
                x41 = both(x36, x37 == ONE)
                x42 = branch(x40, not x38, T)
                x43 = branch(x41, not x39, T)
                x44 = branch(x40, T, F)
                x45 = branch(x41, T, F)
                x10.append(
                    BeamComponentB9E38DC0(
                        left=x33,
                        right=x34,
                        expand_left=x35,
                        expand_right=x36,
                        allow_left=x42,
                        allow_right=x43,
                        alternate_left=x44,
                        alternate_right=x45,
                    )
                )
        x2 = x10
        for x46 in x2:
            for x47 in range(x46.left, add(x46.right, ONE)):
                if grid[x9][x47] == bg:
                    x0[x9][x47] = fill_color
    return format_grid(x0)


def project_beam_b9e38dc0(
    grid: Grid,
) -> Grid:
    x0 = normalize_projector_b9e38dc0(grid)
    x1 = _paint_normalized_b9e38dc0(
        x0["grid"],
        x0["bg"],
        x0["wall"],
        x0["fill"],
        x0["bar_row"],
        x0["bar_left"],
        x0["bar_right"],
    )
    return _unrotate_grid_b9e38dc0(x1, x0["turns"])


def mutable_canvas_b9e38dc0(
    bg: Integer,
    dims: IntegerTuple,
) -> list[list[Integer]]:
    return [list(x0) for x0 in canvas(bg, dims)]


def paint_cells_b9e38dc0(
    grid: list[list[Integer]],
    color_value: Integer,
    cells: Iterable[IntegerTuple],
) -> None:
    x0 = len(grid)
    x1 = len(grid[ZERO])
    for x2, x3 in cells:
        if both(ZERO <= x2 < x0, ZERO <= x3 < x1):
            grid[x2][x3] = color_value


def format_grid_b9e38dc0(
    grid: list[list[Integer]],
) -> Grid:
    return format_grid(grid)
