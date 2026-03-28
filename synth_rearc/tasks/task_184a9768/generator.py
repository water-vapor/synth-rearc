from synth_rearc.core import *
from .verifier import verify_184a9768


MOTIFS_184A9768 = (
    frozenset({(0, 0)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2)}),
    frozenset({(0, 0), (0, 1), (0, 2), (0, 3)}),
    frozenset({(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)}),
    frozenset({(0, 0), (1, 0)}),
    frozenset({(0, 0), (1, 0), (2, 0)}),
    frozenset({(0, 0), (1, 0), (2, 0), (3, 0)}),
    frozenset({(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)}),
    frozenset({(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)}),
)


def _dims_184a9768(patch: frozenset[IntegerTuple]) -> tuple[int, int]:
    return (
        max(i for i, _ in patch) + 1,
        max(j for _, j in patch) + 1,
    )


def _shift_184a9768(
    patch: frozenset[IntegerTuple],
    offset: IntegerTuple,
) -> frozenset[IntegerTuple]:
    di, dj = offset
    return frozenset((i + di, j + dj) for i, j in patch)


def _expand_184a9768(
    patch: frozenset[IntegerTuple],
    radius: int,
) -> frozenset[IntegerTuple]:
    out = set()
    for i, j in patch:
        for di in range(-radius, radius + 1):
            for dj in range(-radius, radius + 1):
                out.add((i + di, j + dj))
    return frozenset(out)


def _touches_184a9768(
    patch: frozenset[IntegerTuple],
    other: frozenset[IntegerTuple],
) -> bool:
    return any(any(abs(i - a) + abs(j - b) == ONE for a, b in other) for i, j in patch)


def generate_184a9768(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = tuple(c for c in interval(ZERO, TEN, ONE) if c not in (ZERO, FIVE))
    while True:
        h = unifint(diff_lb, diff_ub, (20, 29))
        w = unifint(diff_lb, diff_ub, (20, 29))
        ncontainers = choice((ONE, TWO, TWO))
        if ncontainers == TWO and (h < 22 or w < 22):
            continue
        container_cols = sample(cols, ncontainers)
        container_specs = []
        blocked = frozenset()
        ok = True
        for idx in range(ncontainers):
            found = False
            for _ in range(200):
                ch = unifint(diff_lb, diff_ub, (6, 12 if ncontainers == ONE else 10))
                cw = unifint(diff_lb, diff_ub, (8, 15 if ncontainers == ONE else 13))
                if ch >= h - TWO or cw >= w - TWO:
                    continue
                top = randint(ONE, h - ch - ONE)
                left = randint(ONE, w - cw - ONE)
                rect = frozenset(
                    (i, j)
                    for i in range(top, top + ch)
                    for j in range(left, left + cw)
                )
                margin = _expand_184a9768(rect, TWO)
                if margin & blocked:
                    continue
                container_specs.append(
                    {
                        "color": container_cols[idx],
                        "top": top,
                        "left": left,
                        "height": ch,
                        "width": cw,
                        "rect": rect,
                    }
                )
                blocked = blocked | margin
                found = True
                break
            if not found:
                ok = False
                break
        if not ok:
            continue
        piece_specs = []
        ok = True
        for spec in container_specs:
            piece_pool = tuple(c for c in cols if c != spec["color"])
            npieces = unifint(diff_lb, diff_ub, (2, 4))
            holes = frozenset()
            pieces_here = []
            used_cols = []
            used_motifs = []
            for _ in range(npieces):
                found = False
                for _ in range(250):
                    motif_choices = tuple(x for x in MOTIFS_184A9768 if x not in used_motifs)
                    if len(motif_choices) == ZERO:
                        motif_choices = MOTIFS_184A9768
                    motif = choice(motif_choices)
                    color_choices = tuple(x for x in piece_pool if x not in used_cols)
                    if len(color_choices) == ZERO:
                        color_choices = piece_pool
                    color_value = choice(color_choices)
                    mh, mw = _dims_184a9768(motif)
                    if mh > spec["height"] - TWO or mw > spec["width"] - TWO:
                        continue
                    attach = len(holes) > ZERO and randint(ZERO, ONE) == ZERO
                    candidates = []
                    for top in range(spec["top"] + ONE, spec["top"] + spec["height"] - mh):
                        for left in range(spec["left"] + ONE, spec["left"] + spec["width"] - mw):
                            cells = _shift_184a9768(motif, (top, left))
                            if cells & holes:
                                continue
                            if attach and not _touches_184a9768(cells, holes):
                                continue
                            candidates.append(cells)
                    if len(candidates) == ZERO and attach:
                        for top in range(spec["top"] + ONE, spec["top"] + spec["height"] - mh):
                            for left in range(spec["left"] + ONE, spec["left"] + spec["width"] - mw):
                                cells = _shift_184a9768(motif, (top, left))
                                if not (cells & holes):
                                    candidates.append(cells)
                    if len(candidates) == ZERO:
                        continue
                    cells = choice(candidates)
                    piece = {
                        "color": color_value,
                        "motif": motif,
                        "inside": cells,
                    }
                    pieces_here.append(piece)
                    piece_specs.append(piece)
                    holes = holes | cells
                    used_cols.append(color_value)
                    used_motifs.append(motif)
                    found = True
                    break
                if not found:
                    ok = False
                    break
            if not ok:
                break
            spec["holes"] = holes
            spec["pieces"] = tuple(pieces_here)
        if not ok:
            continue
        occupied = frozenset().union(*(spec["rect"] for spec in container_specs))
        blocked = _expand_184a9768(occupied, ONE)
        shuffled_pieces = list(piece_specs)
        shuffle(shuffled_pieces)
        for piece in shuffled_pieces:
            found = False
            mh, mw = _dims_184a9768(piece["motif"])
            for _ in range(400):
                top = randint(ZERO, h - mh)
                left = randint(ZERO, w - mw)
                cells = _shift_184a9768(piece["motif"], (top, left))
                if cells & blocked:
                    continue
                piece["outside"] = cells
                blocked = blocked | _expand_184a9768(cells, ONE)
                occupied = occupied | cells
                found = True
                break
            if not found:
                ok = False
                break
        if not ok:
            continue
        free = tuple(
            (i, j)
            for i in range(h)
            for j in range(w)
            if (i, j) not in occupied
        )
        nnoise = unifint(diff_lb, diff_ub, (6, 12))
        if len(free) <= nnoise:
            continue
        noise = frozenset(sample(free, nnoise))
        gi = canvas(ZERO, (h, w))
        go = canvas(ZERO, (h, w))
        for spec in container_specs:
            gi = fill(gi, spec["color"], spec["rect"])
            gi = fill(gi, ZERO, spec["holes"])
            go = fill(go, spec["color"], spec["rect"])
        for piece in piece_specs:
            gi = fill(gi, piece["color"], piece["outside"])
            go = fill(go, piece["color"], piece["inside"])
        gi = fill(gi, FIVE, noise)
        if mostcolor(gi) != ZERO:
            continue
        if mostcolor(go) != ZERO:
            continue
        try:
            valid = verify_184a9768(gi) == go
        except Exception:
            valid = False
        if not valid:
            continue
        return {"input": gi, "output": go}
