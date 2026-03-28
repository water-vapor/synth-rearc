from synth_rearc.core import *


SIDE_OPTIONS_5ADEE1B2 = (20, 20, 22, 24, 26)
COUNT_OPTIONS_5ADEE1B2 = (ONE, TWO, TWO, THREE, THREE)
TEMPLATE_ROWS_5ADEE1B2 = (
    (
        ".###.",
        ".#.#.",
        "##.##",
        ".#.#.",
        "#####",
    ),
    (
        "##.##",
        ".#.#.",
        ".###.",
        "..#..",
        ".###.",
    ),
    (
        ".#.#.",
        ".#.#.",
        "##.##",
        ".###.",
        "..#..",
    ),
    (
        ".#.#.",
        "#####",
        ".#.#.",
        "##.##",
        ".###.",
    ),
    (
        "##.##",
        ".###.",
        ".#.#.",
        "##.##",
        ".###.",
    ),
    (
        ".###",
        "##.#",
        ".#.#",
        ".#.#",
        "####",
    ),
)


def _parse_template_5adee1b2(
    rows: tuple[str, ...],
) -> Indices:
    return frozenset((i, j) for i, row in enumerate(rows) for j, value in enumerate(row) if value == "#")


def _motif_bank_5adee1b2() -> tuple[Indices, ...]:
    motifs = set()
    for rows in TEMPLATE_ROWS_5ADEE1B2:
        x0 = _parse_template_5adee1b2(rows)
        x1 = normalize(x0)
        x2 = normalize(hmirror(x0))
        x3 = normalize(vmirror(x0))
        x4 = normalize(vmirror(hmirror(x0)))
        motifs.add(x1)
        motifs.add(x2)
        motifs.add(x3)
        motifs.add(x4)
    return tuple(motifs)


MOTIFS_5ADEE1B2 = _motif_bank_5adee1b2()


def _legend_object_5adee1b2(
    top: Integer,
) -> Indices:
    return frozenset({(top, ZERO), (top + ONE, ZERO)})


def _reserve_patch_5adee1b2(
    patch: Indices,
    dims: tuple[int, int],
) -> Indices:
    h, w = dims
    x0 = backdrop(outbox(patch))
    return frozenset((i, j) for i, j in x0 if 0 <= i < h and 0 <= j < w)


def _placement_candidates_5adee1b2(
    patch: Indices,
    dims: tuple[int, int],
    reserved: Indices,
) -> tuple[Indices, ...]:
    h, w = dims
    ph, pw = shape(patch)
    out = []
    for i in range(ONE, h - ph):
        for j in range(ONE, w - pw):
            x0 = shift(patch, (i, j))
            x1 = _reserve_patch_5adee1b2(x0, dims)
            if len(intersection(x1, reserved)) == ZERO:
                out.append(x0)
    return tuple(out)


def _frame_patch_5adee1b2(
    patch: Indices,
) -> Indices:
    x0 = canvas(ZERO, shape(patch))
    x1 = fill(x0, ONE, normalize(patch))
    x2 = objects(x1, T, F, F)
    x3 = colorfilter(x2, ZERO)
    x4 = rbind(bordering, x1)
    x5 = sfilter(x3, x4)
    x6 = shift(toindices(merge(x5)), ulcorner(patch))
    return combine(x6, outbox(patch))


def generate_5adee1b2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    colors = remove(ZERO, interval(ZERO, TEN, ONE))
    for _ in range(400):
        side = choice(SIDE_OPTIONS_5ADEE1B2)
        dims = (side, side)
        palette = sample(colors, FOUR)
        pairs = ((palette[0], palette[2]), (palette[1], palette[3]))
        gi = canvas(ZERO, dims)
        go = canvas(ZERO, dims)
        reserved = frozenset({})
        legend_tops = (side - FIVE, side - TWO)
        for top, (obj_color, frame_color) in zip(legend_tops, pairs):
            x0 = _legend_object_5adee1b2(top)
            x1 = shift(x0, RIGHT)
            x2 = combine(x0, x1)
            gi = fill(gi, obj_color, x0)
            gi = fill(gi, frame_color, x1)
            go = fill(go, obj_color, x0)
            go = fill(go, frame_color, x1)
            reserved = combine(reserved, _reserve_patch_5adee1b2(x2, dims))
        placed = []
        failed = F
        for obj_color, frame_color in pairs:
            nobjs = choice(COUNT_OPTIONS_5ADEE1B2)
            for _ in range(nobjs):
                motifs = list(MOTIFS_5ADEE1B2)
                shuffle(motifs)
                candidates = ()
                patch = frozenset({})
                for motif in motifs:
                    x0 = _placement_candidates_5adee1b2(motif, dims, reserved)
                    if len(x0) > ZERO:
                        patch = choice(x0)
                        candidates = x0
                        break
                if len(candidates) == ZERO:
                    failed = T
                    break
                gi = fill(gi, obj_color, patch)
                go = fill(go, obj_color, patch)
                go = fill(go, frame_color, _frame_patch_5adee1b2(patch))
                reserved = combine(reserved, _reserve_patch_5adee1b2(patch, dims))
                placed.append((obj_color, patch))
            if failed:
                break
        if failed:
            continue
        if len(placed) < TWO:
            continue
        if gi == go:
            continue
        return {"input": gi, "output": go}
    raise RuntimeError("failed to generate 5adee1b2 example")
