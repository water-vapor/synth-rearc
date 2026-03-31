from synth_rearc.core import *

from .helpers import (
    OFFSETS_35AB12C3,
    bbox_35ab12c3,
    infer_outline_35ab12c3,
    isolated_distractor_points_35ab12c3,
    make_outline_from_template_35ab12c3,
    paint_cells_35ab12c3,
    shift_cells_35ab12c3,
    shifted_subpath_35ab12c3,
)
from .verifier import verify_35ab12c3


PRIMARY_TEMPLATES_35AB12C3 = (
    "segment",
    "vshape",
    "corner",
    "rectangle",
    "diamond",
)


def _buffered_overlap_35ab12c3(
    cells: frozenset[tuple[int, int]],
    occupied: frozenset[tuple[int, int]],
) -> bool:
    for x0, x1 in cells:
        for x2 in range(x0 - 1, x0 + 2):
            for x3 in range(x1 - 1, x1 + 2):
                if (x2, x3) in occupied:
                    return True
    return False


def _place_cluster_35ab12c3(
    height_: int,
    width_: int,
    occupied: frozenset[tuple[int, int]],
    input_cells: frozenset[tuple[int, int]],
    output_cells: frozenset[tuple[int, int]],
) -> tuple[tuple[int, int], frozenset[tuple[int, int]], frozenset[tuple[int, int]]] | None:
    x0 = input_cells | output_cells
    x1, x2, x3, x4 = bbox_35ab12c3(x0)
    x5 = x2 - x1 + 1
    x6 = x4 - x3 + 1
    if x5 > height_ or x6 > width_:
        return None
    x7 = list(product(interval(0, height_ - x5 + 1, 1), interval(0, width_ - x6 + 1, 1)))
    shuffle(x7)
    for x8 in x7:
        x9 = (x8[0] - x1, x8[1] - x3)
        x10 = shift_cells_35ab12c3(input_cells, x9)
        x11 = shift_cells_35ab12c3(output_cells, x9)
        if _buffered_overlap_35ab12c3(x11, occupied):
            continue
        return x9, x10, x11
    return None


def _sample_companion_35ab12c3(
    outline,
    primary_cells: frozenset[tuple[int, int]],
) -> tuple[tuple[int, ...], frozenset[tuple[int, int]]] | None:
    x0 = [x1 for x1 in OFFSETS_35AB12C3 if x1 not in ((-1, 1), (1, 1))]
    shuffle(x0)
    x2 = len(outline["sequence"])
    x3 = max(3, x2 // 2)
    x4 = []
    if outline["cycle"]:
        return None
    for x5 in range(x3, x2 + 1):
        x4.append(x5)
    shuffle(x4)
    for x6 in x0:
        for x7 in x4:
            x8 = [0, x2 - x7]
            shuffle(x8)
            for x9 in x8:
                x10 = shifted_subpath_35ab12c3(outline, x6, x9, x7)
                x11 = frozenset(x10)
                if len(x11 & primary_cells) > 0:
                    continue
                x12 = choice((x10[0], x10[-1]))
                return (x12,), x11
    return None


def generate_35ab12c3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (16, 22))
        x1 = unifint(diff_lb, diff_ub, (16, 22))
        x2 = canvas(ZERO, (x0, x1))
        x3 = canvas(ZERO, (x0, x1))
        x4 = set()
        x5 = list(interval(1, 10, 1))
        shuffle(x5)
        x6 = unifint(diff_lb, diff_ub, (2, 4))
        x7 = True
        for _ in range(x6):
            if len(x5) < 2:
                x7 = False
                break
            x10 = None
            for _ in range(50):
                x8 = choice(PRIMARY_TEMPLATES_35AB12C3)
                x9 = randint(0, 7)
                x10 = make_outline_from_template_35ab12c3(x8, diff_lb, diff_ub, x9)
                x10b = infer_outline_35ab12c3(x10["vertices"])
                if x10b is None:
                    continue
                if x10b["cycle"] != x10["cycle"]:
                    continue
                if x10b["cells"] != x10["cells"]:
                    continue
                break
            else:
                x7 = False
                break
            x11 = x5.pop()
            x12 = frozenset(x10["vertices"])
            x13 = x10["cells"]
            x14 = frozenset()
            x15 = frozenset()
            x16 = None
            if not x10["cycle"] and len(x5) > 0 and choice((True, False)):
                x17 = _sample_companion_35ab12c3(x10, x13)
                if x17 is not None:
                    x16 = x5.pop()
                    x14, x15 = frozenset(x17[0]), x17[1]
            x18 = x12 | x14
            x19 = x13 | x15
            x20 = _place_cluster_35ab12c3(x0, x1, frozenset(x4), x18, x19)
            if x20 is None:
                x7 = False
                break
            x21, _, _ = x20
            x22 = shift_cells_35ab12c3(x12, x21)
            x23 = shift_cells_35ab12c3(x13, x21)
            x2 = paint_cells_35ab12c3(x2, x11, x22)
            x3 = paint_cells_35ab12c3(x3, x11, x23)
            if x16 is not None:
                x24 = shift_cells_35ab12c3(x14, x21)
                x25 = shift_cells_35ab12c3(x15, x21)
                x2 = paint_cells_35ab12c3(x2, x16, x24)
                x3 = paint_cells_35ab12c3(x3, x16, x25)
                x4 |= set(x25)
            x4 |= set(x23)
        if not x7:
            continue
        x27 = set()
        for x28 in range(unifint(diff_lb, diff_ub, (0, 1))):
            if len(x5) == 0:
                break
            x29 = set()
            for x30, x31 in x4 | x27:
                for x32 in range(x30 - 2, x30 + 3):
                    for x33 in range(x31 - 2, x31 + 3):
                        if 0 <= x32 < x0 and 0 <= x33 < x1:
                            x29.add((x32, x33))
            x29 = isolated_distractor_points_35ab12c3(
                choice((2, 3)),
                frozenset(x29),
                x0,
                x1,
            )
            if x29 is None:
                continue
            x34 = x5.pop()
            x2 = paint_cells_35ab12c3(x2, x34, x29)
            x3 = paint_cells_35ab12c3(x3, x34, x29)
            x27 |= set(x29)
        if x2 == x3:
            continue
        if verify_35ab12c3(x2) != x3:
            continue
        return {"input": x2, "output": x3}
