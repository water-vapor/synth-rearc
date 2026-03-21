from arc2.core import *


def _adjacent_values(grid: Grid, patch: Patch) -> tuple[int, ...]:
    x0 = toindices(patch)
    x1 = []
    for i, j in x0:
        x2 = dneighbors((i, j))
        for a, b in x2:
            if (a, b) in x0:
                continue
            x3 = index(grid, (a, b))
            if x3 is not None:
                x1.append(x3)
    return tuple(x1)


def _host_colors(grid: Grid, inner_objects: Objects, inner_color: int) -> tuple[int, int]:
    x0 = []
    for obj in inner_objects:
        x1 = _adjacent_values(grid, obj)
        for value in x1:
            if value != inner_color:
                x0.append(value)
    x2 = dedupe(tuple(x0))
    return x2


def _marker_indices(patch: Patch) -> Indices:
    x0 = toindices(patch)
    x1 = {}
    x2 = {}
    for i, j in x0:
        x1.setdefault(i, []).append(j)
        x2.setdefault(j, []).append(i)
    x3 = {i: min(js) for i, js in x1.items()}
    x4 = {i: max(js) for i, js in x1.items()}
    x5 = {j: min(is_) for j, is_ in x2.items()}
    x6 = {j: max(is_) for j, is_ in x2.items()}
    x7 = mostcommon(tuple(x3.values()))
    x8 = mostcommon(tuple(x4.values()))
    x9 = mostcommon(tuple(x5.values()))
    x10 = mostcommon(tuple(x6.values()))
    x11 = set()
    for i in x1:
        x12 = x3[i]
        x13 = x4[i]
        if len(x1[i]) > ONE and abs(x12 - x7) <= ONE and abs(x13 - x8) <= ONE:
            if x12 != x7:
                x11 |= {(i, x7 - ONE), (i, x7)}
            if x13 != x8:
                x11 |= {(i, x8), (i, x8 + ONE)}
    for j in x2:
        x12 = x5[j]
        x13 = x6[j]
        if len(x2[j]) > ONE and abs(x12 - x9) <= ONE and abs(x13 - x10) <= ONE:
            if x12 != x9:
                x11 |= {(x9 - ONE, j), (x9, j)}
            if x13 != x10:
                x11 |= {(x10, j), (x10 + ONE, j)}
    return frozenset(x11)


def _marker_object(grid: Grid, patch: Patch, hosts: tuple[int, int]) -> Object:
    x0 = tuple(value for value in _adjacent_values(grid, patch) if contained(value, hosts))
    x1 = mostcommon(x0)
    x2 = other(hosts, x1)
    x3 = _marker_indices(patch)
    x4 = recolor(x2, x3)
    return x4


def verify_9b5080bb(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = compose(flip, rbind(bordering, I))
    x2 = sfilter(x0, x1)
    x3 = tuple(color(obj) for obj in x2)
    x4 = mostcommon(x3)
    x5 = colorfilter(x2, x4)
    x6 = _host_colors(I, x5, x4)
    x7 = mapply(lambda obj: _marker_object(I, obj, x6), x5)
    x8 = paint(I, x7)
    return x8
