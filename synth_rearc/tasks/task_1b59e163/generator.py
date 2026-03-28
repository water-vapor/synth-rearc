from synth_rearc.core import *
from .verifier import verify_1b59e163


BASE_MOTIFS_1B59E163 = (
    {
        "body": frozenset({(1, 0), (1, 1), (1, 2), (2, 1)}),
        "anchor": (0, 1),
    },
    {
        "body": frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)}),
        "anchor": (2, 1),
    },
    {
        "body": frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}),
        "anchor": (1, 1),
    },
    {
        "body": frozenset({(0, 1), (1, 0), (1, 2)}),
        "anchor": (2, 1),
    },
    {
        "body": frozenset({(0, 1), (1, 1), (2, 0), (2, 2), (3, 1)}),
        "anchor": (2, 1),
    },
    {
        "body": frozenset({(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 2)}),
        "anchor": (2, 1),
    },
    {
        "body": frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 4), (2, 1), (2, 3)}),
        "anchor": (1, 2),
    },
)

TRANSFORMS_1B59E163 = (
    "identity",
    "rot90",
    "rot180",
    "rot270",
    "hmirror",
    "vmirror",
)

def _transform_loc_1b59e163(
    loc: IntegerTuple,
    h: int,
    w: int,
    mode: str,
) -> IntegerTuple:
    i, j = loc
    if mode == "identity":
        return (i, j)
    if mode == "rot90":
        return (j, h - ONE - i)
    if mode == "rot180":
        return (h - ONE - i, w - ONE - j)
    if mode == "rot270":
        return (w - ONE - j, i)
    if mode == "hmirror":
        return (h - ONE - i, j)
    return (i, w - ONE - j)


def _transform_motif_1b59e163(
    body: frozenset[IntegerTuple],
    anchor: IntegerTuple,
    mode: str,
) -> tuple[frozenset[IntegerTuple], IntegerTuple]:
    occupied = body | frozenset({anchor})
    h = max(i for i, _ in occupied) + ONE
    w = max(j for _, j in occupied) + ONE
    new_body = frozenset(_transform_loc_1b59e163(cell, h, w, mode) for cell in body)
    new_anchor = _transform_loc_1b59e163(anchor, h, w, mode)
    new_occupied = new_body | frozenset({new_anchor})
    di = min(i for i, _ in new_occupied)
    dj = min(j for _, j in new_occupied)
    norm_anchor = (new_anchor[0] - di, new_anchor[1] - dj)
    norm_body = frozenset((i - di, j - dj) for i, j in new_body)
    return norm_body, norm_anchor


def _shift_indices_1b59e163(
    cells: frozenset[IntegerTuple],
    offset: IntegerTuple,
) -> frozenset[IntegerTuple]:
    di, dj = offset
    return frozenset((i + di, j + dj) for i, j in cells)


def _expand_1b59e163(
    cells: frozenset[IntegerTuple],
    radius: int,
) -> frozenset[IntegerTuple]:
    out = set()
    for i, j in cells:
        for di in range(-radius, radius + ONE):
            for dj in range(-radius, radius + ONE):
                out.add((i + di, j + dj))
    return frozenset(out)


def _materialize_1b59e163(
    body: frozenset[IntegerTuple],
    anchor: IntegerTuple,
    body_color: int,
    anchor_color: int,
    offset: IntegerTuple,
) -> Object:
    di, dj = offset
    x0 = frozenset((body_color, (i + di, j + dj)) for i, j in body)
    x1 = frozenset({(anchor_color, (anchor[0] + di, anchor[1] + dj))})
    return x0 | x1


def generate_1b59e163(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    h = 18
    w = 18
    bgc = FOUR
    body_pool = (ONE, ONE, ONE, TWO)
    anchor_pool = (TWO, THREE, SIX, SEVEN, EIGHT, NINE)
    while True:
        gi = canvas(bgc, (h, w))
        go = canvas(bgc, (h, w))
        nin = frozenset()
        nout = frozenset()
        nmotifs = unifint(diff_lb, diff_ub, (TWO, FOUR))
        anchors = sample(anchor_pool, nmotifs)
        ok = True
        for anc in anchors:
            base = choice(BASE_MOTIFS_1B59E163)
            mode = choice(TRANSFORMS_1B59E163)
            body, anchor = _transform_motif_1b59e163(base["body"], base["anchor"], mode)
            occupied = body | frozenset({anchor})
            mh = max(i for i, _ in occupied) + ONE
            mw = max(j for _, j in occupied) + ONE
            body_color = choice(tuple(c for c in body_pool if c != anc))
            source = None
            for _ in range(400):
                top = randint(ZERO, h - mh)
                left = randint(ZERO, w - mw)
                footprint = _shift_indices_1b59e163(occupied, (top, left))
                if footprint & nin:
                    continue
                source = (top, left)
                nin = nin | _expand_1b59e163(footprint, ONE)
                break
            if source is None:
                ok = False
                break
            gi = paint(gi, _materialize_1b59e163(body, anchor, body_color, anc, source))
            ncopies = choice((ONE, ONE, TWO, TWO, THREE))
            for _ in range(ncopies):
                placed = False
                for _ in range(500):
                    top = randint(ZERO, h - mh)
                    left = randint(ZERO, w - mw)
                    footprint = _shift_indices_1b59e163(occupied, (top, left))
                    marker = (top + anchor[0], left + anchor[1])
                    if footprint & nout:
                        continue
                    if marker in nin:
                        continue
                    gi = fill(gi, anc, frozenset({marker}))
                    go = paint(go, _materialize_1b59e163(body, anchor, body_color, anc, (top, left)))
                    nin = nin | _expand_1b59e163(frozenset({marker}), ONE)
                    nout = nout | _expand_1b59e163(footprint, ONE)
                    placed = True
                    break
                if not placed:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        ngray = unifint(diff_lb, diff_ub, (TWO, FOUR))
        gray = set()
        for _ in range(500):
            if len(gray) == ngray:
                break
            cell = (randint(ZERO, h - ONE), randint(ZERO, w - ONE))
            if cell in nin:
                continue
            gray.add(cell)
            nin = nin | _expand_1b59e163(frozenset({cell}), ONE)
        if len(gray) != ngray:
            continue
        gi = fill(gi, FIVE, frozenset(gray))
        if gi == go:
            continue
        try:
            valid = verify_1b59e163(gi) == go
        except Exception:
            valid = False
        if not valid:
            continue
        return {"input": gi, "output": go}
