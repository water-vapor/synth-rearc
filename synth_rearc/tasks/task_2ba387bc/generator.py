from __future__ import annotations

from synth_rearc.core import *

from .verifier import verify_2ba387bc


TILE_DIMS_2BA387BC = astuple(FOUR, FOUR)
HEIGHT_VALUES_2BA387BC = (20, 20, 21, 22, 22, 23, 24, 24)
WIDTH_VALUES_2BA387BC = (19, 20, 21, 22, 22, 23, 24, 24)
NONZERO_COLORS_2BA387BC = (ONE, TWO, THREE, FOUR, SIX, SEVEN, EIGHT, NINE)

SOLID_PATCH_2BA387BC = frozenset(
    (i, j)
    for i in range(FOUR)
    for j in range(FOUR)
)
HOLLOW_PATCH_2BA387BC = frozenset(
    (i, j)
    for i in range(FOUR)
    for j in range(FOUR)
    if i in (ZERO, decrement(FOUR)) or j in (ZERO, decrement(FOUR))
)


def _tile_patch_2ba387bc(
    kind: str,
) -> Indices:
    return HOLLOW_PATCH_2BA387BC if kind == "hollow" else SOLID_PATCH_2BA387BC


def _tile_grid_2ba387bc(
    kind: str,
    color_value: Integer,
) -> Grid:
    x0 = canvas(ZERO, TILE_DIMS_2BA387BC)
    x1 = _tile_patch_2ba387bc(kind)
    x2 = fill(x0, color_value, x1)
    return x2


def _location_is_valid_2ba387bc(
    row: Integer,
    col: Integer,
    placed_specs: tuple[tuple[str, Integer, Integer, Integer], ...],
    used_rows: frozenset[Integer],
) -> Boolean:
    if row in used_rows:
        return False
    for _, _, x0, x1 in placed_specs:
        x2 = max(subtract(x0, add(row, FOUR)), subtract(row, add(x0, FOUR)), ZERO)
        x3 = max(subtract(x1, add(col, FOUR)), subtract(col, add(x1, FOUR)), ZERO)
        if both(equality(x2, ZERO), equality(x3, ZERO)):
            return False
    return True


def _sample_location_2ba387bc(
    height_value: Integer,
    width_value: Integer,
    placed_specs: tuple[tuple[str, Integer, Integer, Integer], ...],
    used_rows: frozenset[Integer],
) -> IntegerTuple | None:
    x0 = tuple(
        (x1, x2)
        for x1 in range(ONE, subtract(height_value, FOUR))
        for x2 in range(ONE, subtract(width_value, FOUR))
        if _location_is_valid_2ba387bc(x1, x2, placed_specs, used_rows)
    )
    if len(x0) == ZERO:
        return None
    x3 = choice(x0)
    return x3


def _compose_output_2ba387bc(
    placed_specs: tuple[tuple[str, Integer, Integer, Integer], ...],
) -> Grid:
    x0 = tuple(x1 for x1 in placed_specs if x1[ZERO] == "hollow")
    x1 = tuple(x2 for x2 in placed_specs if x2[ZERO] == "solid")
    x2 = tuple(sorted(x0, key=lambda x3: (x3[TWO], x3[THREE])))
    x3 = tuple(sorted(x1, key=lambda x4: (x4[TWO], x4[THREE])))
    x4 = tuple(_tile_grid_2ba387bc("hollow", x5[ONE]) for x5 in x2)
    x5 = tuple(_tile_grid_2ba387bc("solid", x6[ONE]) for x6 in x3)
    x6 = canvas(ZERO, TILE_DIMS_2BA387BC)
    x7 = maximum(astuple(len(x4), len(x5)))
    x8 = combine(x4, repeat(x6, subtract(x7, len(x4))))
    x9 = combine(x5, repeat(x6, subtract(x7, len(x5))))
    x10 = papply(hconcat, x8, x9)
    x11 = merge(x10)
    return x11


def generate_2ba387bc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(HEIGHT_VALUES_2BA387BC)
        x1 = choice(WIDTH_VALUES_2BA387BC)
        x2 = unifint(diff_lb, diff_ub, (TWO, THREE))
        x3 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x4 = tuple(["hollow"] * x2 + ["solid"] * x3)
        x5 = list(x4)
        shuffle(x5)
        x6 = sample(NONZERO_COLORS_2BA387BC, add(x2, x3))
        x7 = ()
        x8 = frozenset()
        for x9, x10 in zip(x5, x6):
            x11 = _sample_location_2ba387bc(x0, x1, x7, x8)
            if x11 is None:
                x7 = ()
                break
            x12, x13 = x11
            x7 = (*x7, (x9, x10, x12, x13))
            x8 = insert(x12, x8)
        if len(x7) != add(x2, x3):
            continue
        x14 = canvas(ZERO, (x0, x1))
        for x15, x16, x17, x18 in x7:
            x19 = _tile_patch_2ba387bc(x15)
            x20 = shift(x19, (x17, x18))
            x14 = fill(x14, x16, x20)
        x21 = _compose_output_2ba387bc(x7)
        if equality(x14, x21):
            continue
        if verify_2ba387bc(x14) != x21:
            continue
        return {"input": x14, "output": x21}
