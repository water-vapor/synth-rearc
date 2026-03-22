from arc2.core import *


def _turn_96a8c0cd(
    direction: IntegerTuple,
    value: Integer,
) -> IntegerTuple:
    if equality(direction, DOWN):
        return branch(equality(value, ONE), RIGHT, LEFT)
    if equality(direction, UP):
        return branch(equality(value, ONE), LEFT, RIGHT)
    if equality(direction, RIGHT):
        return branch(equality(value, ONE), UP, DOWN)
    return branch(equality(value, ONE), DOWN, UP)


def _tail_96a8c0cd(
    loc: IntegerTuple,
    direction: IntegerTuple,
    dims: IntegerTuple,
) -> IntegerTuple:
    h, w = dims
    if equality(direction, DOWN):
        return astuple(decrement(h), loc[ONE])
    if equality(direction, UP):
        return astuple(ZERO, loc[ONE])
    if equality(direction, RIGHT):
        return astuple(loc[ZERO], decrement(w))
    return astuple(loc[ZERO], ZERO)


def _trace_path_96a8c0cd(
    I: Grid,
) -> Indices:
    x0 = objects(I, T, F, T)
    x1 = first(totuple(colorfilter(x0, TWO)))
    x2 = combine(colorfilter(x0, ONE), colorfilter(x0, THREE))
    x3 = ulcorner(x1)
    x4 = branch(
        equality(x3[ZERO], ZERO),
        DOWN,
        branch(equality(x3[ZERO], decrement(height(I))), UP, branch(equality(x3[ONE], ZERO), RIGHT, LEFT)),
    )
    x5 = initset(x3)
    x6 = {}
    for x7 in x2:
        for x8 in toindices(x7):
            x6[x8] = x7
    x9 = x3
    x10 = shape(I)
    while True:
        x11 = None
        x12 = add(x9, x4)
        while contained(x12[ZERO], interval(ZERO, x10[ZERO], ONE)) and contained(x12[ONE], interval(ZERO, x10[ONE], ONE)):
            if contained(x12, x6):
                x11 = x12
                break
            x12 = add(x12, x4)
        if equality(x11, None):
            x13 = _tail_96a8c0cd(x9, x4, x10)
            x5 = combine(x5, connect(x9, x13))
            return x5
        x14 = x6[x11]
        x15 = subtract(x11, x4)
        x16 = _turn_96a8c0cd(x4, color(x14))
        if equality(x4[ZERO], ZERO):
            x17 = branch(equality(x16, UP), decrement(uppermost(x14)), increment(lowermost(x14)))
            x18 = astuple(x17, x15[ONE])
            x19 = branch(equality(x4, RIGHT), increment(rightmost(x14)), decrement(leftmost(x14)))
            x20 = astuple(x17, x19)
        else:
            x17 = branch(equality(x16, RIGHT), increment(rightmost(x14)), decrement(leftmost(x14)))
            x18 = astuple(x15[ZERO], x17)
            x19 = branch(equality(x4, DOWN), increment(lowermost(x14)), decrement(uppermost(x14)))
            x20 = astuple(x19, x17)
        x5 = combine(x5, connect(x9, x15))
        x5 = combine(x5, connect(x15, x18))
        x5 = combine(x5, connect(x18, x20))
        x9 = x20


def _bar_patch_96a8c0cd(
    horizontal: Boolean,
    axis: Integer,
    start: Integer,
    stop: Integer,
) -> Indices:
    if horizontal:
        return frozenset((axis, j) for j in range(start, increment(stop)))
    return frozenset((i, axis) for i in range(start, increment(stop)))


def _candidate_specs_96a8c0cd(
    horizontal: Boolean,
    lane: Integer,
    lateral: Integer,
) -> tuple[tuple[Integer, Integer, Integer, Integer], ...]:
    out = []
    for value in (ONE, THREE):
        for length in (TWO, THREE, THREE):
            for mag in range(ONE, increment(length)):
                if horizontal:
                    if equality(value, ONE):
                        new_lane = add(lane, mag)
                        stop = decrement(new_lane)
                        start = subtract(stop, decrement(length))
                    else:
                        new_lane = subtract(lane, mag)
                        start = increment(new_lane)
                        stop = add(start, decrement(length))
                else:
                    if equality(value, ONE):
                        new_lane = subtract(lane, mag)
                        start = increment(new_lane)
                        stop = add(start, decrement(length))
                    else:
                        new_lane = add(lane, mag)
                        stop = decrement(new_lane)
                        start = subtract(stop, decrement(length))
                if 0 <= start and stop < lateral and 0 < new_lane < decrement(lateral):
                    out.append((value, start, stop, new_lane))
    return tuple(out)


