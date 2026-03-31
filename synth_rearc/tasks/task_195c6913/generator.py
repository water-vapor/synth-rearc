from synth_rearc.core import *

from .helpers import trace_paths_195c6913
from .verifier import verify_195c6913


MOTIF_PATTERNS_195C6913 = (
    (TWO, THREE),
    (TWO, TWO, THREE),
    (TWO, THREE, FOUR),
    (TWO, THREE, FOUR, FIVE),
    (TWO, TWO, TWO, THREE),
    (TWO, THREE, TWO, FOUR),
)


def _remap_pattern_195c6913(
    pattern: tuple[Integer, ...],
    colors: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    x0 = {base: color_value for base, color_value in zip((TWO, THREE, FOUR, FIVE), colors)}
    return tuple(x0[value] for value in pattern)


def _sample_motif_195c6913(
    palette_values: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    x0 = list(palette_values)
    shuffle(x0)
    x1 = tuple(x0[:FOUR])
    x2 = choice(MOTIF_PATTERNS_195C6913)
    return _remap_pattern_195c6913(x2, x1)


def _step_values_195c6913(
    length: Integer,
    start_value: Integer,
    updates: tuple[tuple[Integer, Integer], ...],
    *,
    lower_bound: Integer,
    upper_bound: Integer,
) -> tuple[Integer, ...]:
    x0 = [start_value for _ in range(length)]
    x1 = start_value
    x2 = ZERO
    x3 = dict(updates)
    while x2 < length:
        if x2 in x3:
            x1 = max(lower_bound, min(upper_bound, x3[x2]))
        x0[x2] = x1
        x2 = increment(x2)
    return tuple(x0)


def _make_band_grid_195c6913(
    dims: IntegerTuple,
    major_a: Integer,
    major_b: Integer,
    left_bounds: tuple[Integer, ...],
    right_bounds: tuple[Integer, ...],
) -> Grid:
    x0, x1 = dims
    x2 = [list(row) for row in canvas(major_a, dims)]
    for x3 in range(x0):
        x4 = left_bounds[x3]
        x5 = right_bounds[x3]
        for x6 in range(x4, add(x5, ONE)):
            x2[x3][x6] = major_b
    return tuple(tuple(row) for row in x2)


def _overlay_input_195c6913(
    base_grid: Grid,
    motif: tuple[Integer, ...],
    corner_color: Integer,
    starts: tuple[IntegerTuple, ...],
    motif_row: Integer,
    corner_ul: IntegerTuple,
) -> Grid:
    x0 = base_grid
    for x1, x2 in enumerate(motif):
        x3 = add(ONE, multiply(THREE, x1))
        x4 = frozenset(
            {
                (motif_row, x3),
                (motif_row, increment(x3)),
                (increment(motif_row), x3),
                (increment(motif_row), increment(x3)),
            }
        )
        x0 = fill(x0, x2, x4)
    for x5 in starts:
        x0 = fill(x0, motif[ZERO], initset(x5))
    x6, x7 = corner_ul
    x8 = frozenset(
        {
            (x6, x7),
            (x6, increment(x7)),
            (increment(x6), x7),
            (increment(x6), increment(x7)),
        }
    )
    x0 = fill(x0, corner_color, x8)
    return x0


def _choose_start_rows_195c6913(
    left_bounds: tuple[Integer, ...],
    right_bounds: tuple[Integer, ...],
) -> tuple[IntegerTuple, ...] | None:
    x0 = [i for i, value in enumerate(left_bounds) if value == ZERO and right_bounds[i] >= TWO]
    x1 = [i for i in x0 if i >= len(left_bounds) // TWO]
    if len(x1) == ZERO:
        return None
    x2 = choice((ONE, TWO, TWO))
    if len(x1) < x2:
        x2 = ONE
    shuffle(x1)
    x3 = []
    for x4 in x1:
        if any(abs(subtract(x4, existing)) <= ONE for existing in x3):
            continue
        x3.append(x4)
        if len(x3) == x2:
            break
    if len(x3) == ZERO:
        return None
    x3 = tuple(sorted(x3))
    return tuple((row, ZERO) for row in x3)


def _sample_boundaries_195c6913(
    n: Integer,
    motif_len: Integer,
) -> tuple[tuple[Integer, ...], tuple[Integer, ...]] | None:
    x0 = add(multiply(THREE, motif_len), TWO)
    if x0 >= subtract(n, FIVE):
        return None
    x1 = randint(x0, subtract(n, FIVE))
    x2 = []
    x3 = x1
    x4 = ZERO
    while x4 < n:
        x5 = randint(TWO, FIVE)
        if x4 > ZERO:
            x3 = max(ZERO, subtract(x3, choice((ZERO, ONE, ONE, TWO, TWO, THREE))))
        x2.append((x4, x3))
        x4 = add(x4, x5)
    x6 = _step_values_195c6913(n, x1, tuple(x2), lower_bound=ZERO, upper_bound=x1)
    x7 = randint(max(add(x0, THREE), n // THREE), subtract(n, TWO))
    x8 = []
    x9 = x7
    x10 = subtract(n, ONE)
    while x10 >= ZERO:
        x11 = randint(TWO, SIX)
        if x10 < subtract(n, ONE):
            x9 = min(subtract(n, ONE), add(x9, choice((ONE, ONE, TWO, TWO, THREE, FOUR))))
        x8.append((max(ZERO, subtract(x10, decrement(x11))), x9))
        x10 = subtract(x10, x11)
    x12 = _step_values_195c6913(n, x7, tuple(sorted(x8)), lower_bound=ZERO, upper_bound=subtract(n, ONE))
    x13 = []
    x14 = []
    for x15, x16 in zip(x6, x12):
        x17 = max(x15, ZERO)
        x18 = min(x16, subtract(n, ONE))
        if x18 < add(x17, TWO):
            x18 = min(subtract(n, ONE), add(x17, TWO))
        if x18 >= n:
            return None
        x13.append(x17)
        x14.append(x18)
    return tuple(x13), tuple(x14)


def generate_195c6913(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((20, 20, 22, 24, 25, 25, 27, 28, 30, 30))
        x1 = tuple(range(TEN))
        x2 = list(x1)
        shuffle(x2)
        x3 = x2.pop()
        x4 = x2.pop()
        x5 = x2.pop()
        x6 = _sample_motif_195c6913(tuple(x2))
        x7 = _sample_boundaries_195c6913(x0, len(x6))
        if x7 is None:
            continue
        x8, x9 = x7
        x10 = _choose_start_rows_195c6913(x8, x9)
        if x10 is None:
            continue
        x11 = _make_band_grid_195c6913((x0, x0), x3, x4, x8, x9)
        x12 = choice((ONE, ONE, TWO))
        if x8[x12] <= add(multiply(THREE, len(x6)), ONE):
            continue
        x13 = [
            row
            for row in range(len(x11) - TWO)
            if add(max(x9[row], x9[add(row, ONE)]), THREE) < x0
        ]
        x14 = [row for row in x13 if row >= len(x11) // THREE]
        if len(x14) == ZERO:
            continue
        x15 = choice(x14)
        x16 = add(max(x9[x15], x9[add(x15, ONE)]), TWO)
        x17 = (x15, x16)
        x18 = _overlay_input_195c6913(x11, x6, x5, x10, x12, x17)
        x19 = trace_paths_195c6913(x11, x6, x5, x10, x4)
        if x18 == x19:
            continue
        if verify_195c6913(x18) != x19:
            continue
        return {"input": x18, "output": x19}
