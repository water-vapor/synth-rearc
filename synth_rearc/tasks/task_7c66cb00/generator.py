from __future__ import annotations

from synth_rearc.core import *

from .helpers import GRID_SHAPE_7C66CB00
from .helpers import make_motif_7c66cb00
from .helpers import place_motif_7c66cb00
from .helpers import render_input_7c66cb00
from .helpers import render_output_7c66cb00


def _band_specs_7c66cb00(
    bg: Integer,
    nbands: Integer,
) -> tuple[tuple[Integer, Integer, Integer, Integer], ...] | None:
    x0 = tuple(x1 for x1 in range(TEN) if x1 != bg)
    x2 = tuple(sample(x0, nbands))
    x3 = []
    for x4 in x2:
        x5 = tuple(x6 for x6 in x0 if both(x6 != x4, x6 not in x3))
        if len(x5) == ZERO:
            return None
        x3.append(choice(x5))
    x6 = []
    x7 = subtract(GRID_SHAPE_7C66CB00[0], choice((ONE, TWO)))
    for x8, x9, x10 in zip(reversed(x2), reversed(x3), reversed(tuple(randint(FOUR, SEVEN) for _ in range(nbands)))):
        x11 = subtract(x7, x10) + ONE
        if x11 < EIGHT:
            return None
        x6.append((x11, x7, x8, x9))
        x7 = subtract(x11, randint(TWO, THREE))
    x6.reverse()
    return tuple(x6)


def _motif_color_sets_7c66cb00(
    fill_colors: tuple[Integer, ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[Integer, ...], ...]:
    x0 = []
    x1 = list(fill_colors)
    shuffle(x1)
    for x2 in x1:
        x3 = tuple(x4 for x4 in fill_colors if x4 != x2)
        if both(len(x3) > ZERO, choice((T, T, F))):
            x4 = choice(x3)
            x5 = (x2, x4)
            x0.append(x5 if choice((T, F)) else x5[::-1])
        else:
            x0.append((x2,))
    x6 = (diff_lb + diff_ub) / 2.0
    x7 = randint(ZERO, ONE + int(x6 > 0.45) + int(x6 > 0.8))
    for _ in range(x7):
        if both(len(fill_colors) > ONE, choice((T, T, F))):
            x8 = tuple(sample(fill_colors, TWO))
            x0.append(x8 if choice((T, F)) else x8[::-1])
        else:
            x0.append((choice(fill_colors),))
    shuffle(x0)
    return tuple(x0)


def generate_7c66cb00(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(interval(ZERO, TEN, ONE))
        x1 = choice((TWO, TWO, THREE))
        x2 = _band_specs_7c66cb00(x0, x1)
        if x2 is None:
            continue
        x3 = tuple(x4[2] for x4 in x2)
        x4 = {x5[2]: subtract(x5[1], x5[0]) + ONE for x5 in x2}
        x5 = subtract(x2[0][0], TWO)
        if x5 < FIVE:
            continue
        x6 = _motif_color_sets_7c66cb00(x3, diff_lb, diff_ub)
        x7 = tuple(make_motif_7c66cb00(x8, min(x4[x9] for x9 in x8)) for x8 in x6)
        x8 = tuple(sorted(x7, key=lambda obj: (height(obj) * width(obj), size(obj)), reverse=T))
        x9 = frozenset()
        x10 = []
        x11 = T
        for x12 in x8:
            x13 = place_motif_7c66cb00(x12, x5, x9)
            if x13 is None:
                x11 = F
                break
            x14, x15 = x13
            x10.append(x14)
            x9 = combine(x9, x15)
        if not x11:
            continue
        x16 = tuple(sorted(x10, key=lambda obj: (uppermost(obj), leftmost(obj))))
        x17 = render_input_7c66cb00(x0, x2, x16)
        x18 = render_output_7c66cb00(x17, x0, x2, x16)
        x19 = colorcount(cellwise(x17, x18, NEG_ONE), NEG_ONE)
        if either(x19 < 20, x19 > 140):
            continue
        return {"input": x17, "output": x18}
