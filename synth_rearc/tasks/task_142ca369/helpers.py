from synth_rearc.core import *


L_NW_142CA369 = frozenset({RIGHT, DOWN, UNITY})
L_NE_142CA369 = frozenset({ORIGIN, DOWN, UNITY})
L_SW_142CA369 = frozenset({ORIGIN, RIGHT, UNITY})
L_SE_142CA369 = frozenset({ORIGIN, RIGHT, DOWN})


def classify_object_142ca369(obj: Object) -> tuple[str, str | None]:
    x0 = toindices(normalize(obj))
    x1 = len(x0)
    if x1 == ONE:
        return ("dot", None)
    if both(equality(x1, THREE), both(equality(height(obj), TWO), equality(width(obj), TWO))):
        if x0 == L_NW_142CA369:
            return ("L", "nw")
        if x0 == L_NE_142CA369:
            return ("L", "ne")
        if x0 == L_SW_142CA369:
            return ("L", "sw")
        if x0 == L_SE_142CA369:
            return ("L", "se")
    if both(equality(x1, THREE), vline(obj)):
        return ("vbar", None)
    if both(equality(x1, THREE), hline(obj)):
        return ("hbar", None)
    raise ValueError(f"unsupported object for 142ca369: {obj}")


def make_object_142ca369(
    color_value: Integer,
    cells: Indices,
) -> Object:
    return frozenset((color_value, loc) for loc in cells)


def make_l_object_142ca369(
    color_value: Integer,
    upper_left: IntegerTuple,
    missing_corner: str,
) -> Object:
    x0, x1 = upper_left
    x2 = {
        "nw": frozenset({(x0, x1 + ONE), (x0 + ONE, x1), (x0 + ONE, x1 + ONE)}),
        "ne": frozenset({(x0, x1), (x0 + ONE, x1), (x0 + ONE, x1 + ONE)}),
        "sw": frozenset({(x0, x1), (x0, x1 + ONE), (x0 + ONE, x1 + ONE)}),
        "se": frozenset({(x0, x1), (x0, x1 + ONE), (x0 + ONE, x1)}),
    }[missing_corner]
    return make_object_142ca369(color_value, x2)


def make_vbar_object_142ca369(
    color_value: Integer,
    top: IntegerTuple,
) -> Object:
    x0, x1 = top
    x2 = frozenset({(x0, x1), (x0 + ONE, x1), (x0 + TWO, x1)})
    return make_object_142ca369(color_value, x2)


def make_hbar_object_142ca369(
    color_value: Integer,
    left: IntegerTuple,
) -> Object:
    x0, x1 = left
    x2 = frozenset({(x0, x1), (x0, x1 + ONE), (x0, x1 + TWO)})
    return make_object_142ca369(color_value, x2)


def make_dot_object_142ca369(
    color_value: Integer,
    loc: IntegerTuple,
) -> Object:
    return make_object_142ca369(color_value, frozenset({loc}))


def l_start_and_direction_142ca369(
    obj: Object,
    missing_corner: str,
) -> tuple[IntegerTuple, IntegerTuple]:
    if missing_corner == "nw":
        return lrcorner(obj), UNITY
    if missing_corner == "ne":
        return llcorner(obj), DOWN_LEFT
    if missing_corner == "sw":
        return urcorner(obj), UP_RIGHT
    return ulcorner(obj), NEG_UNITY


