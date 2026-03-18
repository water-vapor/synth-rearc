from arc2.core import *


FILL_BY_SIZE = {
    FIVE: EIGHT,
    SEVEN: FOUR,
    NINE: THREE,
}


def _frame_patch(size: int, loc: tuple[int, int]) -> Indices:
    x0 = canvas(ZERO, (size, size))
    x1 = asindices(x0)
    x2 = box(x1)
    x3 = shift(x2, loc)
    return x3


def _center_patch(size: int, loc: tuple[int, int]) -> Indices:
    x0 = astuple(size // TWO, size // TWO)
    x1 = initset(x0)
    x2 = shift(x1, loc)
    return x2


def _reserved_patch(size: int, loc: tuple[int, int]) -> Indices:
    i, j = loc
    top = max(ZERO, i - ONE)
    left = max(ZERO, j - ONE)
    bottom = min(29, i + size)
    right = min(29, j + size)
    return frozenset((a, b) for a in range(top, bottom + ONE) for b in range(left, right + ONE))


def generate_00dbd492(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    count_bounds = (ONE, FOUR)
    sizeopts = (FIVE, FIVE, FIVE, SEVEN, SEVEN, NINE)
    while True:
        nsq = unifint(diff_lb, diff_ub, count_bounds)
        sizes = [choice(sizeopts) for _ in range(nsq)]
        placements = []
        reserved = frozenset({})
        failed = False
        for size in sorted(sizes, reverse=True):
            locs = []
            for i in range(31 - size):
                for j in range(31 - size):
                    loc = (i, j)
                    patch = _reserved_patch(size, loc)
                    if len(intersection(patch, reserved)) == ZERO:
                        locs.append(loc)
            if len(locs) == ZERO:
                failed = True
                break
            loc = choice(locs)
            placements.append((size, loc))
            reserved = combine(reserved, _reserved_patch(size, loc))
        if failed:
            continue
        gi = canvas(ZERO, (30, 30))
        go = canvas(ZERO, (30, 30))
        for size, loc in placements:
            frame = _frame_patch(size, loc)
            center = _center_patch(size, loc)
            part = combine(frame, center)
            gi = fill(gi, TWO, part)
            go = fill(go, TWO, part)
            go = underfill(go, FILL_BY_SIZE[size], delta(frame))
        occ = ofcolor(gi, TWO)
        top = uppermost(occ)
        bottom = lowermost(occ)
        left = leftmost(occ)
        right = rightmost(occ)
        boxh = bottom - top + ONE
        boxw = right - left + ONE
        dim = max(boxh, boxw)
        nred = colorcount(gi, TWO)
        mindim = max(dim, max(size + (TWO if size < NINE else ZERO) for size, _ in placements))
        while mindim * mindim <= 2 * nred:
            mindim += ONE
        dimub = min(30, mindim + TWO)
        outdim = unifint(diff_lb, diff_ub, (mindim, dimub))
        ilb = max(ZERO, bottom - outdim + ONE)
        iub = min(top, 30 - outdim)
        jlb = max(ZERO, right - outdim + ONE)
        jub = min(left, 30 - outdim)
        loci = randint(ilb, iub)
        locj = randint(jlb, jub)
        loc = (loci, locj)
        shp = (outdim, outdim)
        gi = crop(gi, loc, shp)
        go = crop(go, loc, shp)
        if choice((T, F)):
            gi = hmirror(gi)
            go = hmirror(go)
        if choice((T, F)):
            gi = vmirror(gi)
            go = vmirror(go)
        if mostcolor(gi) != ZERO:
            continue
        return {"input": gi, "output": go}
