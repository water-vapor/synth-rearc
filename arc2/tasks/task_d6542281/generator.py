from arc2.core import *

from .helpers import (
    build_object_d6542281,
    expanded_indices_d6542281,
    transformed_prototype_d6542281,
)
from .verifier import verify_d6542281


def generate_d6542281(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ZERO, TEN, ONE)
    while True:
        x1 = randint(13, 24)
        x2 = randint(13, 24)
        x3 = astuple(x1, x2)
        x4 = choice(x0)
        x5 = tuple(x6 for x6 in x0 if x6 != x4)
        x6 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x7 = [transformed_prototype_d6542281() for _ in range(x6 + TWO)]
        shuffle(x7)
        x8 = tuple()
        x9 = ZERO
        for x10 in x7:
            x11 = size(x10["groups"])
            if x9 + x11 > len(x5):
                continue
            x8 = combine(x8, (x10,))
            x9 = x9 + x11
            if len(x8) == x6:
                break
        if len(x8) != x6:
            continue
        x10 = list(x5)
        shuffle(x10)
        x11 = set()
        x12 = set()
        x13 = []
        x14 = True
        x15 = tuple(sorted(x8, key=lambda x16: -size(merge(tuple(x16["groups"].values())))))
        for x16 in x15:
            x17 = tuple(sorted(x16["groups"]))
            x18 = x10[:len(x17)]
            x10 = x10[len(x17):]
            x19 = {x20: x21 for x20, x21 in zip(x17, x18)}
            x22 = x16["anchor"]
            x23 = build_object_d6542281(x16["groups"], x19, x22, F)
            x24 = build_object_d6542281(x16["groups"], x19, x22, T)
            x25 = recolor(x19[x22], x16["groups"][x22])
            x26 = toindices(x23)
            x27 = toindices(x25)
            x28 = None
            for _ in range(400):
                x29 = randint(ZERO, x1 - height(x26))
                x30 = randint(ZERO, x2 - width(x26))
                x31 = shift(x26, astuple(x29, x30))
                if x31 & x11:
                    continue
                x28 = astuple(x29, x30)
                x11 |= set(expanded_indices_d6542281(x31))
                x12 |= set(expanded_indices_d6542281(x31))
                break
            if x28 is None:
                x14 = False
                break
            x29 = ONE if randint(ZERO, 99) < 58 else TWO
            x30 = []
            x31 = ZERO
            while x31 < x29:
                x32 = False
                for _ in range(500):
                    x33 = randint(ZERO, x1 - height(x26))
                    x34 = randint(ZERO, x2 - width(x26))
                    x35 = astuple(x33, x34)
                    x36 = shift(x26, x35)
                    x37 = shift(x27, x35)
                    if x36 & x12:
                        continue
                    if x37 & x11:
                        continue
                    x30.append(x35)
                    x11 |= set(expanded_indices_d6542281(x37))
                    x12 |= set(expanded_indices_d6542281(x36))
                    x32 = True
                    break
                if not x32:
                    x14 = False
                    break
                x31 = x31 + ONE
            if not x14:
                break
            x13.append(
                {
                    "anchor": x22,
                    "colors": x19,
                    "copies": tuple(x30),
                    "full": x23,
                    "input_offset": x28,
                    "output": x24,
                }
            )
        if not x14:
            continue
        x16 = canvas(x4, x3)
        x17 = canvas(x4, x3)
        for x18 in x13:
            x19 = shift(x18["full"], x18["input_offset"])
            x20 = shift(x18["output"], x18["input_offset"])
            x21 = recolor(x18["colors"][x18["anchor"]], sfilter(x18["full"], matcher(first, x18["colors"][x18["anchor"]])))
            x16 = paint(x16, x19)
            x17 = paint(x17, x20)
            for x22 in x18["copies"]:
                x23 = shift(x21, x22)
                x24 = shift(x18["full"], x22)
                x16 = paint(x16, x23)
                x17 = paint(x17, x24)
        x18 = verify_d6542281(x16)
        if x18 != x17:
            continue
        if x16 == x17:
            continue
        return {"input": x16, "output": x17}
