from synth_rearc.core import *

from .helpers import (
    classify_object_142ca369,
    color_groups_142ca369,
    make_dot_object_142ca369,
    make_hbar_object_142ca369,
    make_l_object_142ca369,
    make_vbar_object_142ca369,
    output_cells_for_group_142ca369,
)


def _sample_l_group_142ca369(
    color_value: Integer,
    dims: IntegerTuple,
) -> tuple[Object, ...] | None:
    x0, x1 = dims
    x2 = choice((ONE, ONE, TWO, TWO, THREE))
    x3 = list(product(interval(ZERO, subtract(x0, ONE), ONE), interval(ZERO, subtract(x1, ONE), ONE)))
    shuffle(x3)
    x4: list[Object] = []
    x5: set[IntegerTuple] = set()
    x6 = ("nw", "nw", "ne", "sw", "se")
    for x7, x8 in x3:
        if either(x7 >= subtract(x0, ONE), x8 >= subtract(x1, ONE)):
            continue
        x9 = make_l_object_142ca369(color_value, (x7, x8), choice(x6))
        x10 = set(toindices(x9))
        if x10 & x5:
            continue
        x4.append(x9)
        x5 |= x10
        if len(x4) == x2:
            return tuple(x4)
    return None


def _sample_l_dot_group_142ca369(
    color_value: Integer,
    dims: IntegerTuple,
) -> tuple[Object, ...] | None:
    x0, x1 = dims
    x2 = interval(ZERO, subtract(x0, SIX), ONE)
    x3 = interval(ZERO, subtract(x1, SIX), ONE)
    x4 = list(product(x2, x3))
    shuffle(x4)
    for x5, x6 in x4:
        x7 = make_l_object_142ca369(color_value, (x5, x6), "nw")
        x8 = lrcorner(x7)
        x9 = minimum((subtract(x0, x8[0]), subtract(x1, x8[1])))
        if x9 < FIVE:
            continue
        x10 = randint(TWO, subtract(x9, TWO))
        x11 = (x8[0] + x10 + ONE, x8[1] + x10)
        if not both(x11[0] < x0, x11[1] < x1):
            continue
        x12 = make_dot_object_142ca369(color_value, x11)
        return (x7, x12)
    return None


