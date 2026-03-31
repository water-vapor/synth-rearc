from synth_rearc.core import *


def _ordered_line_5961cc34(
    patch: Patch,
    direction: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    x0 = tuple(toindices(patch))
    if direction[0] != ZERO:
        return tuple(sorted(x0, key=lambda ij: (ij[1], ij[0])))
    return tuple(sorted(x0, key=lambda ij: (ij[0], ij[1])))


def _ray_distance_5961cc34(
    start: tuple[int, int],
    target: tuple[int, int],
    direction: tuple[int, int],
) -> Integer | None:
    si, sj = start
    ti, tj = target
    di, dj = direction
    if di != ZERO:
        if sj != tj:
            return None
        x0 = (ti - si) * di
        return x0 if x0 >= ZERO else None
    if si != ti:
        return None
    x0 = (tj - sj) * dj
    return x0 if x0 >= ZERO else None


def _segment_to_border_5961cc34(
    patch: Patch,
    direction: tuple[int, int],
    dims: tuple[int, int],
) -> Indices:
    h, w = dims
    cells = set()
    for i, j in toindices(patch):
        ci, cj = i, j
        while 0 <= ci < h and 0 <= cj < w:
            cells.add((ci, cj))
            ci += direction[0]
            cj += direction[1]
    return frozenset(cells)


def _first_hit_5961cc34(
    objs: Container,
    patch: Patch,
    direction: tuple[int, int],
) -> tuple[Object | None, Indices]:
    x0 = None
    x1 = None
    x2 = frozenset()
    x3 = _ordered_line_5961cc34(patch, direction)
    for obj in objs:
        x4 = []
        x5 = []
        for start in x3:
            x6 = []
            for cell in toindices(obj):
                x7 = _ray_distance_5961cc34(start, cell, direction)
                if x7 is not None:
                    x6.append((x7, cell))
            if len(x6) == ZERO:
                continue
            x8 = min(x6, key=first)
            x4.append(x8[ZERO])
            x5.append(connect(start, x8[ONE]))
        if len(x4) == ZERO:
            continue
        x9 = min(x4)
        if x1 is None or x9 < x1:
            x0 = obj
            x1 = x9
            x2 = frozenset()
            for seg in x5:
                x2 = x2 | frozenset(seg)
    return x0, x2


def _marker_map_5961cc34(
    white_objs: Container,
    red_objs: Container,
) -> dict[Object, Object]:
    x0 = {}
    for obj in white_objs:
        x1 = tuple(marker for marker in red_objs if adjacent(obj, marker))
        if len(x1) == ONE:
            x0[obj] = x1[ZERO]
    return x0


def _trace_patch_5961cc34(
    white_objs: Container,
    red_objs: Container,
    blue_obj: Object,
    gray_obj: Object,
    dims: tuple[int, int],
) -> Indices:
    x0 = _marker_map_5961cc34(white_objs, red_objs)
    x1 = set(white_objs)
    x2 = toindices(blue_obj)
    x3 = toindices(gray_obj)
    x4 = position(blue_obj, gray_obj)
    while True:
        x5, x6 = _first_hit_5961cc34(tuple(x1), x3, x4)
        if x5 is None:
            return x2 | _segment_to_border_5961cc34(x3, x4, dims)
        x2 = x2 | x6 | toindices(x5)
        x1.remove(x5)
        x3 = toindices(x0[x5])
        x4 = position(x5, x0[x5])


def verify_5961cc34(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = colorfilter(x0, THREE)
    x3 = extract(x0, matcher(color, TWO))
    x4 = extract(x0, matcher(color, FOUR))
    x5 = _trace_patch_5961cc34(x1, x2, x3, x4, shape(I))
    x6 = canvas(mostcolor(I), shape(I))
    x7 = recolor(TWO, x5)
    x8 = paint(x6, x7)
    return x8
