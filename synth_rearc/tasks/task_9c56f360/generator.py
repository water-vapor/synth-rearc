from synth_rearc.core import *

from .verifier import verify_9c56f360


def _distribute_9c56f360(
    total: int,
    parts: int,
    minimum: int,
) -> tuple[int, ...]:
    if parts == ZERO:
        return ()
    values = [minimum for _ in range(parts)]
    for _ in range(total - parts * minimum):
        idx = randint(ZERO, parts - ONE)
        values[idx] += ONE
    return tuple(values)


def _make_row_9c56f360(
    width: int,
    role: str,
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    while True:
        if role == "empty":
            run_length = ZERO
        else:
            run_length = choice(tuple(v for v in (ONE, TWO, TWO) if v < width))
        if role == "settled":
            trailing_gap = run_length
        elif role == "active":
            trailing_gap = unifint(diff_lb, diff_ub, (run_length + ONE, width))
        else:
            trailing_gap = unifint(diff_lb, diff_ub, (ZERO, width - ONE))

        max_runs = min(THREE, width - trailing_gap)
        if role == "empty":
            if max_runs < ONE:
                continue
            run_options = tuple(v for v in (ONE, ONE, TWO, TWO, THREE) if v <= max_runs)
        else:
            run_options = tuple(v for v in (ZERO, ONE, ONE, TWO, TWO, THREE) if v <= max_runs)
        if len(run_options) == ZERO:
            continue
        nblue_runs = choice(run_options)

        if nblue_runs == ZERO:
            trailing_gap = width
            blue_total = ZERO
            prefix_zero_total = ZERO
        else:
            prefix_width = width - trailing_gap
            if prefix_width < nblue_runs:
                continue
            blue_total = unifint(diff_lb, diff_ub, (nblue_runs, prefix_width))
            prefix_zero_total = prefix_width - blue_total

        blue_runs = _distribute_9c56f360(blue_total, nblue_runs, ONE)
        prefix_gaps = _distribute_9c56f360(prefix_zero_total, nblue_runs, ZERO)
        slack = trailing_gap - run_length

        gi = []
        go = []
        for gap, blue_run in zip(prefix_gaps, blue_runs):
            gi.extend((ZERO,) * gap)
            go.extend((ZERO,) * gap)
            gi.extend((EIGHT,) * blue_run)
            go.extend((EIGHT,) * blue_run)
        gi.extend((ZERO,) * slack)
        gi.extend((THREE,) * run_length)
        go.extend((THREE,) * run_length)
        go.extend((ZERO,) * slack)

        if len(gi) != width:
            continue
        return tuple(gi), tuple(go)


def generate_9c56f360(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        height_value = unifint(diff_lb, diff_ub, (SEVEN, NINE))
        width_value = unifint(diff_lb, diff_ub, (SIX, NINE))
        max_active = min(FOUR, height_value)
        nactive = unifint(diff_lb, diff_ub, (ONE, max_active))
        active_rows = set(sample(range(height_value), nactive))

        rows_in = []
        rows_out = []
        blue_count = ZERO
        for row in range(height_value):
            if row in active_rows:
                role = "active"
            else:
                role = choice(("empty", "empty", "settled", "empty", "settled"))
            gi_row, go_row = _make_row_9c56f360(width_value, role, diff_lb, diff_ub)
            rows_in.append(gi_row)
            rows_out.append(go_row)
            blue_count += gi_row.count(EIGHT)

        gi = tuple(rows_in)
        go = tuple(rows_out)
        if blue_count == ZERO:
            continue
        if gi == go:
            continue
        if verify_9c56f360(gi) != go:
            continue
        return {"input": gi, "output": go}
