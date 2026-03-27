from arc2.core import *


MAX_SIDE_332EFDB3 = 30
_DIMS_332EFDB3 = ()
_DIMS_IDX_332EFDB3 = ZERO


def _render_332efdb3(dims: IntegerTuple) -> Grid:
    x0 = canvas(ONE, dims)
    x1 = interval(ONE, dims[ZERO], TWO)
    x2 = interval(ONE, dims[ONE], TWO)
    x3 = product(x1, x2)
    x4 = fill(x0, ZERO, x3)
    return x4


def _dims_key_332efdb3(dims: IntegerTuple) -> tuple[int, int, int, int, int]:
    h, w = dims
    odd_pair = both(h % TWO == ONE, w % TWO == ONE)
    big_pair = both(h >= FIVE, w >= FIVE)
    square_pair = h == w
    rank = branch(
        both(odd_pair, big_pair),
        branch(square_pair, ZERO, ONE),
        branch(odd_pair, TWO, THREE),
    )
    return (rank, abs(subtract(h, w)), -min(h, w), -max(h, w), h)


def _next_dims_332efdb3() -> IntegerTuple:
    global _DIMS_332EFDB3
    global _DIMS_IDX_332EFDB3
    if len(_DIMS_332EFDB3) == ZERO:
        x0 = tuple((i, j) for i in range(ONE, increment(MAX_SIDE_332EFDB3)) for j in range(ONE, increment(MAX_SIDE_332EFDB3)))
        _DIMS_332EFDB3 = tuple(sorted(x0, key=_dims_key_332efdb3))
    x1 = _DIMS_332EFDB3[_DIMS_IDX_332EFDB3 % len(_DIMS_332EFDB3)]
    _DIMS_IDX_332EFDB3 = increment(_DIMS_IDX_332EFDB3)
    return x1


def generate_332efdb3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = _next_dims_332efdb3()
    gi = canvas(ZERO, x0)
    go = _render_332efdb3(x0)
    return {"input": gi, "output": go}
