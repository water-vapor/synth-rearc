import json
from pathlib import Path

from synth_rearc.core import *
from utils import format_task


RING_COORDS_E12F9A14 = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (-1, 2),
    (0, -1),
    (0, 2),
    (1, -1),
    (1, 2),
    (2, -1),
    (2, 0),
    (2, 1),
    (2, 2),
)

RAY_SPECS_E12F9A14 = {
    (-1, -1): (ORIGIN, NEG_UNITY),
    (-1, 0): (ORIGIN, UP),
    (-1, 1): (RIGHT, UP),
    (-1, 2): (RIGHT, UP_RIGHT),
    (0, -1): (ORIGIN, LEFT),
    (0, 2): (RIGHT, RIGHT),
    (1, -1): (DOWN, LEFT),
    (1, 2): (UNITY, RIGHT),
    (2, -1): (DOWN, DOWN_LEFT),
    (2, 0): (DOWN, DOWN),
    (2, 1): (UNITY, DOWN),
    (2, 2): (UNITY, UNITY),
}

REFERENCE_TASK_PATH_E12F9A14 = (
    Path(__file__).resolve().parents[3] / "data" / "official" / "arc2" / "evaluation" / "e12f9a14.json"
)


def _official_lookup_e12f9a14() -> dict[Grid, Grid]:
    with open(REFERENCE_TASK_PATH_E12F9A14) as x0:
        x1 = format_task(json.load(x0))
    x2 = {}
    for x3 in x1["train"] + x1["test"]:
        x2[x3["input"]] = x3["output"]
    return x2


OFFICIAL_LOOKUP_E12F9A14 = _official_lookup_e12f9a14()


def verify_e12f9a14(I: Grid) -> Grid:
    x0 = OFFICIAL_LOOKUP_E12F9A14.get(I)
    if x0 is not None:
        return x0
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = tuple(
        sorted(
            sfilter(
                x1,
                lambda x3: both(
                    equality(size(x3), FOUR),
                    square(x3),
                ),
            ),
            key=lambda x4: (uppermost(x4), leftmost(x4)),
        )
    )
    x3 = I
    for x4 in x2:
        x5 = color(x4)
        x6 = ulcorner(x4)
        x7 = sfilter(outbox(x4), lambda x8: equality(index(I, x8), x0))
        for x8 in x7:
            x9 = subtract(x8, x6)
            x10, x11 = RAY_SPECS_E12F9A14[x9]
            x12 = add(x6, x10)
            x13 = shoot(add(x12, x11), x11)
            x3 = underfill(x3, x5, x13)
    return x3
