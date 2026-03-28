from synth_rearc.core import *
from .verifier import verify_29700607


def _render_29700607(
    n: int,
    start: int,
    colors: tuple[int, int, int],
    targets: dict[int, IntegerTuple],
) -> tuple[Grid, Grid]:
    x0 = canvas(ZERO, (n, n))
    x1 = x0
    for x2, x3 in enumerate(colors):
        x4 = start + x2
        x5 = astuple(ZERO, x4)
        x0 = fill(x0, x3, frozenset({x5}))
        x6 = targets.get(x2)
        if x6 is not None:
            x0 = fill(x0, x3, frozenset({x6}))
        x7 = branch(x6 is None, astuple(decrement(n), x4), x6)
        x8 = astuple(first(x7), x4)
        x9 = connect(x5, x8)
        x10 = connect(x8, x7)
        x1 = fill(x1, x3, combine(x9, x10))
    return x0, x1


def generate_29700607(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        n = unifint(diff_lb, diff_ub, (11, 15))
        start = n // 3
        colors = tuple(sample(tuple(range(1, 10)), 3))
        mode = choice(("LLR", "LLR", "LRR", "LRR", "L_M_R"))
        if mode == "LLR":
            x0 = randint(2, n - 4)
            x1 = randint(x0 + 1, n - 2)
            x2 = randint(2, n - 2)
            targets = {
                0: astuple(x0, ZERO),
                1: astuple(x1, ZERO),
                2: astuple(x2, decrement(n)),
            }
        elif mode == "LRR":
            x0 = randint(2, n - 2)
            x1 = randint(2, n - 3)
            x2 = randint(x1 + 1, n - 2)
            targets = {
                0: astuple(x0, ZERO),
                1: astuple(x2, decrement(n)),
                2: astuple(x1, decrement(n)),
            }
        else:
            x0 = randint(2, n - 2)
            x1 = randint(2, n - 2)
            targets = {
                0: astuple(x0, ZERO),
                2: astuple(x1, decrement(n)),
            }
        gi, go = _render_29700607(n, start, colors, targets)
        if verify_29700607(gi) != go:
            continue
        return {"input": gi, "output": go}
