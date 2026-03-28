from synth_rearc.core import *


PANEL_SHAPE_D47AA2FF = (TEN, TEN)
DIVIDER_SHAPE_D47AA2FF = (TEN, ONE)
PANEL_COLORS_D47AA2FF = (THREE, FOUR, SIX, SEVEN, EIGHT, NINE)
PANEL_LOCS_D47AA2FF = tuple((i, j) for i in range(TEN) for j in range(TEN))


def _well_spaced_d47aa2ff(
    loc: tuple[int, int],
    others: tuple[tuple[int, int], ...] | list[tuple[int, int]],
) -> bool:
    return all(max(abs(loc[0] - i), abs(loc[1] - j)) > ONE for i, j in others)


def _sample_sparse_positions_d47aa2ff(
    count: Integer,
    blocked: tuple[tuple[int, int], ...] = (),
    forbidden: tuple[tuple[int, int], ...] = (),
) -> tuple[tuple[int, int], ...] | None:
    x0 = set(forbidden)
    x1 = list(PANEL_LOCS_D47AA2FF)
    shuffle(x1)
    x2 = []
    for x3 in x1:
        if x3 in x0:
            continue
        if not _well_spaced_d47aa2ff(x3, blocked):
            continue
        if not _well_spaced_d47aa2ff(x3, x2):
            continue
        x2.append(x3)
        if len(x2) == count:
            return tuple(x2)
    return None


def _paint_points_d47aa2ff(
    grid: Grid,
    points: tuple[tuple[Integer, tuple[int, int]], ...],
) -> Grid:
    x0 = grid
    for x1, x2 in points:
        x0 = fill(x0, x1, initset(x2))
    return x0


def _spread_enough_d47aa2ff(locs: tuple[tuple[int, int], ...]) -> bool:
    x0 = {i for i, _ in locs}
    x1 = {j for _, j in locs}
    return len(x0) >= FOUR and len(x1) >= FOUR


def generate_d47aa2ff(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((TWO, THREE, THREE))
        x1 = tuple(sample(PANEL_COLORS_D47AA2FF, x0))
        x2 = unifint(diff_lb, diff_ub, (SIX, EIGHT))
        x3 = choice((ONE, TWO, TWO))
        x4 = _sample_sparse_positions_d47aa2ff(x2)
        if x4 is None:
            continue
        x5 = _sample_sparse_positions_d47aa2ff(x3, blocked=x4)
        if x5 is None:
            continue
        x6 = _sample_sparse_positions_d47aa2ff(x3, blocked=x4, forbidden=x5)
        if x6 is None:
            continue
        x7 = x4 + x5
        x8 = x4 + x6
        if not _spread_enough_d47aa2ff(x7):
            continue
        if not _spread_enough_d47aa2ff(x8):
            continue
        x9 = list(x1)
        x9.extend(choice(x1) for _ in range(x2 - x0))
        shuffle(x9)
        x10 = tuple((x11, x12) for x11, x12 in zip(x9, x4))
        x13 = tuple((choice(x1), x14) for x14 in x5)
        x15 = tuple((choice(x1), x16) for x16 in x6)
        x17 = canvas(ZERO, PANEL_SHAPE_D47AA2FF)
        x18 = _paint_points_d47aa2ff(x17, x10 + x13)
        x19 = _paint_points_d47aa2ff(x17, x10 + x15)
        x20 = canvas(ZERO, PANEL_SHAPE_D47AA2FF)
        x21 = _paint_points_d47aa2ff(x20, x10)
        x22 = _paint_points_d47aa2ff(x21, tuple((ONE, x23) for _, x23 in x15))
        go = _paint_points_d47aa2ff(x22, tuple((TWO, x24) for _, x24 in x13))
        x25 = canvas(FIVE, DIVIDER_SHAPE_D47AA2FF)
        gi = hconcat(hconcat(x18, x25), x19)
        return {"input": gi, "output": go}
