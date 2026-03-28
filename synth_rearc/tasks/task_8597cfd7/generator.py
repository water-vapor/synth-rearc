from synth_rearc.core import *


WIDTH = NINE
RED_COL = TWO
YELLOW_COL = SIX


def _draw_vbar(grid: Grid, color: Integer, col: Integer, start_row: Integer, length: Integer) -> Grid:
    end_row = start_row + length - ONE
    cells = connect((start_row, col), (end_row, col))
    return fill(grid, color, cells)


def generate_8597cfd7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        section_height = unifint(diff_lb, diff_ub, (FOUR, NINE))
        deltas = sample(interval(ONE, section_height, ONE), TWO)
        red_delta, yellow_delta = deltas
        top_red = unifint(diff_lb, diff_ub, (ONE, section_height - red_delta))
        top_yellow = unifint(diff_lb, diff_ub, (ONE, section_height - yellow_delta))
        bottom_red = top_red + red_delta
        bottom_yellow = top_yellow + yellow_delta

        height = section_height * TWO + ONE
        divider_row = section_height
        gi = canvas(ZERO, (height, WIDTH))
        divider = connect((divider_row, ZERO), (divider_row, WIDTH - ONE))
        gi = fill(gi, FIVE, divider)
        gi = _draw_vbar(gi, TWO, RED_COL, ZERO, top_red)
        gi = _draw_vbar(gi, FOUR, YELLOW_COL, ZERO, top_yellow)
        gi = _draw_vbar(gi, TWO, RED_COL, divider_row + ONE, bottom_red)
        gi = _draw_vbar(gi, FOUR, YELLOW_COL, divider_row + ONE, bottom_yellow)

        winner = TWO if red_delta > yellow_delta else FOUR
        go = canvas(winner, TWO_BY_TWO)
        return {"input": gi, "output": go}
