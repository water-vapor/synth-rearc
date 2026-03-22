from arc2.core import *


def generate_833dafe3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x1 = unifint(diff_lb, diff_ub, (THREE, 15))
        x2 = canvas(ZERO, astuple(x1, x1))
        x3 = asindices(x2)
        x4 = tuple(sample(x0, THREE))
        x5 = multiply(x1, x1)
        x6 = max(THREE, x5 // 3)
        x7 = min(x5 - ONE, max(x6, (x5 * TWO) // 3))
        x8 = unifint(diff_lb, diff_ub, (THREE, EIGHT))
        x9 = list(x4)
        while len(x9) < x8:
            x9.append(choice(x4))
        x10 = ZERO
        x11 = True
        for x12, x13 in enumerate(x9):
            x14 = x8 - x12 - ONE
            x15 = x7 - x10
            x16 = False
            for _ in range(30):
                x17 = choice((ZERO, ZERO, ONE, ONE, TWO, THREE))
                if x17 == ZERO:
                    x18 = unifint(diff_lb, diff_ub, (TWO, x1))
                    x19 = ONE
                elif x17 == ONE:
                    x18 = ONE
                    x19 = unifint(diff_lb, diff_ub, (TWO, x1))
                elif x17 == TWO:
                    x20 = max(TWO, x1 // 2)
                    x18 = unifint(diff_lb, diff_ub, (TWO, x20))
                    x19 = unifint(diff_lb, diff_ub, (TWO, x20))
                else:
                    x18 = ONE
                    x19 = ONE
                x21 = multiply(x18, x19)
                if x21 > x15 - x14:
                    continue
                x22 = randint(ZERO, x1 - x18)
                x23 = randint(ZERO, x1 - x19)
                x24 = product(interval(x22, x22 + x18, ONE), interval(x23, x23 + x19, ONE))
                if not x24.issubset(x3):
                    continue
                x2 = fill(x2, x13, x24)
                x3 = difference(x3, x24)
                x10 = x10 + x21
                x16 = True
                break
            if not x16:
                x11 = False
                break
        if not x11 or x10 < x6:
            continue
        x25 = hconcat(vmirror(x2), x2)
        x26 = vconcat(hmirror(x25), x25)
        return {"input": x2, "output": x26}
