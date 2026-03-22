from arc2.core import *


def _piece_kind_83b6b474(piece: Object) -> str | None:
    x0 = toindices(piece)
    x1 = height(piece)
    x2 = width(piece)
    if x1 == ONE and x2 == ONE:
        return "dot"
    if x1 == ONE:
        return "h"
    if x2 == ONE:
        return "v"
    x3 = {(ZERO, ZERO), (ZERO, x2 - ONE), (x1 - ONE, ZERO), (x1 - ONE, x2 - ONE)}
    if ({(ZERO, ZERO), (ZERO, x2 - ONE), (x1 - ONE, ZERO)} <= x0 and
            (x1 - ONE, x2 - ONE) not in x0 and
            all(i == ZERO or j == ZERO for i, j in x0)):
        return "tl"
    if ({(ZERO, ZERO), (ZERO, x2 - ONE), (x1 - ONE, x2 - ONE)} <= x0 and
            (x1 - ONE, ZERO) not in x0 and
            all(i == ZERO or j == x2 - ONE for i, j in x0)):
        return "tr"
    if ({(ZERO, ZERO), (x1 - ONE, ZERO), (x1 - ONE, x2 - ONE)} <= x0 and
            (ZERO, x2 - ONE) not in x0 and
            all(i == x1 - ONE or j == ZERO for i, j in x0)):
        return "bl"
    if ({(ZERO, x2 - ONE), (x1 - ONE, ZERO), (x1 - ONE, x2 - ONE)} <= x0 and
            (ZERO, ZERO) not in x0 and
            all(i == x1 - ONE or j == x2 - ONE for i, j in x0)):
        return "br"
    if x0 == x3:
        return "box"
    return None


def _candidate_offsets_83b6b474(
    piece: Object,
    out_shape: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    x0 = _piece_kind_83b6b474(piece)
    if x0 is None:
        return ()
    x1, x2 = out_shape
    x3 = height(piece)
    x4 = width(piece)
    if x3 > x1 or x4 > x2:
        return ()
    if x0 == "tl":
        return ((ZERO, ZERO),)
    if x0 == "tr":
        return ((ZERO, x2 - x4),)
    if x0 == "bl":
        return ((x1 - x3, ZERO),)
    if x0 == "br":
        return ((x1 - x3, x2 - x4),)
    if x0 == "h":
        x5 = tuple((ZERO, j) for j in range(x2 - x4 + ONE))
        x6 = tuple((x1 - ONE, j) for j in range(x2 - x4 + ONE))
        return dedupe(x5 + x6)
    if x0 == "v":
        x7 = tuple((i, ZERO) for i in range(x1 - x3 + ONE))
        x8 = tuple((i, x2 - ONE) for i in range(x1 - x3 + ONE))
        return dedupe(x7 + x8)
    if x0 == "dot":
        x9 = tuple((ZERO, j) for j in range(x2))
        x10 = tuple((x1 - ONE, j) for j in range(x2))
        x11 = tuple((i, ZERO) for i in range(ONE, x1 - ONE))
        x12 = tuple((i, x2 - ONE) for i in range(ONE, x1 - ONE))
        return dedupe(x9 + x10 + x11 + x12)
    return ()


def _assemble_83b6b474(bg: Integer, pieces: tuple[Object, ...]) -> Grid:
    x0 = tuple(normalize(piece) for piece in pieces)
    x1 = sum(len(piece) for piece in x0)
    x2 = x1 + FOUR
    if x2 % TWO != ZERO:
        raise ValueError("invalid perimeter size")
    x3 = x2 // TWO
    x4 = max(height(piece) for piece in x0)
    x5 = max(width(piece) for piece in x0)
    x6 = []
    for h in range(x4, x3 - x5 + ONE):
        w = x3 - h
        if w < x5:
            continue
        x6.append((h, w))
    x7 = sorted(x6, key=lambda dims: (abs(dims[0] - dims[1]), -min(dims), -dims[0]))
    for dims in x7:
        x8 = [tuple(shift(piece, offset) for offset in _candidate_offsets_83b6b474(piece, dims)) for piece in x0]
        if any(len(cands) == ZERO for cands in x8):
            continue
        x9 = tuple(range(len(x0)))
        x10 = tuple(sorted(x9, key=lambda idx: (len(x8[idx]), -len(x0[idx]))))

        def search(k: int, used: frozenset[tuple[int, int]], placed: tuple[Object, ...]) -> tuple[Object, ...] | None:
            if k == len(x10):
                return placed
            idx = x10[k]
            for candidate in x8[idx]:
                cells = toindices(candidate)
                if used & cells:
                    continue
                result = search(k + ONE, used | cells, placed + (candidate,))
                if result is not None:
                    return result
            return None

        x11 = search(ZERO, frozenset(), ())
        if x11 is None:
            continue
        x12 = canvas(bg, dims)
        for piece in x11:
            x12 = paint(x12, piece)
        return x12
    raise ValueError("no border reconstruction found")


def verify_83b6b474(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = totuple(x1)
    x3 = _assemble_83b6b474(x0, x2)
    return x3
