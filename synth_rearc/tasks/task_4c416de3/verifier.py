from collections import defaultdict, deque

from synth_rearc.core import *


def verify_4c416de3(I: Grid) -> Grid:
    def x0(cells, diagonal):
        x1 = set(cells)
        x2 = ((1, 0), (-1, 0), (0, 1), (0, -1))
        x3 = x2 + ((1, 1), (1, -1), (-1, 1), (-1, -1)) if diagonal else x2
        x4 = []
        while len(x1) > 0:
            x5 = x1.pop()
            x6 = deque((x5,))
            x7 = [x5]
            while len(x6) > 0:
                x8 = x6.popleft()
                for x9 in x3:
                    x10 = (x8[0] + x9[0], x8[1] + x9[1])
                    if x10 in x1:
                        x1.remove(x10)
                        x6.append(x10)
                        x7.append(x10)
            x4.append(frozenset(x7))
        return tuple(x4)

    def x11(x12):
        x13 = tuple(i for i, _ in x12)
        x14 = tuple(j for _, j in x12)
        return (minimum(x13), maximum(x13), minimum(x14), maximum(x14))

    def x15(x16):
        x17 = x11(x16)
        x18 = {name: sum(1 for i, j in x16 if i == x17[0]) for name in ("top",)}
        x18["bottom"] = sum(1 for i, j in x16 if i == x17[1])
        x18["left"] = sum(1 for i, j in x16 if j == x17[2])
        x18["right"] = sum(1 for i, j in x16 if j == x17[3])
        x19 = tuple(name for name, count in x18.items() if count > ONE or len(x16) == ONE)
        x20 = {
            frozenset(("top", "left")): (x17[0], x17[2]),
            frozenset(("top", "right")): (x17[0], x17[3]),
            frozenset(("bottom", "left")): (x17[1], x17[2]),
            frozenset(("bottom", "right")): (x17[1], x17[3]),
        }
        if frozenset(x19) in x20 and len(x19) == TWO:
            return ("L", x17, (x20[frozenset(x19)],))
        return ("R", x17, ((x17[0], x17[2]), (x17[0], x17[3]), (x17[1], x17[2]), (x17[1], x17[3])))

    def x21(x22, x23):
        x24 = (x23[0] + x23[1]) / TWO
        x25 = (x23[2] + x23[3]) / TWO
        return (x23[0] if x22[0] < x24 else x23[1], x23[2] if x22[1] < x25 else x23[3])

    def x26(x27, x28):
        x29 = tuple((i, j) for i, j in x27 if i != x28[0] and j != x28[1] and abs(i - x28[0]) == abs(j - x28[1]))
        if len(x29) > 0:
            return argmax(x29, lambda x30: abs(x30[0] - x28[0]))
        return argmax(x27, lambda x30: abs(x30[0] - x28[0]) + abs(x30[1] - x28[1]))

    def x31(x32, x33, x34):
        x35 = 1 if x33[0] > x34[0] else -1 if x33[0] < x34[0] else ZERO
        x36 = 1 if x33[1] > x34[1] else -1 if x33[1] < x34[1] else ZERO
        return frozenset((x35 * (x33[0] - i), x36 * (x33[1] - j)) for i, j in x32)

    def x37(x38, x39, x40):
        x41 = 1 if x39[0] > x40[0] else -1 if x39[0] < x40[0] else ZERO
        x42 = 1 if x39[1] > x40[1] else -1 if x39[1] < x40[1] else ZERO
        return frozenset((x39[0] - x41 * di, x39[1] - x42 * dj) for di, dj in x38)

    x43 = mostcolor(I)
    x44 = len(I)
    x45 = len(I[ZERO])
    x46 = defaultdict(list)
    for x47, x48 in enumerate(I):
        for x49, x50 in enumerate(x48):
            if x50 not in (x43, ZERO):
                x46[x50].append((x47, x49))
    x51 = []
    for x52, x53 in x46.items():
        for x54 in x0(x53, T):
            x51.append({"color": x52, "cells": x54})
    x55 = []
    x56 = tuple((i, j) for i, row in enumerate(I) for j, value in enumerate(row) if value != x43)
    for x57 in x0(x56, T):
        if any(I[i][j] == ZERO for i, j in x57):
            x58 = frozenset((i, j) for i, j in x57 if I[i][j] == ZERO)
            x59, x60, x61 = x15(x58)
            x55.append({"cells": x57, "zeros": x58, "type": x59, "bbox": x60, "corners": x61, "items": []})
    for x62 in x51:
        x63 = F
        for x64 in x55:
            if len(x62["cells"] & x64["cells"]) > ZERO:
                x64["items"].append(x62)
                x63 = T
                break
        if x63:
            continue
        x65 = first(x62["cells"])
        for x64 in x55:
            x66 = x64["bbox"]
            if x66[0] <= x65[0] <= x66[1] and x66[2] <= x65[1] <= x66[3]:
                x64["items"].append(x62)
                x63 = T
                break
        if x63:
            continue
        x67 = argmin(
            x55,
            lambda x68: valmin(x68["zeros"], lambda x69: abs(x65[0] - x69[0]) + abs(x65[1] - x69[1])),
        )
        x67["items"].append(x62)
    x70 = []
    for x71 in x55:
        for x72 in x71["items"]:
            if len(x72["cells"]) > ONE:
                x73 = (
                    (sum(i for i, _ in x72["cells"]) / len(x72["cells"]), sum(j for _, j in x72["cells"]) / len(x72["cells"]))
                    if x71["type"] == "R"
                    else x71["corners"][ZERO]
                )
                x74 = x21(x73, x71["bbox"]) if x71["type"] == "R" else x71["corners"][ZERO]
                x75 = x26(x72["cells"], x74)
                x70.append(x31(x72["cells"], x75, x74))
    x76 = mostcommon(tuple(x70))
    x77 = [list(row) for row in I]
    for x78 in x55:
        if x78["type"] == "R":
            x79 = {x80: None for x80 in x78["corners"]}
            for x81 in x78["items"]:
                if len(x81["cells"]) > ONE:
                    x82 = (
                        sum(i for i, _ in x81["cells"]) / len(x81["cells"]),
                        sum(j for _, j in x81["cells"]) / len(x81["cells"]),
                    )
                else:
                    x82 = first(x81["cells"])
                x83 = x21(x82, x78["bbox"])
                x79[x83] = x81
            x84 = tuple(x79.items())
        else:
            x84 = tuple((x78["corners"][ZERO], x85) for x85 in x78["items"])
        for x86, x87 in x84:
            if x87 is None:
                continue
            x88 = x26(x87["cells"], x86) if len(x87["cells"]) > ONE else first(x87["cells"])
            x89 = x37(x76, x88, x86)
            for x90, x91 in x89:
                if 0 <= x90 < x44 and 0 <= x91 < x45:
                    x77[x90][x91] = x87["color"]
    return tuple(tuple(row) for row in x77)
