from synth_rearc.core import *


def verify_97a05b5b(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = fork(multiply, height, width)
    x2 = fork(equality, size, x1)
    x3 = matcher(numcolors, TWO)
    x4 = fork(both, x2, x3)
    x5 = tuple(order(sfilter(x0, x4), ulcorner))
    x6 = difference(x0, frozenset(x5))
    x7 = merge(x6)
    x8 = color(x7)
    x9 = mostcolor(I)
    x10 = subgrid(x7, I)
    x11 = (identity, rot180, rot90, rot270, hmirror, vmirror, cmirror, dmirror)
    x12 = lbind(canvas, NEG_ONE)
    x13 = compose(x12, shape)
    x14 = fork(paint, x13, normalize)
    x15 = []
    for x16 in x5:
        x17 = x14(x16)
        x18 = other(palette(x16), x8)
        x19 = replace(x17, x8, x9)
        x20 = replace(x19, x18, x8)
        x21 = []
        x22 = set()
        for x23 in x11:
            x24 = x23(x20)
            x25 = tuple(order(occurrences(x10, asobject(x24)), identity))
            x26 = asobject(x23(x17))
            for x27 in x25:
                x28 = shift(x26, x27)
                if x28 in x22:
                    continue
                x22.add(x28)
                x21.append(x28)
        if len(x21) == ZERO:
            raise ValueError("unable to place transformed clue")
        x15.append((x16, tuple(x21)))
    x29 = tuple(sorted(x15, key=lambda item: (len(item[1]), ulcorner(item[0]))))

    def x30(
        x31: Integer,
        x32,
    ):
        if x31 == len(x29):
            return tuple()
        _, x33 = x29[x31]
        for x34 in x33:
            x35 = toindices(x34)
            if len(intersection(x35, x32)) != ZERO:
                continue
            x36 = x30(x31 + ONE, combine(x32, x35))
            if x36 is not None:
                return (x34,) + x36
        return None

    x37 = x30(ZERO, frozenset())
    if x37 is None:
        raise ValueError("unable to resolve transformed clue placement")
    x38 = frozenset()
    for x39 in x37:
        x38 = combine(x38, x39)
    x40 = paint(x10, x38)
    return x40
