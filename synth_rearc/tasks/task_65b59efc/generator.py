from synth_rearc.core import *

from .verifier import verify_65b59efc


NON_SEPARATOR_COLORS_65B59EFC = remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE)))


def _connected_patch_65b59efc(
    patch: Indices,
    size_: Integer,
) -> Boolean:
    x0 = canvas(ZERO, (size_, size_))
    x1 = fill(x0, ONE, patch)
    x2 = objects(x1, T, F, F)
    x3 = colorfilter(x2, ONE)
    return equality(size(x3), ONE)


def _prototype_patch_65b59efc(
    size_: Integer,
) -> Indices:
    x0 = frozenset((i, j) for i in range(size_) for j in range(size_))
    x1 = multiply(size_, size_)
    x2 = maximum((add(size_, ONE), divide(multiply(x1, TWO), THREE)))
    while True:
        x3 = randint(x2, x1)
        x4 = x0
        x5 = 0
        while size(x4) > x3 and x5 < 400:
            x5 += 1
            x6 = choice(totuple(x4))
            x7 = remove(x6, x4)
            if height(x7) != size_ or width(x7) != size_:
                continue
            if not _connected_patch_65b59efc(x7, size_):
                continue
            x4 = x7
        if size(x4) != x3:
            continue
        return x4


def _grow_patch_65b59efc(
    pool: Indices,
    target: Integer,
) -> Indices:
    x0 = {choice(totuple(pool))}
    while len(x0) < target:
        x1 = {
            loc
            for cell in x0
            for loc in dneighbors(cell)
            if loc in pool and loc not in x0
        }
        if not x1:
            break
        x0.add(choice(tuple(x1)))
    return frozenset(x0)


def _layout_masks_65b59efc(
    size_: Integer,
    n_panels: Integer,
) -> tuple[Indices, ...]:
    x0 = frozenset((i, j) for i in range(size_) for j in range(size_))
    x1 = add(size_, ONE)
    for _ in range(200):
        x2 = set(x0)
        x3 = []
        for x4 in range(n_panels):
            x5 = subtract(n_panels, increment(x4))
            x6 = len(x2)
            x7 = min(x1, subtract(x6, x5))
            x8 = randint(ONE, x7)
            x9 = frozenset()
            for _ in range(50):
                x10 = _grow_patch_65b59efc(frozenset(x2), x8)
                if size(x10) > ZERO:
                    x9 = x10
                    break
            if size(x9) == ZERO:
                break
            x3.append(x9)
            x2 -= x9
        if len(x3) != n_panels:
            continue
        x11 = merge(tuple(x3))
        if size(x11) <= n_panels:
            continue
        if maximum(tuple(size(x) for x in x3)) == ONE:
            continue
        return tuple(x3)
    raise RuntimeError("failed to sample layout masks")


def _separator_motif_65b59efc(
    size_: Integer,
) -> tuple[int, ...]:
    if even(size_):
        x0 = {ZERO, subtract(size_, ONE)}
    else:
        x0 = set(range(ZERO, size_, TWO))
    return tuple(FIVE if j in x0 else ZERO for j in range(size_))


def _key_row_65b59efc(
    size_: Integer,
    color_: Integer,
) -> tuple[int, ...]:
    x0 = [ZERO] * size_
    x1 = divide(size_, TWO)
    if even(size_):
        x0[decrement(x1)] = color_
        x0[x1] = color_
    else:
        x0[x1] = color_
    return tuple(x0)


def _patch_grid_65b59efc(
    patch: Indices,
    color_: Integer,
    size_: Integer,
) -> Grid:
    x0 = canvas(ZERO, (size_, size_))
    return fill(x0, color_, patch)


def _join_panels_65b59efc(
    panel_rows: tuple[tuple[int, ...], ...],
    sep_value: Integer,
    right_pad: Integer,
    trailing_sep: Boolean,
) -> tuple[int, ...]:
    x0 = []
    for x1, x2 in enumerate(panel_rows):
        x0.extend(x2)
        if x1 != subtract(len(panel_rows), ONE) or trailing_sep:
            x0.append(sep_value)
    if right_pad > ZERO:
        x0.extend(repeat(ZERO, right_pad))
    return tuple(x0)


