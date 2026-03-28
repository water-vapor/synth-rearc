from synth_rearc.core import *


SMALL_PROFILES_94BE5B80 = (
    ((1, 1), (0, 3), (2, 1)),
    ((1, 2), (0, 3), (2, 1)),
    ((2, 1), (1, 2), (0, 3)),
)

LARGE_PROFILES_94BE5B80 = (
    ((2, 2), (2, 1), (0, 3), (1, 2), (1, 3)),
    ((2, 1), (1, 2), (0, 3), (1, 2), (1, 3)),
    ((1, 2), (2, 1), (0, 4), (1, 2), (1, 3)),
)


def _row_patch_94be5b80(
    row: Integer,
    width: Integer,
    margin: Integer,
    thickness: Integer,
) -> Indices:
    x0 = frozenset((row, j) for j in range(margin, add(margin, thickness)))
    x1 = subtract(subtract(width, margin), thickness)
    x2 = frozenset((row, j) for j in range(x1, subtract(width, margin)))
    return combine(x0, x2)


def _motif_from_profile_94be5b80(
    profile: tuple[tuple[int, int], ...],
    width: Integer,
) -> Indices:
    x0 = frozenset()
    for x1, (x2, x3) in enumerate(profile):
        x4 = _row_patch_94be5b80(x1, width, x2, x3)
        x0 = combine(x0, x4)
    return normalize(x0)


def _connected_94be5b80(
    patch: Indices,
) -> bool:
    x0 = normalize(patch)
    x1 = canvas(ZERO, shape(x0))
    x2 = paint(x1, recolor(ONE, x0))
    x3 = objects(x2, T, F, T)
    return equality(size(x3), ONE)


def _mutate_profile_94be5b80(
    profile: tuple[tuple[int, int], ...],
    width: Integer,
) -> tuple[tuple[int, int], ...]:
    x0 = []
    x1 = width // TWO
    for x2, x3 in profile:
        x4 = x2 if x2 == ZERO else max(ZERO, min(subtract(x1, ONE), add(x2, choice((-ONE, ZERO, ONE)))))
        x5 = subtract(x1, x4)
        x6 = max(ONE, min(x5, add(x3, choice((-ONE, ZERO, ONE)))))
        x0.append((x4, x6))
    return tuple(x0)


def _random_motif_94be5b80() -> Indices:
    while True:
        x0 = choice((THREE, THREE, FIVE))
        x1 = SIX if x0 == THREE else EIGHT
        x2 = SMALL_PROFILES_94BE5B80 if x0 == THREE else LARGE_PROFILES_94BE5B80
        x3 = choice(x2)
        x4 = _mutate_profile_94be5b80(x3, x1)
        x5 = _motif_from_profile_94be5b80(x4, x1)
        if choice((T, F)):
            x5 = normalize(hmirror(x5))
        if width(x5) != x1:
            continue
        if not _connected_94be5b80(x5):
            continue
        x6 = tuple(sum(ONE for x7 in x5 if x7[0] == x8) for x8 in range(height(x5)))
        if len(set(x6)) == ONE:
            continue
        if equality(maximum(x6), minimum(x6)):
            continue
        return x5


def _legend_top_94be5b80(
    side: str,
    grid_h: Integer,
    present_top: Integer,
    present_bottom: Integer,
) -> Integer:
    if side == "top":
        return randint(ZERO, subtract(present_top, FOUR))
    return randint(add(present_bottom, TWO), subtract(grid_h, THREE))


def generate_94be5b80(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ONE, TEN, ONE)
    while True:
        x1 = _random_motif_94be5b80()
        x2 = height(x1)
        x3 = width(x1)
        x4 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x5 = tuple(sample(x0, x4))
        x6 = choice((T, F, F))
        x7 = x5 + ((ZERO,) if x6 else ())
        x8 = unifint(diff_lb, diff_ub, (ZERO, subtract(x4, ONE)))
        x9 = unifint(diff_lb, diff_ub, (ZERO, subtract(subtract(x4, x8), ONE)))
        if equality(add(x8, x9), ZERO):
            continue
        x10 = subtract(subtract(x4, x8), x9)
        x11 = unifint(diff_lb, diff_ub, (ZERO, TWO))
        x12 = unifint(diff_lb, diff_ub, (ZERO, TWO))
        x13 = add(add(multiply(x4, x2), x11), x12)
        x14 = x11
        x15 = add(x14, multiply(x8, x2))
        x16 = subtract(add(x15, multiply(x10, x2)), ONE)
        if both(greater(x8, ZERO), greater(x9, ZERO)):
            x17 = choice(("top", "bottom"))
        else:
            x17 = "top" if greater(x8, ZERO) else "bottom"
        if both(equality(x17, "top"), not greater(x15, THREE)):
            continue
        if both(equality(x17, "bottom"), greater(add(x16, FIVE), x13)):
            continue
        x18 = _legend_top_94be5b80(x17, x13, x15, x16)
        x19 = len(x7)
        x20 = add(max(x3, x19), unifint(diff_lb, diff_ub, (FOUR, NINE)))
        x21 = randint(ZERO, subtract(x20, x3))
        x22 = tuple(j for j in range(add(subtract(x21, ONE), x3 // THREE), add(subtract(x20, x19), ONE)))
        x23 = tuple(range(add(subtract(x20, x19), ONE)))
        x24 = choice(x22) if len(x22) > ZERO else choice(x23)
        gi = canvas(ZERO, (x13, x20))
        for x25, x26 in enumerate(x5[x8 : add(x8, x10)]):
            x27 = add(x14, multiply(add(x8, x25), x2))
            x28 = shift(x1, (x27, x21))
            gi = paint(gi, recolor(x26, x28))
        for x29, x30 in enumerate(x7):
            if x30 == ZERO:
                continue
            x31 = frozenset((add(x18, x32), add(x24, x29)) for x32 in range(THREE))
            gi = paint(gi, recolor(x30, x31))
        go = canvas(ZERO, (x13, x20))
        for x33, x34 in enumerate(x5):
            x35 = add(x14, multiply(x33, x2))
            x36 = shift(x1, (x35, x21))
            go = paint(go, recolor(x34, x36))
        x37 = tuple(tuple(x38) for x38 in gi)
        x38 = tuple(
            x39
            for x39 in range(subtract(len(x37), TWO))
            if both(
                both(equality(x37[x39], x37[add(x39, ONE)]), equality(x37[x39], x37[add(x39, TWO)])),
                any(x40 != ZERO for x40 in x37[x39]),
            )
        )
        if x38 != (x18,):
            continue
        if gi == go:
            continue
        return {"input": gi, "output": go}
