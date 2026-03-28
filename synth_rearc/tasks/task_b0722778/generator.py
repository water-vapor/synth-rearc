from synth_rearc.core import *


RELATIONS_B0722778 = ("vmirror", "rot90", "rot270", "recolor")
RELATION_FUNCS_B0722778 = {
    "vmirror": vmirror,
    "rot90": rot90,
    "rot270": rot270,
}


def _template_b0722778(mask: int) -> Grid:
    return (
        ((mask >> THREE) & ONE, (mask >> TWO) & ONE),
        ((mask >> ONE) & ONE, mask & ONE),
    )


PATTERNS_B0722778 = tuple(
    _template_b0722778(mask)
    for mask in range(ONE, 15)
    if mask not in (SIX, NINE)
)


def _relation_changes_b0722778(pattern: Grid, relation: str) -> bool:
    return RELATION_FUNCS_B0722778[relation](pattern) != pattern


def _relation_unique_b0722778(pattern: Grid, relation: str) -> bool:
    x0 = RELATION_FUNCS_B0722778[relation](pattern)
    if x0 == pattern:
        return False
    return all(
        x0 != RELATION_FUNCS_B0722778[x1](pattern)
        for x1 in RELATION_FUNCS_B0722778
        if x1 != relation
    )


PATTERNS_BY_RELATION_B0722778 = {
    relation: tuple(
        pattern
        for pattern in PATTERNS_B0722778
        if _relation_unique_b0722778(pattern, relation)
    )
    for relation in RELATION_FUNCS_B0722778
}


def _paint_pattern_b0722778(pattern: Grid, colors: tuple[int, int]) -> Grid:
    return tuple(tuple(colors[value] for value in row) for row in pattern)


def _recolor_block_b0722778(block: Grid, mapping: dict[int, int]) -> Grid:
    return tuple(tuple(mapping[value] for value in row) for row in block)


def _band_rows_b0722778(left: Grid, middle: Grid, right: Grid) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return (
        left[ZERO] + (ZERO,) + middle[ZERO] + (ZERO, ZERO) + right[ZERO],
        left[ONE] + (ZERO,) + middle[ONE] + (ZERO, ZERO) + right[ONE],
    )


def generate_b0722778(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ONE, TEN, ONE)
    while True:
        x1 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x2 = [choice(RELATIONS_B0722778) for _ in range(x1)]
        if len(set(x2)) == ONE:
            continue
        x3 = []
        x4 = []
        for x5 in x2:
            if x5 == "recolor":
                x6, x7, x8, x9 = sample(x0, FOUR)
                x10 = choice(PATTERNS_B0722778)
                x11 = choice(PATTERNS_B0722778)
                x12 = _paint_pattern_b0722778(x10, (x6, x7))
                x13 = _paint_pattern_b0722778(x10, (x8, x9))
                x14 = _paint_pattern_b0722778(x11, (x6, x7))
                x15 = {x6: x8, x7: x9}
                x16 = _recolor_block_b0722778(x14, x15)
            else:
                x17, x18, x19, x20 = sample(x0, FOUR)
                x21 = choice(PATTERNS_BY_RELATION_B0722778[x5])
                x22 = choice(
                    tuple(
                        pattern
                        for pattern in PATTERNS_B0722778
                        if _relation_changes_b0722778(pattern, x5)
                    )
                )
                x23 = RELATION_FUNCS_B0722778[x5]
                x12 = _paint_pattern_b0722778(x21, (x17, x18))
                x13 = x23(x12)
                x14 = _paint_pattern_b0722778(x22, (x19, x20))
                x16 = x23(x14)
            x24 = _band_rows_b0722778(x12, x13, x14)
            x3.extend(x24)
            x4.extend(x16)
            if len(x3) < subtract(multiply(x1, THREE), ONE):
                x3.append((ZERO, ZERO, ZERO, ZERO, ZERO, ZERO, ZERO, ZERO, ZERO))
                x4.append((ZERO, ZERO))
        return {"input": tuple(x3), "output": tuple(x4)}
