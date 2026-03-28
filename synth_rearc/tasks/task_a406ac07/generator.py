from synth_rearc.core import *


GRID_SHAPE_A406AC07 = (TEN, TEN)
RUN_COUNTS_A406AC07 = (FOUR, FIVE)
COLORS_A406AC07 = remove(ZERO, interval(ZERO, TEN, ONE))


def _run_length_options_a406ac07(
    ncolors: Integer,
) -> tuple[tuple[Integer, ...], ...]:
    options = []
    values = range(ONE, FOUR)
    if ncolors == FOUR:
        for a in values:
            for b in values:
                for c in values:
                    for d in range(TWO, FOUR):
                        if a + b + c + d == TEN:
                            options.append((a, b, c, d))
    else:
        for a in values:
            for b in values:
                for c in values:
                    for d in values:
                        for e in range(TWO, FOUR):
                            if a + b + c + d + e == TEN:
                                options.append((a, b, c, d, e))
    return tuple(options)


RUN_LENGTH_OPTIONS_A406AC07 = {
    count: _run_length_options_a406ac07(count)
    for count in RUN_COUNTS_A406AC07
}


def _expand_runs_a406ac07(
    colors: tuple[Integer, ...],
    run_lengths: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    pattern = ()
    for value, run_length in zip(colors, run_lengths):
        pattern = combine(pattern, repeat(value, run_length))
    return pattern


def generate_a406ac07(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    ncolors = unifint(diff_lb, diff_ub, RUN_COUNTS_A406AC07)
    run_lengths = choice(RUN_LENGTH_OPTIONS_A406AC07[ncolors])
    colors = tuple(sample(COLORS_A406AC07, ncolors))
    pattern = _expand_runs_a406ac07(colors, run_lengths)
    gi = canvas(ZERO, GRID_SHAPE_A406AC07)
    x0 = frozenset((value, (NINE, j)) for j, value in enumerate(pattern))
    x1 = frozenset((value, (i, NINE)) for i, value in enumerate(pattern))
    gi = paint(gi, x0)
    gi = paint(gi, x1)
    go = paint(canvas(ZERO, GRID_SHAPE_A406AC07), x1)
    go = paint(go, x0)
    for i, value in enumerate(pattern[:NINE]):
        x2 = frozenset((i, j) for j, other in enumerate(pattern) if other == value)
        go = fill(go, value, x2)
    return {"input": gi, "output": go}
