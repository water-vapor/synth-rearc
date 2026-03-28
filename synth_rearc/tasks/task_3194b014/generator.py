from synth_rearc.core import *


GRID_SHAPE_3194B014 = (20, 20)
OUTPUT_SHAPE_3194B014 = (3, 3)
NONZERO_COLORS_3194B014 = tuple(range(ONE, TEN))


def _dims_3194b014(
    patch: Indices,
) -> tuple[int, int]:
    x0 = [x1 for x1, _x2 in patch]
    x1 = [x2 for _x3, x2 in patch]
    return max(x0) - min(x0) + ONE, max(x1) - min(x1) + ONE


def _dilate_3194b014(
    patch: Indices,
) -> Indices:
    x0, x1 = GRID_SHAPE_3194B014
    x2 = set(patch)
    for x3, x4 in patch:
        x2.add((x3 - ONE, x4))
        x2.add((x3 + ONE, x4))
        x2.add((x3, x4 - ONE))
        x2.add((x3, x4 + ONE))
    return frozenset(
        (x3, x4) for x3, x4 in x2 if ZERO <= x3 < x0 and ZERO <= x4 < x1
    )


def _sample_walk_blob_3194b014(
    hmin: Integer,
    hmax: Integer,
    wmin: Integer,
    wmax: Integer,
    amin: Integer,
    amax: Integer,
    spanmax: Integer,
) -> Indices:
    for _ in range(300):
        x0 = randint(hmin, hmax)
        x1 = randint(wmin, wmax)
        x2 = []
        x3 = ZERO
        x4 = x1
        for x5 in range(x0):
            if x5 > ZERO:
                x3 = max(-TWO, min(TWO, x3 + choice((-ONE, ZERO, ZERO, ONE))))
                x4 = max(wmin, min(wmax, x4 + choice((-ONE, ZERO, ZERO, ONE))))
            x2.append((x3, x4))
        x6 = frozenset(
            (x5, x7)
            for x5, (x6, x8) in enumerate(x2)
            for x7 in range(x6, x6 + x8)
        )
        x7 = normalize(x6)
        x8, x9 = _dims_3194b014(x7)
        x10 = len(x7)
        if amin <= x10 <= amax and x9 <= spanmax:
            return x7
    raise RuntimeError("failed to sample blob")


def _sample_blob_3194b014(
    hmin: Integer,
    hmax: Integer,
    wmin: Integer,
    wmax: Integer,
    amin: Integer,
    amax: Integer,
    spanmax: Integer,
) -> Indices:
    if choice((T, F, F)):
        for _ in range(100):
            x0 = randint(hmin, hmax)
            x1 = randint(wmin, wmax)
            x2 = frozenset((x3, x4) for x3 in range(x0) for x4 in range(x1))
            x3 = len(x2)
            if amin <= x3 <= amax and x1 <= spanmax:
                return x2
    return _sample_walk_blob_3194b014(hmin, hmax, wmin, wmax, amin, amax, spanmax)


def _place_blob_3194b014(
    patch: Indices,
    forbidden: Indices,
) -> Indices | None:
    x0, x1 = _dims_3194b014(patch)
    x2, x3 = GRID_SHAPE_3194B014
    x4 = []
    for x5 in range(ONE, x2 - x0):
        for x6 in range(ONE, x3 - x1):
            x7 = shift(patch, (x5, x6))
            if len(intersection(x7, forbidden)) == ZERO:
                x4.append(x7)
    if len(x4) == ZERO:
        return None
    return choice(x4)


def _components_3194b014(
    grid: Grid,
) -> tuple[Object, ...]:
    x0 = objects(grid, T, F, T)
    return tuple(sorted(x0, key=len, reverse=True))


def generate_3194b014(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    _ = diff_lb, diff_ub
    for _ in range(400):
        x0 = choice((THREE, THREE, FOUR))
        x1 = tuple(sample(NONZERO_COLORS_3194B014, x0 + TWO))
        x2 = x1[:TWO]
        x3 = x1[TWO:]
        x4 = _sample_blob_3194b014(FIVE, EIGHT, FOUR, SEVEN, 24, 42, EIGHT)
        x5 = [x4]
        x6 = len(x4)
        x7 = T
        for _x8 in range(x0 - ONE):
            for _x9 in range(120):
                x10 = _sample_blob_3194b014(FOUR, SEVEN, THREE, SIX, 12, 34, SEVEN)
                if len(x10) <= x6 - FOUR:
                    x5.append(x10)
                    break
            else:
                x7 = F
                break
        if not x7:
            continue
        x8 = frozenset({})
        x9 = []
        for x10 in x5:
            x11 = _place_blob_3194b014(x10, x8)
            if x11 is None:
                x7 = F
                break
            x9.append(x11)
            x8 = combine(x8, _dilate_3194b014(x11))
        if not x7:
            continue
        x10 = canvas(ZERO, GRID_SHAPE_3194B014)
        x11 = frozenset({})
        for x12, x13 in zip(x3, x9):
            x10 = fill(x10, x12, x13)
            x11 = combine(x11, x13)
        x12 = difference(asindices(x10), x11)
        x13 = uniform(0.42, 0.56)
        x14 = uniform(0.35, 0.65)
        x15 = set()
        x16 = set()
        for x17 in x12:
            if uniform(0.0, 1.0) >= x13:
                continue
            if uniform(0.0, 1.0) < x14:
                x15.add(x17)
            else:
                x16.add(x17)
        x10 = fill(x10, x2[ZERO], frozenset(x15))
        x10 = fill(x10, x2[ONE], frozenset(x16))
        x17 = _components_3194b014(x10)
        if len(x17) < x0:
            continue
        if color(x17[ZERO]) != x3[ZERO]:
            continue
        if len(x17) > ONE and len(x17[ONE]) >= len(x9[ZERO]):
            continue
        x18 = canvas(x3[ZERO], OUTPUT_SHAPE_3194B014)
        return {"input": x10, "output": x18}
    raise RuntimeError("failed to generate 3194b014 example")
