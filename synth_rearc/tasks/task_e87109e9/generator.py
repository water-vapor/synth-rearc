from synth_rearc.core import *

from .helpers import build_header_e87109e9
from .helpers import rect_patch_e87109e9
from .helpers import render_output_e87109e9
from .helpers import trace_metadata_e87109e9
from .helpers import TURN_CCW_E87109E9
from .helpers import TURN_CW_E87109E9
from .helpers import SEED_COLOR_E87109E9


def _interval_covering_band_e87109e9(
    band_start: Integer,
    band_size: Integer,
    total_width: Integer,
    width_bounds: tuple[Integer, Integer],
) -> tuple[Integer, Integer]:
    x0 = max(width_bounds[0], band_size + TWO)
    x1 = min(width_bounds[1], total_width)
    x2 = randint(x0, x1)
    x3 = max(ZERO, band_start + band_size - x2)
    x4 = min(band_start, total_width - x2)
    x5 = randint(x3, x4)
    return x5, x5 + x2 - ONE


def _random_color_pool_e87109e9(
    background_color: Integer,
) -> tuple[Integer, ...]:
    return tuple(
        x0
        for x0 in interval(ONE, TEN, ONE)
        if x0 not in (background_color, FIVE, SEED_COLOR_E87109E9)
    )


def _turn_for_direction_e87109e9(
    direction_name: str,
    target_direction: str,
) -> str:
    x0 = {
        ("left", "up"): TURN_CW_E87109E9,
        ("left", "down"): TURN_CCW_E87109E9,
        ("right", "up"): TURN_CCW_E87109E9,
        ("right", "down"): TURN_CW_E87109E9,
        ("up", "left"): TURN_CCW_E87109E9,
        ("up", "right"): TURN_CW_E87109E9,
        ("down", "left"): TURN_CW_E87109E9,
        ("down", "right"): TURN_CCW_E87109E9,
    }
    return x0[(direction_name, target_direction)]


def generate_e87109e9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = 24
    while T:
        x1 = unifint(diff_lb, diff_ub, (18, 24))
        x2 = choice((TWO, TWO, THREE))
        x3 = choice((THREE, FOUR, FOUR))
        x4 = tuple(sample(_random_color_pool_e87109e9(x3), FOUR))
        x5 = dict(zip(("up", "right", "down", "left"), x4))
        x6 = choice(("none", "none", "top", "bottom", "left", "right"))
        x7 = randint(max(4, x1 // FOUR), min(x1 - x2 - 6, x1 // TWO))
        x8 = randint(4, x0 - x2 - 6)
        x9 = canvas(x3, (x1, x0))
        x10 = rect_patch_e87109e9(x7, x8, x2, x2)
        x9 = fill(x9, SEED_COLOR_E87109E9, x10)

        x11 = ZERO if x6 == "top" else randint(TWO, FOUR)
        x12 = ZERO if x6 == "bottom" else randint(TWO, FOUR)
        x13 = x11
        x14 = x1 - x12 - ONE
        if x13 > x7 - TWO:
            continue
        if x14 < x7 + x2 + ONE:
            continue

        x15: dict[str, tuple[Integer, Integer, Integer, Integer]] = {}
        x16: dict[Integer, str] = {}

        if x6 != "left":
            x17 = randint(ZERO, min(x8 - TWO, SIX))
            x18 = randint(x13, x7)
            x19 = randint(x7 + x2 - ONE, x14)
            x15["left"] = (x18, ZERO, x19, x17)
            x16[x5["left"]] = choice((TURN_CW_E87109E9, TURN_CCW_E87109E9))
        if x6 != "right":
            x20 = choice((T, F))
            x21 = randint(x8 + x2 + ONE, x0 - THREE)
            x22 = x0 - ONE if x20 else randint(x21 + TWO, x0 - ONE)
            x23 = randint(x13, x7)
            x24 = randint(x7 + x2 - ONE, x14)
            x15["right"] = (x23, x21, x24, x22)
            x16[x5["right"]] = choice((TURN_CW_E87109E9, TURN_CCW_E87109E9))

        x25 = [x8]
        x26 = [x8]
        if "left" in x15:
            x27 = x15["left"][3] + ONE
            x25.append(x27)
            x26.append(x27)
        if "right" in x15:
            x28 = x15["right"][1] - x2
            x25.append(x28)
            x26.append(x28)
        if "left" in x15 and x16[x5["left"]] == TURN_CW_E87109E9:
            x25.append(x15["left"][3] + ONE)
        if "left" in x15 and x16[x5["left"]] == TURN_CCW_E87109E9:
            x26.append(x15["left"][3] + ONE)
        if "right" in x15 and x16[x5["right"]] == TURN_CCW_E87109E9:
            x25.append(x15["right"][1] - x2)
        if "right" in x15 and x16[x5["right"]] == TURN_CW_E87109E9:
            x26.append(x15["right"][1] - x2)

        if x6 != "top":
            x29 = choice(tuple(x25))
            x30 = randint(ZERO, min(x7 - TWO, FOUR))
            x31, x32 = _interval_covering_band_e87109e9(
                x29,
                x2,
                x0,
                (max(x2 + TWO, FOUR), min(x0, 16)),
            )
            x15["up"] = (ZERO, x31, x30, x32)
            x33 = choice(("left", "right"))
            x16[x5["up"]] = _turn_for_direction_e87109e9("up", x33)

        if x6 != "bottom":
            x34 = choice(tuple(x26))
            x35 = randint(max(x7 + x2 + ONE, x1 - FOUR), x1 - THREE)
            x36, x37 = _interval_covering_band_e87109e9(
                x34,
                x2,
                x0,
                (max(x2 + TWO, FOUR), min(x0, 16)),
            )
            x15["down"] = (x35, x36, x1 - ONE, x37)
            x38 = choice(("left", "right"))
            x16[x5["down"]] = _turn_for_direction_e87109e9("down", x38)

        x39 = tuple(x40 for x40 in x4 if x40 not in x16)
        if len(x39) > ONE:
            continue
        if len(x39) == ONE:
            x16[first(x39)] = choice((TURN_CW_E87109E9, TURN_CCW_E87109E9))

        x16 = dict(sample(tuple(x16.items()), len(x16)))

        for x42, (x43, x44, x45, x46) in x15.items():
            x47 = rect_patch_e87109e9(x43, x44, x45 - x43 + ONE, x46 - x44 + ONE)
            x9 = fill(x9, x5[x42], x47)

        if mostcolor(x9) != x3:
            continue
        x48 = frozenset(x49 for x49 in palette(x9) if x49 not in (x3, SEED_COLOR_E87109E9))
        if len(x48) != len(x15):
            continue
        if not all(x49 in x16 for x49 in x48):
            continue

        x49 = build_header_e87109e9(x16)
        x50 = vconcat(x49, x9)
        x51 = render_output_e87109e9(x9, x16)
        x52 = trace_metadata_e87109e9(x9, x16)
        x53 = tuple(x5[x54] for x54 in x15)

        if x52["cycle"]:
            continue
        if len(x52["hit_colors"]) != len(x53):
            continue
        if colorcount(x51, SEED_COLOR_E87109E9) - colorcount(x9, SEED_COLOR_E87109E9) < x2 * SIX:
            continue
        if x50[:SIX] != x49:
            continue
        return {"input": x50, "output": x51}
