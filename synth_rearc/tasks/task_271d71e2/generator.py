from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    BG_271D71E2,
    make_local_component_271d71e2,
    overlay_patch_271d71e2,
    transform_grid_271d71e2,
)


def _empty_mask_271d71e2(
    h: Integer,
    w: Integer,
) -> tuple[tuple[Integer, ...], ...]:
    return tuple(tuple(ZERO for _ in range(w)) for _ in range(h))


def _full_mask_271d71e2(
    h: Integer,
    w: Integer,
) -> tuple[tuple[Integer, ...], ...]:
    return tuple(tuple(ONE for _ in range(w)) for _ in range(h))


def _side_seed_mask_271d71e2(
    h: Integer,
    w: Integer,
    side: str,
) -> tuple[tuple[Integer, ...], ...]:
    mode = choice(("empty", "empty", "stair", "stair", "bar", "full"))
    if mode == "empty":
        return _empty_mask_271d71e2(h, w)
    if mode == "full":
        return _full_mask_271d71e2(h, w)
    data = [[ZERO] * w for _ in range(h)]
    if mode == "bar":
        depth = randint(ONE, h)
        for i in range(depth):
            if side == "left":
                data[i][ZERO] = ONE
            else:
                data[i][w - ONE] = ONE
        return tuple(tuple(row) for row in data)
    depth = randint(ONE, h)
    span = randint(ONE, max(ONE, min(w, depth + ONE)))
    for i in range(depth):
        size = min(w, span + i)
        if side == "left":
            for j in range(size):
                data[i][j] = ONE
        else:
            for j in range(w - size, w):
                data[i][j] = ONE
    return tuple(tuple(row) for row in data)


def _top_seed_mask_271d71e2(
    h: Integer,
    w: Integer,
) -> tuple[tuple[Integer, ...], ...]:
    if w == ONE:
        depth = randint(ONE, h - ONE)
        return tuple((ONE,) if i < depth else (ZERO,) for i in range(h))
    if choice((True, False)):
        return _empty_mask_271d71e2(h, w)
    full_rows = randint(ZERO, h - ONE)
    partial = randint(ONE, w)
    data = [[ZERO] * w for _ in range(h)]
    for i in range(full_rows):
        for j in range(w):
            data[i][j] = ONE
    if full_rows < h:
        for j in range(partial):
            data[full_rows][j] = ONE
    return tuple(tuple(row) for row in data)


def _bottom_seed_mask_271d71e2(
    h: Integer,
    w: Integer,
) -> tuple[tuple[Integer, ...], ...]:
    if w == ONE:
        depth = randint(ONE, h - ONE)
        return tuple((ONE,) if i < depth else (ZERO,) for i in range(h))
    data = [[ZERO] * w for _ in range(h)]
    data[h - ONE][w - ONE] = ONE
    return tuple(tuple(row) for row in data)


