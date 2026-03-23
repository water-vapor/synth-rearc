from arc2.core import *


L_PATCHES_1E5D6875 = (
    frozenset({ORIGIN, DOWN, UNITY}),
    frozenset({ORIGIN, RIGHT, UNITY}),
    frozenset({RIGHT, DOWN, UNITY}),
)


def direct_halo_1e5d6875(patch: Patch) -> Indices:
    x0 = toindices(patch)
    x1 = set(x0)
    for x2 in x0:
        x1 |= dneighbors(x2)
    return frozenset(x1)


def shift_vector_1e5d6875(obj: Object) -> IntegerTuple:
    x0 = toindices(normalize(obj))
    if ORIGIN not in x0:
        x1 = NEG_UNITY
    elif RIGHT not in x0:
        x1 = UP_RIGHT
    elif DOWN not in x0:
        x1 = DOWN_LEFT
    else:
        x1 = UNITY
    return branch(equality(color(obj), FIVE), x1, invert(x1))


def shifted_copy_1e5d6875(obj: Object) -> Object:
    x0 = shift_vector_1e5d6875(obj)
    x1 = shift(obj, x0)
    x2 = branch(equality(color(obj), FIVE), FOUR, THREE)
    return recolor(x2, x1)
