from synth_rearc.core import *


def verify_184a9768(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)

    def x1(x2: Object) -> Boolean:
        x3 = toindices(x2)
        x4 = delta(x2)
        x5 = color(x2)
        x6 = backdrop(x2)
        x7 = size(x4)
        x8 = size(difference(box(x2), x3))
        return x7 > ZERO and x8 == ZERO and all(index(I, ij) in (ZERO, x5) for ij in x6)

    x9 = tuple(sorted(sfilter(x0, x1), key=lambda x: (uppermost(x), leftmost(x))))
    x10 = difference(x0, frozenset(x9))
    x11 = difference(x10, colorfilter(x10, FIVE))
    x12 = tuple(sorted(x11, key=lambda x: (-size(x), color(x), uppermost(x), leftmost(x))))
    x13 = tuple(
        {
            "object": x14,
            "bbox": (uppermost(x14), leftmost(x14), lowermost(x14), rightmost(x14)),
            "holes": frozenset(ij for ij in delta(x14) if index(I, ij) == ZERO),
        }
        for x14 in x9
    )
    x15 = frozenset().union(*(x16["holes"] for x16 in x13))
    x16 = sum(size(x17) for x17 in x12)
    x17 = size(x15)
    if x16 != x17:
        raise ValueError("piece area does not match container holes")
    x18 = tuple(normalize(x19) for x19 in x12)
    x20 = []
    for x21 in x18:
        x22 = []
        x23 = height(x21)
        x24 = width(x21)
        for x25 in x13:
            x26, x27, x28, x29 = x25["bbox"]
            x30 = x25["holes"]
            for x31 in range(x26, x28 - x23 + TWO):
                for x32 in range(x27, x29 - x24 + TWO):
                    x33 = shift(x21, (x31, x32))
                    x34 = toindices(x33)
                    if x34 <= x30:
                        x22.append(x33)
        if len(x22) == ZERO:
            raise ValueError("piece has no legal placement")
        x22 = tuple(sorted(x22, key=lambda x: (uppermost(x), leftmost(x), color(x))))
        x20.append(x22)
    x20 = tuple(x20)

    def x35(x36: frozenset[int], x37: frozenset[IntegerTuple]):
        if len(x36) == ZERO:
            return () if len(x37) == ZERO else None
        x38 = None
        for x39 in x37:
            x40 = []
            for x41 in x36:
                for x42 in x20[x41]:
                    x43 = toindices(x42)
                    if x39 in x43 and x43 <= x37:
                        x40.append((x41, x42, x43))
            if len(x40) == ZERO:
                return None
            if x38 is None or len(x40) < len(x38):
                x38 = x40
                if len(x38) == ONE:
                    break
        for x44, x45, x46 in x38:
            x47 = x35(x36 - frozenset({x44}), x37 - x46)
            if x47 is not None:
                return (x45,) + x47
        return None

    x48 = x35(frozenset(range(len(x20))), x15)
    if x48 is None:
        raise ValueError("no exact placement found")
    x49 = canvas(ZERO, shape(I))
    if len(x9) > ZERO:
        x50 = merge(tuple(x51["object"] for x51 in x13))
        x49 = paint(x49, x50)
    if len(x48) > ZERO:
        x52 = merge(x48)
        x49 = paint(x49, x52)
    return x49