def _reserve_ok_271d71e2(
    occupied: list[list[Boolean]],
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Boolean:
    hh = len(occupied)
    ww = len(occupied[ZERO])
    r0 = max(ZERO, top - ONE)
    c0 = max(ZERO, left - ONE)
    r1 = min(hh - ONE, top + h)
    c1 = min(ww - ONE, left + w)
    for i in range(r0, r1 + ONE):
        for j in range(c0, c1 + ONE):
            if occupied[i][j]:
                return False
    return True


def _mark_reserved_271d71e2(
    occupied: list[list[Boolean]],
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> None:
    hh = len(occupied)
    ww = len(occupied[ZERO])
    r0 = max(ZERO, top - ONE)
    c0 = max(ZERO, left - ONE)
    r1 = min(hh - ONE, top + h)
    c1 = min(ww - ONE, left + w)
    for i in range(r0, r1 + ONE):
        for j in range(c0, c1 + ONE):
            occupied[i][j] = True


def _random_component_271d71e2(
    diff_lb: float,
    diff_ub: float,
    used_shapes: set[tuple[Integer, Integer]],
) -> dict | None:
    variant = choice(
        (
            "side_consume_left",
            "side_consume_right",
            "side_preserve_left",
            "side_preserve_right",
            "top_block",
            "top_consume",
            "top_preserve",
            "bottom_consume",
            "all7_side",
            "all7_bottom",
        )
    )
    if variant == "side_consume_left":
        h = unifint(diff_lb, diff_ub, (TWO, FOUR))
        w = unifint(diff_lb, diff_ub, (THREE, SIX))
        proto = make_local_component_271d71e2(
            "left",
            _side_seed_mask_271d71e2(h, w, "left"),
            detached_gap=unifint(diff_lb, diff_ub, (TWO, FIVE)),
            detached_mode="consume",
        )
    elif variant == "side_consume_right":
        h = unifint(diff_lb, diff_ub, (TWO, FOUR))
        w = unifint(diff_lb, diff_ub, (THREE, SIX))
        proto = make_local_component_271d71e2(
            "right",
            _side_seed_mask_271d71e2(h, w, "right"),
            detached_gap=unifint(diff_lb, diff_ub, (TWO, FIVE)),
            detached_mode="consume",
        )
    elif variant == "side_preserve_left":
        w = unifint(diff_lb, diff_ub, (THREE, SIX))
        proto = make_local_component_271d71e2(
            "left",
            _side_seed_mask_271d71e2(ONE, w, "left"),
            detached_gap=unifint(diff_lb, diff_ub, (THREE, SIX)),
            detached_mode="preserve",
        )
    elif variant == "side_preserve_right":
        w = unifint(diff_lb, diff_ub, (THREE, SIX))
        proto = make_local_component_271d71e2(
            "right",
            _side_seed_mask_271d71e2(ONE, w, "right"),
            detached_gap=unifint(diff_lb, diff_ub, (THREE, SIX)),
            detached_mode="preserve",
        )
    elif variant == "top_block":
        h = unifint(diff_lb, diff_ub, (TWO, FOUR))
        w = unifint(diff_lb, diff_ub, (ONE, THREE))
        proto = make_local_component_271d71e2(
            "top",
            _top_seed_mask_271d71e2(h, w),
            marker_thickness=TWO,
            detached_mode="none",
        )
    elif variant == "top_consume":
        h = unifint(diff_lb, diff_ub, (THREE, NINE))
        w = unifint(diff_lb, diff_ub, (TWO, SIX))
        proto = make_local_component_271d71e2(
            "top",
            _top_seed_mask_271d71e2(h, w),
            detached_gap=unifint(diff_lb, diff_ub, (TWO, FIVE)),
            detached_mode="consume",
        )
    elif variant == "top_preserve":
        h = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        proto = make_local_component_271d71e2(
            "top",
            _top_seed_mask_271d71e2(h, ONE),
            detached_gap=unifint(diff_lb, diff_ub, (TWO, FIVE)),
            detached_mode="preserve",
        )
    elif variant == "bottom_consume":
        h = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        w = unifint(diff_lb, diff_ub, (THREE, FIVE))
        proto = make_local_component_271d71e2(
            "bottom",
            _bottom_seed_mask_271d71e2(h, w),
            detached_gap=unifint(diff_lb, diff_ub, (TWO, FIVE)),
            detached_mode="consume",
        )
    elif variant == "all7_side":
        h = unifint(diff_lb, diff_ub, (TWO, FOUR))
        w = unifint(diff_lb, diff_ub, (THREE, SIX))
        proto = make_local_component_271d71e2(
            choice(("left", "right")),
            _full_mask_271d71e2(h, w),
            detached_gap=unifint(diff_lb, diff_ub, (TWO, FIVE)),
            detached_mode="preserve",
        )
    else:
        h = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
        w = unifint(diff_lb, diff_ub, (TWO, FOUR))
        proto = make_local_component_271d71e2(
            "bottom",
            _full_mask_271d71e2(h, w),
            detached_gap=unifint(diff_lb, diff_ub, (TWO, FIVE)),
            detached_mode="preserve",
        )
    marker_shape = proto["marker_shape"]
    if marker_shape is not None and marker_shape in used_shapes:
        return None
    if marker_shape is not None:
        used_shapes.add(marker_shape)
    return proto


def generate_271d71e2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(200):
        h = unifint(diff_lb, diff_ub, (TEN, 28))
        w = unifint(diff_lb, diff_ub, (TEN, 28))
        gi = [list(row) for row in canvas(BG_271D71E2, (h, w))]
        go = [list(row) for row in canvas(BG_271D71E2, (h, w))]
        occupied = [[False] * w for _ in range(h)]
        used_shapes: set[tuple[Integer, Integer]] = set()
        n_components = unifint(diff_lb, diff_ub, (TWO, FOUR))
        placed = ZERO
        tries = ZERO
        while placed < n_components and tries < 80:
            tries += ONE
            proto = _random_component_271d71e2(diff_lb, diff_ub, used_shapes)
            if proto is None:
                continue
            pi = proto["input"]
            ph, pw = shape(pi)
            if ph > h or pw > w:
                continue
            top = randint(ZERO, h - ph)
            left = randint(ZERO, w - pw)
            if not _reserve_ok_271d71e2(occupied, top, left, ph, pw):
                continue
            overlay_patch_271d71e2(gi, proto["input"], (top, left))
            overlay_patch_271d71e2(go, proto["output"], (top, left))
            _mark_reserved_271d71e2(occupied, top, left, ph, pw)
            placed += ONE
        if placed < TWO:
            continue
        gi_grid = tuple(tuple(row) for row in gi)
        go_grid = tuple(tuple(row) for row in go)
        if transform_grid_271d71e2(gi_grid) != go_grid:
            continue
        return {"input": gi_grid, "output": go_grid}
    raise RuntimeError("failed to generate task 271d71e2")
