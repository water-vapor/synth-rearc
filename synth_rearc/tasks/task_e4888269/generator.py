from synth_rearc.core import *


DIGIT_COLORS_E4888269 = tuple(range(ONE, TEN))
LAYOUTS_E4888269 = ("vertical", "vertical", "vertical", "horizontal", "complex")


def _apply_rules_color_e4888269(
    value: int,
    rules: tuple[tuple[int, int], ...],
) -> int:
    x0 = value
    for x1, x2 in rules:
        if x0 == x1:
            x0 = x2
    return x0


def _apply_rules_grid_e4888269(
    grid: Grid,
    rules: tuple[tuple[int, int], ...],
    protected: frozenset[tuple[int, int]],
) -> Grid:
    x0 = [list(x1) for x1 in grid]
    for x1, x2 in rules:
        for x3, x4 in enumerate(x0):
            for x5, x6 in enumerate(x4):
                if (x3, x5) not in protected and x6 == x1:
                    x4[x5] = x2
    return tuple(tuple(x1) for x1 in x0)


def _make_rules_e4888269(
    colors: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, int], ...]:
    x0 = tuple(colors)
    while True:
        x1 = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        x2 = []
        x3 = choice(x0)
        x4 = choice(tuple(x5 for x5 in x0 if x5 != x3))
        x2.append((x3, x4))
        while len(x2) < x1:
            x5 = [x2[-1][ONE], x2[-1][ONE]]
            x5.extend(x6 for x6, _ in x2)
            x5.extend(x6 for _, x6 in x2)
            x7 = tuple(x6 for x6 in x0 if x6 not in {x8 for x8, _ in x2})
            if len(x7) > ZERO:
                x5.extend(x7)
            x8 = choice(tuple(x5))
            x9 = choice(tuple(x10 for x10 in x0 if x10 != x8))
            x2.append((x8, x9))
        x10 = tuple(x2)
        x11 = {x12 for x12, _ in x10}
        x12 = tuple(x13 for x13 in x0 if x13 not in x11)
        if len(x12) == ZERO:
            continue
        x13 = tuple(_apply_rules_color_e4888269(x14, x10) for x14, _ in x10)
        if all(x14 == x15 for x14, (_, x15) in zip(x13, x10)):
            continue
        return x10


def _table_indices_e4888269(
    top: int,
    left: int,
    rules: tuple[tuple[int, int], ...],
) -> frozenset[tuple[int, int]]:
    x0 = frozenset()
    for x1 in range(len(rules)):
        x2 = frozenset({(top + x1, left), (top + x1, left + ONE)})
        x0 = combine(x0, x2)
    return x0


def _paint_rule_table_e4888269(
    grid: Grid,
    top: int,
    left: int,
    rules: tuple[tuple[int, int], ...],
) -> Grid:
    x0 = grid
    for x1, (x2, x3) in enumerate(rules):
        x4 = fill(x0, x2, initset((top + x1, left)))
        x0 = fill(x4, x3, initset((top + x1, left + ONE)))
    return x0


