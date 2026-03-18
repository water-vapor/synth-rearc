from arc2.core import *

from .verifier import verify_f341894c


RawSignalF341894C = tuple[str, Integer, Integer, Integer]


def _clustered_choice_f341894c(
    candidates: tuple[Integer, ...],
    used: set[Integer],
) -> Integer:
    if len(candidates) == ZERO:
        return None
    x0 = tuple(x1 for x1 in candidates if any(abs(x1 - x2) == ONE for x2 in used))
    if len(x0) > ZERO and choice((T, F)):
        return choice(x0)
    return choice(candidates)


def _marker_choice_f341894c(
    reused: tuple[Integer, ...],
    fresh: tuple[Integer, ...],
    prefer_max: Boolean,
) -> Integer:
    if len(reused) > ZERO and (len(fresh) == ZERO or choice((T, F))):
        return choice(reused)
    if len(fresh) == ZERO:
        return None
    if choice((T, T, F)):
        return max(fresh) if prefer_max else min(fresh)
    return choice(fresh)


def _sample_horizontal_signals_f341894c(
    side: Integer,
    total: Integer,
) -> tuple[tuple[RawSignalF341894C, ...], frozenset[Integer], frozenset[Integer], frozenset[Integer]] | None:
    x0 = tuple()
    x1 = set()
    x2 = set()
    x3 = set()
    x4 = set()
    x5 = set()
    x6 = set()
    for _ in range(total):
        x7 = None
        for _ in range(200):
            x8 = tuple(x9 for x9 in range(side) if x9 not in x1)
            if len(x8) == ZERO:
                return None
            x9 = _clustered_choice_f341894c(x8, x1)
            x10 = choice(("l", "r"))
            if x10 == "l":
                x11 = tuple(x12 for x12 in range(TWO, side - ONE) if x12 not in x6 and x12 + ONE not in x6)
            else:
                x11 = tuple(x12 for x12 in range(ZERO, side - THREE) if x12 not in x6 and x12 + ONE not in x6)
            if len(x11) == ZERO:
                continue
            x12 = tuple(x13 for x13 in x2 if x13 in x11)
            if len(x12) > ZERO and choice((T, F)):
                x13 = choice(x12)
            else:
                x13 = choice(x11)
            if x10 == "l":
                x14 = tuple(x15 for x15 in x4 if x15 <= x13 - TWO and x15 not in x3)
                x15 = tuple(x16 for x16 in range(ZERO, x13 - ONE) if x16 not in x3)
                x16 = _marker_choice_f341894c(x14, x15, F)
            else:
                x14 = tuple(x15 for x15 in x5 if x15 >= x13 + THREE and x15 not in x3)
                x15 = tuple(x16 for x16 in range(x13 + THREE, side) if x16 not in x3)
                x16 = _marker_choice_f341894c(x14, x15, T)
            if x16 is None:
                continue
            x7 = ("h", x9, x13, x16)
            break
        if x7 is None:
            return None
        _, x8, x9, x10 = x7
        x0 = x0 + (x7,)
        x1.add(x8)
        x2.add(x9)
        x3.add(x9)
        x3.add(x9 + ONE)
        x6.add(x10)
        if x10 < x9:
            x4.add(x10)
        else:
            x5.add(x10)
    return x0, frozenset(x1), frozenset(x3), frozenset(x6)


