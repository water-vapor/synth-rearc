from arc2.core import *

from .verifier import verify_25e02866


SLOT_BAGS_25E02866 = {
    TWO: (
        ("tl", "br"),
        ("tr", "bl"),
    ),
    THREE: (
        ("tl", "tr", "bl"),
        ("tl", "tr", "br"),
        ("tl", "bl", "br"),
        ("tr", "bl", "br"),
    ),
    FOUR: (("tl", "tr", "bl", "br"),),
}

SIZE_BAGS_25E02866 = {
    TWO: (
        (ONE, THREE),
        (TWO, TWO),
    ),
    THREE: (
        (ONE, TWO, THREE),
        (ONE, TWO, FOUR),
        (TWO, TWO, THREE),
        (ONE, THREE, THREE),
    ),
    FOUR: (
        (ONE, TWO, TWO, THREE),
        (ONE, TWO, THREE, THREE),
        (ONE, TWO, THREE, FOUR),
        (ONE, THREE, THREE, FOUR),
        (TWO, TWO, THREE, FOUR),
    ),
}


def _neighbors_25e02866(
    loc: IntegerTuple,
    size: Integer,
) -> frozenset[IntegerTuple]:
    i, j = loc
    out = set()
    if i > ONE:
        out.add((i - ONE, j))
    if i < size - TWO:
        out.add((i + ONE, j))
    if j > ONE:
        out.add((i, j - ONE))
    if j < size - TWO:
        out.add((i, j + ONE))
    return frozenset(out)


def _interior_25e02866(
    size: Integer,
) -> frozenset[IntegerTuple]:
    return frozenset(
        (i, j)
        for i in range(ONE, size - ONE)
        for j in range(ONE, size - ONE)
    )


def _grow_component_25e02866(
    ncells: Integer,
    size: Integer,
    occupied: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple] | None:
    x0 = _interior_25e02866(size) - occupied
    if len(x0) < ncells:
        return None
    x1 = choice(tuple(x0))
    x2 = {x1}
    while len(x2) < ncells:
        x3 = set()
        for x4 in tuple(x2):
            x3 |= _neighbors_25e02866(x4, size)
        x3 = tuple((x3 & x0) - x2)
        if len(x3) == ZERO:
            return None
        x2.add(choice(x3))
    return frozenset(x2)


def _slot_anchors_25e02866(
    board_size: Integer,
    patch_size: Integer,
) -> dict[str, IntegerTuple]:
    x0 = board_size - patch_size - THREE
    x1 = board_size - patch_size - ONE
    return {
        "tl": (randint(ONE, THREE), randint(ONE, THREE)),
        "tr": (randint(ONE, THREE), randint(x0, x1)),
        "bl": (randint(x0, x1), randint(ONE, THREE)),
        "br": (randint(x0, x1), randint(x0, x1)),
    }


def _paint_patch_25e02866(
    grid: Grid,
    anchor: IntegerTuple,
    patch_size: Integer,
    fill_color: Integer,
    accent_color: Integer,
    component: frozenset[IntegerTuple],
) -> Grid:
    x0 = canvas(fill_color, (patch_size, patch_size))
    x1 = fill(x0, accent_color, component)
    x2 = shift(asobject(x1), anchor)
    return paint(grid, x2)


def _mark_profile_ok_25e02866(
    occupied: frozenset[IntegerTuple],
) -> Boolean:
    x0 = frozenset(i for i, _ in occupied)
    x1 = frozenset(j for _, j in occupied)
    return both(greater(len(x0), ONE), greater(len(x1), ONE))


def generate_25e02866(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x1 = add(x0, TWO)
        x2 = add(double(x1), SIX)
        x3 = sample(tuple(range(ONE, TEN)), add(x0, TWO))
        x4 = x3[ZERO]
        x5 = x3[ONE]
        x6 = list(x3[TWO:])
        shuffle(x6)
        x7 = list(choice(SIZE_BAGS_25E02866[x0]))
        shuffle(x7)
        x8 = choice(SLOT_BAGS_25E02866[x0])
        x9 = _slot_anchors_25e02866(x2, x1)
        x10 = canvas(x4, (x2, x2))
        x11 = canvas(x5, (x1, x1))
        x12 = frozenset()
        x13 = []
        x14 = F
        for x15, x16 in zip(x7, x6):
            x17 = None
            for _ in range(80):
                x17 = _grow_component_25e02866(x15, x1, x12)
                if x17 is not None:
                    break
            if x17 is None:
                x14 = T
                break
            x12 = combine(x12, x17)
            x11 = fill(x11, x16, x17)
            x13.append((x17, x16))
        if x14:
            continue
        if not _mark_profile_ok_25e02866(x12):
            continue
        for x18, (x19, x20) in zip(x8, x13):
            x21 = x9[x18]
            x10 = _paint_patch_25e02866(x10, x21, x1, x5, x20, x19)
        if verify_25e02866(x10) != x11:
            continue
        return {"input": x10, "output": x11}
