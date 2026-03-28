from synth_rearc.core import *


def _make_body_row(
    bodyw: Integer,
    left: Integer,
    span: Integer,
    palette: Tuple[Integer, ...],
) -> Tuple[Integer, ...]:
    row = [ZERO] * bodyw
    right = left + span - ONE
    nsegs = choice((ONE, ONE, TWO))
    starts = list(range(left, right + ONE))
    shuffle(starts)
    made = ZERO
    used = set()
    for start in starts:
        if made == nsegs:
            break
        maxlen = min(THREE, right - start + ONE)
        seglen = choice(tuple(range(ONE, maxlen + ONE)))
        cells = tuple(range(start, start + seglen))
        if any(cell in used for cell in cells):
            continue
        value = choice(palette)
        for cell in cells:
            row[cell] = value
            used.add(cell)
        made += ONE
    if len(used) == ZERO:
        cell = choice(tuple(range(left, right + ONE)))
        row[cell] = choice(palette)
    return tuple(row)


def generate_12422b43(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(FIVE, interval(ONE, TEN, ONE))
    while True:
        w = unifint(diff_lb, diff_ub, (FIVE, SEVEN))
        k = unifint(diff_lb, diff_ub, (ONE, FOUR))
        extra = unifint(diff_lb, diff_ub, (ONE, THREE))
        reps = unifint(diff_lb, diff_ub, (ONE, THREE))
        h = k + extra + k * reps
        if not (FIVE <= h <= 13):
            continue
        bodyw = decrement(w)
        leftmax = min(ONE, bodyw - TWO)
        left = unifint(diff_lb, diff_ub, (ZERO, leftmax))
        spanmax = min(FOUR, bodyw - left - ONE)
        if spanmax < ONE:
            continue
        span = unifint(diff_lb, diff_ub, (ONE, spanmax))
        npcols = unifint(diff_lb, diff_ub, (TWO, min(FOUR, size(cols))))
        palette = tuple(sample(cols, npcols))

        body = tuple(_make_body_row(bodyw, left, span, palette) for _ in range(k + extra))
        if any(row.count(ZERO) == bodyw for row in body):
            continue
        template = body[:k]
        if k > ONE and len(set(template)) == ONE:
            continue
        usedcols = set()
        for row in body:
            usedcols.update(value for value in row if value != ZERO)
        if len(usedcols) < TWO:
            continue

        top = tuple(((FIVE,) + row) for row in template)
        middle = tuple(((ZERO,) + row) for row in body[k:])
        tail = tuple(tuple(ZERO for _ in range(w)) for _ in range(k * reps))
        gi = top + middle + tail

        repeated = tuple(((ZERO,) + template[idx % k]) for idx in range(k * reps))
        go = top + middle + repeated
        return {"input": gi, "output": go}
