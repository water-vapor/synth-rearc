from arc2.core import *


PANEL_OPTIONS_5A719D11 = (
    (SEVEN, TWO),
    (EIGHT, ONE),
)

BAND_HEIGHTS_5A719D11 = {
    TWO: EIGHT,
    THREE: SEVEN,
    FOUR: SIX,
}


def _grow_shape_5a719d11(
    dims: IntegerTuple,
    target: Integer,
) -> Indices:
    x0, x1 = dims
    x2 = tuple((x3, x4) for x3 in range(ONE, x0 - ONE) for x4 in range(ONE, x1 - ONE))
    x3 = choice(x2)
    x4 = {x3}
    while len(x4) < target:
        x5 = []
        for x6, x7 in x4:
            for x8, x9 in ((NEG_ONE, ZERO), (ONE, ZERO), (ZERO, NEG_ONE), (ZERO, ONE)):
                x10 = (x6 + x8, x7 + x9)
                if ONE <= x10[0] < x0 - ONE and ONE <= x10[1] < x1 - ONE and x10 not in x4:
                    x5.append(x10)
        if len(x5) == ZERO:
            break
        x4.add(choice(x5))
    return frozenset(x4)


def _sample_shape_5a719d11(
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    x2 = multiply(subtract(x0, TWO), subtract(x1, TWO))
    x3 = min(NINE, subtract(x2, ONE))
    x4 = max(FOUR, subtract(x3, randint(ZERO, TWO)))
    return _grow_shape_5a719d11(dims, x4)


def _paint_panel_5a719d11(
    bg: Integer,
    fg: Integer,
    dims: IntegerTuple,
    patch: Indices,
) -> Grid:
    x0 = canvas(bg, dims)
    return fill(x0, fg, patch)


def _assemble_row_5a719d11(
    left: Grid,
    right: Grid,
    gap_width: Integer,
) -> Grid:
    x0 = canvas(ZERO, (height(left), gap_width))
    x1 = hconcat(left, x0)
    return hconcat(x1, right)


def generate_5a719d11(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ONE, TEN, ONE)
    while True:
        x1 = choice((TWO, TWO, THREE, FOUR))
        x2 = choice(PANEL_OPTIONS_5A719D11)
        x3, x4 = x2
        x7 = BAND_HEIGHTS_5A719D11[x1]
        x8 = add(multiply(TWO, x3), x4)
        x10 = []
        x11 = []
        x12 = F
        for _ in range(x1):
            x13 = choice(x0)
            x14 = choice((F, F, T))
            x15 = x13 if x14 else choice(remove(x13, x0))
            x16 = choice(remove(x13, x0))
            x17 = choice(remove(x15, x0))
            x18 = _sample_shape_5a719d11((x7, x3))
            x19 = _sample_shape_5a719d11((x7, x3))
            x20 = _paint_panel_5a719d11(x13, x16, (x7, x3), x18)
            x21 = _paint_panel_5a719d11(x15, x17, (x7, x3), x19)
            x22 = _paint_panel_5a719d11(x13, x15, (x7, x3), x19)
            x23 = _paint_panel_5a719d11(x15, x13, (x7, x3), x18)
            x10.append(_assemble_row_5a719d11(x20, x21, x4))
            x11.append(_assemble_row_5a719d11(x22, x23, x4))
            if x13 != x15:
                x12 = T
        if flip(x12):
            continue
        x24 = x10[0]
        x25 = x11[0]
        x26 = canvas(ZERO, (TWO, x8))
        for x27 in range(ONE, x1):
            x24 = vconcat(x24, x26)
            x24 = vconcat(x24, x10[x27])
            x25 = vconcat(x25, x26)
            x25 = vconcat(x25, x11[x27])
        if equality(x24, x25):
            continue
        from .verifier import verify_5a719d11

        if verify_5a719d11(x24) != x25:
            continue
        return {"input": x24, "output": x25}