def _bar_gap_ok_96a8c0cd(
    horizontal: Boolean,
    axis: Integer,
    start: Integer,
    stop: Integer,
    lateral: Integer,
    occupied: Indices,
) -> bool:
    if horizontal:
        left = (axis, decrement(start))
        right = (axis, increment(stop))
        return (start == ZERO or left not in occupied) and (stop == decrement(lateral) or right not in occupied)
    up = (decrement(start), axis)
    down = (increment(stop), axis)
    return (start == ZERO or up not in occupied) and (stop == decrement(lateral) or down not in occupied)


def generate_96a8c0cd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        horizontal = choice((T, F))
        if horizontal:
            h = unifint(diff_lb, diff_ub, (16, 28))
            w = unifint(diff_lb, diff_ub, (10, 14))
            seed = (ZERO, unifint(diff_lb, diff_ub, (ONE, w - TWO)))
            primary = h
            lateral = w
            target_obs = unifint(diff_lb, diff_ub, (FIVE, NINE))
        else:
            h = unifint(diff_lb, diff_ub, (10, 14))
            w = unifint(diff_lb, diff_ub, (18, 30))
            seed = (unifint(diff_lb, diff_ub, (ONE, h - TWO)), ZERO)
            primary = w
            lateral = h
            target_obs = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        dims = (h, w)
        lane = seed[ONE] if horizontal else seed[ZERO]
        cursor = ZERO
        bars = []
        while len(bars) < target_obs:
            gap_lb = branch(equality(len(bars), ZERO), TWO, ONE)
            room = primary - cursor - THREE
            if room < gap_lb:
                break
            axis = add(cursor, unifint(diff_lb, diff_ub, (gap_lb, min(FOUR, room))))
            specs = _candidate_specs_96a8c0cd(horizontal, lane, lateral)
            if len(specs) == ZERO:
                break
            value, start, stop, new_lane = choice(specs)
            bars.append((value, axis, start, stop))
            lane = new_lane
            cursor = increment(axis)
        if len(bars) < THREE:
            continue
        if frozenset(value for value, _, _, _ in bars) != frozenset((ONE, THREE)):
            continue
        gi = canvas(ZERO, dims)
        gi = fill(gi, TWO, initset(seed))
        occupied = initset(seed)
        for value, axis, start, stop in bars:
            patch = _bar_patch_96a8c0cd(horizontal, axis, start, stop)
            gi = fill(gi, value, patch)
            occupied = combine(occupied, patch)
        path = _trace_path_96a8c0cd(gi)
        extra_target = unifint(diff_lb, diff_ub, (ZERO, max(TWO, len(bars) // TWO)))
        attempts = ZERO
        while attempts < 40 and extra_target > ZERO:
            if horizontal:
                axis = choice(tuple(spec[ONE] for spec in bars) + interval(ONE, decrement(h), ONE))
                length = choice((TWO, THREE, THREE))
                start = randint(ZERO, subtract(w, length))
            else:
                axis = choice(tuple(spec[ONE] for spec in bars) + interval(ONE, decrement(w), ONE))
                length = choice((TWO, THREE, THREE))
                start = randint(ZERO, subtract(h, length))
            stop = add(start, decrement(length))
            patch = _bar_patch_96a8c0cd(horizontal, axis, start, stop)
            attempts = increment(attempts)
            if patch & occupied or patch & path:
                continue
            if flip(_bar_gap_ok_96a8c0cd(horizontal, axis, start, stop, lateral, occupied)):
                continue
            value = choice((ONE, THREE))
            gi = fill(gi, value, patch)
            occupied = combine(occupied, patch)
            extra_target = decrement(extra_target)
        go = fill(gi, TWO, path)
        if equality(gi, go):
            continue
        from .verifier import verify_96a8c0cd

        if verify_96a8c0cd(gi) != go:
            continue
        return {"input": gi, "output": go}
