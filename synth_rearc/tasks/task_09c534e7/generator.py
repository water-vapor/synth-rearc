from synth_rearc.core import *


_MARKER_COLORS = (TWO, THREE, FOUR, SIX, EIGHT)
_ALL_NEIGHBORS = (
    NEG_UNITY,
    UP,
    UP_RIGHT,
    LEFT,
    RIGHT,
    DOWN_LEFT,
    DOWN,
    UNITY,
)


def _bbox(patch: Indices) -> tuple[int, int, int, int]:
    return (
        uppermost(patch),
        leftmost(patch),
        lowermost(patch),
        rightmost(patch),
    )


def _rect(top: int, left: int, h: int, w: int) -> Indices:
    return frozenset((i, j) for i in range(top, top + h) for j in range(left, left + w))


def _normalize(patch: Indices) -> Indices:
    top, left, _, _ = _bbox(patch)
    return shift(patch, (-top, -left))


def _interior(patch: Indices) -> Indices:
    return frozenset(
        (i, j)
        for i, j in patch
        if all((i + di, j + dj) in patch for di, dj in _ALL_NEIGHBORS)
    )


def _attach_room(patch: Indices, max_h: int, max_w: int) -> Indices:
    top, left, bottom, right = _bbox(patch)
    side = choice(("up", "down", "left", "right"))
    room_h = choice((3, 4, 4, 5, 5, 6, 7))
    room_w = choice((3, 4, 4, 5, 5, 6, 7))
    corridor_len = choice((0, 0, 1, 1, 2, 2, 3))
    corridor_w = choice((1, 1, 2, 3, 3, 4))
    if side in ("up", "down"):
        boundary = tuple(j for i, j in patch if i == (top if side == "up" else bottom))
        if len(boundary) == ZERO:
            return patch
        anchor = choice(boundary)
        start = anchor - randint(ZERO, corridor_w - ONE)
        if side == "up":
            corridor = _rect(top - corridor_len, start, corridor_len + ONE, corridor_w)
            room_bottom = top - corridor_len
            room_top = room_bottom - room_h + ONE
            room_left = anchor - randint(ZERO, room_w - ONE)
            room = _rect(room_top, room_left, room_h, room_w)
        else:
            corridor = _rect(bottom, start, corridor_len + ONE, corridor_w)
            room_top = bottom + corridor_len
            room_left = anchor - randint(ZERO, room_w - ONE)
            room = _rect(room_top, room_left, room_h, room_w)
    else:
        boundary = tuple(i for i, j in patch if j == (left if side == "left" else right))
        if len(boundary) == ZERO:
            return patch
        anchor = choice(boundary)
        start = anchor - randint(ZERO, corridor_w - ONE)
        if side == "left":
            corridor = _rect(start, left - corridor_len, corridor_w, corridor_len + ONE)
            room_right = left - corridor_len
            room_left = room_right - room_w + ONE
            room_top = anchor - randint(ZERO, room_h - ONE)
            room = _rect(room_top, room_left, room_h, room_w)
        else:
            corridor = _rect(start, right, corridor_w, corridor_len + ONE)
            room_left = right + corridor_len
            room_top = anchor - randint(ZERO, room_h - ONE)
            room = _rect(room_top, room_left, room_h, room_w)
    candidate = combine(patch, combine(corridor, room))
    new_h = height(candidate)
    new_w = width(candidate)
    if greater(new_h, max_h) or greater(new_w, max_w):
        return patch
    return candidate


def _attach_stub(patch: Indices, max_h: int, max_w: int) -> Indices:
    top, left, bottom, right = _bbox(patch)
    side = choice(("up", "down", "left", "right"))
    length = choice((2, 3, 3, 4))
    thickness = choice((1, 1, 2, 2, 3))
    if side in ("up", "down"):
        boundary = tuple(j for i, j in patch if i == (top if side == "up" else bottom))
        if len(boundary) == ZERO:
            return patch
        anchor = choice(boundary)
        start = anchor - randint(ZERO, thickness - ONE)
        extension = branch(
            equality(side, "up"),
            _rect(top - length + ONE, start, length, thickness),
            _rect(bottom, start, length, thickness),
        )
    else:
        boundary = tuple(i for i, j in patch if j == (left if side == "left" else right))
        if len(boundary) == ZERO:
            return patch
        anchor = choice(boundary)
        start = anchor - randint(ZERO, thickness - ONE)
        extension = branch(
            equality(side, "left"),
            _rect(start, left - length + ONE, thickness, length),
            _rect(start, right, thickness, length),
        )
    candidate = combine(patch, extension)
    new_h = height(candidate)
    new_w = width(candidate)
    if greater(new_h, max_h) or greater(new_w, max_w):
        return patch
    return candidate


