from arc2.core import *

from .verifier import verify_fafd9572


TRI_SHAPE_FAFD9572 = frozenset({
    (ZERO, ZERO),
    (ZERO, ONE),
    (ONE, ZERO),
})
HEX_SHAPE_A_FAFD9572 = frozenset({
    (ZERO, ZERO),
    (ZERO, ONE),
    (ONE, ZERO),
    (ONE, TWO),
    (TWO, ONE),
    (TWO, TWO),
})
HEX_SHAPE_B_FAFD9572 = frozenset({
    (ZERO, ONE),
    (ONE, ZERO),
    (ONE, ONE),
    (ONE, TWO),
    (TWO, ZERO),
    (TWO, TWO),
})
SHAPE_POOL_FAFD9572 = (
    TRI_SHAPE_FAFD9572,
    HEX_SHAPE_A_FAFD9572,
    HEX_SHAPE_B_FAFD9572,
    HEX_SHAPE_A_FAFD9572,
    HEX_SHAPE_B_FAFD9572,
)
PALETTE_COLORS_FAFD9572 = interval(TWO, EIGHT, ONE)
TRANSFORMS_FAFD9572 = (
    identity,
    hmirror,
    vmirror,
    compose(hmirror, vmirror),
    dmirror,
    cmirror,
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
)
LAYOUTS_FAFD9572 = ("left", "right", "top")


def _shape_variants_fafd9572(
    patch: Indices,
) -> tuple[Indices, ...]:
    x0 = set()
    x1 = []
    for x2 in TRANSFORMS_FAFD9572:
        x3 = normalize(x2(patch))
        x4 = tuple(sorted(x3))
        if x4 in x0:
            continue
        x0.add(x4)
        x1.append(x3)
    return tuple(x1)


def _sample_shape_fafd9572() -> Indices:
    x0 = choice(SHAPE_POOL_FAFD9572)
    x1 = _shape_variants_fafd9572(x0)
    return choice(x1)


def _sample_palette_colors_fafd9572(
    patch: Indices,
) -> tuple[Integer, ...]:
    x0 = order(patch, identity)
    x1: dict[IntegerTuple, Integer] = {}
    for x2 in x0:
        x3 = {x1[x4] for x4 in dneighbors(x2) if x4 in x1}
        x5 = tuple(x6 for x6 in PALETTE_COLORS_FAFD9572 if x6 not in x3)
        x1[x2] = choice(x5)
    x7 = tuple(x1[x8] for x8 in x0)
    if len(set(x7)) > ONE:
        return x7
    x9 = last(x0)
    x10 = {x1[x11] for x11 in dneighbors(x9) if x11 in x1 and x11 != x9}
    x12 = tuple(x13 for x13 in PALETTE_COLORS_FAFD9572 if x13 not in x10 and x13 != x1[x9])
    x1[x9] = choice(x12)
    return tuple(x1[x14] for x14 in x0)


def _support_fafd9572(
    patch: Indices,
    anchors: tuple[IntegerTuple, ...],
) -> Indices:
    x0 = frozenset()
    for x1 in anchors:
        x0 = combine(x0, shift(patch, x1))
    return x0


def generate_fafd9572(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_shape_fafd9572()
        x1 = order(x0, identity)
        x2 = shape(x0)
        x3 = add(x2, ONE)
        x4 = tuple(multiply(x5, x3) for x5 in x1)
        x5 = _support_fafd9572(x0, x4)
        x6 = shape(x5)
        x7 = _sample_palette_colors_fafd9572(x0)
        x8 = choice(LAYOUTS_FAFD9572)
        x9 = unifint(diff_lb, diff_ub, (TWO, SIX))
        x10 = randint(ZERO, THREE)
        x11 = randint(ZERO, THREE)
        x12 = randint(ZERO, THREE)
        x13 = randint(ZERO, THREE)
        if x8 == "left":
            x14 = astuple(add(max(x2[ZERO], x6[ZERO]), add(x10, x11)), add(add(x2[ONE], x6[ONE]), add(x9, add(x12, x13))))
            x15 = astuple(add(x10, randint(ZERO, subtract(max(x2[ZERO], x6[ZERO]), x2[ZERO]))), x12)
            x16 = astuple(add(x10, randint(ZERO, subtract(max(x2[ZERO], x6[ZERO]), x6[ZERO]))), add(add(x12, x2[ONE]), x9))
        elif x8 == "right":
            x14 = astuple(add(max(x2[ZERO], x6[ZERO]), add(x10, x11)), add(add(x2[ONE], x6[ONE]), add(x9, add(x12, x13))))
            x15 = astuple(add(x10, randint(ZERO, subtract(max(x2[ZERO], x6[ZERO]), x2[ZERO]))), add(add(x12, x6[ONE]), x9))
            x16 = astuple(add(x10, randint(ZERO, subtract(max(x2[ZERO], x6[ZERO]), x6[ZERO]))), x12)
        else:
            x14 = astuple(add(add(x2[ZERO], x6[ZERO]), add(x9, add(x10, x11))), add(max(x2[ONE], x6[ONE]), add(x12, x13)))
            x15 = astuple(x10, add(x12, randint(ZERO, subtract(max(x2[ONE], x6[ONE]), x2[ONE]))))
            x16 = astuple(add(add(x10, x2[ZERO]), x9), add(x12, randint(ZERO, subtract(max(x2[ONE], x6[ONE]), x6[ONE]))))
        x17 = max(x14[ZERO], unifint(diff_lb, diff_ub, (10, 18)))
        x18 = max(x14[ONE], unifint(diff_lb, diff_ub, (12, 20)))
        x19 = astuple(randint(ZERO, subtract(x17, x14[ZERO])), randint(ZERO, subtract(x18, x14[ONE])))
        x20 = add(x15, x19)
        x21 = add(x16, x19)
        x22 = canvas(ZERO, astuple(x17, x18))
        x23 = x22
        for x24, x25 in zip(x1, x7):
            x26 = frozenset({add(x20, x24)})
            x22 = fill(x22, x25, x26)
            x23 = fill(x23, x25, x26)
        x27 = recolor(ONE, x0)
        for x28, x29 in zip(x4, x7):
            x30 = add(x21, x28)
            x31 = shift(x27, x30)
            x32 = shift(recolor(x29, x0), x30)
            x22 = paint(x22, x31)
            x23 = paint(x23, x32)
        if x22 == x23:
            continue
        if verify_fafd9572(x22) != x23:
            continue
        return {"input": x22, "output": x23}
