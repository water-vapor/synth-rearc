from synth_rearc.core import *


_UPWARD_T_d5c634a2 = frozenset({
    (ZERO, ONE),
    (ONE, ZERO),
    (ONE, ONE),
    (ONE, TWO),
})

_DOWNWARD_T_d5c634a2 = frozenset({
    (ZERO, ZERO),
    (ZERO, ONE),
    (ZERO, TWO),
    (ONE, ONE),
})

_LEFT_PATCHES_d5c634a2 = (
    frozenset(),
    frozenset({(ZERO, ZERO)}),
    frozenset({(ZERO, ZERO), (TWO, ZERO)}),
    frozenset({(ZERO, ZERO), (TWO, ZERO), (ZERO, TWO)}),
    frozenset({(ZERO, ZERO), (TWO, ZERO), (ZERO, TWO), (TWO, TWO)}),
)

_RIGHT_PATCHES_d5c634a2 = tuple(
    shift(patch, tojvec(THREE))
    for patch in _LEFT_PATCHES_d5c634a2
)

_COUNT_PAIRS_d5c634a2 = tuple(
    (nup, ndown)
    for nup in range(ONE, FIVE)
    for ndown in range(ONE, FIVE)
    if nup + ndown <= SEVEN
)


def _render_output_d5c634a2(nup: Integer, ndown: Integer) -> Grid:
    go = canvas(ZERO, (THREE, SIX))
    go = fill(go, THREE, _LEFT_PATCHES_d5c634a2[nup])
    go = fill(go, ONE, _RIGHT_PATCHES_d5c634a2[ndown])
    return go


def _blocked_patch_d5c634a2(patch: Patch) -> Indices:
    return combine(patch, mapply(dneighbors, patch))


def _place_ts_d5c634a2(h: Integer, w: Integer, templates: tuple[Patch, ...]) -> tuple[Patch, ...] | None:
    anchors = list(product(interval(ZERO, h - ONE, ONE), interval(ZERO, w - TWO, ONE)))
    shuffle(anchors)
    blocked = frozenset()
    placed = []
    for template in templates:
        chosen = None
        for anchor in anchors:
            candidate = shift(template, anchor)
            if candidate & blocked:
                continue
            chosen = candidate
            break
        if chosen is None:
            return None
        placed.append(chosen)
        blocked = combine(blocked, _blocked_patch_d5c634a2(chosen))
    return tuple(placed)


def generate_d5c634a2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (ZERO, len(_COUNT_PAIRS_d5c634a2) - ONE))
    x1, x2 = _COUNT_PAIRS_d5c634a2[x0]
    x3 = (_UPWARD_T_d5c634a2,) * x1 + (_DOWNWARD_T_d5c634a2,) * x2
    x4 = list(x3)
    while True:
        shuffle(x4)
        x5 = x1 + x2
        x6 = max(FIVE, x5 + TWO)
        x7 = max(FOUR, x5 + TWO)
        x8 = unifint(diff_lb, diff_ub, (x6, min(15, x6 + SIX)))
        x9 = unifint(diff_lb, diff_ub, (x7, min(15, x7 + SIX)))
        x10 = _place_ts_d5c634a2(x8, x9, tuple(x4))
        if x10 is None:
            continue
        gi = canvas(ZERO, (x8, x9))
        for patch in x10:
            gi = fill(gi, TWO, patch)
        go = _render_output_d5c634a2(x1, x2)
        return {"input": gi, "output": go}
