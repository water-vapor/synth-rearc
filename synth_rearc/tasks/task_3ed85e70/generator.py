from __future__ import annotations

from synth_rearc.core import *

from .helpers import PALETTE_3ed85e70, box_overlap_3ed85e70, expand_box_3ed85e70
from .helpers import object_from_rows_3ed85e70, panel_box_3ed85e70, pattern_spec_3ed85e70
from .helpers import shift_object_3ed85e70
from .verifier import verify_3ed85e70


PATTERN_KINDS_3ed85e70 = (
    "center",
    "center",
    "antidiag",
    "framed",
    "bars",
    "wings",
    "bent",
    "ring",
    "diagonal",
)


def _object_box_3ed85e70(
    obj: Object,
    top_left: tuple[int, int],
) -> tuple[int, int, int, int]:
    x0 = tuple(i for _, (i, _) in obj)
    x1 = tuple(j for _, (_, j) in obj)
    return (top_left[0], top_left[1], top_left[0] + max(x0), top_left[1] + max(x1))


def _can_place_3ed85e70(
    box: tuple[int, int, int, int],
    reserved: tuple[tuple[int, int, int, int], ...],
) -> bool:
    return all(not box_overlap_3ed85e70(expand_box_3ed85e70(box), other) for other in reserved)


def _sample_box_3ed85e70(
    obj: Object,
    forbidden: tuple[tuple[int, int, int, int], ...],
    inside: tuple[int, int, int, int] | None = None,
    outside: tuple[int, int, int, int] | None = None,
) -> tuple[int, int] | None:
    h = max(i for _, (i, _) in obj) + ONE
    w = max(j for _, (_, j) in obj) + ONE
    for _ in range(200):
        i = randint(ZERO, 30 - h)
        j = randint(ZERO, 30 - w)
        box = (i, j, i + h - ONE, j + w - ONE)
        if inside is not None:
            if not (inside[0] <= box[0] and inside[1] <= box[1] and box[2] <= inside[2] and box[3] <= inside[3]):
                continue
        if outside is not None and box_overlap_3ed85e70(box, outside):
            continue
        if _can_place_3ed85e70(box, forbidden):
            return (i, j)
    return None


def _distractor_3ed85e70(
    color: int,
) -> Object:
    x0 = choice(("domino", "square", "bar", "l"))
    if x0 == "domino":
        return object_from_rows_3ed85e70(((color, color),))
    if x0 == "square":
        return object_from_rows_3ed85e70(((color, color), (color, color)))
    if x0 == "bar":
        return object_from_rows_3ed85e70(((color, color, color),))
    return object_from_rows_3ed85e70(((color, ZERO), (color, color)))


def generate_3ed85e70(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("top", "bottom", "left", "right"))
        x1 = unifint(diff_lb, diff_ub, (SIX, EIGHT))
        x2 = panel_box_3ed85e70(x0, x1)
        x3 = unifint(diff_lb, diff_ub, (TWO, THREE))
        x4 = sample(PATTERN_KINDS_3ed85e70, x3)
        x5 = sample(PALETTE_3ed85e70, multiply(TWO, x3))
        x6 = tuple((x5[multiply(TWO, k)], x5[add(multiply(TWO, k), ONE)]) for k in range(x3))
        x7 = tuple(pattern_spec_3ed85e70(kind, colors) for kind, colors in zip(x4, x6))

        gi = canvas(ZERO, (30, 30))
        go = canvas(ZERO, (30, 30))
        gi = fill(gi, THREE, frozenset((i, j) for i in range(x2[0], x2[2] + ONE) for j in range(x2[1], x2[3] + ONE)))
        go = fill(go, THREE, frozenset((i, j) for i in range(x2[0], x2[2] + ONE) for j in range(x2[1], x2[3] + ONE)))

        reserved: list[tuple[int, int, int, int]] = []
        placed = []
        for spec in x7:
            x8 = spec["pattern"]
            x9 = _sample_box_3ed85e70(x8, tuple(reserved), inside=x2)
            if x9 is None:
                placed = None
                break
            x10 = shift_object_3ed85e70(x8, x9)
            gi = paint(gi, x10)
            go = paint(go, x10)
            x11 = _object_box_3ed85e70(x8, x9)
            reserved.append(x11)
            placed.append(spec)
        if placed is None:
            continue

        x12 = unifint(diff_lb, diff_ub, (x3 + ONE, add(x3, THREE)))
        x13 = list(placed)
        shuffle(x13)
        x14 = tuple(x13[k % len(x13)] for k in range(x12))
        for spec in x14:
            x15 = choice(spec["fragments"])
            x16 = spec["pattern"]
            x17 = _sample_box_3ed85e70(x16, tuple(reserved), outside=x2)
            if x17 is None:
                placed = None
                break
            x18 = shift_object_3ed85e70(x15[0], x17)
            x19 = shift_object_3ed85e70(x16, x17)
            gi = paint(gi, x18)
            go = paint(go, x19)
            reserved.append(_object_box_3ed85e70(x16, x17))
        if placed is None:
            continue

        x20 = tuple(color for color in PALETTE_3ed85e70 if color not in x5)
        x21 = unifint(diff_lb, diff_ub, (ZERO, TWO))
        for _ in range(x21):
            x22 = choice(x20) if len(x20) > ZERO else choice(PALETTE_3ed85e70)
            x23 = _distractor_3ed85e70(x22)
            x24 = _sample_box_3ed85e70(x23, tuple(reserved), outside=x2)
            if x24 is None:
                continue
            x25 = shift_object_3ed85e70(x23, x24)
            gi = paint(gi, x25)
            go = paint(go, x25)
            reserved.append(_object_box_3ed85e70(x23, x24))

        if gi == go:
            continue
        if verify_3ed85e70(gi) != go:
            continue
        return {"input": gi, "output": go}