def in_bounds_142ca369(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> Boolean:
    x0, x1 = dims
    x2, x3 = loc
    return both(both(x2 >= ZERO, x2 < x0), both(x3 >= ZERO, x3 < x1))


def trace_l_ray_142ca369(
    start: IntegerTuple,
    direction: IntegerTuple,
    dims: IntegerTuple,
    dots: Indices,
    vbar_tops: Indices,
    vbar_bottoms: Indices,
    blockers: Indices,
) -> Indices:
    x0 = start
    x1 = direction
    x2 = set()
    while True:
        x3 = add(x0, DOWN)
        if both(equality(x1, UNITY), x3 in dots):
            x1 = UP_RIGHT
            continue
        x4 = add(x0, x1)
        if not in_bounds_142ca369(x4, dims):
            break
        if both(x1[0] < ZERO, x4 in vbar_tops):
            x1 = (NEG_ONE, invert(x1[1]))
            continue
        if x4 in vbar_tops:
            break
        if both(positive(x1[0]), x4 in vbar_bottoms):
            x1 = (ONE, invert(x1[1]))
            continue
        if either(x4 in blockers, dneighbors(x4) & blockers):
            break
        x2.add(x4)
        x0 = x4
    return frozenset(x2)


def trace_simple_ray_142ca369(
    start: IntegerTuple,
    direction: IntegerTuple,
    dims: IntegerTuple,
    blockers: Indices,
) -> Indices:
    x0 = start
    x1 = set()
    while True:
        x2 = add(x0, direction)
        if not in_bounds_142ca369(x2, dims):
            break
        if either(x2 in blockers, dneighbors(x2) & blockers):
            break
        x1.add(x2)
        x0 = x2
    return frozenset(x1)


def bar_only_cells_142ca369(
    objs: tuple[Object, ...],
    dims: IntegerTuple,
    blockers: Indices,
) -> Indices:
    x0 = len(objs)
    x1 = toindices(merge(tuple(toindices(obj) for obj in objs)))
    x2 = classify_object_142ca369(first(objs))[0]
    x3, x4 = dims
    x5 = set(x1)
    if both(equality(x0, ONE), equality(x2, "vbar")):
        x6 = first(objs)
        x7 = centerofmass(x6)
        x8 = leftmost(x6)
        x9 = (uppermost(x6), x8)
        x10 = branch(x7[0] < x3 // TWO, branch(x7[1] < x4 // TWO, DOWN_LEFT, UNITY), branch(x7[1] < x4 // TWO, UNITY, DOWN_LEFT))
        x11 = trace_simple_ray_142ca369(x9, x10, dims, blockers)
        x5 |= x11
        return frozenset(loc for loc in x5 if in_bounds_142ca369(loc, dims))
    if both(equality(x0, ONE), equality(x2, "hbar")):
        x6 = first(objs)
        x7 = centerofmass(x6)
        x8 = uppermost(x6)
        x9 = (x8, leftmost(x6))
        x10 = branch(x7[0] < x3 // TWO, UNITY, UP_RIGHT)
        x11 = trace_simple_ray_142ca369(x9, x10, dims, blockers)
        x5 |= x11
        return frozenset(loc for loc in x5 if in_bounds_142ca369(loc, dims))
    if both(equality(x0, TWO), equality(x2, "vbar")):
        x6 = tuple(sorted(objs, key=lambda obj: (centerofmass(obj)[0], centerofmass(obj)[1])))
        x7 = centerofmass(x6[0])
        x8 = centerofmass(x6[1])
        if abs(subtract(x7[0], x8[0])) > abs(subtract(x7[1], x8[1])):
            x9 = lowermost(x6[0])
            x10 = rightmost(x6[0])
            x11 = uppermost(x6[1])
            x12 = leftmost(x6[1])
            x5 |= trace_simple_ray_142ca369((x9, x10), UP_RIGHT, dims, blockers)
            x5 |= trace_simple_ray_142ca369((x11, x12), DOWN_LEFT, dims, blockers)
            return frozenset(loc for loc in x5 if in_bounds_142ca369(loc, dims))
        x13 = tuple(sorted(objs, key=lambda obj: (centerofmass(obj)[1], centerofmass(obj)[0])))
        x14 = uppermost(x13[0])
        x15 = leftmost(x13[0])
        x16 = lowermost(x13[1])
        x17 = rightmost(x13[1])
        x5 |= trace_simple_ray_142ca369((x14, x15), UNITY, dims, blockers)
        x5 |= trace_simple_ray_142ca369((x16, x17), NEG_UNITY, dims, blockers)
        return frozenset(loc for loc in x5 if in_bounds_142ca369(loc, dims))
    if both(equality(x0, TWO), equality(x2, "hbar")):
        x6 = tuple(sorted(objs, key=lambda obj: (centerofmass(obj)[0], centerofmass(obj)[1])))
        x7 = uppermost(x6[0])
        x8 = rightmost(x6[0])
        x9 = uppermost(x6[1])
        x10 = leftmost(x6[1])
        x5 |= trace_simple_ray_142ca369((x7, x8), DOWN_LEFT, dims, blockers)
        x5 |= trace_simple_ray_142ca369((x9, x10), UP_RIGHT, dims, blockers)
        return frozenset(loc for loc in x5 if in_bounds_142ca369(loc, dims))
    raise ValueError("unsupported bar-only layout for 142ca369")


def output_cells_for_group_142ca369(
    objs: tuple[Object, ...],
    dims: IntegerTuple,
    blockers: Indices = frozenset(),
) -> Indices:
    x0 = tuple(sorted(objs, key=ulcorner))
    x1 = tuple(classify_object_142ca369(obj) for obj in x0)
    x2 = set(merge(tuple(toindices(obj) for obj in x0)))
    x3 = frozenset(ulcorner(obj) for obj, sig in zip(x0, x1) if sig[0] == "dot")
    x4 = frozenset((uppermost(obj), leftmost(obj)) for obj, sig in zip(x0, x1) if sig[0] == "vbar")
    x5 = frozenset((lowermost(obj), leftmost(obj)) for obj, sig in zip(x0, x1) if sig[0] == "vbar")
    x6 = tuple((obj, sig[1]) for obj, sig in zip(x0, x1) if sig[0] == "L")
    if x6:
        for x7, x8 in x6:
            x9, x10 = l_start_and_direction_142ca369(x7, x8)
            x11 = trace_l_ray_142ca369(x9, x10, dims, x3, x4, x5, blockers)
            x2 |= x11
        return frozenset(x2)
    return bar_only_cells_142ca369(x0, dims, blockers)


def color_groups_142ca369(grid: Grid) -> tuple[tuple[Integer, tuple[Object, ...]], ...]:
    x0 = objects(grid, T, F, T)
    x1: dict[int, list[Object]] = {}
    for x2 in x0:
        x3 = color(x2)
        x1.setdefault(x3, []).append(x2)
    return tuple((x2, tuple(sorted(x3, key=ulcorner))) for x2, x3 in sorted(x1.items()))


def paint_group_cells_142ca369(
    grid: Grid,
    color_value: Integer,
    cells: Indices,
) -> Grid:
    return fill(grid, color_value, cells)
