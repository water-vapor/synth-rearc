from arc2.core import *

from .helpers import (
    SCAFFOLD_SPECS_880C1354,
    build_scaffold_880c1354,
    ordered_outer_objects_880c1354,
    paint_regions_880c1354,
)


def generate_880c1354(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(FOUR, remove(SEVEN, interval(ZERO, TEN, ONE)))
    x1 = unifint(diff_lb, diff_ub, (ZERO, len(SCAFFOLD_SPECS_880C1354) - ONE))
    x2 = SCAFFOLD_SPECS_880C1354[x1]
    x3 = build_scaffold_880c1354(x2)
    x4 = ordered_outer_objects_880c1354(x3)
    x5 = sample(x0, size(x4))
    x6 = x5[-ONE:] + x5[:-ONE]
    x7 = paint_regions_880c1354(x3, x4, x5)
    x8 = paint_regions_880c1354(x3, x4, x6)
    return {"input": x7, "output": x8}
