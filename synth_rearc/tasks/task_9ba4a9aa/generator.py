from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    GRID_SHAPE_9BA4A9AA,
    checker_object_9ba4a9aa,
    paint_lattice_nodes_9ba4a9aa,
    ring_grid_9ba4a9aa,
    ring_object_9ba4a9aa,
)
from .verifier import verify_9ba4a9aa


TEMPLATES_9BA4A9AA = (
    {
        "checker": (0, 8),
        "target": (8, 7),
        "trunk": (
            (0, 7), (0, 6), (0, 5), (0, 4), (0, 3),
            (1, 3), (2, 3), (3, 3), (4, 3),
            (4, 4), (4, 5), (4, 6), (4, 7),
            (5, 7), (6, 7), (7, 7),
        ),
        "branches": (
            {"center": (0, 0), "path": ((0, 2), (0, 1))},
            {"center": (7, 1), "path": ((4, 2), (4, 1), (5, 1), (6, 1))},
            {"center": (7, 3), "path": ((5, 3), (6, 3))},
        ),
    },
    {
        "checker": (0, 0),
        "target": (8, 1),
        "trunk": (
            (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),
            (6, 3), (6, 2), (6, 1), (7, 1),
        ),
        "branches": (
            {"center": (3, 0), "path": ((3, 3), (3, 2), (3, 1))},
            {"center": (3, 7), "path": ((3, 5), (3, 6))},
            {"center": (7, 8), "path": ((6, 5), (6, 6), (6, 7), (7, 7))},
        ),
    },
    {
        "checker": (8, 0),
        "target": (0, 8),
        "trunk": (
            (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
        ),
        "branches": (
            {"center": (3, 5), "path": ((3, 1), (3, 2), (3, 3), (3, 4))},
            {"center": (6, 5), "path": ((6, 1), (6, 2), (6, 3), (6, 4))},
            {"center": (8, 7), "path": ((7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7))},
        ),
    },
)


def _transform_node_9ba4a9aa(
    node: tuple[int, int],
    variant: int,
) -> tuple[int, int]:
    x0, x1 = node
    if variant == ZERO:
        return (x0, x1)
    if variant == ONE:
        return (x1, NINE - x0)
    if variant == TWO:
        return (NINE - x0, NINE - x1)
    if variant == THREE:
        return (NINE - x1, x0)
    if variant == FOUR:
        return (x0, NINE - x1)
    if variant == FIVE:
        return (NINE - x0, x1)
    if variant == SIX:
        return (x1, x0)
    return (NINE - x1, NINE - x0)


def _transform_template_9ba4a9aa(
    template: dict,
    variant: int,
) -> dict:
    x0 = tuple(_transform_node_9ba4a9aa(x1, variant) for x1 in template["trunk"])
    x1 = tuple(
        {
            "center": _transform_node_9ba4a9aa(x2["center"], variant),
            "path": tuple(_transform_node_9ba4a9aa(x3, variant) for x3 in x2["path"]),
        }
        for x2 in template["branches"]
    )
    return {
        "checker": _transform_node_9ba4a9aa(template["checker"], variant),
        "target": _transform_node_9ba4a9aa(template["target"], variant),
        "trunk": x0,
        "branches": x1,
    }


def _sample_ring_colors_9ba4a9aa(
    palette_values: tuple[int, ...],
) -> tuple[int, int]:
    x0 = choice(palette_values)
    x1 = choice(tuple(x2 for x2 in palette_values if x2 != x0))
    return x0, x1


def generate_9ba4a9aa(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(interval(ZERO, TEN, ONE))
        x1 = sample(tuple(x2 for x2 in interval(ZERO, TEN, ONE) if x2 != x0), FOUR)
        x2 = tuple(x3 for x3 in interval(ZERO, TEN, ONE) if x3 != x0 and x3 not in x1)
        x3 = choice((ONE, TWO))
        x4 = _transform_template_9ba4a9aa(choice(TEMPLATES_9BA4A9AA), randint(ZERO, SEVEN))
        x5 = canvas(x0, GRID_SHAPE_9BA4A9AA)
        x6 = sample(x2, TWO)
        x7 = paint_lattice_nodes_9ba4a9aa(x5, x4["trunk"], x3, x1[ZERO])
        x7 = paint(x7, checker_object_9ba4a9aa(x4["checker"], x3, x6[ZERO], x6[ONE]))
        x8, x9 = _sample_ring_colors_9ba4a9aa(x2)
        x7 = paint(x7, ring_object_9ba4a9aa(x4["target"], x3, x8, x9))
        x10 = ring_grid_9ba4a9aa(x8, x9)
        for x11, x12 in enumerate(x4["branches"]):
            x13, x14 = _sample_ring_colors_9ba4a9aa(x2)
            x7 = paint_lattice_nodes_9ba4a9aa(x7, x12["path"], x3, x1[x11 + ONE])
            x7 = paint(x7, ring_object_9ba4a9aa(x12["center"], x3, x13, x14))
        if verify_9ba4a9aa(x7) != x10:
            continue
        return {"input": x7, "output": x10}
