from synth_rearc.core import *


LAYOUTS_8A371977 = tuple(
    sorted(
        (
            side,
            nrows,
            ncols,
            block_height,
            block_width,
            row_separator,
            col_separator,
            top_border,
            bottom_border,
            left_border,
            right_border,
        )
        for nrows in range(THREE, 12)
        for ncols in range(THREE, 12)
        for block_height in range(ONE, SIX)
        for block_width in range(ONE, SIX)
        for row_separator in (ONE, TWO)
        for col_separator in (ONE, TWO)
        for top_border in (ONE, TWO)
        for bottom_border in (ONE, TWO)
        for left_border in (ONE, TWO)
        for right_border in (ONE, TWO)
        for side in (
            add(add(top_border, bottom_border), add(multiply(nrows, block_height), multiply(decrement(nrows), row_separator))),
        )
        if 19 <= side <= 30
        if side == add(add(left_border, right_border), add(multiply(ncols, block_width), multiply(decrement(ncols), col_separator)))
    )
)


def _block_patch_8a371977(
    start: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    top, left = start
    height0, width0 = dims
    rows = interval(top, add(top, height0), ONE)
    cols = interval(left, add(left, width0), ONE)
    return product(rows, cols)


def generate_8a371977(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = len(LAYOUTS_8A371977)
    x1 = decrement(x0)
    x2 = unifint(diff_lb, diff_ub, (ZERO, x1))
    x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13 = LAYOUTS_8A371977[x2]
    x14 = canvas(ONE, (x3, x3))
    x15 = add(x6, x8)
    x16 = add(x7, x9)
    x17 = interval(ZERO, x4, ONE)
    x18 = interval(ZERO, x5, ONE)
    x19 = lbind(multiply, x15)
    x20 = lbind(multiply, x16)
    x21 = apply(x19, x17)
    x22 = apply(x20, x18)
    x23 = lbind(add, x10)
    x24 = lbind(add, x12)
    x25 = apply(x23, x21)
    x26 = apply(x24, x22)
    x27 = product(x25, x26)
    x28 = rbind(_block_patch_8a371977, (x6, x7))
    x29 = mapply(x28, x27)
    x30 = fill(x14, ZERO, x29)
    x31 = first(x25)
    x32 = last(x25)
    x33 = first(x26)
    x34 = last(x26)
    x35 = matcher(first, x31)
    x36 = matcher(first, x32)
    x37 = matcher(last, x33)
    x38 = matcher(last, x34)
    x39 = fork(either, x35, x36)
    x40 = fork(either, x37, x38)
    x41 = fork(either, x39, x40)
    x42 = sfilter(x27, x41)
    x43 = compose(flip, x41)
    x44 = sfilter(x27, x43)
    x45 = mapply(x28, x42)
    x46 = mapply(x28, x44)
    x47 = fill(x30, TWO, x45)
    x48 = fill(x47, THREE, x46)
    from .verifier import verify_8a371977

    if verify_8a371977(x30) != x48:
        raise ValueError("generator produced an invalid example")
    return {"input": x30, "output": x48}
