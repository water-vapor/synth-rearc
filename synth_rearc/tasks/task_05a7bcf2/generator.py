from synth_rearc.core import *


def _walk_profile_05a7bcf2(length: int, upper: int, require_variation: bool = F) -> Tuple:
    if length == ONE:
        return (randint(ONE, upper),)
    if upper == ONE:
        return tuple(ONE for _ in range(length))
    while True:
        values = [randint(ONE, upper)]
        for _ in range(length - ONE):
            prev = values[-ONE]
            cands = [value for value in (prev - ONE, prev, prev + ONE) if ONE <= value <= upper]
            values.append(choice(cands))
        if not require_variation or len(set(values)) > ONE:
            return tuple(values)


def _groups_05a7bcf2(diff_lb: float, diff_ub: float) -> Tuple:
    while True:
        ngroups = unifint(diff_lb, diff_ub, (THREE, SIX))
        groups = []
        row = randint(ZERO, THREE)
        for group_index in range(ngroups):
            remaining = ngroups - group_index - ONE
            max_height = min(SIX, 30 - row - remaining * TWO)
            if max_height < ONE:
                break
            group_height = randint(ONE, max_height)
            groups.append(tuple(range(row, row + group_height)))
            row += group_height
            if remaining == ZERO:
                continue
            max_gap = 30 - row - remaining
            if max_gap < ONE:
                break
            row += randint(ONE, min(FIVE, max_gap))
        active = sum(len(group) for group in groups)
        if len(groups) != ngroups:
            continue
        if not SIX <= active <= 16:
            continue
        return tuple(groups)


def generate_05a7bcf2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        divider = choice((NINE, TEN))
        max_depth = unifint(diff_lb, diff_ub, (THREE, FIVE))
        anchor_lb = divider + max_depth + THREE
        anchor_ub = 22
        if anchor_lb > anchor_ub:
            continue
        two_anchor = randint(anchor_lb, anchor_ub)
        two_profile = _walk_profile_05a7bcf2(30, max_depth, T)
        groups = _groups_05a7bcf2(diff_lb, diff_ub)
        gi = [[ZERO for _ in range(30)] for _ in range(30)]
        for i in range(30):
            gi[i][divider] = EIGHT
        for i, count in enumerate(two_profile):
            start = two_anchor - count + ONE
            for j in range(start, two_anchor + ONE):
                gi[i][j] = TWO
        go = [row[:] for row in gi]
        for group in groups:
            group_depth = randint(ONE, min(FIVE, divider - TWO))
            anchor = randint(group_depth, divider - TWO)
            widths = _walk_profile_05a7bcf2(len(group), group_depth)
            for i, width_value in zip(group, widths):
                start = anchor - width_value + ONE
                for j in range(start, anchor + ONE):
                    gi[i][j] = FOUR
                    go[i][j] = THREE
                for j in range(anchor + ONE, divider):
                    go[i][j] = FOUR
                packed = two_profile[i]
                for j in range(divider, 30 - packed):
                    go[i][j] = EIGHT
                for j in range(30 - packed, 30):
                    go[i][j] = TWO
        x0 = tuple(tuple(row) for row in gi)
        x1 = tuple(tuple(row) for row in go)
        x2 = choice((identity, vmirror, rot90, rot270))
        x3 = x2(x0)
        x4 = x2(x1)
        if x3 == x4:
            continue
        return {"input": x3, "output": x4}
