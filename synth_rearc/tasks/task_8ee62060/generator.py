from synth_rearc.core import *

from .verifier import verify_8ee62060


_MOTIFS_8EE62060 = (
    (
        (ONE, ONE),
        (TWO, ONE),
    ),
    (
        (TWO, ZERO),
        (ONE, ONE),
    ),
    (
        (ONE, TWO),
        (TWO, ZERO),
    ),
    (
        (ONE, TWO),
        (TWO, ONE),
    ),
)


def _render_bands_8ee62060(
    bands: Integer,
    motif: tuple[tuple[Integer, Integer], tuple[Integer, Integer]],
    colors: tuple[Integer, Integer],
    descending: Boolean,
) -> Grid:
    x0 = multiply(TWO, bands)
    x1 = canvas(ZERO, astuple(x0, x0))
    x2, x3 = colors
    x4 = {ONE: x2, TWO: x3}
    x5 = x1
    for x6 in range(bands):
        x7 = multiply(TWO, x6)
        x8 = branch(descending, subtract(subtract(x0, TWO), x7), x7)
        for x9 in range(TWO):
            for x10 in range(TWO):
                x11 = motif[x9][x10]
                if equality(x11, ZERO):
                    continue
                x12 = astuple(add(x7, x9), add(x8, x10))
                x5 = fill(x5, x4[x11], initset(x12))
    return x5


def generate_8ee62060(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FIVE, SEVEN))
        x1 = choice((T, F))
        x2 = choice(_MOTIFS_8EE62060)
        x3 = choice(tuple(range(ONE, TEN)))
        x4 = choice(tuple(x5 for x5 in range(ONE, TEN) if x5 != x3))
        x6 = _render_bands_8ee62060(x0, x2, (x3, x4), x1)
        x7 = _render_bands_8ee62060(x0, x2, (x3, x4), flip(x1))
        if equality(x6, x7):
            continue
        if verify_8ee62060(x6) != x7:
            continue
        return {"input": x6, "output": x7}
