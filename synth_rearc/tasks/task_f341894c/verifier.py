from synth_rearc.core import *


def _same_line_markers_f341894c(
    markers: Indices,
    pair: Indices,
) -> Indices:
    if hline(pair):
        return sfilter(markers, matcher(first, uppermost(pair)))
    return sfilter(markers, matcher(last, leftmost(pair)))


def _is_valid_pair_f341894c(
    I: Grid,
    markers: Indices,
    a: IntegerTuple,
    b: IntegerTuple,
) -> Boolean:
    x0 = {index(I, a), index(I, b)}
    if x0 != {ONE, SIX}:
        return F
    x1 = frozenset({a, b})
    x2 = _same_line_markers_f341894c(markers, x1)
    return len(x2) > ZERO


def _candidate_pairs_f341894c(
    I: Grid,
    markers: Indices,
) -> tuple[Indices, ...]:
    x0 = combine(ofcolor(I, ONE), ofcolor(I, SIX))
    x1 = set()
    for x2 in x0:
        x3 = add(x2, RIGHT)
        if _is_valid_pair_f341894c(I, markers, x2, x3):
            x1.add(frozenset({x2, x3}))
        x4 = add(x2, DOWN)
        if _is_valid_pair_f341894c(I, markers, x2, x4):
            x1.add(frozenset({x2, x4}))
    return tuple(sorted(x1, key=lambda x5: (uppermost(x5), leftmost(x5), lowermost(x5), rightmost(x5))))


def verify_f341894c(I: Grid) -> Grid:
    x0 = ofcolor(I, SEVEN)
    x1 = _candidate_pairs_f341894c(I, x0)
    x2 = I
    for x3 in x1:
        x4 = _same_line_markers_f341894c(x0, x3)
        x5 = argmin(x4, lambda x6: manhattan(x3, frozenset({x6})))
        if hline(x3):
            x6 = uppermost(x3)
            if x5[ONE] < leftmost(x3):
                x7 = (x6, leftmost(x3))
                x8 = (x6, rightmost(x3))
            else:
                x7 = (x6, rightmost(x3))
                x8 = (x6, leftmost(x3))
        else:
            x6 = leftmost(x3)
            if x5[ZERO] < uppermost(x3):
                x7 = (uppermost(x3), x6)
                x8 = (lowermost(x3), x6)
            else:
                x7 = (lowermost(x3), x6)
                x8 = (uppermost(x3), x6)
        x2 = fill(x2, SIX, frozenset({x7}))
        x2 = fill(x2, ONE, frozenset({x8}))
    return x2
