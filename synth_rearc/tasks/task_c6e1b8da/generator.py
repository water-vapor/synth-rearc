from synth_rearc.core import *


DIRECTIONS_c6e1b8da = (UP, DOWN, LEFT, RIGHT)


def _row_map_c6e1b8da(patch: Patch) -> dict[Integer, tuple[Integer, ...]]:
    out = {}
    for i, j in toindices(patch):
        if i not in out:
            out[i] = []
        out[i].append(j)
    return {i: tuple(sorted(js)) for i, js in out.items()}


def _col_map_c6e1b8da(patch: Patch) -> dict[Integer, tuple[Integer, ...]]:
    out = {}
    for i, j in toindices(patch):
        if j not in out:
            out[j] = []
        out[j].append(i)
    return {j: tuple(sorted(iset)) for j, iset in out.items()}


def _bottom_tail_c6e1b8da(
    row_map: dict[Integer, tuple[Integer, ...]],
    r0: Integer,
    r1: Integer,
    c0: Integer,
    c1: Integer,
) -> Integer:
    col = None
    span = ZERO
    for i in range(r1, r0 - ONE, -ONE):
        cols = row_map[i]
        if len(cols) != ONE:
            break
        j = cols[ZERO]
        if col is None:
            col = j
        if j != col:
            break
        span += ONE
    if span == ZERO or span == r1 - r0 + ONE:
        return ZERO
    if not c0 < col < c1:
        return ZERO
    rr1 = r1 - span
    for i in range(r0, rr1 + ONE):
        cols = row_map[i]
        if not cols[ZERO] <= col <= cols[-ONE]:
            return ZERO
    return span


def _top_tail_c6e1b8da(
    row_map: dict[Integer, tuple[Integer, ...]],
    r0: Integer,
    r1: Integer,
    c0: Integer,
    c1: Integer,
) -> Integer:
    col = None
    span = ZERO
    for i in range(r0, r1 + ONE):
        cols = row_map[i]
        if len(cols) != ONE:
            break
        j = cols[ZERO]
        if col is None:
            col = j
        if j != col:
            break
        span += ONE
    if span == ZERO or span == r1 - r0 + ONE:
        return ZERO
    if not c0 < col < c1:
        return ZERO
    rr0 = r0 + span
    for i in range(rr0, r1 + ONE):
        cols = row_map[i]
        if not cols[ZERO] <= col <= cols[-ONE]:
            return ZERO
    return span


def _right_tail_c6e1b8da(
    col_map: dict[Integer, tuple[Integer, ...]],
    r0: Integer,
    r1: Integer,
    c0: Integer,
    c1: Integer,
) -> Integer:
    row = None
    span = ZERO
    for j in range(c1, c0 - ONE, -ONE):
        rows = col_map[j]
        if len(rows) != ONE:
            break
        i = rows[ZERO]
        if row is None:
            row = i
        if i != row:
            break
        span += ONE
    if span == ZERO or span == c1 - c0 + ONE:
        return ZERO
    if not r0 < row < r1:
        return ZERO
    cc1 = c1 - span
    for j in range(c0, cc1 + ONE):
        rows = col_map[j]
        if not rows[ZERO] <= row <= rows[-ONE]:
            return ZERO
    return span


def _left_tail_c6e1b8da(
    col_map: dict[Integer, tuple[Integer, ...]],
    r0: Integer,
    r1: Integer,
    c0: Integer,
    c1: Integer,
) -> Integer:
    row = None
    span = ZERO
    for j in range(c0, c1 + ONE):
        rows = col_map[j]
        if len(rows) != ONE:
            break
        i = rows[ZERO]
        if row is None:
            row = i
        if i != row:
            break
        span += ONE
    if span == ZERO or span == c1 - c0 + ONE:
        return ZERO
    if not r0 < row < r1:
        return ZERO
    cc0 = c0 + span
    for j in range(cc0, c1 + ONE):
        rows = col_map[j]
        if not rows[ZERO] <= row <= rows[-ONE]:
            return ZERO
    return span