def _sample_vertical_signals_f341894c(
    side: Integer,
    total: Integer,
    horizontal_rows: frozenset[Integer],
    horizontal_domino_cols: frozenset[Integer],
    horizontal_marker_cols: frozenset[Integer],
) -> tuple[RawSignalF341894C, ...] | None:
    x0 = tuple()
    x1 = set()
    x2 = set()
    x3 = set()
    x4 = set()
    x5 = set()
    x6 = set(horizontal_domino_cols)
    x6.update(horizontal_marker_cols)
    for _ in range(total):
        x7 = None
        for _ in range(200):
            x8 = tuple(x9 for x9 in range(side) if x9 not in x1 and x9 not in x6)
            if len(x8) == ZERO:
                return None
            x9 = _clustered_choice_f341894c(x8, x1)
            x10 = choice(("u", "d"))
            x11 = x4 | x5
            if x10 == "u":
                x12 = tuple(
                    x12
                    for x12 in range(TWO, side - ONE)
                    if x12 not in horizontal_rows
                    and x12 + ONE not in horizontal_rows
                    and x12 not in x11
                    and x12 + ONE not in x11
                )
            else:
                x12 = tuple(
                    x12
                    for x12 in range(ZERO, side - THREE)
                    if x12 not in horizontal_rows
                    and x12 + ONE not in horizontal_rows
                    and x12 not in x11
                    and x12 + ONE not in x11
                )
            if len(x12) == ZERO:
                continue
            x13 = tuple(x14 for x14 in x2 if x14 in x12)
            if len(x13) > ZERO and choice((T, F)):
                x14 = choice(x13)
            else:
                x14 = _clustered_choice_f341894c(x12, x2)
            if x10 == "u":
                x15 = tuple(
                    x15
                    for x15 in x4
                    if x15 <= x14 - TWO and x15 not in x3 and x15 not in horizontal_rows
                )
                x16 = tuple(
                    x16
                    for x16 in range(ZERO, x14 - ONE)
                    if x16 not in x3 and x16 not in horizontal_rows
                )
                x17 = _marker_choice_f341894c(x15, x16, F)
            else:
                x15 = tuple(
                    x15
                    for x15 in x5
                    if x15 >= x14 + THREE and x15 not in x3 and x15 not in horizontal_rows
                )
                x16 = tuple(
                    x16
                    for x16 in range(x14 + THREE, side)
                    if x16 not in x3 and x16 not in horizontal_rows
                )
                x17 = _marker_choice_f341894c(x15, x16, T)
            if x17 is None:
                continue
            x7 = ("v", x14, x9, x17)
            break
        if x7 is None:
            return None
        _, x8, x9, x10 = x7
        x0 = x0 + (x7,)
        x1.add(x9)
        x2.add(x8)
        x3.add(x8)
        x3.add(x8 + ONE)
        if x10 < x8:
            x4.add(x10)
        else:
            x5.add(x10)
    return x0


def _signal_layout_f341894c(
    signal: RawSignalF341894C,
) -> tuple[IntegerTuple, IntegerTuple, IntegerTuple]:
    x0, x1, x2, x3 = signal
    if x0 == "h":
        x4 = (x1, x3)
        if x3 < x2:
            return (x1, x2), (x1, x2 + ONE), x4
        return (x1, x2 + ONE), (x1, x2), x4
    x4 = (x3, x2)
    if x3 < x1:
        return (x1, x2), (x1 + ONE, x2), x4
    return (x1 + ONE, x2), (x1, x2), x4


def _render_signal_f341894c(
    signal: RawSignalF341894C,
    flipped: Boolean,
) -> Object:
    x0, x1, x2 = _signal_layout_f341894c(signal)
    if flipped:
        x3 = frozenset({(ONE, x0), (SIX, x1), (SEVEN, x2)})
    else:
        x3 = frozenset({(SIX, x0), (ONE, x1), (SEVEN, x2)})
    return x3


def _build_grid_f341894c(
    side: Integer,
    signals: tuple[RawSignalF341894C, ...],
    flipped_ids: frozenset[Integer],
) -> Grid:
    x0 = canvas(EIGHT, (side, side))
    for x1, x2 in enumerate(signals):
        x3 = _render_signal_f341894c(x2, x1 in flipped_ids)
        x0 = paint(x0, x3)
    return x0


def generate_f341894c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = double(unifint(diff_lb, diff_ub, (4, 11)))
        x1 = max(FOUR, min(x0 - TWO, x0 // TWO + randint(-1, 2)))
        x2 = randint(ONE, x1 - ONE)
        x3 = x1 - x2
        x4 = _sample_horizontal_signals_f341894c(x0, x2)
        if x4 is None:
            continue
        x5, x6, x7, x8 = x4
        x9 = _sample_vertical_signals_f341894c(x0, x3, x6, x7, x8)
        if x9 is None:
            continue
        x10 = x5 + x9
        x11 = randint(ONE, len(x10))
        x12 = frozenset(sample(tuple(range(len(x10))), x11))
        x13 = _build_grid_f341894c(x0, x10, x12)
        x14 = _build_grid_f341894c(x0, x10, frozenset())
        if x13 == x14:
            continue
        if verify_f341894c(x13) != x14:
            continue
        return {"input": x13, "output": x14}
