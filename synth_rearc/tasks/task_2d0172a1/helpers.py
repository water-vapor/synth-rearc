from __future__ import annotations

from dataclasses import dataclass

from synth_rearc.core import *


MODE_IDENTITY_2D0172A1 = "identity"
MODE_HMIRROR_2D0172A1 = "hmirror"
MODE_VMIRROR_2D0172A1 = "vmirror"
MODE_ROT180_2D0172A1 = "rot180"
MODES_2D0172A1 = (
    MODE_IDENTITY_2D0172A1,
    MODE_HMIRROR_2D0172A1,
    MODE_VMIRROR_2D0172A1,
    MODE_ROT180_2D0172A1,
)
COLOR_POOL_2D0172A1 = tuple(range(ONE, TEN))


@dataclass(frozen=True)
class Archetype2d0172a1:
    name: str
    input_grid: Grid
    output_grid: Grid


def _binary_rows_2d0172a1(
    rows: tuple[str, ...],
) -> Grid:
    return tuple(
        tuple(ONE if value == "#" else ZERO for value in row)
        for row in rows
    )


def transform_binary_grid_2d0172a1(
    grid: Grid,
    mode: str,
) -> Grid:
    if mode == MODE_IDENTITY_2D0172A1:
        return grid
    if mode == MODE_HMIRROR_2D0172A1:
        return hmirror(grid)
    if mode == MODE_VMIRROR_2D0172A1:
        return vmirror(grid)
    if mode == MODE_ROT180_2D0172A1:
        return rot180(grid)
    raise ValueError(f"unknown mode: {mode}")


def recolor_binary_grid_2d0172a1(
    grid: Grid,
    background: int,
    foreground: int,
) -> Grid:
    x0 = canvas(background, shape(grid))
    x1 = ofcolor(grid, ONE)
    x2 = fill(x0, foreground, x1)
    return x2


def crop_binary_input_2d0172a1(
    grid: Grid,
    foreground: int,
) -> Grid:
    x0 = ofcolor(grid, foreground)
    x1 = ulcorner(x0)
    x2 = shape(x0)
    x3 = crop(grid, x1, x2)
    return tuple(
        tuple(ONE if value == foreground else ZERO for value in row)
        for row in x3
    )


def pad_binary_input_2d0172a1(
    grid: Grid,
    background: int,
    foreground: int,
    top: int,
    left: int,
    bottom: int,
    right: int,
) -> Grid:
    x0 = shape(grid)
    x1 = astuple(x0[ZERO] + top + bottom, x0[ONE] + left + right)
    x2 = canvas(background, x1)
    x3 = shift(ofcolor(grid, ONE), astuple(top, left))
    x4 = fill(x2, foreground, x3)
    return x4


