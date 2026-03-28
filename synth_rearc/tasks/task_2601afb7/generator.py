from synth_rearc.core import *


COLOR_POOL = remove(SEVEN, interval(ZERO, TEN, ONE))


def _render_bars(
    dim: int,
    tops: tuple[int, ...],
    colors: tuple[int, ...],
) -> Grid:
    x0 = tuple(range(ONE, dim, TWO))
    x1 = decrement(dim)
    x2 = pair(tops, x0)
    x3 = pair(repeat(x1, len(x0)), x0)
    x4 = papply(connect, x2, x3)
    x5 = mpapply(recolor, colors, x4)
    x6 = canvas(SEVEN, (dim, dim))
    x7 = paint(x6, x5)
    return x7


def generate_2601afb7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        nbars = unifint(diff_lb, diff_ub, (THREE, FIVE))
        dim = 2 * nbars + ONE
        tops = tuple(randint(ONE, dim - ONE) for _ in range(nbars))
        if len(set(tops)) == ONE:
            continue
        if min(tops) > THREE:
            continue
        if max(tops) < dim - THREE:
            continue
        colors = tuple(sample(COLOR_POOL, nbars))
        gi = _render_bars(dim, tops, colors)
        x0 = tops[ONE:] + tops[:ONE]
        x1 = colors[-ONE:] + colors[:-ONE]
        go = _render_bars(dim, x0, x1)
        return {"input": gi, "output": go}
