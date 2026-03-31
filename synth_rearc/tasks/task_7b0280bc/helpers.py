from __future__ import annotations

from synth_rearc.core import *


def block_patch_7b0280bc(
    upper_left: IntegerTuple,
    square_size: Integer = TWO,
) -> Indices:
    x0, x1 = upper_left
    return frozenset(
        (i, j)
        for i in range(x0, x0 + square_size)
        for j in range(x1, x1 + square_size)
    )


def eight_halo_7b0280bc(
    patch: Patch,
) -> Indices:
    x0 = set(toindices(patch))
    for x1 in tuple(x0):
        x0 |= neighbors(x1)
    return frozenset(x0)


def patch_in_bounds_7b0280bc(
    patch: Patch,
    side: Integer,
) -> Boolean:
    return all(ZERO <= i < side and ZERO <= j < side for i, j in toindices(patch))


def center_hint_7b0280bc(
    patch: Patch,
) -> IntegerTuple:
    x0 = ulcorner(patch)
    x1 = lrcorner(patch)
    return (x0[ZERO] + x1[ZERO], x0[ONE] + x1[ONE])


def port_candidates_7b0280bc(
    block: Patch,
    target_hint: IntegerTuple,
    side: Integer,
    blocked: Indices,
) -> tuple[IntegerTuple, ...]:
    x0 = tuple(
        x1
        for x1 in outbox(block)
        if ZERO <= x1[ZERO] < side and ZERO <= x1[ONE] < side and x1 not in blocked
    )
    return tuple(
        sorted(
            x0,
            key=lambda x2: (
                max(abs(add(x2[ZERO], x2[ZERO]) - target_hint[ZERO]), abs(add(x2[ONE], x2[ONE]) - target_hint[ONE])),
                abs(add(x2[ZERO], x2[ZERO]) - target_hint[ZERO]) + abs(add(x2[ONE], x2[ONE]) - target_hint[ONE]),
                x2[ZERO],
                x2[ONE],
            ),
        )
    )


def monotone_path_7b0280bc(
    start: IntegerTuple,
    goal: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0 = start
    x1 = [x0]
    x2 = {x0}
    while x0 != goal:
        x3 = ZERO if x0[ZERO] == goal[ZERO] else ONE if goal[ZERO] > x0[ZERO] else NEG_ONE
        x4 = ZERO if x0[ONE] == goal[ONE] else ONE if goal[ONE] > x0[ONE] else NEG_ONE
        x5 = []
        if x3 != ZERO and x4 != ZERO:
            x5 = [(x3, x4), (x3, ZERO), (ZERO, x4)]
            if choice((T, F)):
                x5.reverse()
        elif x3 != ZERO:
            x5 = [(x3, ZERO)]
        else:
            x5 = [(ZERO, x4)]
        shuffle(x5)
        for x6 in x5:
            x7 = (x0[ZERO] + x6[ZERO], x0[ONE] + x6[ONE])
            if x7 in x2:
                continue
            x0 = x7
            x1.append(x0)
            x2.add(x0)
            break
        else:
            raise ValueError("monotone path stalled")
    return tuple(x1)


def chebyshev_7b0280bc(
    a: IntegerTuple,
    b: IntegerTuple,
) -> Integer:
    return max(abs(a[ZERO] - b[ZERO]), abs(a[ONE] - b[ONE]))
