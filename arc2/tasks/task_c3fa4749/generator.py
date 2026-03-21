from arc2.core import *

from .verifier import verify_c3fa4749


def _neighbors_c3fa4749(
    cell,
    height: Integer,
    width: Integer,
):
    i, j = cell
    out = []
    for ni, nj in ((i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE)):
        if ZERO <= ni < height and ZERO <= nj < width:
            out.append((ni, nj))
    return tuple(out)


def _border_cells_c3fa4749(
    cells,
    height: Integer,
    width: Integer,
):
    return frozenset(
        cell for cell in cells
        if cell[ZERO] in (ZERO, height - ONE) or cell[ONE] in (ZERO, width - ONE)
    )


def _connected_c3fa4749(
    cells,
    height: Integer,
    width: Integer,
):
    if len(cells) == ZERO:
        return False
    target = set(cells)
    stack = [next(iter(target))]
    seen = {stack[ZERO]}
    while stack:
        cell = stack.pop()
        for neighbor in _neighbors_c3fa4749(cell, height, width):
            if neighbor not in target or neighbor in seen:
                continue
            seen.add(neighbor)
            stack.append(neighbor)
    return len(seen) == len(target)


def _random_shape_c3fa4749(
    height: Integer,
    width: Integer,
    target_size: Integer,
):
    for _ in range(200):
        side = choice(("top", "bottom", "left", "right"))
        if side == "top":
            anchor = (ZERO, randint(ONE, width - TWO))
        elif side == "bottom":
            anchor = (height - ONE, randint(ONE, width - TWO))
        elif side == "left":
            anchor = (randint(ONE, height - TWO), ZERO)
        else:
            anchor = (randint(ONE, height - TWO), width - ONE)
        shape = {anchor}
        inward = {
            "top": (ONE, ZERO),
            "bottom": (NEG_ONE, ZERO),
            "left": (ZERO, ONE),
            "right": (ZERO, NEG_ONE),
        }[side]
        stem = (anchor[ZERO] + inward[ZERO], anchor[ONE] + inward[ONE])
        shape.add(stem)
        while len(shape) < target_size:
            candidates = []
            for cell in tuple(shape):
                for neighbor in _neighbors_c3fa4749(cell, height, width):
                    if neighbor in shape:
                        continue
                    if neighbor != anchor and neighbor in _border_cells_c3fa4749(initset(neighbor), height, width):
                        continue
                    candidates.append(neighbor)
            if len(candidates) == ZERO:
                break
            shape.add(choice(candidates))
            if randint(ZERO, TWO) != ZERO:
                continue
            thick_candidates = []
            for cell in tuple(shape):
                for neighbor in _neighbors_c3fa4749(cell, height, width):
                    if neighbor in shape:
                        continue
                    if neighbor != anchor and neighbor in _border_cells_c3fa4749(initset(neighbor), height, width):
                        continue
                    thick_candidates.append(neighbor)
            if len(thick_candidates) > ZERO:
                shape.add(choice(thick_candidates))
        if len(shape) < THREE:
            continue
        if len(_border_cells_c3fa4749(shape, height, width)) != ONE:
            continue
        return frozenset(shape)
    return frozenset()


def _input_and_output_shapes_c3fa4749(
    shape,
    height: Integer,
    width: Integer,
):
    cavities = []
    for cell in shape:
        if cell in _border_cells_c3fa4749(initset(cell), height, width):
            continue
        if not all(neighbor in shape for neighbor in _neighbors_c3fa4749(cell, height, width)):
            continue
        reduced = frozenset(other for other in shape if other != cell)
        if len(reduced) >= THREE and _connected_c3fa4749(reduced, height, width):
            cavities.append(cell)
    if len(cavities) == ZERO or randint(ZERO, TWO) != ZERO:
        return shape, shape
    cavity = choice(cavities)
    return frozenset(cell for cell in shape if cell != cavity), shape


def _border_distractor_c3fa4749(
    height: Integer,
    width: Integer,
    occupied,
):
    for _ in range(50):
        side = choice(("top", "bottom", "left", "right"))
        cells = set()
        if side in ("top", "bottom"):
            row = ZERO if side == "top" else height - ONE
            length = randint(TWO, min(FOUR, width - ONE))
            start = randint(ZERO, width - length)
            cells = {(row, start + offset) for offset in range(length)}
            if randint(ZERO, ONE) == ONE:
                inward = ONE if side == "top" else NEG_ONE
                pivot = start + length // TWO
                cells.add((row + inward, pivot))
        else:
            col = ZERO if side == "left" else width - ONE
            length = randint(TWO, min(FOUR, height - ONE))
            start = randint(ZERO, height - length)
            cells = {(start + offset, col) for offset in range(length)}
            if randint(ZERO, ONE) == ONE:
                inward = ONE if side == "left" else NEG_ONE
                pivot = start + length // TWO
                cells.add((pivot, col + inward))
        if cells & occupied:
            continue
        return frozenset(cells)
    return frozenset()