def _generate_component(max_h: int, max_w: int) -> tuple[Indices, Indices]:
    for _ in range(400):
        room_h = choice((4, 4, 5, 5, 6, 7))
        room_w = choice((4, 4, 5, 5, 6, 7))
        patch = _rect(ZERO, ZERO, room_h, room_w)
        for _ in range(choice((ONE, TWO, TWO, THREE))):
            patch = _attach_room(patch, max_h, max_w)
        for _ in range(choice((ZERO, ZERO, ONE, ONE, TWO))):
            patch = _attach_stub(patch, max_h, max_w)
        patch = _normalize(patch)
        interior = _interior(patch)
        bbox_area = height(patch) * width(patch)
        area = size(patch)
        density = area / bbox_area
        ratio = size(interior) / area
        if area < 24 or area > 180:
            continue
        if size(interior) < THREE:
            continue
        if density < 0.33 or density > 0.9:
            continue
        if ratio < 0.14 or ratio > 0.45:
            continue
        return patch, interior
    raise RuntimeError("failed to generate a valid component")


def _bbox_pad(patch: Indices, dim: int) -> Indices:
    top, left, bottom, right = _bbox(patch)
    top = max(ZERO, top - ONE)
    left = max(ZERO, left - ONE)
    bottom = min(dim - ONE, bottom + ONE)
    right = min(dim - ONE, right + ONE)
    return frozenset((i, j) for i in range(top, bottom + ONE) for j in range(left, right + ONE))


def _place_components(dim: int, components: list[tuple[Indices, Indices]]) -> list[tuple[Indices, Indices]] | None:
    reserved = frozenset({})
    placed: list[tuple[Indices, Indices]] = []
    ordered_components = sorted(components, key=lambda item: len(item[0]), reverse=True)
    for patch, interior in ordered_components:
        h = height(patch)
        w = width(patch)
        placements = []
        for i in range(dim - h + ONE):
            for j in range(dim - w + ONE):
                loc = (i, j)
                shifted_patch = shift(patch, loc)
                padding = _bbox_pad(shifted_patch, dim)
                if len(intersection(padding, reserved)) != ZERO:
                    continue
                shifted_interior = shift(interior, loc)
                placements.append((shifted_patch, shifted_interior, padding))
        if len(placements) == ZERO:
            return None
        shifted_patch, shifted_interior, padding = choice(placements)
        reserved = combine(reserved, padding)
        placed.append((shifted_patch, shifted_interior))
    return placed


def generate_09c534e7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        dim = 2 * unifint(diff_lb, diff_ub, (9, 15))
        count_options = (TWO, THREE, THREE, THREE) if dim <= 22 else (TWO, THREE, THREE, THREE, THREE)
        ncomponents = choice(count_options)
        max_h = max(8, dim - 6)
        max_w = max(10, dim - 4)
        components = [_generate_component(max_h, max_w) for _ in range(ncomponents)]
        occupancy = sum(size(patch) for patch, _ in components) / (dim * dim)
        if occupancy < 0.28 or occupancy > 0.5:
            continue
        placed = _place_components(dim, components)
        if placed is None:
            continue
        gi = canvas(ZERO, (dim, dim))
        go = canvas(ZERO, (dim, dim))
        for patch, interior in placed:
            marker = choice(_MARKER_COLORS)
            gi = fill(gi, ONE, patch)
            go = fill(go, ONE, patch)
            go = fill(go, marker, interior)
            seed = choice(totuple(interior))
            gi = fill(gi, marker, initset(seed))
        return {"input": gi, "output": go}
