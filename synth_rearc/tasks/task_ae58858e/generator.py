from synth_rearc.core import *

from .verifier import verify_ae58858e


SMALL_COMPONENTS_AE58858E = (
    frozenset({(0, 0)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (1, 0)}),
    frozenset({(0, 0), (0, 1), (0, 2)}),
    frozenset({(0, 0), (1, 0), (2, 0)}),
    frozenset({(0, 0), (0, 1), (1, 0)}),
    frozenset({(0, 0), (0, 1), (1, 1)}),
    frozenset({(0, 0), (1, 0), (1, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1)}),
)


def _frontier_key_ae58858e(
    patch: frozenset[tuple[int, int]],
    cell: tuple[int, int],
) -> tuple[int, int, int]:
    x0 = patch | frozenset({cell})
    x1 = sum(ONE for x2 in dneighbors(cell) if x2 in patch)
    x2 = multiply(height(x0), width(x0))
    x3 = add(height(x0), width(x0))
    return (x1, invert(x2), invert(x3))


def _large_component_ae58858e(size_target: int) -> frozenset[tuple[int, int]]:
    while True:
        x0 = frozenset({ORIGIN})
        x1 = FOUR if size_target <= SIX else FIVE
        while len(x0) < size_target:
            x2 = set()
            for x3 in x0:
                for x4 in dneighbors(x3):
                    if x4 in x0:
                        continue
                    x5 = x0 | frozenset({x4})
                    if greater(height(x5), x1) or greater(width(x5), x1):
                        continue
                    x2.add(x4)
            if len(x2) == ZERO:
                break
            x6 = tuple(sorted(x2, key=lambda x7: _frontier_key_ae58858e(x0, x7), reverse=True))
            x7 = min(THREE, len(x6))
            x8 = choice(x6[:x7])
            x0 = x0 | frozenset({x8})
        x9 = normalize(x0)
        if len(x9) != size_target:
            continue
        if equality(height(x9), ONE) or equality(width(x9), ONE):
            continue
        return x9


def _component_ae58858e(size_target: int) -> frozenset[tuple[int, int]]:
    if size_target <= THREE:
        x0 = tuple(x1 for x1 in SMALL_COMPONENTS_AE58858E if len(x1) == size_target)
        return choice(x0)
    return _large_component_ae58858e(size_target)


def _blocked_cells_ae58858e(
    patch: frozenset[tuple[int, int]],
    dimensions: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    x0, x1 = dimensions
    x2 = set(patch)
    for x3 in patch:
        x2.update(neighbors(x3))
    return frozenset((i, j) for i, j in x2 if 0 <= i < x0 and 0 <= j < x1)


def generate_ae58858e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (SIX, 12))
        x1 = unifint(diff_lb, diff_ub, (SIX, 13))
        x2 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x3 = unifint(diff_lb, diff_ub, (TWO, FIVE))
        x4 = [randint(FOUR, SEVEN) for _ in range(x2)]
        x5 = [randint(ONE, THREE) for _ in range(x3)]
        x6 = sorted(x4 + x5, reverse=True)
        x7 = canvas(ZERO, (x0, x1))
        x8 = canvas(ZERO, (x0, x1))
        x9 = frozenset()
        x10 = ZERO
        x11 = ZERO
        x12 = T
        for x13 in x6:
            x14 = _component_ae58858e(x13)
            x15 = height(x14)
            x16 = width(x14)
            x17 = F
            for _ in range(100):
                x18 = randint(ZERO, subtract(x0, x15))
                x19 = randint(ZERO, subtract(x1, x16))
                x20 = shift(x14, (x18, x19))
                if len(intersection(x20, x9)) != ZERO:
                    continue
                x17 = T
                break
            if flip(x17):
                x12 = F
                break
            x7 = fill(x7, TWO, x20)
            x21 = branch(greater(x13, THREE), SIX, TWO)
            x8 = fill(x8, x21, x20)
            x9 = combine(x9, _blocked_cells_ae58858e(x20, (x0, x1)))
            x10 = add(x10, branch(greater(x13, THREE), ONE, ZERO))
            x11 = add(x11, branch(greater(FOUR, x13), ONE, ZERO))
        if flip(x12):
            continue
        if flip(equality(verify_ae58858e(x7), x8)):
            continue
        if equality(x7, x8):
            continue
        if either(equality(x10, ZERO), equality(x11, ZERO)):
            continue
        return {"input": x7, "output": x8}
