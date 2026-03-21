from arc2.core import *


_UPWARD_T_d5c634a2 = frozenset({
    (ZERO, ONE),
    (ONE, ZERO),
    (ONE, ONE),
    (ONE, TWO),
})

_DOWNWARD_T_d5c634a2 = frozenset({
    (ZERO, ZERO),
    (ZERO, ONE),
    (ZERO, TWO),
    (ONE, ONE),
})

_LEFT_PATCHES_d5c634a2 = (
    frozenset(),
    frozenset({(ZERO, ZERO)}),
    frozenset({(ZERO, ZERO), (TWO, ZERO)}),
    frozenset({(ZERO, ZERO), (TWO, ZERO), (ZERO, TWO)}),
    frozenset({(ZERO, ZERO), (TWO, ZERO), (ZERO, TWO), (TWO, TWO)}),
)

_RIGHT_PATCHES_d5c634a2 = tuple(
    shift(patch, tojvec(THREE))
    for patch in _LEFT_PATCHES_d5c634a2
)


def verify_d5c634a2(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = sizefilter(x0, FOUR)
    x2 = compose(toindices, normalize)
    x3 = matcher(x2, _UPWARD_T_d5c634a2)
    x4 = matcher(x2, _DOWNWARD_T_d5c634a2)
    x5 = sfilter(x1, x3)
    x6 = sfilter(x1, x4)
    x7 = size(x5)
    x8 = size(x6)
    x9 = canvas(ZERO, (THREE, SIX))
    x10 = fill(x9, THREE, _LEFT_PATCHES_d5c634a2[x7])
    x11 = fill(x10, ONE, _RIGHT_PATCHES_d5c634a2[x8])
    return x11
