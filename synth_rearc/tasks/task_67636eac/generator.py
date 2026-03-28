from synth_rearc.core import *


THREE_BY_THREE_67636EAC = (THREE, THREE)
PLUS_PATCH_67636EAC = frozenset(
    {
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, ONE),
        (ONE, TWO),
        (TWO, ONE),
    }
)
DIAMOND_PATCH_67636EAC = frozenset(
    {
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, TWO),
        (TWO, ONE),
    }
)
MOTIFS_67636EAC = (PLUS_PATCH_67636EAC, DIAMOND_PATCH_67636EAC)
COLORS_67636EAC = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _tile_67636eac(value: Integer, patch: Indices) -> Grid:
    return fill(canvas(ZERO, THREE_BY_THREE_67636EAC), value, patch)


def _motif_object_67636eac(
    value: Integer,
    patch: Indices,
    location: IntegerTuple,
) -> Object:
    return shift(recolor(value, patch), location)


def _sample_relative_locs_67636eac(
    vertical: Boolean,
    count: Integer,
) -> tuple[IntegerTuple, ...]:
    while True:
        locs = []
        if vertical:
            row = ZERO
            base_col = randint(ZERO, TWO)
            for _ in range(count):
                locs.append((row, base_col + randint(ZERO, TWO)))
                row += randint(FOUR, SIX)
        else:
            base_row = randint(ZERO, TWO)
            col = ZERO
            for _ in range(count):
                locs.append((base_row + randint(ZERO, TWO), col))
                col += randint(FOUR, SIX)
        rows = tuple(i for i, _ in locs)
        cols = tuple(j for _, j in locs)
        span_h = maximum(rows) - minimum(rows) + THREE
        span_w = maximum(cols) - minimum(cols) + THREE
        if vertical == greater(span_h, span_w):
            return tuple(locs)


def _fit_locs_67636eac(
    locs: tuple[IntegerTuple, ...],
) -> tuple[tuple[IntegerTuple, ...], Integer, Integer]:
    rows = tuple(i for i, _ in locs)
    cols = tuple(j for _, j in locs)
    min_row = minimum(rows)
    max_row = maximum(rows)
    min_col = minimum(cols)
    max_col = maximum(cols)
    span_h = max_row - min_row + THREE
    span_w = max_col - min_col + THREE
    room_h = 30 - span_h
    room_w = 30 - span_w
    top = randint(ZERO, min(SIX, room_h))
    left = randint(ZERO, min(SIX, room_w))
    bottom = randint(ZERO, min(SIX, room_h - top))
    right = randint(ZERO, min(SIX, room_w - left))
    offset = subtract((top, left), (min_row, min_col))
    fitted = tuple(add(loc, offset) for loc in locs)
    return fitted, span_h + top + bottom, span_w + left + right


def _concat_67636eac(
    grids: tuple[Grid, ...],
    vertical: Boolean,
) -> Grid:
    result = grids[ZERO]
    join = vconcat if vertical else hconcat
    for grid in grids[ONE:]:
        result = join(result, grid)
    return result


def generate_67636eac(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    vertical = choice((T, F))
    count = unifint(diff_lb, diff_ub, (TWO, FOUR))
    patch = choice(MOTIFS_67636EAC)
    locs = _sample_relative_locs_67636eac(vertical, count)
    locs, h, w = _fit_locs_67636eac(locs)
    colors = sample(COLORS_67636EAC, count)
    gi = canvas(ZERO, (h, w))
    for value, loc in zip(colors, locs):
        gi = paint(gi, _motif_object_67636eac(value, patch, loc))
    axis = ZERO if vertical else ONE
    ordered = tuple(sorted(zip(locs, colors), key=lambda item: item[ZERO][axis]))
    pieces = tuple(_tile_67636eac(value, patch) for _, value in ordered)
    go = _concat_67636eac(pieces, vertical)
    return {"input": gi, "output": go}