def _render_input_65b59efc(
    size_: Integer,
    prototypes: tuple[Grid, ...],
    masks: tuple[Grid, ...],
    key_colors: tuple[int, ...],
    right_pad: Integer,
    bottom_pad: Integer,
    trailing_sep: Boolean,
) -> Grid:
    x0 = _separator_motif_65b59efc(size_)
    x1 = tuple(repeat(ZERO, size_))
    x2 = tuple(_key_row_65b59efc(size_, x) for x in key_colors)
    x3 = []
    for i in range(size_):
        x4 = tuple(x[i] for x in prototypes)
        x5 = x0[i]
        x3.append(_join_panels_65b59efc(x4, x5, right_pad, trailing_sep))
    x6 = _join_panels_65b59efc(tuple(repeat(x0, len(prototypes))), FIVE, right_pad, trailing_sep)
    x3.append(x6)
    for i in range(size_):
        x7 = tuple(x[i] for x in masks)
        x8 = x0[i]
        x3.append(_join_panels_65b59efc(x7, x8, right_pad, trailing_sep))
    x3.append(x6)
    x9 = _join_panels_65b59efc(tuple(repeat(x1, len(prototypes))), FIVE, right_pad, trailing_sep)
    x3.append(x9)
    x10 = _join_panels_65b59efc(x2, ZERO, right_pad, trailing_sep)
    x3.append(x10)
    x11 = len(x10)
    for _ in range(bottom_pad):
        x3.append(repeat(ZERO, x11))
    return tuple(x3)


def _render_output_65b59efc(
    size_: Integer,
    prototypes: tuple[Grid, ...],
    layout_masks: tuple[Indices, ...],
    prototype_colors: tuple[int, ...],
    key_colors: tuple[int, ...],
) -> Grid:
    x0 = multiply(size_, size_)
    x1 = canvas(ZERO, (x0, x0))
    for x2, x3, x4, x5 in zip(prototypes, layout_masks, prototype_colors, key_colors):
        x6 = asobject(replace(x2, x4, x5))
        for x7 in x3:
            x8 = multiply(x7[ZERO], size_)
            x9 = multiply(x7[ONE], size_)
            x10 = shift(x6, (x8, x9))
            x1 = paint(x1, x10)
    return x1


def generate_65b59efc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((THREE, THREE, FOUR, FIVE, FIVE))
        x1 = choice((THREE, THREE, FOUR))
        x2 = sample(NON_SEPARATOR_COLORS_65B59EFC, x1)
        x3 = []
        for _ in range(x1):
            x4 = _prototype_patch_65b59efc(x0)
            x3.append(x4)
        if size(frozenset(x3)) != x1:
            continue
        x5 = tuple(_patch_grid_65b59efc(x, c, x0) for x, c in zip(x3, x2))
        x6 = _layout_masks_65b59efc(x0, x1)
        x7 = tuple(_patch_grid_65b59efc(x, c, x0) for x, c in zip(x6, x2))
        x8 = tuple(sample(interval(ZERO, x1, ONE), x1))
        x9 = interval(ZERO, x1, ONE)
        if x8 == x9:
            continue
        x10 = tuple(x7[i] for i in x8)
        x11 = tuple(sample(NON_SEPARATOR_COLORS_65B59EFC, x1))
        if any(a == b for a, b in zip(x2, x11)):
            continue
        x12 = even(x0)
        x13 = ZERO if x12 else randint(ZERO, add(x0, TWO)) if uniform(0.0, 1.0) < 0.18 else ZERO
        x14 = randint(ZERO, TWO) if uniform(0.0, 1.0) < 0.2 else ZERO
        gi = _render_input_65b59efc(x0, x5, x10, x11, x13, x14, x12)
        go = _render_output_65b59efc(x0, x5, x6, x2, x11)
        if height(go) != multiply(x0, x0) or width(go) != multiply(x0, x0):
            continue
        if go == canvas(ZERO, shape(go)):
            continue
        if verify_65b59efc(gi) != go:
            continue
        return {"input": gi, "output": go}
