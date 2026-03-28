from arc2.core import *


HEIGHT_BOUNDS_5AF49B42 = (12, 18)
WIDTH_BOUNDS_5AF49B42 = (13, 20)
BAR_LENGTH_BOUNDS_5AF49B42 = (THREE, SIX)
COLORS_5AF49B42 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
SLOTS_5AF49B42 = ("top_left", "top_right", "bottom_left", "bottom_right")
MIN_ROW_GAP_5AF49B42 = ONE


def _bar_row_5af49b42(slot: str, h: int) -> int:
    return ZERO if slot.startswith("top") else h - ONE


def _bar_start_5af49b42(slot: str, w: int, length: int) -> int:
    return ZERO if slot.endswith("left") else w - length


def _bar_object_5af49b42(slot: str, values: tuple[int, ...], h: int, w: int) -> Object:
    x0 = _bar_row_5af49b42(slot, h)
    x1 = _bar_start_5af49b42(slot, w, len(values))
    return frozenset((x2, (x0, x1 + x3)) for x3, x2 in enumerate(values))


def _copy_object_5af49b42(
    values: tuple[int, ...],
    row: int,
    col: int,
    color_index: int,
) -> Object:
    x0 = col - color_index
    return frozenset((x1, (row, x0 + x2)) for x2, x1 in enumerate(values))


def _sample_lengths_5af49b42(
    diff_lb: float,
    diff_ub: float,
    w: int,
    slots: tuple[str, ...],
) -> dict[str, int]:
    while True:
        x0 = {
            x1: unifint(diff_lb, diff_ub, BAR_LENGTH_BOUNDS_5AF49B42)
            for x1 in slots
        }
        x2 = True
        for x3, x4 in (("top_left", "top_right"), ("bottom_left", "bottom_right")):
            if x3 in x0 and x4 in x0 and x0[x3] + x0[x4] > w - THREE:
                x2 = False
        if x2:
            return x0


def _sample_bars_5af49b42(
    lengths: dict[str, int],
) -> tuple[dict[str, tuple[int, ...]], dict[str, tuple[tuple[int, int], ...]]]:
    while True:
        x0 = {
            x1: tuple(sample(COLORS_5AF49B42, x2))
            for x1, x2 in lengths.items()
        }
        x1 = {}
        for x2 in x0.values():
            for x3 in x2:
                x1[x3] = x1.get(x3, ZERO) + ONE
        x4 = {
            x5: tuple(
                (x6, x7)
                for x6, x7 in enumerate(x0[x5])
                if x1[x7] == ONE
            )
            for x5 in x0
        }
        if all(len(x8) > ZERO for x8 in x4.values()):
            return x0, x4


def _choose_marker_specs_5af49b42(
    diff_lb: float,
    diff_ub: float,
    unique_map: dict[str, tuple[tuple[int, int], ...]],
) -> list[tuple[str, int, int]]:
    x0 = []
    x1 = []
    for x2, x3 in unique_map.items():
        x4 = list(x3)
        shuffle(x4)
        x0.append((x2, x4[ZERO][ZERO], x4[ZERO][ONE]))
        x1.extend((x2, x5[ZERO], x5[ONE]) for x5 in x4[ONE:])
    x6 = len(x0)
    x7 = x6 + len(x1)
    x8 = min(SEVEN, x7)
    x9 = unifint(diff_lb, diff_ub, (x6, x8))
    shuffle(x1)
    x10 = x0 + x1[: x9 - x6]
    shuffle(x10)
    return x10


def _interval_compatible_5af49b42(
    interval: tuple[int, int],
    intervals: list[tuple[int, int]],
) -> bool:
    x0, x1 = interval
    return all(x1 < y0 - MIN_ROW_GAP_5AF49B42 or x0 > y1 + MIN_ROW_GAP_5AF49B42 for y0, y1 in intervals)


def _place_markers_5af49b42(
    bars: dict[str, tuple[int, ...]],
    marker_specs: list[tuple[str, int, int]],
    h: int,
    w: int,
) -> list[tuple[str, int, int, int]]:
    x0 = list(range(ONE, h - ONE))
    x1 = {x2: [] for x2 in x0}
    x2 = {
        (_bar_row_5af49b42(x3, h), _bar_start_5af49b42(x3, w, len(x4)) + x5)
        for x3, x4 in bars.items()
        for x5 in range(len(x4))
    }
    x3 = set()
    x4 = []
    for x5, x6, x7 in marker_specs:
        x8 = len(bars[x5])
        x9 = False
        for _ in range(200):
            x10 = [x11 for x11 in x0 if len(x1[x11]) == ZERO]
            x12 = [x11 for x11 in x0 if len(x1[x11]) == ONE]
            x13 = x10
            if len(x12) > ZERO and randint(ZERO, FOUR) == ZERO:
                x13 = x10 + x12
            x14 = choice(x13 if len(x13) > ZERO else x0)
            x15 = []
            if x6 > ZERO:
                x15.extend(range(x6))
            if x6 < x8 - ONE:
                x15.extend(range(w - x8 + x6 + ONE, w))
            x16 = choice(x15) if len(x15) > ZERO and randint(ZERO, TWO) == ZERO else randint(ZERO, w - ONE)
            x17 = x16 - x6
            x18 = (max(ZERO, x17), min(w - ONE, x17 + x8 - ONE))
            x19 = (x14, x16)
            if not _interval_compatible_5af49b42(x18, x1[x14]):
                continue
            if x19 in x3:
                continue
            if any(x20 in x2 or x20 in x3 for x20 in dneighbors(x19)):
                continue
            x1[x14].append(x18)
            x3.add(x19)
            x4.append((x5, x14, x16, x7))
            x9 = True
            break
        if not x9:
            raise ValueError("failed to place marker")
    return x4


def generate_5af49b42(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_5AF49B42)
        x1 = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_5AF49B42)
        x2 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x3 = tuple(sample(SLOTS_5AF49B42, x2))
        x4 = _sample_lengths_5af49b42(diff_lb, diff_ub, x1, x3)
        x5, x6 = _sample_bars_5af49b42(x4)
        try:
            x7 = _choose_marker_specs_5af49b42(diff_lb, diff_ub, x6)
            x8 = _place_markers_5af49b42(x5, x7, x0, x1)
        except ValueError:
            continue
        x9 = canvas(ZERO, (x0, x1))
        for x10, x11 in x5.items():
            x9 = paint(x9, _bar_object_5af49b42(x10, x11, x0, x1))
        x12 = x9
        for x13, x14, x15, x16 in x8:
            x17 = frozenset({(x16, (x14, x15))})
            x12 = paint(x12, x17)
        x18 = x12
        for x19, x20, x21, x22 in x8:
            x23 = x5[x19]
            x24 = x23.index(x22)
            x18 = paint(x18, _copy_object_5af49b42(x23, x20, x21, x24))
        return {"input": x12, "output": x18}
