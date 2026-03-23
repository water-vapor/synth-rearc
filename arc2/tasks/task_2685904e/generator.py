from arc2.core import *


HEIGHT_2685904e = TEN
WIDTH_2685904e = TEN
SEPARATOR_ROW_2685904e = SIX
SOURCE_ROW_2685904e = EIGHT
ROW_COLORS_2685904e = remove(FIVE, interval(ONE, TEN, ONE))


def _sample_counts_2685904e(
    total: Integer,
    target: Integer,
    keep_count: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, ...]:
    if total == ZERO:
        return ()
    max_parts = min(total, FIVE - keep_count)
    while True:
        nparts = unifint(diff_lb, diff_ub, (ONE, max_parts))
        counts = []
        remaining = total
        for idx in range(nparts):
            if idx == nparts - ONE:
                value = remaining
            else:
                slots = nparts - idx - ONE
                upper = remaining - slots
                value = randint(ONE, upper)
            counts.append(value)
            remaining -= value
        shuffle(counts)
        if all(value != target for value in counts):
            return tuple(counts)


def generate_2685904e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    n = unifint(diff_lb, diff_ub, (ONE, FOUR))
    max_keep = min(THREE, (WIDTH_2685904e - ONE) // n)
    nkeep = unifint(diff_lb, diff_ub, (ONE, max_keep))
    keep_colors = sample(ROW_COLORS_2685904e, nkeep)
    remainder = WIDTH_2685904e - nkeep * n
    extra_counts = _sample_counts_2685904e(remainder, n, nkeep, diff_lb, diff_ub)
    extra_colors = sample(difference(ROW_COLORS_2685904e, keep_colors), len(extra_counts))
    row_values = []
    for color in keep_colors:
        row_values.extend([color] * n)
    for color, count in zip(extra_colors, extra_counts):
        row_values.extend([color] * count)
    shuffle(row_values)
    row_values = tuple(row_values)

    gi = canvas(ZERO, (HEIGHT_2685904e, WIDTH_2685904e))
    top_run = frozenset((ZERO, j) for j in range(n))
    separator = frozenset((SEPARATOR_ROW_2685904e, j) for j in range(WIDTH_2685904e))
    source = frozenset((value, (SOURCE_ROW_2685904e, j)) for j, value in enumerate(row_values))
    gi = fill(gi, EIGHT, top_run)
    gi = fill(gi, FIVE, separator)
    gi = paint(gi, source)

    go = gi
    bars = frozenset(
        (value, (i, j))
        for j, value in enumerate(row_values)
        if value in keep_colors
        for i in range(SEPARATOR_ROW_2685904e - n, SEPARATOR_ROW_2685904e)
    )
    go = paint(go, bars)
    return {"input": gi, "output": go}