ARCHETYPES_2D0172A1 = (
    Archetype2d0172a1(
        name="train_1",
        input_grid=_binary_rows_2d0172a1(
            (
                "...#######...........",
                "####.....###.........",
                "#..........###.......",
                "#............##......",
                "#.............#......",
                "#...######....##.....",
                "#..##....##....#..##.",
                "#..#......#....#..###",
                "#..#.###..#....#...##",
                "#.##..##..#....#.....",
                "#..#......#...##.....",
                "#..##....##...#......",
                "#...######....#......",
                "#.............#......",
                "#............##......",
                "##...###.....#.......",
                ".#...###....##.......",
                ".#..........#........",
                ".#.........##........",
                ".###########.........",
            )
        ),
        output_grid=_binary_rows_2d0172a1(
            (
                "#########...",
                "#.......#...",
                "#.#####.#...",
                "#.#...#.#...",
                "#.#.#.#.#.#.",
                "#.#...#.#...",
                "#.#####.#...",
                "#.......#...",
                "#...#...#...",
                "#.......#...",
                "#########...",
            )
        ),
    ),
    Archetype2d0172a1(
        name="train_2",
        input_grid=_binary_rows_2d0172a1(
            (
                "...######",
                ".###....#",
                "##...#..#",
                "#..###..#",
                "#..###..#",
                "#...#...#",
                "#......##",
                "##...###.",
                ".#####...",
            )
        ),
        output_grid=_binary_rows_2d0172a1(
            (
                "#####",
                "#...#",
                "#.#.#",
                "#...#",
                "#####",
            )
        ),
    ),
    Archetype2d0172a1(
        name="train_3",
        input_grid=_binary_rows_2d0172a1(
            (
                "...######.",
                "..##....#.",
                "###.....##",
                "#........#",
                "#...##...#",
                "#..###...#",
                "#..##....#",
                "#........#",
                "#....#...#",
                "#..###..##",
                "#...##..#.",
                "##......#.",
                ".#......#.",
                "##......#.",
                "#......##.",
                "####..##..",
                "...####...",
            )
        ),
        output_grid=_binary_rows_2d0172a1(
            (
                "#####",
                "#...#",
                "#.#.#",
                "#...#",
                "#.#.#",
                "#...#",
                "#####",
            )
        ),
    ),
    Archetype2d0172a1(
        name="train_4",
        input_grid=_binary_rows_2d0172a1(
            (
                "......#######....",
                "#######.....#....",
                "#...........##...",
                "#...######...###.",
                "#..##....#.....##",
                "#..#..##.#......#",
                "#..#.###.#.###..#",
                "##.#.###.#.##...#",
                ".#.#.....#.....##",
                ".#.###..##...###.",
                ".#...####...##...",
                ".##........##....",
                "..##########.....",
            )
        ),
        output_grid=_binary_rows_2d0172a1(
            (
                "###########",
                "#.........#",
                "#.#####...#",
                "#.#...#...#",
                "#.#.#.#.#.#",
                "#.#...#...#",
                "#.#####...#",
                "#.........#",
                "###########",
            )
        ),
    ),
    Archetype2d0172a1(
        name="test_1",
        input_grid=_binary_rows_2d0172a1(
            (
                "..........###...........",
                "...########.#####.......",
                ".###............##......",
                "##...............###....",
                "#..................###..",
                "#....#######.........##.",
                "#...##.....######.....##",
                "#..##...........#......#",
                "#..#............##.##..#",
                "#..#..##...####..#.##..#",
                "#..#..###..####..#.....#",
                "#..#...##..###..##.....#",
                "#..#...........##......#",
                "#..###.......###......##",
                "##...#########........#.",
                ".##.................###.",
                "..#.............#####...",
                "..##.......######.......",
                "...#########............",
            )
        ),
        output_grid=_binary_rows_2d0172a1(
            (
                "#############",
                "#...........#",
                "#.#######...#",
                "#.#.....#...#",
                "#.#.#.#.#.#.#",
                "#.#.....#...#",
                "#.#######...#",
                "#...........#",
                "#############",
            )
        ),
    ),
    Archetype2d0172a1(
        name="test_2",
        input_grid=_binary_rows_2d0172a1(
            (
                "....##############....",
                ".####............###..",
                "##.................##.",
                "#.........###.......#.",
                "#........####.......#.",
                "#...................#.",
                "#...................##",
                "#.......#######......#",
                "#.......#.....##.....#",
                "#.###...#.###..#.....#",
                "#.###...#.###..#....##",
                "#..##...#..#..##....#.",
                "#.......##...##.....#.",
                "#........#####.....##.",
                "##.................#..",
                ".##...............##..",
                "..##..............#...",
                "...####..........##...",
                "......############....",
                "......................",
                "......................",
                "..........###.........",
                ".........####.........",
                "..........##..........",
            )
        ),
        output_grid=_binary_rows_2d0172a1(
            (
                "###########",
                "#.........#",
                "#.....#...#",
                "#.........#",
                "#...#####.#",
                "#...#...#.#",
                "#.#.#.#.#.#",
                "#...#...#.#",
                "#...#####.#",
                "#.........#",
                "###########",
                "...........",
                "......#....",
                "...........",
            )
        ),
    ),
)


def reconstruct_picture_2d0172a1(
    grid: Grid,
) -> Grid:
    x0 = mostcolor(grid)
    x1 = other(palette(grid), x0)
    x2 = crop_binary_input_2d0172a1(grid, x1)
    for x3 in ARCHETYPES_2D0172A1:
        for x4 in MODES_2D0172A1:
            x5 = transform_binary_grid_2d0172a1(x3.input_grid, x4)
            if x2 != x5:
                continue
            x6 = transform_binary_grid_2d0172a1(x3.output_grid, x4)
            x7 = recolor_binary_grid_2d0172a1(x6, x0, x1)
            return x7
    raise ValueError("unrecognized 2d0172a1 archetype")


__all__ = [
    "ARCHETYPES_2D0172A1",
    "COLOR_POOL_2D0172A1",
    "MODES_2D0172A1",
    "pad_binary_input_2d0172a1",
    "recolor_binary_grid_2d0172a1",
    "reconstruct_picture_2d0172a1",
    "transform_binary_grid_2d0172a1",
]
