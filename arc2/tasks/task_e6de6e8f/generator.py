from arc2.core import *

from .helpers import (
    marker_color_e6de6e8f,
    render_input_e6de6e8f,
    render_output_e6de6e8f,
)


def _candidate_steps_e6de6e8f() -> Tuple:
    positions = interval(ZERO, FIVE, ONE)
    choices = []
    for zero_positions in product(positions, positions):
        if zero_positions[ZERO] >= zero_positions[ONE]:
            continue
        signed_positions = tuple(pos for pos in positions if pos not in zero_positions)
        for signs in product((NEG_ONE, ONE), (NEG_ONE, ONE)):
            for last_sign in (NEG_ONE, ONE):
                sequence = []
                sign_values = signs + (last_sign,)
                sign_index = ZERO
                for pos in positions:
                    if pos in zero_positions:
                        sequence.append(ZERO)
                        continue
                    sequence.append(sign_values[sign_index])
                    sign_index += ONE
                choices.append(tuple(sequence))
    return tuple(choices)


CANDIDATE_STEPS_E6DE6E8F = _candidate_steps_e6de6e8f()


def generate_e6de6e8f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    colors = interval(ZERO, TEN, ONE)
    while True:
        bg_color = choice(colors)
        path_color = choice(remove(bg_color, colors))
        marker_color = marker_color_e6de6e8f(path_color, bg_color)
        steps = choice(CANDIDATE_STEPS_E6DE6E8F)
        gi = render_input_e6de6e8f(steps, bg_color, path_color)
        walk = [THREE]
        for step in steps:
            walk.append(walk[-ONE] + step)
            if step == ZERO:
                walk.append(walk[-ONE])
        go = render_output_e6de6e8f(tuple(walk[:EIGHT]), bg_color, path_color, marker_color)
        if gi == go:
            continue
        return {"input": gi, "output": go}
