from __future__ import annotations

import itertools

from synth_rearc.core import *


def _find_panels_4c7dc4dd(I: Grid) -> tuple[int, tuple[Grid, ...]]:
    x0 = height(I)
    x1 = width(I)
    x2 = []
    for x3 in range(TWO, min(x0, x1) - ONE):
        x4 = x3 + TWO
        for x5 in range(x0 - x4 + ONE):
            for x6 in range(x1 - x4 + ONE):
                x7 = (
                    [(x5, x8) for x8 in range(x6, x6 + x4)] +
                    [(x5 + x4 - ONE, x8) for x8 in range(x6, x6 + x4)] +
                    [(x8, x6) for x8 in range(x5 + ONE, x5 + x4 - ONE)] +
                    [(x8, x6 + x4 - ONE) for x8 in range(x5 + ONE, x5 + x4 - ONE)]
                )
                x9 = {I[x10][x11] for x10, x11 in x7}
                if len(x9) == ONE:
                    x12 = next(iter(x9))
                    if x12 != ZERO:
                        x2.append((x3, x5, x6))
    x13 = max(x14 for x14, _, _ in x2)
    x15 = sorted((x16, x17) for x14, x16, x17 in x2 if x14 == x13)
    x18 = tuple(crop(I, (x19 + ONE, x20 + ONE), (x13, x13)) for x19, x20 in x15)
    return x13, x18


def _nonzero_indices_4c7dc4dd(G: Grid) -> frozenset[tuple[int, int]]:
    return frozenset((x0, x1) for x0, x2 in enumerate(G) for x1, x3 in enumerate(x2) if x3 != ZERO)


def _nonzero_palette_4c7dc4dd(G: Grid) -> tuple[int, ...]:
    return tuple(sorted({x0 for x1 in G for x0 in x1 if x0 != ZERO}))


def _overlay_4c7dc4dd(A: Grid, B: Grid) -> Grid:
    x0 = len(A)
    x1 = []
    for x2 in range(x0):
        x3 = []
        for x4 in range(x0):
            x5 = A[x2][x4]
            x6 = B[x2][x4]
            x3.append(x5 if x5 != ZERO else x6)
        x1.append(tuple(x3))
    return tuple(x1)


def _complement_mode_4c7dc4dd(A: Grid, B: Grid) -> bool:
    x0 = _nonzero_indices_4c7dc4dd(A)
    x1 = _nonzero_indices_4c7dc4dd(B)
    x2 = len(A)
    return len(intersection(x0, x1)) == ZERO and len(combine(x0, x1)) == x2 * x2


def _solve_complement_4c7dc4dd(source_full: Grid, target_seed: Grid) -> Grid:
    x0 = {}
    x1 = len(target_seed)
    for x2 in range(x1):
        for x3 in range(x1):
            x4 = target_seed[x2][x3]
            if x4 != ZERO:
                x5 = source_full[x2][x3]
                x6 = x0.get(x5)
                if x6 is None:
                    x0[x5] = x4
                elif x6 != x4:
                    raise ValueError((x5, x6, x4))
    x7 = []
    for x8 in range(x1):
        x9 = []
        for x10 in range(x1):
            x11 = target_seed[x8][x10]
            if x11 != ZERO:
                x9.append(ZERO)
            else:
                x9.append(x0[source_full[x8][x10]])
        x7.append(tuple(x9))
    return tuple(x7)


def _corner_mode_4c7dc4dd(seed: Grid) -> bool:
    x0 = _nonzero_indices_4c7dc4dd(seed)
    if len(x0) == ZERO:
        return False
    x1 = minimum(apply(first, x0))
    x2 = maximum(apply(first, x0))
    x3 = minimum(apply(last, x0))
    x4 = maximum(apply(last, x0))
    x5 = len(seed) - ONE
    return x2 - x1 <= ONE and x4 - x3 <= ONE and len(intersection(frozenset((x1, x2)), frozenset((ZERO, x5)))) > ZERO and len(intersection(frozenset((x3, x4)), frozenset((ZERO, x5)))) > ZERO


