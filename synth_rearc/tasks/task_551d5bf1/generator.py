from synth_rearc.core import *


FRAME_COLOR_551D5BF1 = ONE
FILL_COLOR_551D5BF1 = EIGHT
BACKGROUND_COLOR_551D5BF1 = ZERO
GRID_BOUNDS_551D5BF1 = (24, 28)
FRAME_COUNT_BOUNDS_551D5BF1 = (5, 6)
FRAME_HEIGHT_BOUNDS_551D5BF1 = (3, 8)
FRAME_WIDTH_BOUNDS_551D5BF1 = (5, 9)
FRAME_SIDES_551D5BF1 = ("top", "bottom", "left", "right")
SCENE_ATTEMPTS_551D5BF1 = 200
PLACEMENT_ATTEMPTS_551D5BF1 = 400


def _frame_box_551d5bf1(frame: dict) -> frozenset[tuple[int, int]]:
    x0 = frame["top"]
    x1 = frame["left"]
    x2 = frame["height"]
    x3 = frame["width"]
    return frozenset((i, j) for i in range(x0, x0 + x2) for j in range(x1, x1 + x3))


def _frame_border_551d5bf1(frame: dict) -> frozenset[tuple[int, int]]:
    x0 = frame["top"]
    x1 = frame["left"]
    x2 = frame["height"]
    x3 = frame["width"]
    x4 = x0 + x2 - 1
    x5 = x1 + x3 - 1
    x6 = frozenset((x0, j) for j in range(x1, x5 + 1))
    x7 = frozenset((x4, j) for j in range(x1, x5 + 1))
    x8 = frozenset((i, x1) for i in range(x0, x4 + 1))
    x9 = frozenset((i, x5) for i in range(x0, x4 + 1))
    return x6 | x7 | x8 | x9


def _frame_interior_551d5bf1(frame: dict) -> frozenset[tuple[int, int]]:
    return _frame_box_551d5bf1(frame) - _frame_border_551d5bf1(frame)


def _frame_moat_551d5bf1(frame: dict, height: int, width: int) -> frozenset[tuple[int, int]]:
    x0 = max(ZERO, frame["top"] - 1)
    x1 = max(ZERO, frame["left"] - 1)
    x2 = min(height - 1, frame["top"] + frame["height"])
    x3 = min(width - 1, frame["left"] + frame["width"])
    return frozenset((i, j) for i in range(x0, x2 + 1) for j in range(x1, x3 + 1))


def _gap_direction_551d5bf1(frame: dict) -> tuple[int, int] | None:
    x0 = frame["gap"]
    if x0 is None:
        return None
    x1 = x0["side"]
    if x1 == "top":
        return UP
    if x1 == "bottom":
        return DOWN
    if x1 == "left":
        return LEFT
    return RIGHT


def _gap_cell_551d5bf1(frame: dict) -> tuple[int, int] | None:
    x0 = frame["gap"]
    if x0 is None:
        return None
    return x0["cell"]


def _leak_path_551d5bf1(frame: dict, height: int, width: int) -> frozenset[tuple[int, int]]:
    x0 = _gap_cell_551d5bf1(frame)
    if x0 is None:
        return frozenset()
    x1 = _gap_direction_551d5bf1(frame)
    x2 = shoot(x0, x1)
    return frozenset((i, j) for i, j in x2 if 0 <= i < height and 0 <= j < width)


def _make_gap_551d5bf1(frame: dict) -> dict:
    x0 = choice(FRAME_SIDES_551D5BF1)
    x1 = frame["top"]
    x2 = frame["left"]
    x3 = frame["height"]
    x4 = frame["width"]
    if x0 == "top":
        x5 = randint(x2 + 1, x2 + x4 - 2)
        x6 = (x1, x5)
    elif x0 == "bottom":
        x5 = randint(x2 + 1, x2 + x4 - 2)
        x6 = (x1 + x3 - 1, x5)
    elif x0 == "left":
        x5 = randint(x1 + 1, x1 + x3 - 2)
        x6 = (x5, x2)
    else:
        x5 = randint(x1 + 1, x1 + x3 - 2)
        x6 = (x5, x2 + x4 - 1)
    return {"side": x0, "cell": x6}


def _render_input_551d5bf1(height: int, width: int, frames: tuple[dict, ...]) -> Grid:
    x0 = canvas(BACKGROUND_COLOR_551D5BF1, (height, width))
    for x1 in frames:
        x2 = _frame_border_551d5bf1(x1)
        x3 = _gap_cell_551d5bf1(x1)
        x4 = x2 if x3 is None else difference(x2, frozenset((x3,)))
        x0 = fill(x0, FRAME_COLOR_551D5BF1, x4)
    return x0


def _render_output_551d5bf1(height: int, width: int, frames: tuple[dict, ...]) -> Grid:
    x0 = _render_input_551d5bf1(height, width, frames)
    for x1 in frames:
        x2 = _frame_interior_551d5bf1(x1)
        x0 = fill(x0, FILL_COLOR_551D5BF1, x2)
        x3 = _leak_path_551d5bf1(x1, height, width)
        x0 = fill(x0, FILL_COLOR_551D5BF1, x3)
    return x0


def _sample_frame_551d5bf1(height: int, width: int, leaky: bool) -> dict:
    x0 = min(FRAME_HEIGHT_BOUNDS_551D5BF1[1], height - 2)
    x1 = min(FRAME_WIDTH_BOUNDS_551D5BF1[1], width - 2)
    x2 = randint(FRAME_HEIGHT_BOUNDS_551D5BF1[0], x0)
    x3 = randint(FRAME_WIDTH_BOUNDS_551D5BF1[0], x1)
    x4 = randint(1, height - x2 - 1)
    x5 = randint(1, width - x3 - 1)
    x6 = {"top": x4, "left": x5, "height": x2, "width": x3, "gap": None}
    if leaky:
        x6["gap"] = _make_gap_551d5bf1(x6)
    return x6


def generate_551d5bf1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(SCENE_ATTEMPTS_551D5BF1):
        x0 = unifint(diff_lb, diff_ub, GRID_BOUNDS_551D5BF1)
        x1 = unifint(diff_lb, diff_ub, GRID_BOUNDS_551D5BF1)
        x2 = unifint(diff_lb, diff_ub, FRAME_COUNT_BOUNDS_551D5BF1)
        x3 = tuple(range(x2))
        x4 = unifint(diff_lb, diff_ub, (THREE, x2 - 1))
        x5 = set(sample(x3, x4))
        x6 = []
        x7 = frozenset()
        for x8 in x3:
            x9 = x8 in x5
            x10 = False
            for _ in range(PLACEMENT_ATTEMPTS_551D5BF1):
                x11 = _sample_frame_551d5bf1(x0, x1, x9)
                x12 = _frame_moat_551d5bf1(x11, x0, x1)
                x13 = _leak_path_551d5bf1(x11, x0, x1) - x12
                if size(intersection(x12, x7)) != ZERO:
                    continue
                if size(intersection(x13, x7)) != ZERO:
                    continue
                x6.append(x11)
                x7 = combine(x7, x12)
                x7 = combine(x7, x13)
                x10 = True
                break
            if not x10:
                break
        if len(x6) != x2:
            continue
        x14 = tuple(x6)
        x15 = _render_input_551d5bf1(x0, x1, x14)
        x16 = _render_output_551d5bf1(x0, x1, x14)
        return {"input": x15, "output": x16}
    raise RuntimeError("failed to place non-overlapping leaking frames for 551d5bf1")