def _describe_object_c6e1b8da(
    obj: Object,
) -> tuple[IntegerTuple, IntegerTuple, IntegerTuple]:
    x0 = uppermost(obj)
    x1 = lowermost(obj)
    x2 = leftmost(obj)
    x3 = rightmost(obj)
    x4 = _row_map_c6e1b8da(obj)
    x5 = _col_map_c6e1b8da(obj)
    x6 = _bottom_tail_c6e1b8da(x4, x0, x1, x2, x3)
    x7 = _top_tail_c6e1b8da(x4, x0, x1, x2, x3)
    x8 = _right_tail_c6e1b8da(x5, x0, x1, x2, x3)
    x9 = _left_tail_c6e1b8da(x5, x0, x1, x2, x3)
    x10 = (
        (x6, DOWN, (x0, x2), (x1 - x0 - x6 + ONE, x3 - x2 + ONE)),
        (x7, UP, (x0 + x7, x2), (x1 - x0 - x7 + ONE, x3 - x2 + ONE)),
        (x8, RIGHT, (x0, x2), (x1 - x0 + ONE, x3 - x2 - x8 + ONE)),
        (x9, LEFT, (x0, x2 + x9), (x1 - x0 + ONE, x3 - x2 - x9 + ONE)),
    )
    x11 = tuple(item for item in x10 if item[ZERO] > ZERO)
    if len(x11) == ZERO:
        return ((x0, x2), (x1 - x0 + ONE, x3 - x2 + ONE), ORIGIN)
    x12 = max(x11, key=lambda item: item[ZERO])
    return (x12[TWO], x12[THREE], multiply(x12[ONE], x12[ZERO]))


def _rect_patch_c6e1b8da(
    ul: IntegerTuple,
    dims: IntegerTuple,
) -> Patch:
    rows = interval(ul[ZERO], ul[ZERO] + dims[ZERO], ONE)
    cols = interval(ul[ONE], ul[ONE] + dims[ONE], ONE)
    return product(rows, cols)


def _tail_patch_c6e1b8da(
    ul: IntegerTuple,
    dims: IntegerTuple,
    direction: IntegerTuple,
    span: Integer,
    offset: Integer,
) -> Patch:
    i, j = ul
    h, w = dims
    if direction == DOWN:
        start = (i + h, j + offset)
        stop = (i + h + span - ONE, j + offset)
        return connect(start, stop)
    if direction == UP:
        start = (i - span, j + offset)
        stop = (i - ONE, j + offset)
        return connect(start, stop)
    if direction == RIGHT:
        start = (i + offset, j + w)
        stop = (i + offset, j + w + span - ONE)
        return connect(start, stop)
    start = (i + offset, j - span)
    stop = (i + offset, j - ONE)
    return connect(start, stop)


def _sample_stationary_c6e1b8da(
    dims: IntegerTuple,
    color_value: Integer,
    blocked: Patch,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Object, IntegerTuple] | None:
    h = dims[ZERO]
    w = dims[ONE]
    for _ in range(200):
        rh = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        rw = unifint(diff_lb, diff_ub, (THREE, NINE))
        if rh >= h or rw >= w:
            continue
        i = randint(ZERO, h - rh)
        j = randint(ZERO, w - rw)
        patch = _rect_patch_c6e1b8da((i, j), (rh, rw))
        if len(intersection(patch, blocked)) > ZERO:
            continue
        obj = recolor(color_value, patch)
        return (color_value, obj, (i, j))
    return None