def _sample_single_bar_group_142ca369(
    color_value: Integer,
    dims: IntegerTuple,
) -> tuple[Object, ...] | None:
    x0, x1 = dims
    x2 = choice(("v_upper_left", "v_lower_left", "h_upper_right", "h_lower_left"))
    if x2 == "v_upper_left":
        x3 = randint(ONE, subtract(x0 // TWO, FOUR))
        x4 = randint(ONE, maximum((ONE, subtract(x1 // TWO, THREE))))
        return (make_vbar_object_142ca369(color_value, (x3, x4)),)
    if x2 == "v_lower_left":
        x3 = randint(add(x0 // TWO, ONE), subtract(x0, FOUR))
        x4 = randint(ONE, maximum((ONE, subtract(x1 // TWO, THREE))))
        return (make_vbar_object_142ca369(color_value, (x3, x4)),)
    if x2 == "h_upper_right":
        x3 = randint(ONE, maximum((ONE, subtract(x0 // TWO, THREE))))
        x4 = randint(add(x1 // TWO, ONE), subtract(x1, FOUR))
        return (make_hbar_object_142ca369(color_value, (x3, x4)),)
    x3 = randint(add(x0 // TWO, ONE), subtract(x0, THREE))
    x4 = randint(ONE, maximum((ONE, subtract(x1 // TWO, FOUR))))
    return (make_hbar_object_142ca369(color_value, (x3, x4)),)


def _sample_bar_pair_group_142ca369(
    color_value: Integer,
    dims: IntegerTuple,
) -> tuple[Object, ...] | None:
    x0, x1 = dims
    x2 = choice(("v_tb", "v_lr", "h_diag"))
    if x2 == "v_tb":
        x3 = randint(add(x1 // TWO, NEG_ONE), add(x1 // TWO, ONE))
        x4 = randint(ONE, maximum((ONE, subtract(x0 // TWO, FOUR))))
        x5 = randint(add(x0 // TWO, ONE), subtract(x0, FOUR))
        if subtract(x5, x4) < FIVE:
            return None
        return (
            make_vbar_object_142ca369(color_value, (x4, x3)),
            make_vbar_object_142ca369(color_value, (x5, subtract(x3, ONE))),
        )
    if x2 == "v_lr":
        x3 = randint(add(x0 // TWO, NEG_TWO), add(x0 // TWO, ONE))
        x4 = randint(ONE, maximum((ONE, subtract(x0, FOUR))))
        return (
            make_vbar_object_142ca369(color_value, (x3, ZERO)),
            make_vbar_object_142ca369(color_value, (subtract(x3, ONE), subtract(x1, ONE))),
        )
    x5 = randint(ONE, maximum((ONE, subtract(x0 // TWO, FOUR))))
    x6 = randint(ONE, maximum((ONE, subtract(x1 // TWO, FOUR))))
    x7 = randint(add(x0 // TWO, ONE), subtract(x0, THREE))
    x8 = randint(add(x1 // TWO, ONE), subtract(x1, FOUR))
    return (
        make_hbar_object_142ca369(color_value, (x5, x6)),
        make_hbar_object_142ca369(color_value, (x7, x8)),
    )


def _sample_group_142ca369(
    color_value: Integer,
    dims: IntegerTuple,
) -> tuple[Object, ...] | None:
    x0 = choice(("l", "l", "l_dot", "single_bar", "bar_pair"))
    if x0 == "l":
        return _sample_l_group_142ca369(color_value, dims)
    if x0 == "l_dot":
        return _sample_l_dot_group_142ca369(color_value, dims)
    if x0 == "single_bar":
        return _sample_single_bar_group_142ca369(color_value, dims)
    return _sample_bar_pair_group_142ca369(color_value, dims)


def _group_cells_142ca369(
    objs: tuple[Object, ...],
    dims: IntegerTuple,
) -> tuple[Indices, Indices]:
    x0 = frozenset(merge(tuple(toindices(obj) for obj in objs)))
    x1 = output_cells_for_group_142ca369(objs, dims)
    return x0, x1


def _group_is_separate_142ca369(
    objs: tuple[Object, ...],
    dims: IntegerTuple,
) -> Boolean:
    x0 = canvas(ZERO, dims)
    x1 = _paint_objects_142ca369(x0, objs)
    x2 = objects(x1, T, F, T)
    return equality(len(x2), len(objs))


def _paint_objects_142ca369(
    grid: Grid,
    objs: tuple[Object, ...],
) -> Grid:
    x0 = grid
    for x1 in objs:
        x0 = paint(x0, x1)
    return x0


def _render_output_142ca369(
    grid: Grid,
) -> Grid:
    x0 = canvas(ZERO, shape(grid))
    x1 = color_groups_142ca369(grid)
    for x2, x3 in x1:
        x4 = []
        for x5, x6 in x1:
            if x5 == x2:
                continue
            for x7 in x6:
                if classify_object_142ca369(x7)[0] == "L":
                    continue
                x4.append(toindices(x7))
        x8 = frozenset(merge(tuple(x4))) if x4 else frozenset()
        x9 = output_cells_for_group_142ca369(x3, shape(grid), blockers=x8)
        x0 = fill(x0, x2, x9)
    return x0


def generate_142ca369(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (18, 24))
        x1 = branch(choice((T, F)), x0, unifint(diff_lb, diff_ub, (18, 24)))
        x2 = (x0, x1)
        x3 = canvas(ZERO, x2)
        x4: list[tuple[Integer, tuple[Object, ...], Indices]] = []
        x5: set[IntegerTuple] = set()
        x6 = list(difference(interval(ONE, TEN, ONE), initset(ZERO)))
        shuffle(x6)
        x7 = choice((THREE, THREE, FOUR, FOUR, FIVE))
        for x8 in x6:
            if len(x4) == x7:
                break
            for _ in range(40):
                x9 = _sample_group_142ca369(x8, x2)
                if x9 is None:
                    continue
                if not _group_is_separate_142ca369(x9, x2):
                    continue
                x10, x11 = _group_cells_142ca369(x9, x2)
                if x11 & x5:
                    continue
                x4.append((x8, x9, x11))
                x5 |= set(x11)
                x3 = _paint_objects_142ca369(x3, x9)
                break
        if len(x4) < THREE:
            continue
        x12 = _render_output_142ca369(x3)
        if x3 == x12:
            continue
        if len(color_groups_142ca369(x3)) < THREE:
            continue
        return {"input": x3, "output": x12}
