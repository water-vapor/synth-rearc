from collections import defaultdict, deque

from synth_rearc.core import *


BACKGROUND_E9FC42F2 = TWO
FILL_E9FC42F2 = ONE
OPPOSITE_SIDE_E9FC42F2 = {
    "top": "bottom",
    "bottom": "top",
    "left": "right",
    "right": "left",
}


def extract_tiles_e9fc42f2(I: Grid) -> tuple[Grid, ...]:
    x0 = objects(I, F, F, T)
    x1 = tuple(
        sorted(
            x0,
            key=lambda x2: (uppermost(x2), leftmost(x2), height(x2), width(x2)),
        )
    )
    return tuple(subgrid(x2, I) for x2 in x1)


def _connector_map_e9fc42f2(tile: Grid) -> dict[Integer, tuple[IntegerTuple, tuple[str, ...]]]:
    x0, x1 = shape(tile)
    x2 = dict()
    for x3, x4 in enumerate(tile):
        for x5, x6 in enumerate(x4):
            if x6 in (BACKGROUND_E9FC42F2, FILL_E9FC42F2):
                continue
            x7 = tuple(
                x8
                for x8, x9 in (
                    ("top", x3 == ZERO),
                    ("bottom", x3 == x0 - ONE),
                    ("left", x5 == ZERO),
                    ("right", x5 == x1 - ONE),
                )
                if x9
            )
            x2[x6] = ((x3, x5), x7)
    return x2


def _relative_offset_e9fc42f2(
    tile_a: Grid,
    tile_b: Grid,
    color_value: Integer,
) -> IntegerTuple:
    x0 = _connector_map_e9fc42f2(tile_a)[color_value]
    x1 = _connector_map_e9fc42f2(tile_b)[color_value]
    x2, x3 = x0
    x4, x5 = x1
    x6, x7 = x2
    x8, x9 = x4
    for x10 in x3:
        x11 = OPPOSITE_SIDE_E9FC42F2[x10]
        if x11 not in x5:
            continue
        if x10 == "top":
            return (x6 - ONE - x8, x7 - x9)
        if x10 == "bottom":
            return (x6 + ONE - x8, x7 - x9)
        if x10 == "left":
            return (x6 - x8, x7 - ONE - x9)
        return (x6 - x8, x7 + ONE - x9)
    raise ValueError(f"no matching border pairing for color {color_value}")


def compact_positions_e9fc42f2(tiles: tuple[Grid, ...]) -> tuple[IntegerTuple, ...]:
    x0 = tuple(_connector_map_e9fc42f2(x1) for x1 in tiles)
    x1: defaultdict[Integer, list[Integer]] = defaultdict(list)
    for x2, x3 in enumerate(x0):
        for x4 in x3:
            x1[x4].append(x2)
    x5: defaultdict[Integer, list[tuple[Integer, Integer]]] = defaultdict(list)
    for x6, x7 in x1.items():
        if len(x7) != TWO:
            continue
        x8, x9 = x7
        x5[x8].append((x9, x6))
        x5[x9].append((x8, x6))
    x10 = {ZERO: (ZERO, ZERO)}
    x11 = deque([ZERO])
    while len(x11) > ZERO:
        x12 = x11.popleft()
        x13, x14 = x10[x12]
        for x15, x16 in x5[x12]:
            x17, x18 = _relative_offset_e9fc42f2(tiles[x12], tiles[x15], x16)
            x19 = (x13 + x17, x14 + x18)
            if x15 in x10:
                if x10[x15] != x19:
                    raise ValueError("inconsistent compact placement")
                continue
            x10[x15] = x19
            x11.append(x15)
    if len(x10) != len(tiles):
        raise ValueError("disconnected tile graph")
    x20 = minimum(tuple(x21[ZERO] for x21 in x10.values()))
    x22 = minimum(tuple(x23[ONE] for x23 in x10.values()))
    return tuple((x10[x24][ZERO] - x20, x10[x24][ONE] - x22) for x24 in range(len(tiles)))


def assemble_tiles_e9fc42f2(tiles: tuple[Grid, ...]) -> Grid:
    x0 = compact_positions_e9fc42f2(tiles)
    x1 = maximum(tuple(x2[ZERO] + len(x3) for x3, x2 in zip(tiles, x0)))
    x4 = maximum(tuple(x5[ONE] + len(x6[ZERO]) for x6, x5 in zip(tiles, x0)))
    x7 = canvas(BACKGROUND_E9FC42F2, (x1, x4))
    for x8, x9 in zip(tiles, x0):
        x7 = paint(x7, shift(asobject(x8), x9))
    return x7
