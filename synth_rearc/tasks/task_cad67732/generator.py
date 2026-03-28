from synth_rearc.core import *


NONZERO_COLORS_CAD67732 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _period_cad67732(
    grid: Grid,
) -> Integer:
    height_ = len(grid)
    width_ = len(grid[0])
    cells = tuple(
        (i, j, value)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value != ZERO
    )
    for step in range(ONE, height_):
        seen = False
        valid = True
        for i, j, value in cells:
            a = i + step
            b = j + step
            if a < height_ and b < width_:
                seen = True
                if grid[a][b] != value:
                    valid = False
                    break
        if valid and seen:
            return step
    return height_


def _render_main_cad67732(
    base: Object,
    step: Integer,
    dims: IntegerTuple,
) -> Grid:
    grid = canvas(ZERO, dims)
    limit = max(dims) + max(height(base), width(base))
    offset = astuple(step, step)
    for k in range(limit):
        grid = paint(grid, shift(base, multiply(k, offset)))
    return grid


def _sample_base_cad67732(
    step: Integer,
    overlap: Integer,
) -> Object:
    size_ = step + overlap
    while True:
        radius = ONE if overlap == ONE else choice((ZERO, ONE)) if size_ > TWO else choice((ZERO, ZERO, ONE))
        allowed = tuple(
            (i, j)
            for i in range(size_)
            for j in range(size_)
            if abs(i - j) <= radius and not (overlap == ONE and i == step and j == step)
        )
        allowed_by_row = {
            i: tuple(cell for cell in allowed if cell[0] == i)
            for i in range(size_)
        }
        allowed_by_col = {
            j: tuple(cell for cell in allowed if cell[1] == j)
            for j in range(size_)
        }
        if any(len(options) == ZERO for options in allowed_by_row.values()):
            continue
        if any(len(options) == ZERO for options in allowed_by_col.values()):
            continue
        chosen = {(ZERO, ZERO)}
        density = choice((0.45, 0.55, 0.65, 0.75))
        for cell in allowed:
            if cell == (ZERO, ZERO):
                continue
            if uniform(0.0, 1.0) < density:
                chosen.add(cell)
        for i in range(size_):
            if not any(cell in chosen for cell in allowed_by_row[i]):
                chosen.add(choice(allowed_by_row[i]))
        for j in range(size_):
            if not any(cell in chosen for cell in allowed_by_col[j]):
                chosen.add(choice(allowed_by_col[j]))
        if len(chosen) > ONE:
            break
    npalette = randint(TWO, min(FOUR, len(chosen)))
    palette_ = sample(NONZERO_COLORS_CAD67732, npalette)
    chosen = list(chosen)
    shuffle(chosen)
    colors = [choice(palette_) for _ in chosen]
    if len(set(colors)) == ONE and len(palette_) > ONE and len(colors) > ONE:
        colors[0] = palette_[0]
        colors[1] = palette_[1]
    return frozenset((colors[idx], cell) for idx, cell in enumerate(chosen))


def generate_cad67732(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        step = unifint(diff_lb, diff_ub, (TWO, FOUR))
        overlap = choice((ZERO, ONE))
        size_ = step + overlap
        max_copies = ONE + (15 - size_) // step
        if max_copies < TWO:
            continue
        ncopies = randint(TWO, max_copies)
        tail = randint(ONE, size_)
        side = step * decrement(ncopies) + tail
        if side < max(FIVE, size_):
            continue
        base = _sample_base_cad67732(step, overlap)
        input_ = _render_main_cad67732(base, step, (side, side))
        if _period_cad67732(input_) != step:
            continue
        output = _render_main_cad67732(base, step, double(shape(input_)))
        if choice((False, True)):
            input_ = vmirror(input_)
            output = vmirror(output)
        return {"input": input_, "output": output}
