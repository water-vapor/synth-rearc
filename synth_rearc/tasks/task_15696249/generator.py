from synth_rearc.core import *


COLORS_15696249 = (ONE, TWO, THREE, FOUR, FIVE, SIX)


def _mixed_strip_15696249(length: int, a: int, b: int) -> tuple[int, ...]:
    while True:
        row = tuple(choice((a, b)) for _ in range(length))
        if len(set(row)) == TWO:
            return row


def _stamp_output_15696249(grid: Grid, orient: str, pos: int) -> Grid:
    x0 = canvas(ZERO, (NINE, NINE))
    if orient == "row":
        x1 = hconcat(grid, grid)
        x2 = hconcat(x1, grid)
        x3 = shift(asobject(x2), (THREE * pos, ZERO))
        return paint(x0, x3)
    x1 = vconcat(grid, grid)
    x2 = vconcat(x1, grid)
    x3 = shift(asobject(x2), (ZERO, THREE * pos))
    return paint(x0, x3)


def generate_15696249(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        cue, a, b = sample(COLORS_15696249, THREE)
        orient = choice(("row", "col"))
        pos = randint(ZERO, TWO)
        cells = [[None for _ in range(THREE)] for _ in range(THREE)]
        if orient == "row":
            for j in range(THREE):
                cells[pos][j] = cue
            others = [i for i in range(THREE) if i != pos]
            for i in others:
                strip = _mixed_strip_15696249(THREE, a, b)
                for j, value in enumerate(strip):
                    cells[i][j] = value
        else:
            for i in range(THREE):
                cells[i][pos] = cue
            others = [j for j in range(THREE) if j != pos]
            for j in others:
                strip = _mixed_strip_15696249(THREE, a, b)
                for i, value in enumerate(strip):
                    cells[i][j] = value
        gi = tuple(tuple(row) for row in cells)
        if len(frontiers(gi)) != ONE:
            continue
        go = _stamp_output_15696249(gi, orient, pos)
        return {"input": gi, "output": go}
