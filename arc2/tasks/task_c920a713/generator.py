from collections import Counter

from arc2.core import *


_TEMPLATE_GRIDS_C920A713 = (
    (
        "000000011111000000",
        "000033313301000000",
        "000030010301000000",
        "222232215351555000",
        "200030210301005000",
        "200033313301005000",
        "222222210077777777",
        "000000510071005007",
        "000000515571555007",
        "000000010071000007",
        "000000011171000007",
        "000000000070000007",
        "000000000070000007",
        "000000000070000007",
        "000000000070000007",
        "000000000077777777",
    ),
    (
        "0333330000",
        "1311232210",
        "1333330210",
        "1000200210",
        "1000244244",
        "1000240214",
        "1000222214",
        "1088848814",
        "1080044444",
        "1111111110",
        "0088888800",
    ),
    (
        "22222220000000000000",
        "20000020000000000000",
        "20000020000000000000",
        "20000020000000000000",
        "44444444444444444400",
        "40000020000000000400",
        "40000020000000000400",
        "40055555555555500400",
        "40050020000000500400",
        "42252220000000500400",
        "40050000000000500400",
        "40050000000000500400",
        "40050999999777577777",
        "40050900000790500407",
        "33353934444744544407",
        "30055555555555500007",
        "30000930000790000007",
        "30000930000790000007",
        "30000999999790000007",
        "30000030000700000007",
        "33333330000777777777",
    ),
    (
        "0000000000022222222",
        "0000000000020000002",
        "0000000000020000002",
        "0000000000020000002",
        "0000000000020000002",
        "0333333333333300002",
        "0300000000020300002",
        "0305555555555555002",
        "0305000000022325222",
        "0305000000000305000",
        "0305000000000305000",
        "0305000000000305000",
        "0305000000000305000",
        "1111110066666666688",
        "1305010060000805608",
        "1305515565555555608",
        "1300010060000800608",
        "1333313363333800608",
        "1000444464400888688",
        "1000410060400000600",
        "1111444464400000600",
        "0000000066666666600",
    ),
)


def _parse_template_c920a713(rows: tuple[str, ...]) -> Grid:
    return tuple(tuple(int(x0) for x0 in x1) for x1 in rows)


def _target_grid_c920a713(colors: Tuple) -> Grid:
    x0 = subtract(double(len(colors)), ONE)
    x1 = canvas(first(colors), (x0, x0))
    for x2, x3 in enumerate(colors[1:], ONE):
        x4 = decrement(subtract(x0, x2))
        x5 = box(frozenset({(x2, x2), (x4, x4)}))
        x1 = fill(x1, x3, x5)
    return x1


def _intrusion_order_c920a713(grid: Grid) -> Tuple:
    x0 = fgpartition(grid)
    x1 = order(x0, color)
    x2 = tuple(color(x3) for x3 in x1)
    x3 = {color(x4): x4 for x4 in x1}
    x4 = {x5: Counter(x6 for x6, _ in toobject(box(x3[x5]), grid) if x6 != x5) for x5 in x2}
    x5 = {x6: sum(x7.values()) for x6, x7 in x4.items()}
    x6 = {x7: height(x3[x7]) * width(x3[x7]) for x7 in x2}
    x7 = [min(x2, key=lambda x8: (x5[x8], x6[x8], x8))]
    x8 = set(x2) - set(x7)
    while len(x8) > ZERO:
        x9 = set(x7)
        x10 = min(
            x8,
            key=lambda x11: (
                sum(x12 for x13, x12 in x4[x11].items() if x13 not in x9),
                -sum(x12 for x13, x12 in x4[x11].items() if x13 in x9),
                x5[x11],
                x6[x11],
                x11,
            ),
        )
        x7.append(x10)
        x8.remove(x10)
    return tuple(reversed(x7))


def _recolor_template_c920a713(
    grid: Grid,
    source_order: Tuple,
    target_order: Tuple,
) -> Grid:
    x0 = {x1: x2 for x1, x2 in zip(source_order, target_order)}
    return tuple(tuple(x0[x3] if x3 != ZERO else ZERO for x3 in x4) for x4 in grid)


def _embed_grid_c920a713(
    grid: Grid,
    shape_: tuple[int, int],
    offset: tuple[int, int],
) -> Grid:
    return paint(canvas(ZERO, shape_), shift(asobject(grid), offset))


def generate_c920a713(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _parse_template_c920a713(choice(_TEMPLATE_GRIDS_C920A713))
        x1 = _intrusion_order_c920a713(x0)
        x2 = tuple(sample((ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE), len(x1)))
        gi = _recolor_template_c920a713(x0, x1, x2)
        x3, x4 = shape(gi)
        x5 = unifint(diff_lb, diff_ub, (x3, 30))
        x6 = unifint(diff_lb, diff_ub, (x4, 30))
        x7 = randint(ZERO, subtract(x5, x3))
        x8 = randint(ZERO, subtract(x6, x4))
        gi = _embed_grid_c920a713(gi, (x5, x6), (x7, x8))
        x9 = choice((ZERO, ZERO, ONE, TWO, THREE))
        for _ in range(x9):
            gi = rot90(gi)
        if choice((T, F)):
            gi = hmirror(gi)
        if choice((T, F)):
            gi = vmirror(gi)
        x10 = _intrusion_order_c920a713(gi)
        go = _target_grid_c920a713(x10)
        if gi == go:
            continue
        return {"input": gi, "output": go}
