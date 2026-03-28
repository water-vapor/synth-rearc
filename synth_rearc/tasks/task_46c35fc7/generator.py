from synth_rearc.core import *


_RING_PATCH_46c35fc7 = frozenset(
    {
        (ZERO, ZERO),
        (ZERO, ONE),
        (ZERO, TWO),
        (ONE, ZERO),
        (ONE, TWO),
        (TWO, ZERO),
        (TWO, ONE),
        (TWO, TWO),
    }
)
_NON_SEVEN_COLORS_46c35fc7 = tuple(value for value in range(10) if value != SEVEN)


def _transform_block_46c35fc7(
    block: Grid,
) -> Grid:
    return (
        (block[ZERO][TWO], block[ONE][ZERO], block[TWO][TWO]),
        (block[TWO][ONE], block[ONE][ONE], block[ZERO][ONE]),
        (block[ZERO][ZERO], block[ONE][TWO], block[TWO][ZERO]),
    )


def _make_block_46c35fc7(
    values: tuple[int, ...],
) -> Grid:
    return (
        (values[ZERO], values[ONE], values[TWO]),
        (values[THREE], SEVEN, values[FOUR]),
        (values[FIVE], values[SIX], values[SEVEN]),
    )


def _halo_46c35fc7(
    patch: Indices,
) -> Indices:
    out = set(patch)
    for loc in patch:
        out.update(dneighbors(loc))
    return frozenset(out)


def generate_46c35fc7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    dims = (SEVEN, SEVEN)
    positions = [(i, j) for i in range(FIVE) for j in range(FIVE)]
    while True:
        count = unifint(diff_lb, diff_ub, (ONE, TWO))
        shuffle(positions)
        blocked = frozenset()
        offsets = []
        for offset in positions:
            patch = shift(_RING_PATCH_46c35fc7, offset)
            halo = _halo_46c35fc7(patch)
            if len(intersection(halo, blocked)) > ZERO:
                continue
            offsets.append(offset)
            blocked = combine(blocked, halo)
            if len(offsets) == count:
                break
        if len(offsets) != count:
            continue
        gi = canvas(SEVEN, dims)
        go = canvas(SEVEN, dims)
        for offset in offsets:
            while True:
                values = tuple(choice(_NON_SEVEN_COLORS_46c35fc7) for _ in range(EIGHT))
                block = _make_block_46c35fc7(values)
                transformed = _transform_block_46c35fc7(block)
                if block != transformed:
                    break
            gi = paint(gi, shift(asobject(block), offset))
            go = paint(go, shift(asobject(transformed), offset))
        return {"input": gi, "output": go}
