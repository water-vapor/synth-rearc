from arc2.core import *


NON_GRAY_COLORS_2C737E39 = tuple(color for color in range(ONE, TEN) if color != FIVE)


def _connected_patch_2c737e39(
    height_value: Integer,
    width_value: Integer,
    count: Integer,
) -> Indices:
    x0 = tuple((i, j) for i in range(height_value) for j in range(width_value))
    while True:
        x1 = {choice(x0)}
        while len(x1) < count:
            x2 = []
            for x3 in tuple(x1):
                for x4 in dneighbors(x3):
                    if x4 in x1:
                        continue
                    if not (ZERO <= x4[0] < height_value and ZERO <= x4[1] < width_value):
                        continue
                    x2.append(x4)
            if len(x2) == ZERO:
                break
            x1.add(choice(x2))
        x5 = frozenset(x1)
        if len(x5) != count:
            continue
        if height(x5) == ONE or width(x5) == ONE:
            continue
        return x5


def _local_structure_2c737e39() -> tuple[str, Object, Object]:
    while True:
        x0 = randint(TWO, FIVE)
        x1 = randint(TWO, SIX)
        x2 = randint(max(THREE, min(x0, x1) + ONE), min(x0 * x1, NINE))
        x3 = _connected_patch_2c737e39(x0, x1, x2)
        x4 = choice(("internal", "internal", "internal", "adjacent"))
        if x4 == "internal":
            x5 = choice(tuple(x3))
        else:
            x6 = frozenset().union(*(dneighbors(x7) for x7 in x3)) - x3
            if len(x6) == ZERO:
                continue
            x5 = choice(tuple(x6))
        x8 = frozenset(shift(x3, invert(x5)))
        x9 = size(x8) - (ONE if x4 == "internal" else ZERO)
        x10 = randint(TWO, min(FIVE, x9))
        x11 = sample(NON_GRAY_COLORS_2C737E39, x10)
        x12 = []
        x13 = []
        x14 = []
        for x15 in sorted(x8):
            if x4 == "internal" and x15 == ORIGIN:
                x12.append((FIVE, x15))
                continue
            x16 = choice(x11)
            x12.append((x16, x15))
            x13.append((x16, x15))
            x14.append(x16)
        if len(set(x14)) < TWO:
            continue
        x17 = frozenset(x12)
        x18 = frozenset(x13)
        if height(x18) == ONE or width(x18) == ONE:
            continue
        if x4 == "adjacent":
            if manhattan(x18, initset(ORIGIN)) != ONE:
                continue
        else:
            x19 = intersection(toindices(x18), dneighbors(ORIGIN))
            if len(x19) == ZERO:
                continue
        x20 = branch(x4 == "internal", x17, combine(x17, frozenset({(FIVE, ORIGIN)})))
        return x4, x20, x18


def _fits_2c737e39(
    patch: Patch,
    dims: IntegerTuple,
) -> Boolean:
    return (
        uppermost(patch) >= ZERO
        and leftmost(patch) >= ZERO
        and lowermost(patch) < dims[0]
        and rightmost(patch) < dims[1]
    )


def generate_2c737e39(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1, x2 = _local_structure_2c737e39()
        x3 = toindices(x1)
        x4 = max(NINE, height(x3) + height(x2) + TWO)
        x5 = max(NINE, width(x3) + width(x2) + TWO)
        x6 = min(16, x4 + unifint(diff_lb, diff_ub, (ONE, THREE)))
        x7 = min(16, x5 + unifint(diff_lb, diff_ub, (ONE, THREE)))
        if x4 > x6 or x5 > x7:
            continue
        x8 = (x6, x7)
        x9 = tuple(
            (i, j)
            for i in range(x8[0])
            for j in range(x8[1])
            if _fits_2c737e39(shift(x3, (i, j)), x8)
        )
        x9 = list(x9)
        shuffle(x9)
        for x10 in x9:
            x11 = shift(x1, x10)
            x12 = toindices(x11)
            x13 = []
            for i in range(x8[0]):
                for j in range(x8[1]):
                    x14 = (i, j)
                    if x14 in x12:
                        continue
                    if len(intersection(dneighbors(x14), x12)) > ZERO:
                        continue
                    x15 = shift(x2, x14)
                    x16 = toindices(x15)
                    if not _fits_2c737e39(x16, x8):
                        continue
                    if len(intersection(x16, x12)) > ZERO:
                        continue
                    if manhattan(x16, x12) <= ONE:
                        continue
                    x17 = abs(i - x10[0]) + abs(j - x10[1])
                    if x17 < THREE:
                        continue
                    x13.append(x14)
            if len(x13) == ZERO:
                continue
            x18 = choice(x13)
            x19 = canvas(ZERO, x8)
            x20 = paint(x19, x11)
            x21 = fill(x20, FIVE, initset(x18))
            x22 = fill(x21, ZERO, initset(x18))
            x23 = paint(x22, shift(x2, x18))
            return {"input": x21, "output": x23}
