from synth_rearc.core import *


HEIGHT_BOUNDS_99CAAF76 = (EIGHT, 22)
WIDTH_BOUNDS_99CAAF76 = (FIVE, 22)
OBJECT_COUNT_BOUNDS_99CAAF76 = (ONE, FOUR)
ARM_COLORS_99CAAF76 = (ZERO, TWO, THREE, FIVE, SIX, SEVEN, NINE)

RIGHT_TEMPLATE_99CAAF76 = {
    "shape": (THREE, SIX),
    "ones": ((ZERO, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ZERO)),
    "motif": ((ZERO, FOUR), (ONE, THREE), (ONE, FOUR), (ONE, FIVE), (TWO, FOUR)),
}
LEFT_TEMPLATE_99CAAF76 = {
    "shape": (THREE, SIX),
    "ones": ((ZERO, FIVE), (ONE, THREE), (ONE, FOUR), (TWO, FIVE)),
    "motif": ((ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE)),
}
DOWN_TEMPLATE_99CAAF76 = {
    "shape": (SIX, THREE),
    "ones": ((ZERO, ZERO), (ZERO, TWO), (ONE, ONE), (TWO, ONE)),
    "motif": ((THREE, ONE), (FOUR, ZERO), (FOUR, ONE), (FOUR, TWO), (FIVE, ONE)),
}
UP_TEMPLATE_99CAAF76 = {
    "shape": (SIX, THREE),
    "ones": ((THREE, ONE), (FOUR, ONE), (FIVE, ZERO), (FIVE, TWO)),
    "motif": ((ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE)),
}
TEMPLATES_99CAAF76 = {
    RIGHT: RIGHT_TEMPLATE_99CAAF76,
    LEFT: LEFT_TEMPLATE_99CAAF76,
    DOWN: DOWN_TEMPLATE_99CAAF76,
    UP: UP_TEMPLATE_99CAAF76,
}


def _origin_99caaf76(
    direction: IntegerTuple,
    orth: Integer,
    dims: Tuple,
    output: Boolean,
) -> Tuple:
    x0, x1 = dims
    x2, x3 = TEMPLATES_99CAAF76[direction]["shape"]
    if direction == RIGHT:
        return (orth, branch(output, x1 - x3, ZERO))
    if direction == LEFT:
        return (orth, branch(output, ZERO, x1 - x3))
    if direction == DOWN:
        return (branch(output, x0 - x2, ZERO), orth)
    return (branch(output, ZERO, x0 - x2), orth)


def _orth_99caaf76(
    direction: IntegerTuple,
    dims: Tuple,
) -> Integer:
    x0, x1 = dims
    x2, x3 = TEMPLATES_99CAAF76[direction]["shape"]
    if direction in (RIGHT, LEFT):
        return randint(ZERO, x0 - x2)
    return randint(ZERO, x1 - x3)


def _rotate_arms_99caaf76(
    arms: Tuple,
) -> Tuple:
    x0, x1, x2, x3 = arms
    return (x3, x2, x1, x0)


def _render_object_99caaf76(
    top: Integer,
    left: Integer,
    direction: IntegerTuple,
    arms: Tuple,
) -> Object:
    x0 = TEMPLATES_99CAAF76[direction]
    x1 = frozenset((ONE, (top + x2, left + x3)) for x2, x3 in x0["ones"])
    x4, x5, x6, x7 = arms
    x8 = (x4, x5, FOUR, x6, x7)
    x9 = frozenset(
        (x10, (top + x11, left + x12))
        for x10, (x11, x12) in zip(x8, x0["motif"])
    )
    return combine(x1, x9)


def _halo_99caaf76(
    obj: Object,
    dims: Tuple,
) -> Indices:
    x0, x1 = dims
    x2 = set()
    for x3, x4 in toindices(obj):
        for x5 in (NEG_ONE, ZERO, ONE):
            for x6 in (NEG_ONE, ZERO, ONE):
                x7 = x3 + x5
                x8 = x4 + x6
                if 0 <= x7 < x0 and 0 <= x8 < x1:
                    x2.add((x7, x8))
    return frozenset(x2)


def generate_99caaf76(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_99CAAF76)
        x1 = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_99CAAF76)
        x2 = []
        if x1 >= EIGHT:
            x2.extend((RIGHT, LEFT))
        if x0 >= EIGHT:
            x2.extend((DOWN, UP))
        if len(x2) == ZERO:
            continue
        x3 = unifint(diff_lb, diff_ub, OBJECT_COUNT_BOUNDS_99CAAF76)
        x4 = canvas(EIGHT, (x0, x1))
        x5 = canvas(EIGHT, (x0, x1))
        x6 = set()
        x7 = set()
        x8 = T
        for _ in range(x3):
            x9 = F
            for _ in range(96):
                x10 = choice(tuple(x2))
                x11 = _orth_99caaf76(x10, (x0, x1))
                x12 = tuple(sample(ARM_COLORS_99CAAF76, FOUR))
                x13, x14 = _origin_99caaf76(x10, x11, (x0, x1), F)
                x15 = _origin_99caaf76(x10, x11, (x0, x1), T)
                x16 = _render_object_99caaf76(x13, x14, x10, x12)
                x17 = _render_object_99caaf76(x15[ZERO], x15[ONE], x10, _rotate_arms_99caaf76(x12))
                x18 = _halo_99caaf76(x16, (x0, x1))
                x19 = _halo_99caaf76(x17, (x0, x1))
                if any(x20 in x6 for x20 in x18):
                    continue
                if any(x21 in x7 for x21 in x19):
                    continue
                x4 = paint(x4, x16)
                x5 = paint(x5, x17)
                x6 |= set(x18)
                x7 |= set(x19)
                x9 = T
                break
            if not x9:
                x8 = F
                break
        if not x8 or x4 == x5:
            continue
        return {"input": x4, "output": x5}
