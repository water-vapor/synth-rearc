from __future__ import annotations

from synth_rearc.core import *

from .helpers import paint_region_305b1341, region_patches_305b1341


GRID_SHAPE_305B1341 = (20, 20)
PRIMARY_COLORS_305B1341 = tuple(range(ONE, TEN))


def _marker_rows_305b1341(
    top: Integer,
    nrows: Integer,
) -> tuple[Integer, ...]:
    return tuple(top + TWO * x0 for x0 in range(nrows))


def _marker_cols_305b1341(
    left: Integer,
    ncols: Integer,
) -> tuple[Integer, ...]:
    return tuple(left + TWO * x0 for x0 in range(ncols))


def _marker_patch_305b1341(
    top: Integer,
    left: Integer,
    nrows: Integer,
    ncols: Integer,
    style: str,
) -> Indices:
    x0 = _marker_rows_305b1341(top, nrows)
    x1 = _marker_cols_305b1341(left, ncols)
    x2 = set((x0[ZERO], x3) for x3 in x1)
    if style == "full":
        for x3 in x0[ONE:]:
            x2.update((x3, x4) for x4 in x1)
    elif style == "sides":
        x3 = (x1[ZERO],) if ncols == ONE else (x1[ZERO], x1[-ONE])
        for x4 in x0[ONE:]:
            x2.update((x4, x5) for x5 in x3)
    elif style == "right":
        x3 = x1[-min(TWO, ncols) :]
        for x4 in x0[ONE:]:
            x2.update((x4, x5) for x5 in x3)
    elif style == "left":
        x3 = x1[: min(TWO, ncols)]
        for x4 in x0[ONE:]:
            x2.update((x4, x5) for x5 in x3)
    else:
        x3 = choice((x1[ZERO], x1[-ONE]))
        for x4 in x0[ONE:]:
            x2.add((x4, x3))
    return frozenset(x2)


def _secondary_color_305b1341(
    primary: Integer,
    primaries: tuple[Integer, ...],
    secondaries: tuple[Integer, ...],
) -> Integer:
    x0 = tuple(x1 for x1 in primaries if x1 != primary)
    x1 = tuple(x2 for x2 in x0 if x2 not in secondaries)
    x2 = tuple(x3 for x3 in PRIMARY_COLORS_305B1341 if x3 != primary)
    if len(x1) > ZERO and choice((T, T, F)):
        return choice(x1)
    if len(x0) > ZERO and choice((T, F)):
        return choice(x0)
    return choice(x2)


def _sample_region_305b1341(
    marker_union: Indices,
    region_union: Indices,
    want_overlap: Boolean,
) -> tuple[Indices, Indices] | None:
    x0, x1 = GRID_SHAPE_305B1341
    for _ in range(400):
        x2 = randint(TWO, EIGHT)
        x3 = randint(TWO, FIVE)
        x4 = randint(ONE, x0 - (TWO * x2))
        x5 = randint(THREE, x1 - (TWO * x3))
        x6 = choice(("full", "full", "sides", "right", "left", "single"))
        x7 = _marker_patch_305b1341(x4, x5, x2, x3, x6)
        if len(intersection(x7, marker_union)) > ZERO:
            continue
        x8, _ = region_patches_305b1341(x7, GRID_SHAPE_305B1341)
        if want_overlap and len(intersection(x8, region_union)) == ZERO:
            continue
        if not want_overlap and len(intersection(x8, region_union)) > ZERO and choice((T, F)):
            continue
        return x7, x8
    return None


def generate_305b1341(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    _ = diff_lb, diff_ub
    for _ in range(400):
        x0 = choice((TWO, TWO, THREE, THREE))
        x1 = tuple(sample(PRIMARY_COLORS_305B1341, x0))
        x2 = []
        for x3 in x1:
            x4 = _secondary_color_305b1341(x3, x1, tuple(x2))
            x2.append(x4)
        x5 = tuple(zip(x1, x2))
        x6 = [None] * x0
        x7 = frozenset()
        x8 = frozenset()
        for x9 in range(x0 - ONE, -ONE, -ONE):
            x10 = len(x8) > ZERO and choice((T, T, F))
            x11 = _sample_region_305b1341(x7, x8, x10)
            if x11 is None:
                break
            x12, x13 = x11
            x6[x9] = x12
            x7 = combine(x7, x12)
            x8 = combine(x8, x13)
        else:
            x14 = canvas(ZERO, GRID_SHAPE_305B1341)
            for x15, (x16, _x17) in enumerate(x5):
                x14 = fill(x14, x16, frozenset({(x15, ZERO)}))
                x14 = fill(x14, x2[x15], frozenset({(x15, ONE)}))
                x14 = fill(x14, x16, x6[x15])
            x18 = canvas(ZERO, GRID_SHAPE_305B1341)
            for x19, x20 in zip(reversed(x6), reversed(x5)):
                x18 = paint_region_305b1341(x18, x19, x20[ZERO], x20[ONE])
            return {"input": x14, "output": x18}
    raise RuntimeError("failed to generate 305b1341 example")
