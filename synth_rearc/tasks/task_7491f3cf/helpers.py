from collections import deque

from synth_rearc.core import *


PANEL_SHAPE_7491F3CF = (FIVE, FIVE)
FULL_PANEL_PATCH_7491F3CF = frozenset((i, j) for i in range(FIVE) for j in range(FIVE))
MAIN_DIAG_PATCH_7491F3CF = frozenset((i, i) for i in range(FIVE))
ANTI_DIAG_PATCH_7491F3CF = frozenset((i, subtract(FOUR, i)) for i in range(FIVE))
VERTICAL_SEPARATOR_PATCH_7491F3CF = frozenset((i, TWO) for i in range(FIVE))
HORIZONTAL_SEPARATOR_PATCH_7491F3CF = frozenset((TWO, j) for j in range(FIVE))
ELBOW_SEPARATOR_PATCH_7491F3CF = frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO), (TWO, ONE), (TWO, TWO)})
MOTIF_PATCHES_7491F3CF = (
    frozenset({(ZERO, ZERO), (ZERO, FOUR), (ONE, ONE), (ONE, THREE), (TWO, TWO), (THREE, ONE), (THREE, THREE), (FOUR, ZERO), (FOUR, FOUR)}),
    frozenset({(ZERO, TWO), (ONE, TWO), (TWO, ZERO), (TWO, ONE), (TWO, TWO), (TWO, THREE), (TWO, FOUR), (THREE, TWO), (FOUR, TWO)}),
    MAIN_DIAG_PATCH_7491F3CF,
    ANTI_DIAG_PATCH_7491F3CF,
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE), (THREE, THREE), (THREE, FOUR), (FOUR, THREE), (FOUR, FOUR)}),
    frozenset({(ZERO, THREE), (ZERO, FOUR), (ONE, THREE), (ONE, FOUR), (THREE, ZERO), (THREE, ONE), (FOUR, ZERO), (FOUR, ONE)}),
    frozenset({(ZERO, TWO), (ONE, ONE), (ONE, THREE), (TWO, ZERO), (TWO, FOUR), (THREE, ONE), (THREE, THREE), (FOUR, TWO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ONE, ZERO), (TWO, ZERO)}),
    frozenset({(ZERO, ONE), (ZERO, THREE), (ONE, ONE), (ONE, THREE), (TWO, ONE), (TWO, THREE), (THREE, ONE), (THREE, THREE), (FOUR, ONE), (FOUR, THREE)}),
    frozenset({(ONE, ZERO), (ONE, ONE), (ONE, TWO), (THREE, TWO), (THREE, THREE), (THREE, FOUR)}),
)


def _neighbors8_7491f3cf(
    loc: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    i, j = loc
    return (
        (i - ONE, j - ONE),
        (i - ONE, j),
        (i - ONE, j + ONE),
        (i, j - ONE),
        (i, j + ONE),
        (i + ONE, j - ONE),
        (i + ONE, j),
        (i + ONE, j + ONE),
    )


def _components8_7491f3cf(
    patch: Indices,
) -> tuple[Indices, ...]:
    remaining = set(patch)
    out: list[Indices] = []
    while remaining:
        seed = remaining.pop()
        comp = {seed}
        queue = [seed]
        while queue:
            loc = queue.pop()
            for nbr in _neighbors8_7491f3cf(loc):
                if nbr in remaining:
                    remaining.remove(nbr)
                    comp.add(nbr)
                    queue.append(nbr)
        out.append(frozenset(comp))
    return tuple(out)


def _component4_from_seed_7491f3cf(
    cells: Indices,
    seed: IntegerTuple,
) -> Indices:
    if seed not in cells:
        raise ValueError("seed not contained in candidate cells")
    queue = deque([seed])
    seen = {seed}
    while queue:
        i, j = queue.popleft()
        for nbr in ((i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE)):
            if nbr in cells and nbr not in seen:
                seen.add(nbr)
                queue.append(nbr)
    return frozenset(seen)


def render_patch_panel_7491f3cf(
    bg: Integer,
    value: Integer,
    patch: Patch,
) -> Grid:
    x0 = canvas(bg, PANEL_SHAPE_7491F3CF)
    return fill(x0, value, patch)


def rotate_patch_cw_7491f3cf(
    patch: Indices,
) -> Indices:
    return frozenset((j, subtract(FOUR, i)) for i, j in patch)


def mirror_patch_7491f3cf(
    patch: Indices,
) -> Indices:
    return frozenset((i, subtract(FOUR, j)) for i, j in patch)


def panel_mask_from_marker_patch_7491f3cf(
    patch: Indices,
) -> Indices:
    x0 = _components8_7491f3cf(patch)
    x1 = tuple(sorted((len(obj) for obj in x0)))
    if x1 != (ONE, FIVE):
        raise ValueError(f"expected marker parts of sizes 1 and 5, found {x1}")
    x2 = min(x0, key=len)
    x3 = max(x0, key=len)
    x4 = next(iter(x2))
    x5 = normalize(x3)
    if x5 == MAIN_DIAG_PATCH_7491F3CF:
        if greater(x4[0], x4[1]):
            return frozenset((i, j) for i in range(FIVE) for j in range(FIVE) if i >= j)
        return frozenset((i, j) for i in range(FIVE) for j in range(FIVE) if i <= j)
    if x5 == ANTI_DIAG_PATCH_7491F3CF:
        x6 = add(x4[0], x4[1])
        if x6 < FOUR:
            return frozenset((i, j) for i in range(FIVE) for j in range(FIVE) if add(i, j) <= FOUR)
        return frozenset((i, j) for i in range(FIVE) for j in range(FIVE) if add(i, j) >= FOUR)
    if vline(x5):
        x6 = leftmost(x3)
        x7 = x4[0]
        if x4[1] < x6:
            return frozenset((i, j) for i in range(FIVE) for j in range(x6)) | frozenset({(x7, x6)})
        return frozenset((i, j) for i in range(FIVE) for j in range(x6 + ONE, FIVE)) | frozenset({(x7, x6)})
    if hline(x5):
        x6 = uppermost(x3)
        x7 = x4[1]
        if x4[0] < x6:
            return frozenset((i, j) for i in range(x6) for j in range(FIVE)) | frozenset({(x6, x7)})
        return frozenset((i, j) for i in range(x6 + ONE, FIVE) for j in range(FIVE)) | frozenset({(x6, x7)})
    x6 = backdrop(x3)
    x7 = difference(x6, x3)
    return _component4_from_seed_7491f3cf(x7, x4)


def panel_mask_7491f3cf(
    marker_panel: Grid,
) -> Indices:
    x0 = mostcolor(marker_panel)
    x1 = other(palette(marker_panel), x0)
    x2 = ofcolor(marker_panel, x1)
    return panel_mask_from_marker_patch_7491f3cf(x2)
