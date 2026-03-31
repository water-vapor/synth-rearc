from synth_rearc.core import *


def donor_indices_28a6681f(
    grid: Grid,
) -> Indices:
    return ofcolor(grid, ONE)


def scaffold_indices_28a6681f(
    grid: Grid,
) -> Indices:
    x0 = objects(grid, T, F, T)
    x1 = matcher(color, ONE)
    x2 = compose(flip, x1)
    x3 = sfilter(x0, x2)
    x4 = apply(toindices, x3)
    x5 = merge(x4)
    return x5


def infer_side_mode_28a6681f(
    grid: Grid,
) -> str:
    x0 = donor_indices_28a6681f(grid)
    x1 = scaffold_indices_28a6681f(grid)
    x2 = {}
    for x3, x4 in x1:
        if x3 not in x2:
            x2[x3] = []
        x2[x3].append(x4)
    x5 = ZERO
    x6 = ZERO
    for x7, x8 in x0:
        if x7 not in x2:
            continue
        x9 = min(x2[x7])
        x10 = max(x2[x7])
        if x8 > x10:
            x5 += ONE
        if x8 < x9:
            x6 += ONE
    if x5 > x6 and x5 > ZERO:
        return "right"
    if x6 > x5 and x6 > ZERO:
        return "left"
    return "none"


def ordered_target_mask_28a6681f(
    patch: Patch,
    grid_width: Integer,
    side_mode: str,
) -> tuple[IntegerTuple, ...]:
    x0 = {}
    for x1, x2 in toindices(patch):
        if x1 not in x0:
            x0[x1] = []
        x0[x1].append(x2)
    x3 = []
    for x4 in sorted(x0, reverse=True):
        x5 = sorted(x0[x4])
        x6 = []
        x7 = [x5[ZERO]]
        for x8 in x5[ONE:]:
            if x8 == x7[-ONE] + ONE:
                x7.append(x8)
            else:
                x6.append(tuple(x7))
                x7 = [x8]
        x6.append(tuple(x7))
        x9 = []
        for x10, x11 in zip(x6, x6[ONE:]):
            x12 = range(x10[-ONE] + ONE, x11[ZERO])
            x9.extend((x4, x13) for x13 in x12)
        if side_mode == "right":
            x14 = range(x6[-ONE][-ONE] + ONE, grid_width)
            x9.extend((x4, x15) for x15 in x14)
            x9.sort(key=lambda x16: -x16[ONE])
        elif side_mode == "left":
            x14 = range(x6[ZERO][ZERO])
            x9.extend((x4, x15) for x15 in x14)
            x9.sort(key=lambda x16: x16[ONE])
        else:
            x9.sort(key=lambda x16: -x16[ONE])
        x3.extend(x9)
    return tuple(x3)


def target_prefix_28a6681f(
    patch: Patch,
    grid_width: Integer,
    side_mode: str,
    count: Integer,
) -> Indices:
    x0 = ordered_target_mask_28a6681f(patch, grid_width, side_mode)
    return frozenset(x0[:count])
