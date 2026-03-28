from arc2.core import *

from .verifier import verify_5751f35e


FAMILIES_5751F35E = (
    {
        "size": TEN,
        "margins": (ZERO, ONE, THREE),
    },
    {
        "size": TEN,
        "margins": (ONE, TWO),
    },
    {
        "size": 12,
        "margins": (ZERO, TWO, FOUR),
    },
)


def _square_patch_5751f35e(
    size_value: Integer,
    margin: Integer,
) -> Indices:
    x0 = astuple(margin, margin)
    x1 = decrement(subtract(size_value, margin))
    x2 = astuple(x1, x1)
    return backdrop(frozenset({x0, x2}))


def _sample_clues_5751f35e(
    patch: Indices,
    size_value: Integer,
    margin: Integer,
) -> Indices:
    x0 = tuple(patch)
    x1 = size(patch)
    x2 = decrement(subtract(size_value, margin))
    x3 = tuple(x4 for x4 in x0 if x4[ZERO] == margin)
    x5 = tuple(x6 for x6 in x0 if x6[ZERO] == x2)
    x7 = tuple(x8 for x8 in x0 if x8[ONE] == margin)
    x9 = tuple(x10 for x10 in x0 if x10[ONE] == x2)
    x11 = set()
    x12 = choice(("top", "bottom", "both"))
    x13 = choice(("left", "right", "both"))
    if x12 in ("top", "both"):
        x11.add(choice(x3))
    if x12 in ("bottom", "both"):
        x11.add(choice(x5))
    if x13 in ("left", "both"):
        x11.add(choice(x7))
    if x13 in ("right", "both"):
        x11.add(choice(x9))
    x14 = tuple(x15 for x15 in x0 if x15 not in x11)
    x16 = max(len(x11), x1 // FOUR)
    x17 = max(x16, (x1 * TWO) // THREE)
    x18 = randint(x16, x17)
    x19 = min(len(x14), subtract(x18, len(x11)))
    x20 = frozenset(x11)
    if x19 > ZERO:
        x20 = combine(x20, sample(x14, x19))
    return x20


def generate_5751f35e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(FAMILIES_5751F35E)
        x1 = x0["size"]
        x2 = x0["margins"]
        x3 = sample((ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE), len(x2))
        x4 = canvas(ZERO, astuple(x1, x1))
        for x5, x6 in zip(x3, x2):
            x7 = _square_patch_5751f35e(x1, x6)
            x4 = fill(x4, x5, x7)
        x8 = canvas(ZERO, astuple(x1, x1))
        for x9, x10 in zip(x3, x2):
            x11 = ofcolor(x4, x9)
            x12 = _sample_clues_5751f35e(x11, x1, x10)
            x8 = fill(x8, x9, x12)
        if x8 == x4:
            continue
        if verify_5751f35e(x8) != x4:
            continue
        return {"input": x8, "output": x4}
