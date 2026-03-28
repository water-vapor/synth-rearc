from synth_rearc.core import *

from .helpers import assemble_tiles_e9fc42f2, compact_positions_e9fc42f2


BACKGROUND_E9FC42F2 = TWO
FILL_E9FC42F2 = ONE
CONNECTOR_COLORS_E9FC42F2 = (THREE, FOUR, EIGHT)
OPPOSITE_SIDE_E9FC42F2 = {
    "top": "bottom",
    "bottom": "top",
    "left": "right",
    "right": "left",
}
STEP_E9FC42F2 = {
    "top": (-ONE, ZERO),
    "bottom": (ONE, ZERO),
    "left": (ZERO, -ONE),
    "right": (ZERO, ONE),
}
SIDE_ORDER_E9FC42F2 = ("top", "bottom", "left", "right")
TEMPLATE_SEEDS_E9FC42F2 = (
    ("..#..", "..#..", "#####", "..#..", "..*.."),
    ("#*##", "#..*", "####"),
    (".#*#.", "##.##", "#...#", "##.##", ".###."),
    ("###", "*.#", "#*#"),
    ("######", ".....*", "######"),
    ("###", "#.*", "###"),
    ("#*#", "#.#", "#.#", "#.#", "#*#"),
    ("###", "*.#", "#*#"),
    ("####", ".#..", "#*##"),
    ("#*#", "#.#", "*.#", "#.#", "#.#", "#.#", "#.*", "###"),
    ("#.#", "#.*", "###", ".#."),
    (".#.##", ".###*", "#*###"),
    ("##*#", ".##.", ".##."),
    ("#####", "*...#", "##*##"),
    (".#*#", "####", "#..#", "#..#", "#..#"),
)


def _bbox_overlap_e9fc42f2(
    a: tuple[Integer, Integer, Integer, Integer],
    b: tuple[Integer, Integer, Integer, Integer],
) -> Boolean:
    x0, x1, x2, x3 = a
    x4, x5, x6, x7 = b
    return x0 < x4 + x6 and x4 < x0 + x2 and x1 < x5 + x7 and x5 < x1 + x3


def _sample_walk_e9fc42f2(n_tiles: Integer) -> tuple[IntegerTuple, ...] | None:
    for _ in range(200):
        x0 = ((ZERO, ZERO),)
        x1 = frozenset({(ZERO, ZERO)})
        x2 = None
        x3 = True
        for _ in range(n_tiles - ONE):
            x4 = tuple()
            for x5 in SIDE_ORDER_E9FC42F2:
                if x2 is not None and x5 == OPPOSITE_SIDE_E9FC42F2[x2]:
                    continue
                x6, x7 = STEP_E9FC42F2[x5]
                x8 = (x0[-ONE][ZERO] + x6, x0[-ONE][ONE] + x7)
                if x8 in x1:
                    continue
                x4 = x4 + (x5,)
            if len(x4) == ZERO:
                x3 = False
                break
            x9 = choice(x4)
            x10, x11 = STEP_E9FC42F2[x9]
            x12 = (x0[-ONE][ZERO] + x10, x0[-ONE][ONE] + x11)
            x0 = x0 + (x12,)
            x1 = insert(x12, x1)
            x2 = x9
        if x3:
            return x0
    return None


def _edge_side_e9fc42f2(a: IntegerTuple, b: IntegerTuple) -> str:
    x0 = (b[ZERO] - a[ZERO], b[ONE] - a[ONE])
    for x1, x2 in STEP_E9FC42F2.items():
        if x2 == x0:
            return x1
    raise ValueError("non-adjacent walk step")


def _rotate_seed_e9fc42f2(seed: tuple[str, ...]) -> tuple[str, ...]:
    x0 = len(seed)
    x1 = len(seed[ZERO])
    return tuple("".join(seed[x0 - ONE - x2][x3] for x2 in range(x0)) for x3 in range(x1))


