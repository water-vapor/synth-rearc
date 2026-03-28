from synth_rearc.core import *

from .helpers import make_rect_object_9841fdad, project_panel_object_9841fdad


def _sample_bands_9841fdad(interior_height: Integer) -> tuple[tuple[int, int], ...]:
    while True:
        x0 = choice((TWO, THREE, THREE, FOUR))
        x1: list[tuple[int, int]] = []
        x2: set[int] = set()
        x3 = F
        for _ in range(x0):
            x4 = choice((ONE, TWO, TWO))
            x5 = tuple(
                top
                for top in range(ONE, interior_height - x4)
                if all(row not in x2 for row in range(top - ONE, top + x4 + ONE))
            )
            if len(x5) == 0:
                x3 = T
                break
            x6 = choice(x5)
            x1.append((x6, x4))
            x2 |= set(range(x6 - ONE, x6 + x4 + ONE))
        if not x3:
            return tuple(sorted(x1))


def generate_9841fdad(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = ONE
    x1 = unifint(diff_lb, diff_ub, (9, 12))
    x2 = unifint(diff_lb, diff_ub, (6, 8))
    x3 = add(x2, unifint(diff_lb, diff_ub, (6, 8)))
    x4 = interval(ZERO, TEN, ONE)
    x5 = choice(remove(x0, x4))
    x6 = choice(remove(x5, remove(x0, x4)))
    x7 = canvas(x5, (add(x1, TWO), add(add(x2, x3), THREE)))
    x8 = fill(x7, x0, product(interval(ONE, add(x1, ONE), ONE), interval(ONE, add(x2, ONE), ONE)))
    x9 = add(x2, TWO)
    x10 = fill(
        x8,
        x6,
        product(interval(ONE, add(x1, ONE), ONE), interval(x9, add(add(x9, x3), ZERO), ONE)),
    )
    x11 = _sample_bands_9841fdad(x1)
    x12 = remove(x6, remove(x0, x4))
    x13: tuple[Object, ...] = tuple()
    for x14, x15 in x11:
        x16 = choice(("wide", "wide", "left", "right", "pair" if x2 > SIX else "wide"))
        if x16 == "wide":
            x17 = choice(x12)
            x18 = make_rect_object_9841fdad(x17, x14, ONE, x15, subtract(x2, TWO))
            x13 = x13 + (x18,)
        elif x16 == "left":
            x17 = choice(x12)
            x18 = make_rect_object_9841fdad(x17, x14, ONE, x15, TWO)
            x13 = x13 + (x18,)
        elif x16 == "right":
            x17 = choice(x12)
            x18 = make_rect_object_9841fdad(x17, x14, subtract(x2, THREE), x15, TWO)
            x13 = x13 + (x18,)
        else:
            x17, x18 = sample(x12, TWO)
            x19 = make_rect_object_9841fdad(x17, x14, ONE, x15, TWO)
            x20 = make_rect_object_9841fdad(x18, x14, subtract(x2, THREE), x15, TWO)
            x13 = x13 + (x19, x20)
    x14 = shift(merge(x13), (ONE, ONE))
    x15 = paint(x10, x14)
    x16 = lbind(project_panel_object_9841fdad, x2)
    x17 = lbind(x16, x3)
    x18 = mapply(x17, x13)
    x19 = shift(x18, (ONE, x9))
    x20 = paint(x15, x19)
    return {"input": x15, "output": x20}
