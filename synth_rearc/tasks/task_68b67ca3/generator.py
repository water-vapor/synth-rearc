from synth_rearc.core import *


_COLORS_68B67CA3 = interval(ONE, TEN, ONE)
_LOCS_68B67CA3 = tuple((i, j) for i in range(THREE) for j in range(THREE))


def _covered_68b67ca3(locs: tuple[tuple[int, int], ...]) -> Boolean:
    rows = {i for i, _ in locs}
    cols = {j for _, j in locs}
    return len(rows) == THREE and len(cols) == THREE


def _color_sequence_68b67ca3(ncells: Integer, ncolors: Integer) -> tuple[Integer, ...]:
    cols = list(sample(_COLORS_68B67CA3, ncolors))
    vals = cols[:]
    while len(vals) < ncells:
        vals.append(choice(cols))
    shuffle(vals)
    return tuple(vals)


def generate_68b67ca3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        x1 = tuple(sample(_LOCS_68B67CA3, x0))
        if not _covered_68b67ca3(x1):
            continue
        x2 = min(FOUR, x0 - ONE)
        x3 = unifint(diff_lb, diff_ub, (THREE, x2))
        x4 = _color_sequence_68b67ca3(x0, x3)
        go = canvas(ZERO, (THREE, THREE))
        gi = canvas(ZERO, (SIX, SIX))
        for x5, x6 in zip(x1, x4):
            go = fill(go, x6, initset(x5))
            x7, x8 = x5
            x9 = astuple(double(x7), double(x8))
            gi = fill(gi, x6, initset(x9))
        return {"input": gi, "output": go}