def _flip_seed_e9fc42f2(seed: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(x0[::-ONE] for x0 in seed)


def _template_data_e9fc42f2(seed: tuple[str, ...]) -> dict:
    x0 = len(seed)
    x1 = len(seed[ZERO])
    x2 = frozenset(
        (x3, x4)
        for x3, x5 in enumerate(seed)
        for x4, x6 in enumerate(x5)
        if x6 != "."
    )
    x7 = dict()
    for x8, x9 in enumerate(seed):
        for x10, x11 in enumerate(x9):
            if x11 != "*":
                continue
            x12 = tuple(
                x13
                for x13, x14 in (
                    ("top", x8 == ZERO),
                    ("bottom", x8 == x0 - ONE),
                    ("left", x10 == ZERO),
                    ("right", x10 == x1 - ONE),
                )
                if x14
            )
            if len(x12) != ONE:
                raise ValueError("connector must lie on exactly one border")
            x7[x12[ZERO]] = (x8, x10)
    return {"shape": seed, "cells": x2, "connectors": x7}


def _variant_library_e9fc42f2() -> dict[frozenset[str], tuple[dict, ...]]:
    x0: dict[frozenset[str], list[dict]] = dict()
    for x1 in TEMPLATE_SEEDS_E9FC42F2:
        x2 = set()
        x3 = x1
        for _ in range(FOUR):
            for x4 in (x3, _flip_seed_e9fc42f2(x3)):
                x5 = tuple(x4)
                if x5 in x2:
                    continue
                x2.add(x5)
                x6 = _template_data_e9fc42f2(x5)
                x7 = frozenset(x6["connectors"])
                if x7 not in x0:
                    x0[x7] = []
                x0[x7].append(x6)
            x3 = _rotate_seed_e9fc42f2(x3)
    return {x8: tuple(x9) for x8, x9 in x0.items()}


TILE_VARIANTS_E9FC42F2 = _variant_library_e9fc42f2()


def _build_tile_e9fc42f2(
    ports: dict[str, Integer],
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    del diff_lb, diff_ub
    x0 = frozenset(ports)
    x1 = TILE_VARIANTS_E9FC42F2.get(x0)
    if x1 is None:
        raise ValueError(f"unsupported port set {tuple(sorted(x0))}")
    x2 = choice(x1)
    x3 = canvas(BACKGROUND_E9FC42F2, (len(x2["shape"]), len(x2["shape"][ZERO])))
    x4 = fill(x3, FILL_E9FC42F2, x2["cells"])
    for x5, x6 in ports.items():
        x4 = fill(x4, x6, initset(x2["connectors"][x5]))
    return x4


def _valid_tile_e9fc42f2(tile: Grid) -> Boolean:
    x0, x1 = shape(tile)
    if x0 < THREE or x1 < THREE:
        return False
    for x2, x3 in enumerate(tile):
        for x4, x5 in enumerate(x3):
            if x5 in (BACKGROUND_E9FC42F2, FILL_E9FC42F2):
                continue
            if x2 in (ZERO, x0 - ONE) and x4 in (ZERO, x1 - ONE):
                return False
    return True


def _tiles_to_input_e9fc42f2(tiles: tuple[Grid, ...]) -> Grid | None:
    x0 = canvas(BACKGROUND_E9FC42F2, (13, 13))
    x1 = tuple(range(len(tiles)))
    for _ in range(300):
        x2 = tuple()
        x3 = dict()
        x4 = True
        for x5 in sample(x1, len(x1)):
            x6 = tiles[x5]
            x7, x8 = shape(x6)
            x9 = tuple()
            for x10 in range(13 - x7 + ONE):
                for x11 in range(13 - x8 + ONE):
                    x12 = (x10, x11, x7, x8)
                    x13 = True
                    for x14 in x2:
                        if _bbox_overlap_e9fc42f2(
                            (x12[ZERO] - ONE, x12[ONE] - ONE, x12[TWO] + TWO, x12[THREE] + TWO),
                            (x14[ZERO] - ONE, x14[ONE] - ONE, x14[TWO] + TWO, x14[THREE] + TWO),
                        ):
                            x13 = False
                            break
                    if x13:
                        x9 = x9 + ((x10, x11),)
            if len(x9) == ZERO:
                x4 = False
                break
            x15 = choice(x9)
            x3[x5] = x15
            x2 = x2 + ((x15[ZERO], x15[ONE], x7, x8),)
        if not x4:
            continue
        x16 = x0
        for x17, x18 in enumerate(tiles):
            x16 = paint(x16, shift(asobject(x18), x3[x17]))
        return x16
    return None


def generate_e9fc42f2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(600):
        x0 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x1 = _sample_walk_e9fc42f2(x0)
        if x1 is None:
            continue
        x2 = [dict() for _ in range(x0)]
        x3 = tuple(sample(CONNECTOR_COLORS_E9FC42F2, x0 - ONE))
        for x4, x5 in enumerate(x3):
            x6 = _edge_side_e9fc42f2(x1[x4], x1[x4 + ONE])
            x2[x4][x6] = x5
            x2[x4 + ONE][OPPOSITE_SIDE_E9FC42F2[x6]] = x5
        x7 = tuple(x8 for x8 in CONNECTOR_COLORS_E9FC42F2 if x8 not in x3)
        if len(x7) > ZERO and choice((T, T, F)):
            x8 = tuple(
                (x9, x10)
                for x9, x11 in enumerate(x2)
                for x10 in SIDE_ORDER_E9FC42F2
                if x10 not in x11
            )
            if len(x8) > ZERO:
                x9, x10 = choice(x8)
                x2[x9][x10] = choice(x7)
        x11 = tuple(_build_tile_e9fc42f2(x12, diff_lb, diff_ub) for x12 in x2)
        if any(not _valid_tile_e9fc42f2(x12) for x12 in x11):
            continue
        x13 = compact_positions_e9fc42f2(x11)
        x14 = tuple((x15[ZERO], x15[ONE], height(x16), width(x16)) for x15, x16 in zip(x13, x11))
        x17 = True
        for x18, x19 in enumerate(x14):
            for x20 in x14[x18 + ONE:]:
                if _bbox_overlap_e9fc42f2(x19, x20):
                    x17 = False
                    break
            if not x17:
                break
        if not x17:
            continue
        x21 = assemble_tiles_e9fc42f2(x11)
        x22, x23 = shape(x21)
        if x22 < EIGHT or x22 > 11 or x23 < FIVE or x23 > 11:
            continue
        x24 = _tiles_to_input_e9fc42f2(x11)
        if x24 is None:
            continue
        return {"input": x24, "output": x21}
    raise RuntimeError("failed to generate e9fc42f2 example")