def _sample_mover_c6e1b8da(
    dims: IntegerTuple,
    color_value: Integer,
    input_blocked: Patch,
    output_blocked: Patch,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Object, Object, Object, IntegerTuple, IntegerTuple] | None:
    h = dims[ZERO]
    w = dims[ONE]
    for _ in range(400):
        direction = choice(DIRECTIONS_c6e1b8da)
        span = unifint(diff_lb, diff_ub, (TWO, SIX))
        rh = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        rw = unifint(diff_lb, diff_ub, (THREE, NINE))
        if direction in (UP, DOWN):
            if h - rh - span < ZERO:
                continue
            if direction == DOWN:
                i = randint(ZERO, h - rh - span)
            else:
                i = randint(span, h - rh)
            j = randint(ZERO, w - rw)
            offset = randint(ONE, rw - TWO)
        else:
            if w - rw - span < ZERO:
                continue
            i = randint(ZERO, h - rh)
            if direction == RIGHT:
                j = randint(ZERO, w - rw - span)
            else:
                j = randint(span, w - rw)
            offset = randint(ONE, rh - TWO)
        ul = (i, j)
        rect_in = recolor(color_value, _rect_patch_c6e1b8da(ul, (rh, rw)))
        tail = recolor(color_value, _tail_patch_c6e1b8da(ul, (rh, rw), direction, span, offset))
        full_in = combine(rect_in, tail)
        vec = multiply(direction, span)
        rect_out = shift(rect_in, vec)
        if len(intersection(toindices(full_in), input_blocked)) > ZERO:
            continue
        if len(intersection(toindices(rect_out), output_blocked)) > ZERO:
            continue
        return (color_value, rect_in, tail, rect_out, vec, ul)
    return None


def _connected_singletons_c6e1b8da(grid: Grid) -> Boolean:
    x0 = objects(grid, T, F, T)
    x1 = palette(grid)
    x2 = remove(ZERO, x1)
    for value in x2:
        if size(colorfilter(x0, value)) != ONE:
            return False
    return True


def _descriptors_match_c6e1b8da(
    grid: Grid,
    expected: dict[Integer, tuple[IntegerTuple, IntegerTuple, IntegerTuple]],
) -> Boolean:
    x0 = fgpartition(grid)
    x1 = {color(obj): _describe_object_c6e1b8da(obj) for obj in x0}
    return x1 == expected


def generate_c6e1b8da(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    dims = (20, 20)
    colors = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        nobjs = unifint(diff_lb, diff_ub, (THREE, FIVE))
        nmovers = unifint(diff_lb, diff_ub, (ONE, min(THREE, nobjs - ONE)))
        palette0 = sample(colors, nobjs)
        shuffle(palette0)
        mover_colors = tuple(palette0[:nmovers])
        stationary_colors = tuple(palette0[nmovers:])

        stationary = []
        stationary_out = frozenset()
        for value in stationary_colors:
            item = _sample_stationary_c6e1b8da(dims, value, stationary_out, diff_lb, diff_ub)
            if item is None:
                break
            stationary.append(item)
            stationary_out = combine(stationary_out, toindices(item[ONE]))
        else:
            movers = []
            movers_in = frozenset()
            movers_out = frozenset()
            for value in mover_colors:
                item = _sample_mover_c6e1b8da(
                    dims,
                    value,
                    movers_in,
                    movers_out,
                    diff_lb,
                    diff_ub,
                )
                if item is None:
                    break
                movers.append(item)
                movers_in = combine(movers_in, toindices(combine(item[ONE], item[TWO])))
                movers_out = combine(movers_out, toindices(item[THREE]))
            else:
                gi = canvas(ZERO, dims)
                for _, rect_obj, _ in stationary:
                    gi = paint(gi, rect_obj)
                latent_expected = {}
                for value, rect_obj, ul in stationary:
                    latent_expected[value] = (ul, shape(rect_obj), ORIGIN)
                input_overlap = False
                output_overlap = False
                for value, rect_obj, tail, rect_out, vec, ul in movers:
                    gi_before = gi
                    gi = paint(gi, combine(rect_obj, tail))
                    if gi_before != gi and len(intersection(toindices(rect_obj), stationary_out)) > ZERO:
                        input_overlap = True
                    latent_expected[value] = (ul, shape(rect_obj), vec)
                go = canvas(ZERO, dims)
                for _, rect_obj, _ in stationary:
                    go = paint(go, rect_obj)
                for _, _, _, rect_out, _, _ in movers:
                    go_before = go
                    go = paint(go, rect_out)
                    if go_before != go and len(intersection(toindices(rect_out), stationary_out)) > ZERO:
                        output_overlap = True
                if not (input_overlap or output_overlap):
                    continue
                if gi == go:
                    continue
                if not _connected_singletons_c6e1b8da(gi):
                    continue
                if not _connected_singletons_c6e1b8da(go):
                    continue
                if not _descriptors_match_c6e1b8da(gi, latent_expected):
                    continue
                return {"input": gi, "output": go}
