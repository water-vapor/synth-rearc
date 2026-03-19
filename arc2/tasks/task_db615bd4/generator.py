from arc2.core import *

from .helpers import packed_rectangles_db615bd4, sparse_box_db615bd4, sparse_rectangle_db615bd4


LANDSCAPE_DIMS_DB615BD4 = (
    (THREE, THREE),
    (THREE, FIVE),
    (FIVE, THREE),
    (FIVE, FIVE),
)

PORTRAIT_DIMS_DB615BD4 = LANDSCAPE_DIMS_DB615BD4 + ((ONE, THREE),)


def _base_grid_db615bd4(
    bg: Integer,
    lattice: Integer,
    n: Integer,
) -> Grid:
    x0 = canvas(bg, (n, n))
    x1 = frozenset((i, j) for i in range(ONE, n, TWO) for j in range(ONE, n, TWO))
    x2 = fill(x0, lattice, x1)
    return x2


def _ordered_starts_db615bd4(
    sizes: tuple[Integer, ...],
    lo: Integer,
    limit: Integer,
) -> tuple[Integer, ...] | None:
    out = []
    cursor = lo
    for k, size0 in enumerate(sizes):
        rem = sizes[k + ONE :]
        req = sum(rem) + max(ZERO, len(rem) - ONE)
        hi = limit - size0 if len(rem) == ZERO else limit - size0 - ONE - req
        cands = tuple(v for v in range(cursor, hi + ONE, TWO))
        if len(cands) == ZERO:
            return None
        start = choice(cands)
        out.append(start)
        cursor = start + size0 + ONE
    return tuple(out)


def generate_db615bd4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    n = 25
    colors = interval(ONE, TEN, ONE)
    while True:
        portrait_frame = choice((T, F))
        npieces = unifint(diff_lb, diff_ub, (TWO, THREE))
        dim_bank = PORTRAIT_DIMS_DB615BD4 if portrait_frame else LANDSCAPE_DIMS_DB615BD4
        piece_dims = tuple(choice(dim_bank) for _ in range(npieces))
        heights = tuple(h for h, _ in piece_dims)
        widths = tuple(w for _, w in piece_dims)
        pad = unifint(diff_lb, diff_ub, (ONE, THREE))

        if portrait_frame:
            inner_h = sum(heights) + npieces + ONE
            inner_w = max(widths) + double(pad)
        else:
            inner_h = max(heights) + double(pad)
            inner_w = sum(widths) + npieces + ONE

        frame_h = inner_h + TWO
        frame_w = inner_w + TWO
        if portrait_frame and frame_h <= frame_w:
            continue
        if (not portrait_frame) and frame_w <= frame_h:
            continue
        if frame_h > 15 or frame_w > 17:
            continue

        top_cands = tuple(range(THREE, n - frame_h - (ONE if portrait_frame else FIVE) + ONE, TWO))
        left_cands = tuple(range(THREE, n - frame_w - (FIVE if portrait_frame else ONE) + ONE, TWO))
        if len(top_cands) == ZERO or len(left_cands) == ZERO:
            continue
        top = choice(top_cands)
        left = choice(left_cands)

        if portrait_frame:
            piece_axis = _ordered_starts_db615bd4(heights, top + ONE, n)
        else:
            piece_axis = _ordered_starts_db615bd4(widths, ZERO, n)
        if piece_axis is None:
            continue

        if portrait_frame:
            piece_left_cands = tuple(
                tuple(range(left + frame_w + TWO, n - w + ONE, TWO))
                for w in widths
            )
            if any(len(cands) == ZERO for cands in piece_left_cands):
                continue
            piece_tops = piece_axis
            piece_lefts = tuple(choice(cands) for cands in piece_left_cands)
        else:
            piece_top_cands = tuple(
                tuple(range(top + frame_h + TWO, n - h + ONE, TWO))
                for h in heights
            )
            if any(len(cands) == ZERO for cands in piece_top_cands):
                continue
            piece_tops = tuple(choice(cands) for cands in piece_top_cands)
            piece_lefts = piece_axis

        palette = sample(colors, npieces + THREE)
        bg = palette[ZERO]
        lattice = palette[ONE]
        frame_color = palette[TWO]
        piece_colors = tuple(palette[THREE:])

        gi = _base_grid_db615bd4(bg, lattice, n)
        frame_patch = sparse_box_db615bd4(top, left, frame_h, frame_w)
        gi = fill(gi, frame_color, frame_patch)

        piece_patches = []
        for value, h, w, pi, pj in zip(piece_colors, heights, widths, piece_tops, piece_lefts):
            patch = sparse_rectangle_db615bd4(pi, pj, h, w)
            piece_patches.append(patch)
            gi = fill(gi, value, patch)

        x0 = gi
        for x1 in piece_patches:
            x0 = fill(x0, bg, x1)
        x2 = fill(x0, bg, backdrop(frame_patch))
        go = fill(x2, frame_color, box(frame_patch))
        x3 = packed_rectangles_db615bd4(frame_patch, piece_dims)
        for x4, x5 in zip(piece_colors, x3):
            go = fill(go, x4, x5)

        x6 = fgpartition(gi)
        x7 = argmax(x6, size)
        x8 = remove(x7, x6)
        x9 = argmax(x8, compose(size, backdrop))
        if x9 != recolor(frame_color, frame_patch):
            continue
        return {"input": gi, "output": go}