def _solve_corner_4c7dc4dd(target_seed: Grid) -> Grid:
    x0 = _nonzero_indices_4c7dc4dd(target_seed)
    x1 = minimum(apply(first, x0))
    x2 = maximum(apply(first, x0))
    x3 = minimum(apply(last, x0))
    x4 = maximum(apply(last, x0))
    x5 = len(target_seed)
    x6 = x5 - ONE
    if x1 == ZERO and x3 == ZERO:
        x7 = (ONE, ONE)
        x8 = ((ZERO, ONE), (ONE, ZERO))
    elif x1 == ZERO and x4 == x6:
        x7 = (ONE, x5 - TWO)
        x8 = ((ZERO, x5 - TWO), (ONE, x6))
    elif x2 == x6 and x3 == ZERO:
        x7 = (x5 - TWO, ONE)
        x8 = ((x5 - TWO, ZERO), (x6, ONE))
    else:
        x7 = (x5 - TWO, x5 - TWO)
        x8 = ((x5 - TWO, x6), (x6, x5 - TWO))
    x9 = target_seed[x7[0]][x7[1]]
    x10 = target_seed[x8[0][0]][x8[0][1]]
    x11 = canvas(x9, (x5, x5))
    x12 = frozenset({(ZERO, ZERO), (ZERO, x6), (x6, ZERO), (x6, x6)})
    x13 = frozenset({
        (ZERO, ONE),
        (ONE, ZERO),
        (ZERO, x5 - TWO),
        (ONE, x6),
        (x5 - TWO, ZERO),
        (x6, ONE),
        (x5 - TWO, x6),
        (x6, x5 - TWO),
    })
    x14 = fill(x11, ZERO, x12)
    return fill(x14, x10, x13)


def _connect_axis_4c7dc4dd(a: tuple[int, int], b: tuple[int, int]) -> tuple[tuple[int, int], ...] | None:
    x0, x1 = a
    x2, x3 = b
    if x0 == x2:
        x4 = ONE if x3 >= x1 else NEG_ONE
        return tuple((x0, x5) for x5 in range(x1, x3 + x4, x4))
    if x1 == x3:
        x4 = ONE if x2 >= x0 else NEG_ONE
        return tuple((x5, x1) for x5 in range(x0, x2 + x4, x4))
    return None


def _solve_path_4c7dc4dd(target_seed: Grid) -> Grid:
    x0 = tuple(_nonzero_indices_4c7dc4dd(target_seed))
    x1 = None
    for x2 in itertools.permutations(x0):
        x3 = []
        x4 = True
        for x5, x6 in zip(x2, x2[ONE:]):
            x7 = _connect_axis_4c7dc4dd(x5, x6)
            if x7 is None:
                x4 = False
                break
            x3.append(frozenset(x7))
        if not x4:
            continue
        x8 = target_seed[x2[ZERO][ZERO]][x2[ZERO][ONE]]
        x9 = target_seed[x2[NEG_ONE][ZERO]][x2[NEG_ONE][ONE]]
        x10 = (x8 == x9, len(merge(tuple(x3))) if len(x3) > ZERO else ZERO)
        if x1 is None or x10 > x1[ZERO]:
            x1 = (x10, x2, x8)
    if x1 is None:
        raise ValueError(target_seed)
    x11 = x1[ONE]
    x12 = x1[TWO]
    x13 = len(target_seed)
    x14 = canvas(ZERO, (x13, x13))
    for x15, x16 in zip(x11, x11[ONE:]):
        x17 = _connect_axis_4c7dc4dd(x15, x16)
        x14 = fill(x14, x12, frozenset(x17))
    x18 = set()
    for x19, x20 in x0:
        x18.add((target_seed[x19][x20], (x19, x20)))
    return paint(x14, frozenset(x18))


def verify_4c7dc4dd(I: Grid) -> Grid:
    x0, x1 = _find_panels_4c7dc4dd(I)
    x2 = tuple(_nonzero_palette_4c7dc4dd(x3) for x3 in x1)
    x3 = tuple(x4 for x4, x5 in enumerate(x1) if len(_nonzero_indices_4c7dc4dd(x5)) > ZERO)
    x4 = None
    for x5, x6 in itertools.combinations(x3, TWO):
        if x2[x5] == x2[x6]:
            x4 = (x5, x6)
            break
    if x4 is None:
        raise ValueError(I)
    x7 = x1[x4[ZERO]]
    x8 = x1[x4[ONE]]
    x9 = next(x10 for x10 in x3 if x10 not in x4)
    x10 = x1[x9]
    if _complement_mode_4c7dc4dd(x7, x8):
        x11 = _overlay_4c7dc4dd(x7, x8)
        return _solve_complement_4c7dc4dd(x11, x10)
    x11 = x7 if len(_nonzero_indices_4c7dc4dd(x7)) <= len(_nonzero_indices_4c7dc4dd(x8)) else x8
    if _corner_mode_4c7dc4dd(x11):
        return _solve_corner_4c7dc4dd(x10)
    return _solve_path_4c7dc4dd(x10)
