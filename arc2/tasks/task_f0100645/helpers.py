from arc2.core import *


MOTIFS_F0100645 = (
    frozenset({(0, 0)}),
    frozenset({(0, 0), (1, 0)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (1, 0), (1, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1)}),
    frozenset({(0, 0), (0, 1), (1, 1)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)}),
    frozenset({(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)}),
)


def mirror_patch_f0100645(
    patch: Indices,
) -> Indices:
    max_j = max(j for _, j in patch)
    return frozenset((i, max_j - j) for i, j in patch)


def shift_patch_f0100645(
    patch: Indices,
    top: Integer,
    left: Integer,
) -> Indices:
    return frozenset((i + top, j + left) for i, j in patch)


def halo_patch_f0100645(
    patch: Indices,
) -> Indices:
    res = set(patch)
    for i, j in patch:
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                res.add((i + di, j + dj))
    return frozenset(res)


def slide_object_f0100645(
    obj: Object,
    blockers: Indices,
    delta_col: Integer,
    width_value: Integer,
) -> Object:
    current = obj
    while True:
        moved = shift(current, (ZERO, delta_col))
        moved_inds = toindices(moved)
        if any(j < ZERO or j >= width_value for _, j in moved_inds):
            return current
        if len(moved_inds & blockers) > ZERO:
            return current
        current = moved


def _settle_side_objects_f0100645(
    objs: tuple[Object, ...],
    border: Indices,
    width_value: Integer,
    delta_col: Integer,
    keyfunc,
) -> tuple[Object, ...]:
    blockers = border
    settled = []
    for obj in sorted(objs, key=keyfunc):
        moved = slide_object_f0100645(obj, blockers, delta_col, width_value)
        settled.append(moved)
        blockers = blockers | toindices(moved)
    return tuple(settled)


def settle_left_objects_f0100645(
    objs: tuple[Object, ...],
    border: Indices,
    width_value: Integer,
) -> tuple[Object, ...]:
    return _settle_side_objects_f0100645(
        objs,
        border,
        width_value,
        -ONE,
        lambda obj: (leftmost(obj), uppermost(obj), size(obj)),
    )


def settle_right_objects_f0100645(
    objs: tuple[Object, ...],
    border: Indices,
    width_value: Integer,
) -> tuple[Object, ...]:
    return _settle_side_objects_f0100645(
        objs,
        border,
        width_value,
        ONE,
        lambda obj: (-rightmost(obj), uppermost(obj), size(obj)),
    )
