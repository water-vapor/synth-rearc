from synth_rearc.core import *


SIDE_ORDER_3DC255DB = {
    "up": ZERO,
    "right": ONE,
    "left": TWO,
    "down": THREE,
}

STEP_3DC255DB = {
    "up": UP,
    "down": DOWN,
    "left": LEFT,
    "right": RIGHT,
}


def _major_minor_patches_3dc255db(
    obj: Object,
):
    patches = {}
    for value, loc in obj:
        patches.setdefault(value, set()).add(loc)
    items = tuple((len(cells), value, frozenset(cells)) for value, cells in patches.items())
    major = max(items, key=lambda item: (item[ZERO], invert(item[ONE])))
    minor = min(items, key=lambda item: (item[ZERO], item[ONE]))
    return major[ONE], minor[ONE], major[TWO], minor[TWO]


def _side_patch_3dc255db(
    patch,
    direction: str,
):
    if direction == "up":
        target = uppermost(patch)
        return frozenset(cell for cell in patch if cell[ZERO] == target)
    if direction == "down":
        target = lowermost(patch)
        return frozenset(cell for cell in patch if cell[ZERO] == target)
    if direction == "left":
        target = leftmost(patch)
        return frozenset(cell for cell in patch if cell[ONE] == target)
    target = rightmost(patch)
    return frozenset(cell for cell in patch if cell[ONE] == target)


def _orth_distance_3dc255db(
    side_patch,
    patch,
    direction: str,
) -> float:
    top = uppermost(patch)
    bottom = lowermost(patch)
    left = leftmost(patch)
    right = rightmost(patch)
    mid_row = (top + bottom) / TWO
    mid_col = (left + right) / TWO
    if direction in ("up", "down"):
        return min(abs(cell[ONE] - mid_col) for cell in side_patch)
    return min(abs(cell[ZERO] - mid_row) for cell in side_patch)


def pointing_side_3dc255db(
    patch,
) -> str:
    scores = []
    for direction in ("up", "right", "left", "down"):
        side_patch = _side_patch_3dc255db(patch, direction)
        score = (
            len(side_patch),
            _orth_distance_3dc255db(side_patch, patch, direction),
            SIDE_ORDER_3DC255DB[direction],
            direction,
        )
        scores.append(score)
    return min(scores)[-ONE]


def pointing_endpoint_3dc255db(
    patch,
):
    direction = pointing_side_3dc255db(patch)
    side_patch = _side_patch_3dc255db(patch, direction)
    top = uppermost(patch)
    bottom = lowermost(patch)
    left = leftmost(patch)
    right = rightmost(patch)
    mid_row = (top + bottom) / TWO
    mid_col = (left + right) / TWO
    if direction in ("up", "down"):
        endpoint = argmin(side_patch, lambda cell: (abs(cell[ONE] - mid_col), cell[ONE], cell[ZERO]))
    else:
        endpoint = argmin(side_patch, lambda cell: (abs(cell[ZERO] - mid_row), cell[ZERO], cell[ONE]))
    return direction, endpoint


def extension_patch_3dc255db(
    endpoint,
    direction: str,
    length: Integer,
):
    step = STEP_3DC255DB[direction]
    return frozenset(
        add(endpoint, multiply(step, offset))
        for offset in interval(ONE, increment(length), ONE)
    )


def normalize_patch_3dc255db(
    patch,
):
    if len(patch) == ZERO:
        return frozenset()
    return frozenset(normalize(patch))


def shift_patch_3dc255db(
    patch,
    offset,
):
    if len(patch) == ZERO:
        return frozenset()
    return frozenset(shift(patch, offset))


def rotate_patch_3dc255db(
    patch,
    turns: Integer,
):
    turns = turns % FOUR
    if turns == ZERO:
        return normalize_patch_3dc255db(patch)
    norm = normalize_patch_3dc255db(patch)
    height_ = height(norm)
    width_ = width(norm)
    rotated = set()
    for i, j in norm:
        if turns == ONE:
            rotated.add((j, subtract(height_, increment(i))))
        elif turns == TWO:
            rotated.add((subtract(height_, increment(i)), subtract(width_, increment(j))))
        else:
            rotated.add((subtract(width_, increment(j)), i))
    return frozenset(rotated)


def chebyshev_halo_3dc255db(
    patch,
):
    halo = set()
    for i, j in patch:
        for ni in range(i - ONE, i + TWO):
            for nj in range(j - ONE, j + TWO):
                halo.add((ni, nj))
    return frozenset(halo)


def eight_neighbors_3dc255db(
    cell,
):
    i, j = cell
    return frozenset(
        (ni, nj)
        for ni in range(i - ONE, i + TWO)
        for nj in range(j - ONE, j + TWO)
        if flip(equality((ni, nj), cell))
    )
