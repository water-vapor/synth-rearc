from synth_rearc.core import *


def _color_object_e8686506(
    grid: Grid,
    colors: tuple[Integer, ...],
) -> Object:
    return frozenset((value, (i, j)) for i, row in enumerate(grid) for j, value in enumerate(row) if value in colors)


def _placement_options_e8686506(
    obj: Object,
    target: Indices,
) -> tuple[Object, ...]:
    if len(target) == ZERO:
        return ()
    x0 = normalize(obj)
    x1, x2 = ulcorner(target)
    x3, x4 = lrcorner(target)
    x5 = height(x0)
    x6 = width(x0)
    x7 = []
    for x8 in range(x1, x3 - x5 + TWO):
        for x9 in range(x2, x4 - x6 + TWO):
            x10 = shift(x0, (x8, x9))
            if toindices(x10) <= target:
                x7.append(x10)
    return tuple(sorted(x7, key=lambda patch: (ulcorner(patch), tuple(sorted(toindices(patch))))))


def _pack_e8686506(
    objs: tuple[Object, ...],
    target: Indices,
) -> tuple[tuple[Integer, Object], ...] | None:
    x0 = tuple(_placement_options_e8686506(obj, target) for obj in objs)
    if any(len(options) == ZERO for options in x0):
        return None
    x1 = tuple(sorted(range(len(objs)), key=lambda k: (len(x0[k]), -size(objs[k]), color(objs[k]), ulcorner(objs[k]))))
    x2 = set()

    def search(
        idx: Integer,
        remaining: Indices,
        acc: tuple[tuple[Integer, Object], ...],
    ) -> tuple[tuple[Integer, Object], ...] | None:
        if idx == len(x1):
            return acc if len(remaining) == ZERO else None
        x3 = (idx, tuple(sorted(remaining)))
        if x3 in x2:
            return None
        x4 = x1[idx]
        for x5 in x0[x4]:
            x6 = toindices(x5)
            if x6 <= remaining:
                x7 = search(idx + ONE, remaining - x6, acc + ((x4, x5),))
                if x7 is not None:
                    return x7
        x2.add(x3)
        return None

    return search(ZERO, target, ())


def verify_e8686506(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = tuple(sorted(difference(palette(I), initset(x0))))
    x2 = tuple(objects(I, T, F, T))
    for x3 in range(ONE, TWO ** len(x1)):
        x4 = tuple(x1[x5] for x5 in range(len(x1)) if (x3 >> x5) & ONE)
        x5 = _color_object_e8686506(I, x4)
        x6 = delta(x5)
        if len(x6) == ZERO:
            continue
        x7 = tuple(obj for obj in x2 if color(obj) not in x4)
        x8 = sum(size(obj) for obj in x7)
        if x8 != len(x6):
            continue
        x9 = _pack_e8686506(x7, x6)
        if x9 is None:
            continue
        x10 = subgrid(x5, I)
        x11 = invert(ulcorner(x5))
        for x12, x13 in x9:
            x14 = recolor(color(x7[x12]), x13)
            x10 = paint(x10, shift(x14, x11))
        return x10
    raise ValueError("no valid carrier subset")
