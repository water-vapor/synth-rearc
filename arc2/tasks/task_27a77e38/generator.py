from arc2.core import *

from .verifier import verify_27a77e38


HALF_HEIGHT_BOUNDS_27a77e38 = (ONE, SIX)
PALETTE_BONUS_BOUNDS_27a77e38 = (ONE, FOUR)
NON_SPECIAL_COLORS_27a77e38 = remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE)))
DOMINANT_WEIGHT_27a77e38 = FOUR
OTHER_WEIGHT_CHOICES_27a77e38 = (ONE, TWO, TWO, THREE)


def generate_27a77e38(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        half_height = unifint(diff_lb, diff_ub, HALF_HEIGHT_BOUNDS_27a77e38)
        side_length = increment(double(half_height))
        top_cell_count = multiply(half_height, side_length)
        palette_size = unifint(
            diff_lb,
            diff_ub,
            (
                TWO,
                min(
                    EIGHT,
                    decrement(top_cell_count),
                    add(half_height, unifint(diff_lb, diff_ub, PALETTE_BONUS_BOUNDS_27a77e38)),
                ),
            ),
        )
        palette_values = sample(NON_SPECIAL_COLORS_27a77e38, palette_size)
        dominant_color = choice(palette_values)
        other_colors = tuple(value for value in palette_values if value != dominant_color)
        bag = [dominant_color] * DOMINANT_WEIGHT_27a77e38
        for value in other_colors:
            bag.extend([value] * choice(OTHER_WEIGHT_CHOICES_27a77e38))
        while True:
            top_values = [choice(bag) for _ in range(top_cell_count)]
            if any(top_values.count(value) == ZERO for value in palette_values):
                continue
            dominant_count = top_values.count(dominant_color)
            if dominant_count >= top_cell_count:
                continue
            if dominant_count <= max(top_values.count(value) for value in other_colors):
                continue
            break
        shuffle(top_values)
        gi = canvas(ZERO, (side_length, side_length))
        separator = frozenset((half_height, j) for j in range(side_length))
        gi = fill(gi, FIVE, separator)
        top_cells = tuple((i, j) for i in range(half_height) for j in range(side_length))
        top_object = frozenset((value, cell) for value, cell in zip(top_values, top_cells))
        gi = paint(gi, top_object)
        output_cell = astuple(decrement(side_length), halve(side_length))
        go = fill(gi, dominant_color, initset(output_cell))
        if verify_27a77e38(gi) != go:
            continue
        return {"input": gi, "output": go}
