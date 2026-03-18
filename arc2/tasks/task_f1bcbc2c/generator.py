from arc2.core import *

from .helpers import GRID_SHAPE_F1BCBC2C, polyline_f1bcbc2c, walls_from_path_f1bcbc2c


def _sample_one_turn_bottom_f1bcbc2c(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, int], ...]:
    x0 = unifint(diff_lb, diff_ub, (ONE, SIX))
    x1 = unifint(diff_lb, diff_ub, (x0 + TWO, EIGHT))
    x2 = unifint(diff_lb, diff_ub, (TWO, SEVEN))
    return ((ZERO, x0), (x2, x0), (x2, x1), (NINE, x1))


def _sample_two_turn_side_f1bcbc2c(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, int], ...]:
    x0 = unifint(diff_lb, diff_ub, (ONE, FIVE))
    x1 = unifint(diff_lb, diff_ub, (x0 + TWO, SEVEN))
    x2 = unifint(diff_lb, diff_ub, (TWO, FOUR))
    x3 = unifint(diff_lb, diff_ub, (x2 + TWO, EIGHT))
    return ((ZERO, x0), (x2, x0), (x2, x1), (x3, x1), (x3, NINE))


def _sample_two_turn_bottom_f1bcbc2c(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, int], ...]:
    x0 = unifint(diff_lb, diff_ub, (ONE, FOUR))
    x1 = unifint(diff_lb, diff_ub, (x0 + TWO, SIX))
    x2 = unifint(diff_lb, diff_ub, (x1 + TWO, EIGHT))
    x3 = unifint(diff_lb, diff_ub, (TWO, FOUR))
    x4 = unifint(diff_lb, diff_ub, (x3 + TWO, SEVEN))
    return ((ZERO, x0), (x3, x0), (x3, x1), (x4, x1), (x4, x2), (NINE, x2))


def _vertical_straights_f1bcbc2c(
    path: tuple[tuple[int, int], ...],
) -> tuple[tuple[int, int], ...]:
    x0 = []
    for idx in range(ONE, len(path) - ONE):
        x1 = path[idx - ONE]
        x2 = path[idx]
        x3 = path[idx + ONE]
        if x1[1] == x2[1] == x3[1]:
            x0.append(x2)
    return tuple(x0)


def _build_full_example_f1bcbc2c(
    path: tuple[tuple[int, int], ...],
    marker: tuple[int, int] | None,
) -> dict:
    x0 = walls_from_path_f1bcbc2c(path)
    x1 = canvas(ZERO, GRID_SHAPE_F1BCBC2C)
    x2 = fill(x1, SEVEN, x0)
    if marker is not None:
        x2 = fill(x2, NINE, frozenset({marker}))
    x3 = fill(x2, EIGHT, frozenset(path))
    return {"input": x2, "output": x3}


def _build_corner_example_f1bcbc2c(
    path: tuple[tuple[int, int], ...],
    marker: tuple[int, int],
) -> dict:
    x0 = walls_from_path_f1bcbc2c(path)
    x1 = path.index(marker)
    x2 = frozenset(path[:x1])
    x3 = canvas(ZERO, GRID_SHAPE_F1BCBC2C)
    x4 = fill(x3, SEVEN, x0)
    x5 = fill(x4, NINE, frozenset({marker}))
    x6 = fill(x5, EIGHT, x2)
    return {"input": x5, "output": x6}


def generate_f1bcbc2c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("plain", "plain", "straight", "straight", "corner", "side"))
        if x0 == "side":
            x1 = _sample_two_turn_side_f1bcbc2c(diff_lb, diff_ub)
        elif x0 == "corner":
            x1 = _sample_two_turn_bottom_f1bcbc2c(diff_lb, diff_ub)
        else:
            x1 = choice((
                _sample_one_turn_bottom_f1bcbc2c(diff_lb, diff_ub),
                _sample_two_turn_bottom_f1bcbc2c(diff_lb, diff_ub),
            ))
        x2 = polyline_f1bcbc2c(x1)
        x3 = walls_from_path_f1bcbc2c(x2)
        x4 = set(x2) | set(x3)
        if any(i < ZERO or i >= TEN or j < ZERO or j >= TEN for i, j in x4):
            continue
        if len(intersection(frozenset(x2), x3)) > ZERO:
            continue
        if x0 == "plain":
            x5 = _build_full_example_f1bcbc2c(x2, None)
        elif x0 == "straight":
            x5 = _vertical_straights_f1bcbc2c(x2)
            if len(x5) == ZERO:
                continue
            x6 = choice(x5)
            x5 = _build_full_example_f1bcbc2c(x2, x6)
        elif x0 == "corner":
            x6 = x1[THREE]
            x5 = _build_corner_example_f1bcbc2c(x2, x6)
        else:
            x5 = _build_full_example_f1bcbc2c(x2, None)
        if x0 in ("plain", "straight", "corner") and choice((T, F)):
            x5 = {
                "input": vmirror(x5["input"]),
                "output": vmirror(x5["output"]),
            }
        if x5["input"] == x5["output"]:
            continue
        return x5
