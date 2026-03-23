from arc2.core import *

from .verifier import verify_2037f2c7


COLORS = (ONE, TWO, THREE, FOUR, SIX, SEVEN)

FAMILY_SPECS = (
    {
        "full_prefix": (
            (0, 0, 1, 1, 1, 1, 0, 0),
            (2, 2, 3, 4, 4, 3, 2, 2),
            (5, 5, 5, 5, 5, 5, 5, 5),
        ),
        "band_full": (
            (2, 6, 3, 4, 4, 3, 6, 2),
            (2, 6, 3, 4, 4, 3, 6, 2),
            (2, 6, 3, 4, 4, 3, 6, 2),
            (2, 6, 3, 4, 4, 3, 6, 2),
        ),
        "band_variant": (
            (2, 0, 3, 4, 4, 3, 0, 0),
            (0, 0, 0, 4, 0, 0, 0, 0),
            (2, 6, 0, 4, 4, 3, 6, 0),
            (2, 6, 3, 4, 4, 3, 6, 0),
        ),
        "full_suffix": (
            (2, 2, 3, 4, 4, 3, 2, 2),
            (5, 3, 3, 6, 6, 3, 3, 5),
            (5, 3, 3, 6, 6, 3, 3, 5),
            (5, 0, 0, 6, 6, 0, 0, 5),
        ),
        "pre_bounds": (0, 3),
        "post_bounds": (0, 2),
        "palette_size": 6,
        "slot_to_palette": {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5},
    },
    {
        "full_prefix": (
            (0, 0, 1, 1, 1, 0, 0),
            (2, 2, 3, 4, 3, 2, 2),
        ),
        "band_full": (
            (2, 5, 3, 4, 3, 5, 2),
            (2, 5, 3, 4, 3, 5, 2),
            (2, 5, 3, 4, 3, 5, 2),
        ),
        "band_variant": (
            (0, 5, 3, 4, 3, 5, 0),
            (0, 0, 3, 4, 3, 0, 0),
            (0, 5, 3, 4, 3, 5, 0),
        ),
        "full_suffix": (
            (2, 2, 3, 4, 3, 2, 2),
            (0, 0, 1, 1, 1, 0, 0),
        ),
        "pre_bounds": (2, 6),
        "post_bounds": (1, 4),
        "palette_size": 4,
        "slot_to_palette": {1: 0, 2: 0, 3: 1, 4: 2, 5: 3},
    },
    {
        "full_prefix": (
            (1, 1, 1, 1, 1, 1),
            (2, 2, 2, 2, 2, 2),
            (0, 3, 3, 3, 3, 0),
        ),
        "band_full": (
            (4, 5, 6, 6, 5, 4),
            (0, 5, 6, 6, 5, 0),
        ),
        "band_variant": (
            (0, 0, 0, 6, 0, 0),
            (0, 5, 0, 6, 5, 0),
        ),
        "full_suffix": (
            (0, 5, 6, 6, 5, 0),
        ),
        "pre_bounds": (2, 4),
        "post_bounds": (0, 0),
        "palette_size": 4,
        "slot_to_palette": {1: 0, 2: 1, 3: 0, 4: 2, 5: 0, 6: 3},
    },
)


def _rows_to_object(rows: tuple[tuple[int, ...], ...]) -> Object:
    return frozenset(
        (value, (i, j))
        for i, row in enumerate(rows)
        for j, value in enumerate(row)
        if value != ZERO
    )


def _make_slotmap(spec: dict) -> dict[int, int]:
    palette = sample(COLORS, spec["palette_size"])
    slotmap = {0: ZERO}
    for slot, idx in spec["slot_to_palette"].items():
        slotmap[slot] = palette[idx]
    return slotmap


def _materialize_rows(
    slotmap: dict[int, int],
    rows: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(slotmap[value] for value in row) for row in rows)


def _shape_output(a: Object, b: Object) -> Grid:
    x0 = toindices(a)
    x1 = toindices(b)
    x2 = difference(x0, x1)
    x3 = difference(x1, x0)
    x4 = combine(x2, x3)
    x5 = combine(x0, x1)
    x6 = canvas(ZERO, shape(x5))
    x7 = fill(x6, EIGHT, x4)
    x8 = subgrid(x4, x7)
    return x8


def _build_pair(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Object, Object, Grid]:
    spec = choice(FAMILY_SPECS)
    npre = unifint(diff_lb, diff_ub, spec["pre_bounds"])
    npost = unifint(diff_lb, diff_ub, spec["post_bounds"])
    x0 = spec["full_prefix"]
    x1 = (spec["band_full"][0],) * npre
    x2 = spec["band_full"]
    x3 = (spec["band_full"][-1],) * npost
    x4 = spec["full_suffix"]
    x5 = x0 + x1 + x2 + x3 + x4
    x6 = x0 + x1 + spec["band_variant"] + x3 + x4
    x7 = _make_slotmap(spec)
    x8 = _materialize_rows(x7, x5)
    x9 = _materialize_rows(x7, x6)
    x10 = _rows_to_object(x8)
    x11 = _rows_to_object(x9)
    x12 = _shape_output(x10, x11)
    return x10, x11, x12


def _separated(a: Patch, b: Patch) -> bool:
    x0 = ulcorner(a)
    x1 = lrcorner(a)
    x2 = ulcorner(b)
    x3 = lrcorner(b)
    return (
        x1[0] + 1 < x2[0]
        or x3[0] + 1 < x0[0]
        or x1[1] + 1 < x2[1]
        or x3[1] + 1 < x0[1]
    )


def generate_2037f2c7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1, x2 = _build_pair(diff_lb, diff_ub)
        x3 = (x0, x1)
        if choice((True, False)):
            x3 = (x1, x0)
        x4 = maximum((height(first(x3)), height(last(x3))))
        x5 = maximum((width(first(x3)), width(last(x3))))
        x6 = (max(18, x4 + 6), min(30, x4 + 14))
        x7 = (max(18, 2 * x5 + 4), 30)
        x8 = unifint(diff_lb, diff_ub, x6)
        x9 = unifint(diff_lb, diff_ub, x7)
        x10 = canvas(ZERO, (x8, x9))
        for _ in range(200):
            x11 = (randint(0, x8 - height(first(x3))), randint(0, x9 - width(first(x3))))
            x12 = (randint(0, x8 - height(last(x3))), randint(0, x9 - width(last(x3))))
            x13 = shift(first(x3), x11)
            x14 = shift(last(x3), x12)
            x15 = toindices(x13)
            x16 = toindices(x14)
            if not _separated(x15, x16):
                continue
            x17 = paint(x10, x13)
            x18 = paint(x17, x14)
            x19 = objects(x18, F, F, T)
            if len(x19) != 2:
                continue
            if verify_2037f2c7(x18) != x2:
                continue
            return {"input": x18, "output": x2}