def _paint_rectangle_c3fa4749(
    grid,
    top: Integer,
    left: Integer,
    height: Integer,
    width: Integer,
    value: Integer,
):
    for i in range(top, top + height):
        for j in range(left, left + width):
            grid[i][j] = value


def generate_c3fa4749(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        height = unifint(diff_lb, diff_ub, (18, 26))
        width = unifint(diff_lb, diff_ub, (18, 26))
        gi = [[randint(ZERO, NINE) for _ in range(width)] for _ in range(height)]
        go = [row[:] for row in gi]
        rectangles = []
        nrects = unifint(diff_lb, diff_ub, (TWO, THREE))
        ok = True
        for _ in range(nrects):
            placed = False
            for _ in range(200):
                rect_h = unifint(diff_lb, diff_ub, (FIVE, min(TEN, height - TWO)))
                rect_w = unifint(diff_lb, diff_ub, (FIVE, min(TEN, width - TWO)))
                top = randint(ZERO, height - rect_h)
                left = randint(ZERO, width - rect_w)
                overlap = False
                for other_top, other_left, other_h, other_w in rectangles:
                    if not (
                        top + rect_h + ONE <= other_top
                        or other_top + other_h + ONE <= top
                        or left + rect_w + ONE <= other_left
                        or other_left + other_w + ONE <= left
                    ):
                        overlap = True
                        break
                if overlap:
                    continue
                bg = randint(ZERO, NINE)
                fg_choices = [value for value in range(TEN) if value != bg]
                fg = choice(fg_choices)
                target_size = unifint(diff_lb, diff_ub, (THREE, min(14, rect_h * rect_w // TWO)))
                shape_out = _random_shape_c3fa4749(rect_h, rect_w, target_size)
                if len(shape_out) < THREE:
                    continue
                shape_in, shape_out = _input_and_output_shapes_c3fa4749(shape_out, rect_h, rect_w)
                anchor = next(iter(_border_cells_c3fa4749(shape_out, rect_h, rect_w)))
                _paint_rectangle_c3fa4749(gi, top, left, rect_h, rect_w, bg)
                _paint_rectangle_c3fa4749(go, top, left, rect_h, rect_w, bg)
                for cell in shape_out:
                    go[top + cell[ZERO]][left + cell[ONE]] = fg
                changed = False
                non_anchor = [cell for cell in shape_in if cell != anchor]
                for cell in shape_in:
                    abs_i = top + cell[ZERO]
                    abs_j = left + cell[ONE]
                    if cell == anchor or randint(ZERO, THREE) == ZERO:
                        gi[abs_i][abs_j] = fg
                        continue
                    noisy_choices = [value for value in range(TEN) if value != bg]
                    noisy = choice(noisy_choices)
                    gi[abs_i][abs_j] = noisy
                    if noisy != fg:
                        changed = True
                if not changed and len(non_anchor) > ZERO:
                    forced = choice(non_anchor)
                    forced_choices = [value for value in range(TEN) if value not in (bg, fg)]
                    gi[top + forced[ZERO]][left + forced[ONE]] = choice(forced_choices)
                occupied = set(shape_out)
                if randint(ZERO, TWO) != ZERO:
                    distractor = _border_distractor_c3fa4749(rect_h, rect_w, occupied)
                    if len(distractor) > ZERO:
                        distractor_choices = [value for value in range(TEN) if value != bg]
                        for cell in distractor:
                            value = choice(distractor_choices)
                            abs_i = top + cell[ZERO]
                            abs_j = left + cell[ONE]
                            gi[abs_i][abs_j] = value
                            go[abs_i][abs_j] = value
                rectangles.append((top, left, rect_h, rect_w))
                placed = True
                break
            if not placed:
                ok = False
                break
        if not ok:
            continue
        gi = format_grid(gi)
        go = format_grid(go)
        if gi == go:
            continue
        if verify_c3fa4749(gi) != go:
            continue
        return {"input": gi, "output": go}
