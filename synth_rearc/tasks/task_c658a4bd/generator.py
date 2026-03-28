from synth_rearc.core import *


def _square_box(size: int, loc: tuple[int, int]) -> Indices:
    corner = decrement(size)
    patch = box(frozenset({ORIGIN, (corner, corner)}))
    return shift(patch, loc)


def _nested_output(colors: tuple[int, ...], sizes: tuple[int, ...]) -> Grid:
    dim = sizes[0]
    go = canvas(ZERO, (dim, dim))
    for color_value, size in zip(colors, sizes):
        inset = (dim - size) // 2
        patch = shift(_square_box(size, ORIGIN), (inset, inset))
        go = fill(go, color_value, patch)
    return go


def _latent_matches(grid: Grid, colors: tuple[int, ...], sizes: tuple[int, ...]) -> bool:
    objs = {color(obj): obj for obj in fgpartition(grid)}
    if set(objs) != set(colors):
        return False
    return all(maximum(shape(objs[color_value])) == size for color_value, size in zip(colors, sizes))


def _layout_outer9() -> tuple[tuple[int, int], ...]:
    loc9 = (9, randint(4, 6))
    loc7 = (randint(7, 8), randint(0, 2))
    loc5 = (randint(1, 2), randint(2, 4))
    loc3 = (randint(2, 4), randint(9, 11))
    loc1 = (randint(1, 3), randint(0, 1))
    return (loc9, loc7, loc5, loc3, loc1)


def _layout_outer8() -> tuple[tuple[int, int], ...]:
    loc8 = (4, randint(2, 4))
    loc6 = (randint(1, 2), randint(0, 1))
    loc4 = (randint(1, 2), randint(8, 9))
    loc2 = (randint(9, 10), randint(0, 1))
    return (loc8, loc6, loc4, loc2)


def _layout_outer10() -> tuple[tuple[int, int], ...]:
    loc10 = (randint(1, 2), randint(1, 3))
    loc8 = add(loc10, (4, 3))
    loc6 = add(loc10, (2, 2))
    loc4 = (randint(14, 15), randint(11, 12))
    loc2 = (randint(1, 3), randint(15, 16))
    return (loc10, loc8, loc6, loc4, loc2)


def generate_c658a4bd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    specs = (
        ((9, 7, 5, 3, 1), 16, _layout_outer9, (2, 3, 1, 0, 4)),
        ((8, 6, 4, 2), 13, _layout_outer8, (1, 0, 2, 3)),
        ((10, 8, 6, 4, 2), 19, _layout_outer10, (0, 2, 1, 4, 3)),
    )
    while True:
        sizes, dim, layout_fn, order = choice(specs)
        colors = tuple(sample(cols, len(sizes)))
        locs = layout_fn()
        patches = tuple(_square_box(size, loc) for size, loc in zip(sizes, locs))
        gi = canvas(ZERO, (dim, dim))
        for idx in order:
            gi = fill(gi, colors[idx], patches[idx])
        if mostcolor(gi) != ZERO:
            continue
        if not _latent_matches(gi, colors, sizes):
            continue
        go = _nested_output(colors, sizes)
        return {"input": gi, "output": go}
