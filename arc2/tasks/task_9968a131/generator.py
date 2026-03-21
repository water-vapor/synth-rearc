from arc2.core import *


BG_9968A131 = SEVEN
FG_COLORS_9968A131 = remove(BG_9968A131, interval(ZERO, TEN, ONE))
HEIGHT_BOUNDS_9968A131 = (FOUR, EIGHT)
WIDTH_BOUNDS_9968A131 = (FOUR, EIGHT)


def _row_9968a131(
    width_value: Integer,
    left: Integer,
    first_color: Integer,
    second_color: Integer,
) -> tuple[int, ...]:
    x0 = [BG_9968A131] * width_value
    x0[left] = first_color
    x0[add(left, ONE)] = second_color
    return tuple(x0)


def _shifted_row_9968a131(
    width_value: Integer,
    left: Integer,
    first_color: Integer,
    second_color: Integer,
) -> tuple[int, ...]:
    x0 = [BG_9968A131] * width_value
    x1 = add(left, ONE)
    x2 = add(left, TWO)
    x0[x1] = first_color
    x0[x2] = second_color
    return tuple(x0)


def _anomaly_rows_9968a131(active_height: Integer) -> tuple[int, ...]:
    x0 = choice(("alternating", "alternating", "center"))
    if x0 == "center" and active_height >= THREE and flip(even(active_height)):
        return (active_height // TWO,)
    return tuple(range(ONE, active_height, TWO))


def generate_9968a131(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_9968A131)
        x1 = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_9968A131)
        x2 = unifint(diff_lb, diff_ub, (THREE, x0))
        x3 = randint(ZERO, subtract(x0, x2))
        x4 = unifint(diff_lb, diff_ub, (ZERO, subtract(x1, THREE)))
        x5, x6 = sample(FG_COLORS_9968A131, TWO)
        x7 = _row_9968a131(x1, x4, x5, x6)
        x8 = _row_9968a131(x1, x4, x6, x5)
        x9 = _shifted_row_9968a131(x1, x4, x6, x5)
        x10 = set(_anomaly_rows_9968a131(x2))
        x11 = tuple(BG_9968A131 for _ in range(x1))
        x12 = []
        x13 = []
        for x14 in range(x0):
            x15 = subtract(x14, x3)
            if ZERO <= x15 < x2:
                if x15 in x10:
                    x12.append(x8)
                    x13.append(x9)
                else:
                    x12.append(x7)
                    x13.append(x7)
            else:
                x12.append(x11)
                x13.append(x11)
        x16 = tuple(x12)
        x17 = tuple(x13)
        if x16 == x17:
            continue
        return {"input": x16, "output": x17}