def _target_colors_e4888269(
    colors: tuple[int, ...],
    rules: tuple[tuple[int, int], ...],
    count: int,
) -> tuple[int, ...]:
    x0 = tuple({x1 for x1, _ in rules})
    x1 = tuple(x2 for x2 in colors if _apply_rules_color_e4888269(x2, rules) == x2)
    x2 = []
    x3 = max(TWO, count // THREE)
    for _ in range(x3):
        x2.append(choice(x0))
    for _ in range(count - x3):
        x4 = choice((T, T, F)) if len(x1) > ZERO else T
        x5 = choice(x0 if x4 else x1)
        x2.append(x5)
    shuffle(x2)
    return tuple(x2)


def _l_shape_e4888269(
    top: int,
    left: int,
    h: int,
    w: int,
) -> frozenset[tuple[int, int]]:
    x0 = connect((top, left), (top + h - ONE, left))
    x1 = connect((top + h - ONE, left), (top + h - ONE, left + w - ONE))
    return combine(x0, x1)


def _box_shape_e4888269(
    top: int,
    left: int,
    h: int,
    w: int,
) -> frozenset[tuple[int, int]]:
    x0 = frozenset({(top, left), (top + h - ONE, left + w - ONE)})
    return box(x0)


def _filled_rect_e4888269(
    top: int,
    left: int,
    h: int,
    w: int,
) -> frozenset[tuple[int, int]]:
    x0 = frozenset({(top, left), (top + h - ONE, left + w - ONE)})
    return backdrop(x0)


def _patch_ok_e4888269(
    patch: frozenset[tuple[int, int]],
    h: int,
    w: int,
    blocked: frozenset[tuple[int, int]],
) -> bool:
    if len(patch) == ZERO:
        return False
    for x0 in patch:
        if x0 in blocked:
            return False
        if x0[ZERO] < ZERO or x0[ZERO] >= h or x0[ONE] < ZERO or x0[ONE] >= w:
            return False
    return True


def _inflate_e4888269(
    patch: frozenset[tuple[int, int]],
) -> frozenset[tuple[int, int]]:
    x0 = frozenset(patch)
    for x1 in patch:
        x0 = combine(x0, dneighbors(x1))
    return x0


def _generate_vertical_e4888269(
    bg: int,
    colors: tuple[int, ...],
    rules: tuple[tuple[int, int], ...],
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = len(rules)
    x1 = max(TEN, x0 + unifint(diff_lb, diff_ub, (FOUR, EIGHT)))
    x2 = unifint(diff_lb, diff_ub, (18, 26))
    x3 = tuple({x4 for x4, _ in rules})
    x4 = choice(tuple(x5 for x5 in colors if x5 not in x3))
    x5 = canvas(bg, (x1, x2))
    x6 = randint(ZERO, x1 - x0)
    x7 = randint(ZERO, ONE)
    x8 = randint(x7 + FOUR, x2 - FIVE)
    x9 = _paint_rule_table_e4888269(x5, x6, x7, rules)
    x10 = connect((ZERO, x8), (x1 - ONE, x8))
    x9 = fill(x9, x4, x10)
    x11 = _table_indices_e4888269(x6, x7, rules)
    x12 = combine(x11, x10)
    x13 = difference(
        frozenset(product(interval(ZERO, x1, ONE), interval(x8 + TWO, x2 - ONE, ONE))),
        x12,
    )
    x14 = tuple(x13)
    x15 = unifint(diff_lb, diff_ub, (FOUR, TEN))
    if len(x14) < x15:
        return _generate_vertical_e4888269(bg, colors, rules, diff_lb, diff_ub)
    x16 = tuple(sample(x14, x15))
    x17 = _target_colors_e4888269(colors, rules, x15)
    x18 = x9
    for x19, x20 in zip(x16, x17):
        x18 = fill(x18, x20, initset(x19))
    x21 = _apply_rules_grid_e4888269(x18, rules, x12)
    return {"input": x18, "output": x21}


def _generate_horizontal_e4888269(
    bg: int,
    colors: tuple[int, ...],
    rules: tuple[tuple[int, int], ...],
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = len(rules)
    x1 = max(16, x0 + unifint(diff_lb, diff_ub, (NINE, 13)))
    x2 = unifint(diff_lb, diff_ub, (13, 18))
    x3 = tuple({x4 for x4, _ in rules})
    x4 = choice(tuple(x5 for x5 in colors if x5 not in x3))
    x5 = canvas(bg, (x1, x2))
    x6 = randint(ONE, THREE)
    x7 = randint(max(ZERO, x2 - FOUR), x2 - TWO)
    x8 = randint(x6 + x0 + THREE, x1 - THREE)
    x9 = _paint_rule_table_e4888269(x5, x6, x7 - ONE, rules)
    x10 = connect((x8, ZERO), (x8, x2 - ONE))
    x9 = fill(x9, x4, x10)
    x11 = _table_indices_e4888269(x6, x7 - ONE, rules)
    x12 = combine(x11, x10)
    x13 = difference(
        frozenset(product(interval(x8 + THREE, x1 - ONE, ONE), interval(ZERO, x2, ONE))),
        x12,
    )
    x14 = tuple(x13)
    x15 = unifint(diff_lb, diff_ub, (FIVE, TEN))
    if len(x14) < x15:
        return _generate_horizontal_e4888269(bg, colors, rules, diff_lb, diff_ub)
    x16 = tuple(sample(x14, x15))
    x17 = _target_colors_e4888269(colors, rules, x15)
    x18 = x9
    for x19, x20 in zip(x16, x17):
        x18 = fill(x18, x20, initset(x19))
    x21 = _apply_rules_grid_e4888269(x18, rules, x12)
    return {"input": x18, "output": x21}


def _generate_complex_e4888269(
    bg: int,
    colors: tuple[int, ...],
    rules: tuple[tuple[int, int], ...],
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = len(rules)
    x1 = unifint(diff_lb, diff_ub, (26, 30))
    x2 = unifint(diff_lb, diff_ub, (26, 30))
    x3 = tuple({x4 for x4, _ in rules})
    x4 = choice(tuple(x5 for x5 in colors if x5 not in x3))
    x5 = canvas(bg, (x1, x2))
    x6 = randint(x1 // TWO - TWO, x1 // TWO + TWO)
    x7 = x6 + TWO
    x8 = x7 + x0 + THREE
    if x8 >= x1 - THREE:
        x6 = x1 - x0 - 8
        x7 = x6 + TWO
        x8 = x7 + x0 + THREE
    x9 = randint(THREE, FIVE)
    x10 = randint(x9 + FIVE, x9 + EIGHT)
    x11 = connect((x6, x10), (x6, x2 - ONE))
    x12 = connect((x6, x10), (x8, x10))
    x13 = connect((x8, ZERO), (x8, x10))
    x14 = connect((x7, ZERO), (x7, x9))
    x15 = connect((x7, x9), (x8, x9))
    x16 = combine(x11, x12)
    x16 = combine(x16, x13)
    x16 = combine(x16, x14)
    x16 = combine(x16, x15)
    x5 = fill(x5, x4, x16)
    x17 = x7 + TWO
    x18 = max(x9 + ONE, x10 - THREE)
    x5 = _paint_rule_table_e4888269(x5, x17, x18, rules)
    x19 = _table_indices_e4888269(x17, x18, rules)
    x20 = combine(x16, x19)
    x21 = frozenset()
    x22 = x5
    x23 = frozenset()
    x24 = (
        (ONE, ONE, x6 - TWO, x2 - TWO),
        (x7 + ONE, x10 + THREE, x8 - ONE, x2 - TWO),
    )
    x25 = ("rect", "rect", "hbar", "vbar", "box", "l")
    x26 = unifint(diff_lb, diff_ub, (FIVE, EIGHT))
    x27 = _target_colors_e4888269(colors, rules, x26)
    for x28 in x27:
        x29 = False
        for _ in range(80):
            x30 = choice(x24)
            x31, x32, x33, x34 = x30
            if x33 <= x31 or x34 <= x32:
                continue
            x35 = choice(x25)
            if x35 == "hbar":
                x36 = randint(x31, x33)
                x37 = randint(x32, max(x32, x34 - THREE))
                x38 = randint(THREE, min(SIX, x34 - x37 + ONE))
                x39 = connect((x36, x37), (x36, x37 + x38 - ONE))
            elif x35 == "vbar":
                x36 = randint(x31, max(x31, x33 - THREE))
                x37 = randint(x32, x34)
                x38 = randint(THREE, min(SIX, x33 - x36 + ONE))
                x39 = connect((x36, x37), (x36 + x38 - ONE, x37))
            else:
                x36 = randint(x31, max(x31, x33 - TWO))
                x37 = randint(x32, max(x32, x34 - TWO))
                x38 = randint(TWO, min(FIVE, x33 - x36 + ONE))
                x40 = randint(TWO, min(FIVE, x34 - x37 + ONE))
                if x35 == "rect":
                    x39 = _filled_rect_e4888269(x36, x37, x38, x40)
                elif x35 == "box":
                    if x38 < THREE or x40 < THREE:
                        continue
                    x39 = _box_shape_e4888269(x36, x37, x38, x40)
                else:
                    x39 = _l_shape_e4888269(x36, x37, x38, x40)
            if not _patch_ok_e4888269(x39, x1, x2, x23):
                continue
            x41 = _inflate_e4888269(x39)
            if not _patch_ok_e4888269(x41, x1, x2, frozenset()):
                continue
            if len(intersection(x41, x20)) > ZERO or len(intersection(x41, x23)) > ZERO:
                continue
            x22 = fill(x22, x28, x39)
            x21 = combine(x21, x39)
            x23 = combine(x23, x41)
            x29 = True
            break
        if not x29:
            return _generate_complex_e4888269(bg, colors, rules, diff_lb, diff_ub)
    x42 = _apply_rules_grid_e4888269(x22, rules, x20)
    if x22 == x42:
        return _generate_complex_e4888269(bg, colors, rules, diff_lb, diff_ub)
    return {"input": x22, "output": x42}


def generate_e4888269(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(LAYOUTS_E4888269)
        x1 = ONE if x0 == "complex" else choice((ZERO, ZERO, ZERO, ONE))
        x2 = tuple(x3 for x3 in DIGIT_COLORS_E4888269 if x3 != x1)
        x3 = _make_rules_e4888269(x2, diff_lb, diff_ub)
        if x0 == "vertical":
            x4 = _generate_vertical_e4888269(x1, x2, x3, diff_lb, diff_ub)
        elif x0 == "horizontal":
            x4 = _generate_horizontal_e4888269(x1, x2, x3, diff_lb, diff_ub)
        else:
            x4 = _generate_complex_e4888269(x1, x2, x3, diff_lb, diff_ub)
        if x4["input"] != x4["output"]:
            return x4
