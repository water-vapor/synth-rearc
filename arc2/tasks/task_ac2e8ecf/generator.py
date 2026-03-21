from arc2.core import *

from .helpers import (
    column_overlap_ac2e8ecf,
    cross_patch_ac2e8ecf,
    frame_patch_ac2e8ecf,
    is_hollow_frame_ac2e8ecf,
    pack_bottom_ac2e8ecf,
    pack_top_ac2e8ecf,
    paint_objects_ac2e8ecf,
    reserve_box_ac2e8ecf,
)


def _axis_choices_ac2e8ecf(span: int) -> tuple[int, ...]:
    opts = {ZERO, span - ONE, span // TWO}
    if span > THREE:
        opts.add(ONE)
        opts.add(span - TWO)
    if even(span):
        opts.add(span // TWO - ONE)
    return tuple(sorted(opts))


def _make_frame_object_ac2e8ecf(
    diff_lb: float,
    diff_ub: float,
    value: int,
) -> Object:
    box_h = unifint(diff_lb, diff_ub, (THREE, FIVE))
    box_w = unifint(diff_lb, diff_ub, (THREE, FIVE))
    patch = frame_patch_ac2e8ecf(box_h, box_w)
    return recolor(value, patch)


def _make_nonframe_object_ac2e8ecf(
    diff_lb: float,
    diff_ub: float,
    value: int,
) -> Object:
    box_h = unifint(diff_lb, diff_ub, (THREE, FIVE))
    box_w = unifint(diff_lb, diff_ub, (THREE, FIVE))
    row_opts = _axis_choices_ac2e8ecf(box_h)
    col_opts = _axis_choices_ac2e8ecf(box_w)
    pairs = []
    for row_idx in row_opts:
        for col_idx in col_opts:
            on_h_edge = row_idx in (ZERO, box_h - ONE)
            on_w_edge = col_idx in (ZERO, box_w - ONE)
            if on_h_edge and on_w_edge:
                continue
            pairs.append((row_idx, col_idx))
    row_idx, col_idx = choice(pairs)
    patch = cross_patch_ac2e8ecf(box_h, box_w, row_idx, col_idx)
    return recolor(value, patch)


def _place_objects_ac2e8ecf(
    objs: tuple[Object, ...],
    dims: IntegerTuple,
) -> tuple[Object, ...] | None:
    grid_h, grid_w = dims
    pending = sorted(objs, key=lambda obj: (height(obj) * width(obj), size(obj)), reverse=True)
    placed: tuple[Object, ...] = ()
    reserved = frozenset({})
    for obj in pending:
        obj_h, obj_w = shape(obj)
        locs = []
        for top in range(grid_h - obj_h + ONE):
            for left in range(grid_w - obj_w + ONE):
                candidate = shift(obj, (top, left))
                footprint = reserve_box_ac2e8ecf(candidate, dims)
                if len(intersection(footprint, reserved)) == ZERO:
                    locs.append(candidate)
        if len(locs) == ZERO:
            return None
        candidate = choice(locs)
        placed = placed + (candidate,)
        reserved = combine(reserved, reserve_box_ac2e8ecf(candidate, dims))
    return placed


def _class_order_is_clear_ac2e8ecf(objs: tuple[Object, ...]) -> Boolean:
    for idx, obj in enumerate(objs):
        for other in objs[idx + ONE:]:
            if not column_overlap_ac2e8ecf(obj, other):
                continue
            if uppermost(obj) == uppermost(other):
                return False
    return True


def _packed_contacts_are_safe_ac2e8ecf(objs: tuple[Object, ...]) -> Boolean:
    for idx, obj in enumerate(objs):
        for other in objs[idx + ONE:]:
            if color(obj) != color(other):
                continue
            if adjacent(obj, other):
                return False
    return True


def generate_ac2e8ecf(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        grid_h = unifint(diff_lb, diff_ub, (13, 17))
        grid_w = unifint(diff_lb, diff_ub, (13, 17))
        nframes = unifint(diff_lb, diff_ub, (TWO, THREE))
        nothers = unifint(diff_lb, diff_ub, (TWO, THREE))
        palette_size = unifint(diff_lb, diff_ub, (THREE, FIVE))
        colors = sample(tuple(range(ONE, TEN)), palette_size)
        objs = []
        for _ in range(nframes):
            objs.append(_make_frame_object_ac2e8ecf(diff_lb, diff_ub, choice(colors)))
        for _ in range(nothers):
            objs.append(_make_nonframe_object_ac2e8ecf(diff_lb, diff_ub, choice(colors)))
        shuffle(objs)
        placed = _place_objects_ac2e8ecf(tuple(objs), (grid_h, grid_w))
        if placed is None:
            continue
        frames = tuple(obj for obj in placed if is_hollow_frame_ac2e8ecf(obj))
        others = tuple(obj for obj in placed if not is_hollow_frame_ac2e8ecf(obj))
        if len(frames) != nframes or len(others) != nothers:
            continue
        if not _class_order_is_clear_ac2e8ecf(frames):
            continue
        if not _class_order_is_clear_ac2e8ecf(others):
            continue
        if not (min(uppermost(obj) for obj in frames) < max(uppermost(obj) for obj in others)):
            continue
        if not (min(uppermost(obj) for obj in others) < max(uppermost(obj) for obj in frames)):
            continue
        gi = canvas(ZERO, (grid_h, grid_w))
        gi = paint_objects_ac2e8ecf(gi, placed)
        packed_top = pack_top_ac2e8ecf(frames)
        packed_bottom = pack_bottom_ac2e8ecf(others, grid_h)
        if not _packed_contacts_are_safe_ac2e8ecf(packed_top):
            continue
        if not _packed_contacts_are_safe_ac2e8ecf(packed_bottom):
            continue
        top_low = max(lowermost(obj) for obj in packed_top)
        bottom_high = min(uppermost(obj) for obj in packed_bottom)
        if bottom_high - top_low < THREE:
            continue
        go = canvas(ZERO, (grid_h, grid_w))
        go = paint_objects_ac2e8ecf(go, packed_top)
        go = paint_objects_ac2e8ecf(go, packed_bottom)
        if gi == go:
            continue
        return {"input": gi, "output": go}
