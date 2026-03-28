from synth_rearc.core import *

from .verifier import verify_c4d1a9ae


GRID_SHAPE_C4D1A9AE = (TEN, EIGHT)
BAND_WIDTHS_C4D1A9AE = (
    (TWO, TWO, TWO),
    (THREE, ONE, TWO),
)
LEFT_W2_MOTIFS_C4D1A9AE = (
    (
        (ONE, ZERO),
        (ZERO, ONE),
        (ONE, ZERO),
        (ZERO, ONE),
        (ONE, ZERO),
        (ZERO, ONE),
        (ONE, ZERO),
        (ZERO, ONE),
        (ONE, ZERO),
        (ZERO, ONE),
    ),
    (
        (ONE, ZERO),
        (ONE, ZERO),
        (ZERO, ONE),
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, ZERO),
        (ZERO, ONE),
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, ZERO),
    ),
)
LEFT_W3_MOTIFS_C4D1A9AE = (
    (
        (ZERO, ZERO, ZERO),
        (ONE, ZERO, ZERO),
        (ZERO, ONE, ZERO),
        (ZERO, ZERO, ONE),
        (ZERO, ONE, ZERO),
        (ONE, ZERO, ZERO),
        (ZERO, ONE, ZERO),
        (ZERO, ZERO, ONE),
        (ZERO, ONE, ZERO),
        (ONE, ZERO, ZERO),
    ),
)
MIDDLE_W1_MOTIFS_C4D1A9AE = (
    (
        (ZERO,),
        (ONE,),
        (ZERO,),
        (ONE,),
        (ZERO,),
        (ONE,),
        (ZERO,),
        (ONE,),
        (ZERO,),
        (ONE,),
    ),
)
MIDDLE_W2_MOTIFS_C4D1A9AE = (
    (
        (ZERO, ONE),
        (ZERO, ONE),
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, ZERO),
        (ONE, ZERO),
        (ONE, ZERO),
        (ZERO, ONE),
        (ZERO, ONE),
        (ZERO, ONE),
    ),
    (
        (ONE, ONE),
        (ONE, ZERO),
        (ZERO, ONE),
        (ONE, ONE),
        (ONE, ONE),
        (ONE, ZERO),
        (ZERO, ONE),
        (ONE, ONE),
        (ONE, ONE),
        (ONE, ZERO),
    ),
)
RIGHT_W2_MOTIFS_C4D1A9AE = (
    (
        (ONE, ONE),
        (ZERO, ONE),
        (ONE, ONE),
        (ZERO, ONE),
        (ONE, ONE),
        (ZERO, ONE),
        (ONE, ONE),
        (ZERO, ONE),
        (ONE, ONE),
        (ZERO, ONE),
    ),
    (
        (ZERO, ONE),
        (ONE, ZERO),
        (ZERO, ONE),
        (ZERO, ONE),
        (ONE, ZERO),
        (ZERO, ONE),
        (ZERO, ONE),
        (ONE, ZERO),
        (ZERO, ONE),
        (ZERO, ONE),
    ),
    (
        (ZERO, ZERO),
        (ONE, ONE),
        (ONE, ZERO),
        (ZERO, ONE),
        (ONE, ONE),
        (ZERO, ZERO),
        (ONE, ONE),
        (ONE, ZERO),
        (ZERO, ONE),
        (ONE, ONE),
    ),
)


def _mirror_states_c4d1a9ae(
    states: tuple[tuple[Integer, ...], ...],
) -> tuple[tuple[Integer, ...], ...]:
    return tuple(tuple(row[::-ONE]) for row in states)


def _roll_states_c4d1a9ae(
    states: tuple[tuple[Integer, ...], ...],
    offset: Integer,
) -> tuple[tuple[Integer, ...], ...]:
    return states[offset:] + states[:offset]


def _sample_states_c4d1a9ae(
    motifs: tuple[tuple[tuple[Integer, ...], ...], ...],
    *,
    allow_mirror: Boolean,
) -> tuple[tuple[Integer, ...], ...]:
    x0 = choice(motifs)
    if allow_mirror and choice((T, F)):
        x0 = _mirror_states_c4d1a9ae(x0)
    if choice((T, F)):
        x0 = x0[::-ONE]
    x1 = randint(ZERO, decrement(len(x0)))
    return _roll_states_c4d1a9ae(x0, x1)


def _band_states_c4d1a9ae(
    index: Integer,
    width: Integer,
) -> tuple[tuple[Integer, ...], ...]:
    if index == ZERO and width == TWO:
        return _sample_states_c4d1a9ae(LEFT_W2_MOTIFS_C4D1A9AE, allow_mirror=T)
    if index == ZERO:
        return _sample_states_c4d1a9ae(LEFT_W3_MOTIFS_C4D1A9AE, allow_mirror=T)
    if index == ONE and width == ONE:
        return _sample_states_c4d1a9ae(MIDDLE_W1_MOTIFS_C4D1A9AE, allow_mirror=F)
    if index == ONE:
        return _sample_states_c4d1a9ae(MIDDLE_W2_MOTIFS_C4D1A9AE, allow_mirror=T)
    return _sample_states_c4d1a9ae(RIGHT_W2_MOTIFS_C4D1A9AE, allow_mirror=T)


def _band_starts_c4d1a9ae(
    widths: tuple[Integer, Integer, Integer],
) -> tuple[Integer, Integer, Integer]:
    x0, x1, _ = widths
    return ZERO, add(x0, ONE), add(add(x0, x1), TWO)


def _band_patch_c4d1a9ae(
    start: Integer,
    states: tuple[tuple[Integer, ...], ...],
) -> Indices:
    return frozenset(
        (i, add(start, j))
        for i, row in enumerate(states)
        for j, value in enumerate(row)
        if value == ONE
    )


def _band_box_c4d1a9ae(
    start: Integer,
    width: Integer,
) -> Indices:
    x0 = frozenset(
        {
            (ZERO, start),
            (decrement(GRID_SHAPE_C4D1A9AE[ZERO]), add(start, decrement(width))),
        }
    )
    return backdrop(x0)


def generate_c4d1a9ae(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(BAND_WIDTHS_C4D1A9AE)
        x1 = _band_starts_c4d1a9ae(x0)
        x2 = sample(interval(ZERO, TEN, ONE), FOUR)
        x3 = x2[ZERO]
        x4 = tuple(x2[ONE:])
        x5 = tuple(_band_states_c4d1a9ae(x6, x7) for x6, x7 in enumerate(x0))
        x6 = tuple(_band_patch_c4d1a9ae(x7, x8) for x7, x8 in zip(x1, x5))
        x7 = canvas(x3, GRID_SHAPE_C4D1A9AE)
        for x8, x9 in zip(x4, x6):
            x7 = fill(x7, x8, x9)
        x8 = x7
        x9 = x4[ONE:] + x4[:ONE]
        for x10, x11, x12, x13 in zip(x4, x9, x1, x0):
            x14 = _band_box_c4d1a9ae(x12, x13)
            x15 = ofcolor(x8, x10)
            x16 = difference(x14, x15)
            x8 = fill(x8, x11, x16)
        if x7 == x8:
            continue
        if verify_c4d1a9ae(x7) != x8:
            continue
        return {"input": x7, "output": x8}
