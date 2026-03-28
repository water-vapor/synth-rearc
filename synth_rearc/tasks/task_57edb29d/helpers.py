from __future__ import annotations

from synth_rearc.core import *


def visible_pairs_57edb29d(
    dims: IntegerTuple,
    pairs: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple]:
    x0, x1 = dims
    x2 = (x0 - ONE) // TWO
    x3 = (x1 - ONE) // TWO
    return frozenset((x4, x5) for x4, x5 in pairs if x4 <= x2 and x5 <= x3)


def distance_pairs_57edb29d(
    marker: Integer,
    panel: Grid,
) -> frozenset[IntegerTuple]:
    x0 = len(panel)
    x1 = len(panel[0])
    x2 = ofcolor(panel, marker)
    return frozenset(
        (min(x3, x0 - ONE - x3), min(x4, x1 - ONE - x4))
        for x3, x4 in x2
    )


def indices_for_pairs_57edb29d(
    dims: IntegerTuple,
    pairs: frozenset[IntegerTuple],
) -> Indices:
    x0, x1 = dims
    return frozenset(
        (x2, x3)
        for x2 in range(x0)
        for x3 in range(x1)
        if (min(x2, x0 - ONE - x2), min(x3, x1 - ONE - x3)) in pairs
    )


def render_panel_57edb29d(
    base_color: Integer,
    marker: Integer,
    dims: IntegerTuple,
    pairs: frozenset[IntegerTuple],
) -> Grid:
    x0 = canvas(base_color, dims)
    x1 = indices_for_pairs_57edb29d(dims, visible_pairs_57edb29d(dims, pairs))
    return fill(x0, marker, x1)
