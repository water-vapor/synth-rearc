from __future__ import annotations

from synth_rearc.core import *

from .verifier import verify_db0c5428


PATTERN_LIBRARY_DB0C5428 = (
    {
        "A": ("ssm", "sms", "msc"),
        "B": ("msm", "sms", "ses"),
        "D": ("mss", "sme", "mss"),
    },
    {
        "A": ("msm", "smm", "mmc"),
        "B": ("mmm", "mmm", "mem"),
        "D": ("mmm", "mme", "mmm"),
    },
)


def _render_tile_db0c5428(
    pattern: tuple[str, str, str],
    color_map: dict[str, int],
) -> Grid:
    return tuple(tuple(color_map[ch] for ch in row) for row in pattern)


def _build_tiles_db0c5428(
    family: dict[str, tuple[str, str, str]],
    main_color: int,
    secondary_color: int,
    edge_color: int,
    corner_color: int,
) -> tuple[Grid, Grid, Grid, Grid, Grid, Grid, Grid, Grid, Grid]:
    x0 = {
        "m": main_color,
        "s": secondary_color,
        "e": edge_color,
        "c": corner_color,
    }
    x1 = _render_tile_db0c5428(family["A"], x0)
    x2 = _render_tile_db0c5428(family["B"], x0)
    x3 = vmirror(x1)
    x4 = _render_tile_db0c5428(family["D"], x0)
    x5 = vmirror(x4)
    x6 = hmirror(x1)
    x7 = hmirror(x2)
    x8 = rot180(x1)
    x9 = (
        (corner_color, edge_color, corner_color),
        (edge_color, main_color, edge_color),
        (corner_color, edge_color, corner_color),
    )
    return x1, x2, x3, x4, x5, x6, x7, x8, x9


def _hjoin_db0c5428(
    blocks: tuple[Grid, ...],
) -> Grid:
    x0 = first(blocks)
    for x1 in blocks[ONE:]:
        x0 = hconcat(x0, x1)
    return x0


def _vjoin_db0c5428(
    blocks: tuple[Grid, ...],
) -> Grid:
    x0 = first(blocks)
    for x1 in blocks[ONE:]:
        x0 = vconcat(x0, x1)
    return x0


def _compose_input_db0c5428(
    tiles: tuple[Grid, Grid, Grid, Grid, Grid, Grid, Grid, Grid, Grid],
    background: int,
) -> Grid:
    x0, x1, x2, x3, x4, x5, x6, x7, _ = tiles
    x8 = canvas(background, (THREE, THREE))
    x9 = _hjoin_db0c5428((x0, x1, x2))
    x10 = _hjoin_db0c5428((x3, x8, x4))
    x11 = _hjoin_db0c5428((x5, x6, x7))
    return _vjoin_db0c5428((x9, x10, x11))


def _compose_output_db0c5428(
    tiles: tuple[Grid, Grid, Grid, Grid, Grid, Grid, Grid, Grid, Grid],
    background: int,
) -> Grid:
    x0, x1, x2, x3, x4, x5, x6, x7, x8 = tiles
    x9 = canvas(background, (THREE, THREE))
    x10 = _hjoin_db0c5428((x7, x9, x6, x9, x5))
    x11 = _hjoin_db0c5428((x9, x0, x1, x2, x9))
    x12 = _hjoin_db0c5428((x4, x3, x8, x4, x3))
    x13 = _hjoin_db0c5428((x9, x5, x6, x7, x9))
    x14 = _hjoin_db0c5428((x2, x9, x1, x9, x0))
    return _vjoin_db0c5428((x10, x11, x12, x13, x14))


def generate_db0c5428(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = EIGHT
        x1 = choice(PATTERN_LIBRARY_DB0C5428)
        x2 = [value for value in range(ONE, TEN) if value != x0]
        x3 = choice(x2)
        x4 = [value for value in x2 if value != x3]
        if uniform(0.0, 1.0) < 0.35:
            x5 = x3
        else:
            x5 = choice(x4)
            x4 = [value for value in x4 if value != x5]
        x6 = choice(x4)
        if uniform(0.0, 1.0) < 0.7:
            x7 = x6
        else:
            x8 = [value for value in x4 if value != x6]
            x7 = choice(x8) if len(x8) > ZERO else x6
        x9 = _build_tiles_db0c5428(x1, x3, x5, x6, x7)
        x10 = _compose_input_db0c5428(x9, x0)
        x11 = _compose_output_db0c5428(x9, x0)
        x12 = unifint(diff_lb, diff_ub, (16, 22))
        x13 = unifint(diff_lb, diff_ub, (16, 22))
        x14 = randint(THREE, x12 - 12)
        x15 = randint(THREE, x13 - 12)
        x16 = paint(canvas(x0, (x12, x13)), shift(asobject(x10), (x14, x15)))
        x17 = paint(canvas(x0, (x12, x13)), shift(asobject(x11), (x14 - THREE, x15 - THREE)))
        if x16 == x17:
            continue
        if verify_db0c5428(x16) != x17:
            continue
        return {"input": x16, "output": x17}
