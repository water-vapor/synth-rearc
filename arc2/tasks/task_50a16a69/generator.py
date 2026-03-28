from arc2.core import *
from .verifier import verify_50a16a69


PATTERN_PERIODS_50A16A69 = (TWO, TWO, THREE, FOUR)
NONZERO_COLORS_50A16A69 = tuple(range(ONE, TEN))


def _row_50a16a69(
    palette_: tuple[int, ...],
    shift_: int,
    row_idx: int,
    width_: int,
    offset_: int,
) -> tuple[int, ...]:
    x0 = ZERO if row_idx % TWO == ZERO else shift_
    return tuple(
        palette_[(x0 + j + offset_) % len(palette_)]
        for j in range(width_)
    )


def _render_output_50a16a69(
    palette_: tuple[int, ...],
    shift_: int,
    size_: int,
) -> Grid:
    return tuple(
        _row_50a16a69(palette_, shift_, i, size_, ONE)
        for i in range(size_)
    )


def _render_input_50a16a69(
    palette_: tuple[int, ...],
    filler_: int,
    shift_: int,
    size_: int,
    visible_: int,
) -> Grid:
    x0 = canvas(filler_, (size_, size_))
    x1 = tuple(_row_50a16a69(palette_, shift_, i, visible_, ZERO) for i in range(visible_))
    x2 = tuple(
        tuple(
            filler_ if j >= visible_ else x1[i][j]
            for j in range(size_)
        )
        for i in range(visible_)
    )
    return x2 + tuple(x0[i] for i in range(visible_, size_))


def generate_50a16a69(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        size_ = unifint(diff_lb, diff_ub, (SIX, 30))
        period_ = choice(PATTERN_PERIODS_50A16A69)
        min_visible = max(FIVE, add(period_, TWO))
        if size_ <= min_visible:
            size_ = min_visible + ONE
        visible_ = unifint(diff_lb, diff_ub, (min_visible, decrement(size_)))
        colors = sample(NONZERO_COLORS_50A16A69, increment(period_))
        palette_ = tuple(colors[:period_])
        filler_ = colors[-ONE]
        shift_ = halve(period_) if even(period_) else ONE
        gi = _render_input_50a16a69(palette_, filler_, shift_, size_, visible_)
        go = _render_output_50a16a69(palette_, shift_, size_)
        if gi == go:
            continue
        if verify_50a16a69(gi) != go:
            continue
        return {"input": gi, "output": go}
