from synth_rearc.core import *

from .verifier import verify_1c02dbbe


GRID_DIMS_1C02DBBE = (15, 15)
CORNERS_1C02DBBE = ("tl", "tr", "bl", "br")
REGION_COUNT_BAG_1C02DBBE = (ONE, TWO, TWO, THREE, THREE, FOUR)
MARKER_COLORS_1C02DBBE = remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE)))


def _rect_patch_1c02dbbe(
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
) -> Indices:
    x0 = interval(top, bottom + ONE, ONE)
    x1 = interval(left, right + ONE, ONE)
    x2 = product(x0, x1)
    return x2


def _sample_frame_1c02dbbe(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Integer, Integer, Integer]:
    x0 = unifint(diff_lb, diff_ub, (10, 13))
    x1 = unifint(diff_lb, diff_ub, (10, 13))
    x2 = randint(ONE, 14 - x0)
    x3 = randint(ONE, 14 - x1)
    x4 = x2 + x0 - ONE
    x5 = x3 + x1 - ONE
    return x2, x3, x4, x5


def _sample_regions_1c02dbbe(
    top: Integer,
    left: Integer,
    bottom: Integer,
    right: Integer,
    corners: tuple[str, ...],
    colors: tuple[Integer, ...],
) -> tuple[tuple[Integer, Indices, Indices], ...]:
    x0 = contained("tl", corners) or contained("tr", corners)
    x1 = contained("bl", corners) or contained("br", corners)
    x2 = contained("tl", corners) or contained("bl", corners)
    x3 = contained("tr", corners) or contained("br", corners)
    x4 = None
    x5 = None
    x6 = None
    x7 = None
    if x0 and x1:
        x4 = randint(top + 3, bottom - 6)
        x5 = randint(x4 + 3, bottom - 3)
    elif x0:
        x4 = randint(top + 3, bottom - 3)
    else:
        x5 = randint(top + 3, bottom - 3)
    if x2 and x3:
        x6 = randint(left + 3, right - 6)
        x7 = randint(x6 + 3, right - 3)
    elif x2:
        x6 = randint(left + 3, right - 3)
    else:
        x7 = randint(left + 3, right - 3)
    x8 = []
    for x9, x10 in zip(corners, colors):
        if x9 == "tl":
            x11 = randint(top + 3, x4)
            x12 = randint(left + 3, x6)
            x13 = _rect_patch_1c02dbbe(top, x11, left, x12)
            x14 = frozenset({(top, left), (top - ONE, x12), (x11, left - ONE)})
        elif x9 == "tr":
            x11 = randint(top + 3, x4)
            x12 = randint(x7, right - 3)
            x13 = _rect_patch_1c02dbbe(top, x11, x12, right)
            x14 = frozenset({(top, right), (top - ONE, x12), (x11, right + ONE)})
        elif x9 == "bl":
            x11 = randint(x5, bottom - 3)
            x12 = randint(left + 3, x6)
            x13 = _rect_patch_1c02dbbe(x11, bottom, left, x12)
            x14 = frozenset({(bottom, left), (x11, left - ONE), (bottom + ONE, x12)})
        else:
            x11 = randint(x5, bottom - 3)
            x12 = randint(x7, right - 3)
            x13 = _rect_patch_1c02dbbe(x11, bottom, x12, right)
            x14 = frozenset({(bottom, right), (x11, right + ONE), (bottom + ONE, x12)})
        x8.append((x10, x13, x14))
    return tuple(x8)


def generate_1c02dbbe(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(REGION_COUNT_BAG_1C02DBBE)
        x1 = tuple(sample(CORNERS_1C02DBBE, x0))
        x2 = tuple(sample(MARKER_COLORS_1C02DBBE, x0))
        x3, x4, x5, x6 = _sample_frame_1c02dbbe(diff_lb, diff_ub)
        x7 = _rect_patch_1c02dbbe(x3, x5, x4, x6)
        x8 = _sample_regions_1c02dbbe(x3, x4, x5, x6, x1, x2)
        gi = canvas(ZERO, GRID_DIMS_1C02DBBE)
        gi = fill(gi, FIVE, x7)
        go = canvas(ZERO, GRID_DIMS_1C02DBBE)
        go = fill(go, FIVE, x7)
        for x9, x10, x11 in x8:
            gi = fill(gi, x9, x11)
            go = fill(go, x9, x10)
        if verify_1c02dbbe(gi) != go:
            continue
        return {"input": gi, "output": go}
