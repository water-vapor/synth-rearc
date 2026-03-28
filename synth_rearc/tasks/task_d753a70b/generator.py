from synth_rearc.core import *

from .helpers import diamond_outline_d753a70b
from .verifier import verify_d753a70b


BG_D753A70B = SEVEN
GRID_SHAPE_D753A70B = (16, 16)
_PASSIVE_COLORS_D753A70B = (EIGHT, EIGHT, NINE)
_CLIP_SIDES_D753A70B = ("top", "bottom", "left", "right")
_CLIP_CORNERS_D753A70B = ("tl", "tr", "bl", "br")


def _radius_d753a70b(
    value: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Integer:
    if value == TWO:
        return unifint(diff_lb, diff_ub, (ONE, SIX))
    if value == FIVE:
        return unifint(diff_lb, diff_ub, (ZERO, FOUR))
    return unifint(diff_lb, diff_ub, (ZERO, TWO))


def _transformed_patch_d753a70b(
    value: Integer,
    center: IntegerTuple,
    radius: Integer,
    dims: IntegerTuple,
) -> Indices:
    if value == TWO:
        return diamond_outline_d753a70b(center, maximum((ZERO, subtract(radius, ONE))), dims)
    if value == FIVE:
        return diamond_outline_d753a70b(center, add(radius, ONE), dims)
    return diamond_outline_d753a70b(center, radius, dims)


def _reserved_box_d753a70b(
    patch: Indices,
    dims: IntegerTuple,
) -> Indices:
    if len(patch) == ZERO:
        return frozenset()
    h, w = dims
    top = max(ZERO, subtract(uppermost(patch), ONE))
    bottom = min(subtract(h, ONE), add(lowermost(patch), ONE))
    left = max(ZERO, subtract(leftmost(patch), ONE))
    right = min(subtract(w, ONE), add(rightmost(patch), ONE))
    return frozenset((i, j) for i in range(top, bottom + ONE) for j in range(left, right + ONE))


def _sample_center_d753a70b(
    value: Integer,
    radius: Integer,
    dims: IntegerTuple,
    diff_lb: float,
    diff_ub: float,
) -> IntegerTuple | None:
    h, w = dims
    mode = choice(("interior", "interior", "edge", "edge", "corner"))
    for _ in range(200):
        if mode == "interior":
            if radius > min(h, w) // TWO:
                return None
            ci = randint(radius, subtract(subtract(h, ONE), radius))
            cj = randint(radius, subtract(subtract(w, ONE), radius))
        elif mode == "edge":
            side = choice(_CLIP_SIDES_D753A70B)
            if side == "top":
                ci = randint(ZERO, min(radius, subtract(h, ONE)))
                cj = randint(ZERO, subtract(w, ONE))
                if radius > ZERO and ci >= radius and ci <= subtract(subtract(h, ONE), radius) and cj >= radius and cj <= subtract(subtract(w, ONE), radius):
                    continue
            elif side == "bottom":
                ci = randint(max(ZERO, subtract(h, add(radius, ONE))), subtract(h, ONE))
                cj = randint(ZERO, subtract(w, ONE))
                if value == FIVE and radius == ONE and ci == subtract(h, ONE):
                    continue
                if radius > ZERO and ci >= radius and ci <= subtract(subtract(h, ONE), radius) and cj >= radius and cj <= subtract(subtract(w, ONE), radius):
                    continue
            elif side == "left":
                ci = randint(ZERO, subtract(h, ONE))
                cj = randint(ZERO, min(radius, subtract(w, ONE)))
                if radius > ZERO and ci >= radius and ci <= subtract(subtract(h, ONE), radius) and cj >= radius and cj <= subtract(subtract(w, ONE), radius):
                    continue
            else:
                ci = randint(ZERO, subtract(h, ONE))
                cj = randint(max(ZERO, subtract(w, add(radius, ONE))), subtract(w, ONE))
                if radius > ZERO and ci >= radius and ci <= subtract(subtract(h, ONE), radius) and cj >= radius and cj <= subtract(subtract(w, ONE), radius):
                    continue
        else:
            corner = choice(_CLIP_CORNERS_D753A70B)
            if corner == "tl":
                ci = randint(ZERO, min(radius, subtract(h, ONE)))
                cj = randint(ZERO, min(radius, subtract(w, ONE)))
            elif corner == "tr":
                ci = randint(ZERO, min(radius, subtract(h, ONE)))
                cj = randint(max(ZERO, subtract(w, add(radius, ONE))), subtract(w, ONE))
            elif corner == "bl":
                ci = randint(max(ZERO, subtract(h, add(radius, ONE))), subtract(h, ONE))
                cj = randint(ZERO, min(radius, subtract(w, ONE)))
            else:
                ci = randint(max(ZERO, subtract(h, add(radius, ONE))), subtract(h, ONE))
                cj = randint(max(ZERO, subtract(w, add(radius, ONE))), subtract(w, ONE))
            if value == FIVE and radius == ONE and ci == subtract(h, ONE):
                continue
        return astuple(ci, cj)
    return None


def _place_component_d753a70b(
    value: Integer,
    dims: IntegerTuple,
    occupied: Indices,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, Indices, Indices] | None:
    for _ in range(300):
        radius = _radius_d753a70b(value, diff_lb, diff_ub)
        center = _sample_center_d753a70b(value, radius, dims, diff_lb, diff_ub)
        if center is None:
            continue
        gi_patch = diamond_outline_d753a70b(center, radius, dims)
        go_patch = _transformed_patch_d753a70b(value, center, radius, dims)
        if len(gi_patch) == ZERO or len(go_patch) == ZERO:
            continue
        if gi_patch == go_patch and value in (TWO, FIVE):
            continue
        reserve = _reserved_box_d753a70b(gi_patch | go_patch, dims)
        if len(intersection(reserve, occupied)) > ZERO:
            continue
        return gi_patch, go_patch, reserve
    return None


def generate_d753a70b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    dims = GRID_SHAPE_D753A70B
    while True:
        gi = canvas(BG_D753A70B, dims)
        go = canvas(BG_D753A70B, dims)
        occupied = frozenset()
        n2 = choice((ONE, ONE, TWO))
        n5 = choice((ONE, ONE, TWO))
        npassive = choice((ZERO, ONE, ONE, TWO))
        colors = [TWO] * n2 + [FIVE] * n5 + [choice(_PASSIVE_COLORS_D753A70B) for _ in range(npassive)]
        shuffle(colors)
        ok = T
        for value in colors:
            placed = _place_component_d753a70b(value, dims, occupied, diff_lb, diff_ub)
            if placed is None:
                ok = F
                break
            gi_patch, go_patch, reserve = placed
            gi = fill(gi, value, gi_patch)
            go = fill(go, value, go_patch)
            occupied = occupied | reserve
        if not ok or gi == go:
            continue
        if verify_d753a70b(gi) != go:
            continue
        return {"input": gi, "output": go}
