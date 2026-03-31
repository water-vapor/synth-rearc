from __future__ import annotations

from synth_rearc.core import *

from .helpers import paint_selected_stems_97d7923e
from .helpers import paint_selector_97d7923e
from .helpers import paint_stem_97d7923e
from .verifier import verify_97d7923e


SELECTOR_COLORS_97D7923E = (ONE, TWO, THREE, FOUR)
BODY_COLORS_97D7923E = (FIVE, FIVE, FIVE, SEVEN, SIX, EIGHT, NINE)


def _selector_columns_97d7923e(
    num_colors: Integer,
) -> tuple[Integer, ...]:
    x0 = []
    x1 = ZERO
    for _ in range(num_colors):
        x0.append(x1)
        x1 = add(x1, choice((ONE, ONE, TWO)))
    return tuple(x0)


def _counts_by_color_97d7923e(
    colors: tuple[Integer, ...],
    diff_lb: float,
    diff_ub: float,
) -> dict[Integer, Integer]:
    x0 = {x1: TWO for x1 in colors}
    x2 = unifint(diff_lb, diff_ub, (multiply(TWO, len(colors)), min(EIGHT, multiply(THREE, len(colors)))))
    x3 = subtract(x2, multiply(TWO, len(colors)))
    while positive(x3):
        x4 = tuple(x5 for x5 in colors if x0[x5] < THREE)
        if len(x4) == ZERO:
            break
        x5 = choice(x4)
        x0[x5] = increment(x0[x5])
        x3 = decrement(x3)
    return x0


def _body_color_map_97d7923e(
    colors: tuple[Integer, ...],
) -> dict[Integer, Integer]:
    x0 = tuple(x1 for x1 in BODY_COLORS_97D7923E if x1 not in colors)
    if choice((T, F)):
        x1 = choice(x0)
        return {x2: x1 for x2 in colors}
    return {x3: choice(x0) for x3 in colors}


def _stem_latents_97d7923e(
    colors: tuple[Integer, ...],
    counts_by_color: dict[Integer, Integer],
    body_color_map: dict[Integer, Integer],
) -> tuple[tuple[Integer, Integer, Integer], ...]:
    x0 = []
    for x1 in colors:
        x2 = sorted(sample(tuple(range(THREE, TEN)), counts_by_color[x1]), reverse=True)
        x3 = body_color_map[x1]
        for x4 in x2:
            x0.append((x1, x3, x4))
    shuffle(x0)
    return tuple(sorted(x0, key=lambda x1: invert(x1[TWO])))


def _selector_rank_map_97d7923e(
    colors: tuple[Integer, ...],
    counts_by_color: dict[Integer, Integer],
) -> dict[Integer, Integer]:
    return {x0: randint(ONE, counts_by_color[x0]) for x0 in colors}


def _cluster_specs_97d7923e(
    latents: tuple[tuple[Integer, Integer, Integer], ...],
) -> tuple[tuple[str, tuple[Integer, Integer, Integer], tuple[Integer, Integer, Integer] | None], ...]:
    x0 = list(latents)
    x1 = []
    while len(x0) > ZERO:
        x2 = x0.pop(ZERO)
        x3 = tuple(x4 for x4 in x0 if x4[TWO] < x2[TWO])
        x4 = choice((T, F, F))
        if len(x3) == ZERO or not x4:
            x1.append(("solo", x2, None))
            continue
        x5 = choice(x3)
        x0.remove(x5)
        x6 = choice(("left", "right"))
        x1.append((x6, x2, x5))
    return tuple(x1)


def _render_input_97d7923e(
    selector_colors: tuple[Integer, ...],
    selector_cols: tuple[Integer, ...],
    selector_ranks: dict[Integer, Integer],
    cluster_specs: tuple[tuple[str, tuple[Integer, Integer, Integer], tuple[Integer, Integer, Integer] | None], ...],
) -> Grid | None:
    x0 = add(selector_cols[-ONE], choice((THREE, FOUR, FIVE)))
    x1 = []
    for x2 in cluster_specs:
        x3, x4, x5 = x2
        if x3 == "solo":
            x1.append((x4[ZERO], x4[ONE], x0, subtract(TEN, x4[TWO]), x4[TWO]))
            x0 = add(x0, choice((THREE, FOUR)))
            continue
        if x5 is None:
            return None
        if x3 == "left":
            x6 = x0
            x7 = increment(x0)
            x1.append((x5[ZERO], x5[ONE], x6, subtract(TEN, x5[TWO]), x5[TWO]))
            x1.append((x4[ZERO], x4[ONE], x7, subtract(TEN, x4[TWO]), x4[TWO]))
        else:
            x6 = x0
            x7 = increment(x0)
            x1.append((x4[ZERO], x4[ONE], x6, subtract(TEN, x4[TWO]), x4[TWO]))
            x1.append((x5[ZERO], x5[ONE], x7, subtract(TEN, x5[TWO]), x5[TWO]))
        x0 = add(x0, choice((THREE, FOUR)))
    x8 = max(TEN, subtract(x0, choice((TWO, THREE))))
    if greater(x8, 30):
        return None
    x9 = canvas(ZERO, (TEN, x8))
    x10 = x9
    for x11, x12 in zip(selector_colors, selector_cols):
        x10 = paint_selector_97d7923e(x10, x11, x12, selector_ranks[x11])
    for x13, x14, x15, x16, _ in x1:
        x10 = paint_stem_97d7923e(x10, x13, x14, x15, x16)
    if len(tuple(x17 for x17 in x1 if x17[TWO] == selector_cols[ZERO])) == ZERO and choice((T, F, F)):
        x18 = tuple(x19 for x19 in x1 if greater(x19[THREE], add(selector_ranks[selector_colors[ZERO]], ONE)))
        if len(x18) > ZERO:
            x19 = choice(x18)
            x20 = tuple(x21 for x21 in x1 if x21 != x19)
            x22 = tuple(
                (x23, x24, selector_cols[ZERO] if x25 == x19[TWO] else x25, x26, x27)
                for x23, x24, x25, x26, x27 in x20 + (x19,)
            )
            x10 = canvas(ZERO, (TEN, x8))
            for x11, x12 in zip(selector_colors, selector_cols):
                x10 = paint_selector_97d7923e(x10, x11, x12, selector_ranks[x11])
            for x13, x14, x15, x16, _ in x22:
                x10 = paint_stem_97d7923e(x10, x13, x14, x15, x16)
    return x10


def generate_97d7923e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x1 = tuple(sorted(sample(SELECTOR_COLORS_97D7923E, x0)))
        x2 = _counts_by_color_97d7923e(x1, diff_lb, diff_ub)
        x3 = _selector_rank_map_97d7923e(x1, x2)
        x4 = _body_color_map_97d7923e(x1)
        x5 = _stem_latents_97d7923e(x1, x2, x4)
        x6 = _cluster_specs_97d7923e(x5)
        x7 = _selector_columns_97d7923e(len(x1))
        x8 = _render_input_97d7923e(x1, x7, x3, x6)
        if x8 is None:
            continue
        x9 = paint_selected_stems_97d7923e(x8)
        if verify_97d7923e(x8) != x9:
            continue
        if x8 == x9:
            continue
        return {"input": x8, "output": x9}
