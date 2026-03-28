from synth_rearc.core import *


OUTPUT_SIDE = 16
INPUT_SIDE_OPTIONS = (15, 16, 16)
INPUT_COLOR_OPTIONS = tuple(color for color in range(10) if color != SEVEN)
HEIGHT_BOUNDS = (5, 12)
WIDTH_UPPER = 14


def _make_output(height: int, width: int) -> Grid:
    go = canvas(SEVEN, (OUTPUT_SIDE, OUTPUT_SIDE))
    rows = interval(OUTPUT_SIDE - height, OUTPUT_SIDE, ONE)
    cols = interval(ZERO, width, ONE)
    go = fill(go, TWO, product(rows, cols))
    for offset in range(height):
        row = OUTPUT_SIDE - 1 - offset
        col = min(offset, width - 1 - offset)
        go = fill(go, FOUR, ((row, col), (row, width - 1 - col)))
    return go


def generate_878187ab(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    side = choice(INPUT_SIDE_OPTIONS)
    height = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS)
    width_lb = max(height + 1, 7)
    width = unifint(diff_lb, diff_ub, (width_lb, WIDTH_UPPER))
    colors = sample(INPUT_COLOR_OPTIONS, 2)
    counts = [height, width]
    shuffle(counts)

    all_locs = [(i, j) for i in range(side) for j in range(side)]
    chosen_locs = sample(all_locs, sum(counts))
    split = counts[0]
    loc_groups = (chosen_locs[:split], chosen_locs[split:])

    gi = canvas(SEVEN, (side, side))
    for color, locs in zip(colors, loc_groups):
        gi = fill(gi, color, tuple(locs))

    go = _make_output(height, width)
    return {"input": gi, "output": go}
