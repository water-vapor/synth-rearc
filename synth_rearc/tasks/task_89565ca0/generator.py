from synth_rearc.core import *

from .helpers import build_shape_spec_89565ca0
from .helpers import can_place_grid_89565ca0
from .helpers import damage_shape_spec_89565ca0
from .helpers import occupied_cells_89565ca0
from .helpers import paint_grid_89565ca0
from .helpers import scatter_noise_89565ca0
from .helpers import translate_rooms_89565ca0
from .verifier import verify_89565ca0


def _sample_counts_89565ca0(
    n_shapes: int,
) -> tuple[int, ...]:
    x0 = randint(max(FOUR, n_shapes), SIX)
    x1 = list(sample(tuple(interval(ONE, x0 + ONE, ONE)), n_shapes))
    if x0 not in x1:
        x1[randint(ZERO, n_shapes - ONE)] = x0
    return tuple(sorted(x1))


def _sample_colors_89565ca0(
    n_shapes: int,
    noise: int,
) -> tuple[int, ...]:
    x0 = tuple(x1 for x1 in interval(ONE, TEN, ONE) if x1 != noise)
    return tuple(sample(x0, n_shapes))


def _place_spec_89565ca0(
    canvas_grid: Grid,
    occupied: frozenset[tuple[int, int]],
    spec: dict[str, object],
    nesting_rooms: list[tuple[int, int, int, int]],
) -> tuple[Grid, frozenset[tuple[int, int]], tuple[int, int], tuple[tuple[int, int, int, int], ...]] | None:
    x0 = spec["grid"]
    x1 = spec["height"]
    x2 = spec["width"]
    x3 = height(canvas_grid)
    x4 = width(canvas_grid)
    if either(x1 > x3, x2 > x4):
        return None
    x5: tuple[int, int] | None = None
    x6 = list(nesting_rooms)
    shuffle(x6)
    if both(len(x6) > ZERO, choice((T, T, F))):
        for x7 in x6:
            x8 = x7[2] - x7[0] + ONE
            x9 = x7[3] - x7[1] + ONE
            if either(x1 > x8, x2 > x9):
                continue
            for _ in range(25):
                x10 = randint(x7[0], x7[2] - x1 + ONE)
                x11 = randint(x7[1], x7[3] - x2 + ONE)
                if can_place_grid_89565ca0(x0, x10, x11, x3, x4, occupied):
                    x5 = (x10, x11)
                    break
            if x5 is not None:
                break
    if x5 is None:
        for _ in range(300):
            x7 = randint(ZERO, x3 - x1)
            x8 = randint(ZERO, x4 - x2)
            if can_place_grid_89565ca0(x0, x7, x8, x3, x4, occupied):
                x5 = (x7, x8)
                break
    if x5 is None:
        return None
    x7 = paint_grid_89565ca0(canvas_grid, x0, x5[0], x5[1])
    x8 = occupied_cells_89565ca0(x7)
    x9 = translate_rooms_89565ca0(spec["rooms"], x5)
    return (x7, x8, x5, x9)


def _latent_output_89565ca0(
    counts_colors: tuple[tuple[int, int], ...],
    noise: int,
) -> Grid:
    x0 = max(x1 for x1, x2 in counts_colors)
    x1 = tuple(sorted(counts_colors))
    return tuple(
        tuple([x3] * x2 + [noise] * (x0 - x2))
        for x2, x3 in x1
    )


def generate_89565ca0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (22, 30))
        x1 = unifint(diff_lb, diff_ub, (22, 30))
        x2 = choice(tuple(interval(ONE, TEN, ONE)))
        x3 = choice((THREE, FOUR, FIVE))
        x4 = _sample_counts_89565ca0(x3)
        x5 = _sample_colors_89565ca0(x3, x2)
        x6 = tuple(sorted(zip(x4, x5), reverse=T))
        x7 = []
        try:
            for x8, x9 in x6:
                x10 = build_shape_spec_89565ca0(x8, x9)
                x11 = damage_shape_spec_89565ca0(x10, x2)
                x7.append(x11)
        except RuntimeError:
            continue
        x8 = canvas(ZERO, (x0, x1))
        x9 = frozenset()
        x10: list[tuple[int, int, int, int]] = []
        x11 = T
        for x12 in sorted(x7, key=lambda x13: (x13["height"] * x13["width"]), reverse=T):
            x13 = _place_spec_89565ca0(x8, x9, x12, x10)
            if x13 is None:
                x11 = F
                break
            x8, x9, x14, x15 = x13
            for x16 in x15:
                x17 = x16[2] - x16[0] + ONE
                x18 = x16[3] - x16[1] + ONE
                if both(x17 >= FOUR, x18 >= FOUR):
                    x10.append(x16)
        if not x11:
            continue
        x12 = randint(max(10, x0 // TWO), max(18, x0 + x1))
        x8, x9 = scatter_noise_89565ca0(x8, x2, x9, x12)
        x13 = tuple((x14["room_count"], x14["color"]) for x14 in x7)
        x14 = _latent_output_89565ca0(x13, x2)
        if verify_89565ca0(x8) != x14:
            continue
        return {"input": x8, "output": x14}
