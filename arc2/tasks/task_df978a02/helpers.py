from arc2.core import *


CARDINALS_DF978A02 = (
    (-1, ZERO),
    (ONE, ZERO),
    (ZERO, -1),
    (ZERO, ONE),
)

LARGE_TEMPLATES_DF978A02 = (
    frozenset(
        {
            (-5, -1),
            (-5, ZERO),
            (-5, ONE),
            (-4, -1),
            (-4, ZERO),
            (-4, ONE),
            (-3, -1),
            (-3, ZERO),
            (-3, ONE),
            (-2, -1),
            (-2, ZERO),
            (-2, ONE),
            (-1, -1),
            (-1, ZERO),
            (-1, ONE),
            (ZERO, ZERO),
        }
    ),
    frozenset(
        {
            (-2, -2),
            (-2, -1),
            (-2, ZERO),
            (-2, ONE),
            (-2, TWO),
            (-1, -1),
            (-1, ZERO),
            (-1, ONE),
            (ZERO, ZERO),
        }
    ),
    frozenset(
        {
            (-3, -4),
            (-3, -3),
            (-3, -2),
            (-3, -1),
            (-3, ZERO),
            (-3, ONE),
            (-3, TWO),
            (-3, THREE),
            (-3, FOUR),
            (-2, -3),
            (-2, -2),
            (-2, -1),
            (-2, ZERO),
            (-2, ONE),
            (-2, TWO),
            (-2, THREE),
            (-1, -2),
            (-1, -1),
            (-1, ZERO),
            (-1, ONE),
            (-1, TWO),
            (ZERO, ZERO),
        }
    ),
    frozenset(
        {
            (-3, -2),
            (-3, -1),
            (-3, ZERO),
            (-3, ONE),
            (-3, TWO),
            (-2, -4),
            (-2, -3),
            (-2, -2),
            (-2, -1),
            (-2, ZERO),
            (-2, ONE),
            (-2, TWO),
            (-2, THREE),
            (-1, -2),
            (-1, -1),
            (-1, ZERO),
            (-1, ONE),
            (-1, TWO),
            (ZERO, ZERO),
        }
    ),
)

SMALL_TEMPLATES_DF978A02 = (
    frozenset(
        {
            (-2, ZERO),
            (-1, -1),
            (-1, ZERO),
            (ZERO, ZERO),
        }
    ),
    frozenset(
        {
            (-2, -1),
            (-2, ZERO),
            (-2, ONE),
            (-2, TWO),
            (-1, -1),
            (-1, ZERO),
            (-1, ONE),
            (ZERO, ZERO),
        }
    ),
    frozenset(
        {
            (-5, FOUR),
            (-4, THREE),
            (-4, FOUR),
            (-3, TWO),
            (-3, THREE),
            (-2, -2),
            (-2, -1),
            (-2, ONE),
            (-2, TWO),
            (-1, -1),
            (-1, ZERO),
            (-1, ONE),
            (ZERO, ZERO),
        }
    ),
)


def opposite_df978a02(
    direction: IntegerTuple,
) -> IntegerTuple:
    return (-direction[ZERO], -direction[ONE])


def transform_template_df978a02(
    template: Indices,
    direction: IntegerTuple,
) -> Indices:
    if direction == (ONE, ZERO):
        return template
    if direction == (-1, ZERO):
        return frozenset({(-i, j) for i, j in template})
    if direction == (ZERO, ONE):
        return frozenset({(j, -i) for i, j in template})
    return frozenset({(-j, i) for i, j in template})


def place_template_df978a02(
    template: Indices,
    direction: IntegerTuple,
    tip: IntegerTuple,
) -> Indices:
    x0 = transform_template_df978a02(template, direction)
    x1 = shift(x0, tip)
    return frozenset(x1)


def foreground_focus_df978a02(
    objs: Objects,
) -> IntegerTuple:
    x0 = mapply(toindices, objs)
    return centerofmass(x0)


def direction_df978a02(
    obj: Patch,
    focus: IntegerTuple,
) -> IntegerTuple:
    oi, oj = centerofmass(obj)
    fi, fj = focus
    di = fi - oi
    dj = fj - oj
    if abs(di) >= abs(dj):
        return (ONE if di > ZERO else -1, ZERO)
    return (ZERO, ONE if dj > ZERO else -1)


def edge_cells_df978a02(
    patch: Patch,
    direction: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    inds = toindices(patch)
    if direction == (-1, ZERO):
        row = uppermost(patch)
        return tuple(sorted((loc for loc in inds if loc[ZERO] == row), key=last))
    if direction == (ONE, ZERO):
        row = lowermost(patch)
        return tuple(sorted((loc for loc in inds if loc[ZERO] == row), key=last))
    if direction == (ZERO, -1):
        col = leftmost(patch)
        return tuple(sorted((loc for loc in inds if loc[ONE] == col), key=first))
    col = rightmost(patch)
    return tuple(sorted((loc for loc in inds if loc[ONE] == col), key=first))


def tip_cell_df978a02(
    obj: Patch,
    direction: IntegerTuple,
) -> IntegerTuple:
    x0 = edge_cells_df978a02(obj, direction)
    return x0[len(x0) // TWO]


def cap_patch_df978a02(
    obj: Patch,
    direction: IntegerTuple,
) -> Indices:
    x0 = opposite_df978a02(direction)
    x1 = edge_cells_df978a02(obj, x0)
    x2 = len(x1)
    x3 = x1 if x2 <= THREE else x1[(x2 - THREE) // TWO:(x2 - THREE) // TWO + THREE]
    x4 = shift(frozenset(x3), x0)
    return frozenset(x4)
