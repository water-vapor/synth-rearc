from synth_rearc.core import *


RoomRect89565ca0 = tuple[int, int, int, int]
ShapeSpec89565ca0 = dict[str, object]


def _room_dims_89565ca0(room: RoomRect89565ca0) -> tuple[int, int]:
    return (room[2] - room[0] + ONE, room[3] - room[1] + ONE)


def _room_patch_89565ca0(height: int, width: int) -> RoomRect89565ca0:
    return (ONE, ONE, height - TWO, width - TWO)


def _split_options_89565ca0(room: RoomRect89565ca0) -> tuple[str, ...]:
    x0 = room[2] - room[0] + ONE
    x1 = room[3] - room[1] + ONE
    x2: list[str] = []
    if x1 >= THREE:
        x2.extend(("v", "v", "v"))
    if x0 >= THREE:
        x2.append("h")
    return tuple(x2)


def _split_room_89565ca0(
    room: RoomRect89565ca0,
    orientation: str,
) -> tuple[frozenset[tuple[int, int]], tuple[RoomRect89565ca0, RoomRect89565ca0]]:
    x0, x1, x2, x3 = room
    if orientation == "v":
        x4 = randint(x1 + ONE, x3 - ONE)
        x5 = frozenset(connect((x0 - ONE, x4), (x2 + ONE, x4)))
        x6 = (x0, x1, x2, x4 - ONE)
        x7 = (x0, x4 + ONE, x2, x3)
        return x5, (x6, x7)
    x4 = randint(x0 + ONE, x2 - ONE)
    x5 = frozenset(connect((x4, x1 - ONE), (x4, x3 + ONE)))
    x6 = (x0, x1, x4 - ONE, x3)
    x7 = (x4 + ONE, x1, x2, x3)
    return x5, (x6, x7)


def _shape_grid_89565ca0(
    height: int,
    width: int,
    color: int,
    walls: frozenset[tuple[int, int]],
) -> Grid:
    x0 = canvas(ZERO, (height, width))
    x1 = recolor(color, walls)
    return paint(x0, x1)


def build_shape_spec_89565ca0(
    room_count: int,
    color: int,
) -> ShapeSpec89565ca0:
    for _ in range(200):
        x0 = randint(max(FOUR, room_count + TWO), min(TEN, room_count + SIX))
        x1 = randint(max(SIX, room_count * THREE + ONE), room_count * FIVE + FIVE)
        x2 = set(box(frozenset({(ZERO, ZERO), (x0 - ONE, x1 - ONE)})))
        x3 = [_room_patch_89565ca0(x0, x1)]
        x4 = T
        for _ in range(room_count - ONE):
            x5 = tuple((x6, _split_options_89565ca0(x6)) for x6 in x3)
            x6 = tuple(x7 for x7 in x5 if len(x7[1]) > ZERO)
            if len(x6) == ZERO:
                x4 = F
                break
            x7 = choice(x6)
            x8 = x7[0]
            x9 = choice(x7[1])
            x10, x11 = _split_room_89565ca0(x8, x9)
            x2.update(x10)
            x3.remove(x8)
            x3.extend(x11)
        if not x4:
            continue
        x5 = _shape_grid_89565ca0(x0, x1, color, frozenset(x2))
        return {
            "color": color,
            "room_count": room_count,
            "grid": x5,
            "rooms": tuple(x3),
            "walls": frozenset(x2),
            "height": x0,
            "width": x1,
        }
    raise RuntimeError("failed to build 89565ca0 room frame")


def damage_shape_spec_89565ca0(
    spec: ShapeSpec89565ca0,
    noise: int,
) -> ShapeSpec89565ca0:
    x0 = spec["color"]
    x1 = spec["grid"]
    x2 = spec["height"]
    x3 = spec["width"]
    x4 = min(SIX, min(x2, x3) - ONE)
    x5 = [list(x6) for x6 in x1]
    x6 = {x7 for x7 in spec["walls"]}
    x7 = {x8: sum((x8, x9) in x6 for x9 in range(x3)) for x8 in range(x2)}
    x8 = {x9: sum((x10, x9) in x6 for x10 in range(x2)) for x9 in range(x3)}
    x9 = tuple(
        x10 for x10 in x6
        if either(x7[x10[0]] >= x4, x8[x10[1]] >= x4)
    )
    x10 = list(x9)
    shuffle(x10)
    x11 = randint(ZERO, min(FOUR, len(x10) // max(TWO, x4)))
    x12 = ZERO
    for x13 in x10:
        if x12 == x11:
            break
        x14, x15 = x13
        x16 = both(x7[x14] >= x4, x7[x14] - ONE >= x4)
        x17 = both(x8[x15] >= x4, x8[x15] - ONE >= x4)
        if not either(x16, x17):
            continue
        x5[x14][x15] = noise
        x6.remove(x13)
        x7[x14] -= ONE
        x8[x15] -= ONE
        x12 += ONE
    x18 = tuple(tuple(x19) for x19 in x5)
    x20 = dict(spec)
    x20["grid"] = x18
    x20["walls"] = frozenset(x6)
    return x20


def translate_rooms_89565ca0(
    rooms: tuple[RoomRect89565ca0, ...],
    offset: tuple[int, int],
) -> tuple[RoomRect89565ca0, ...]:
    x0, x1 = offset
    return tuple(
        (x2 + x0, x3 + x1, x4 + x0, x5 + x1)
        for x2, x3, x4, x5 in rooms
    )


def can_place_grid_89565ca0(
    grid: Grid,
    top: int,
    left: int,
    height: int,
    width: int,
    occupied: frozenset[tuple[int, int]],
) -> bool:
    x0 = len(grid)
    x1 = len(grid[0])
    if top + x0 > height:
        return F
    if left + x1 > width:
        return F
    for x2, x3 in product(interval(ZERO, x0, ONE), interval(ZERO, x1, ONE)):
        if grid[x2][x3] == ZERO:
            continue
        x4 = (top + x2, left + x3)
        if x4 in occupied:
            return F
    return T


def paint_grid_89565ca0(
    grid: Grid,
    patch: Grid,
    top: int,
    left: int,
) -> Grid:
    x0 = [list(x1) for x1 in grid]
    x1 = len(patch)
    x2 = len(patch[0])
    for x3, x4 in product(interval(ZERO, x1, ONE), interval(ZERO, x2, ONE)):
        x5 = patch[x3][x4]
        if x5 == ZERO:
            continue
        x0[top + x3][left + x4] = x5
    return tuple(tuple(x6) for x6 in x0)


def occupied_cells_89565ca0(grid: Grid) -> frozenset[tuple[int, int]]:
    return frozenset((x0, x1) for x0, x2 in enumerate(grid) for x1, x3 in enumerate(x2) if x3 != ZERO)


def scatter_noise_89565ca0(
    grid: Grid,
    noise: int,
    occupied: frozenset[tuple[int, int]],
    count: int,
) -> tuple[Grid, frozenset[tuple[int, int]]]:
    x0 = [list(x1) for x1 in grid]
    x1 = set(occupied)
    x2 = len(grid)
    x3 = len(grid[0])
    x4 = ZERO
    x5 = ZERO
    while both(x4 < count, x5 < 5000):
        x5 += ONE
        x6 = randint(ZERO, x2 - ONE)
        x7 = randint(ZERO, x3 - ONE)
        x8 = choice((
            ((ZERO, ZERO),),
            ((ZERO, ZERO),),
            ((ZERO, ZERO), (ZERO, ONE)),
            ((ZERO, ZERO), (ONE, ZERO)),
        ))
        x9 = tuple(
            (x6 + x10, x7 + x11)
            for x10, x11 in x8
            if both(x6 + x10 < x2, x7 + x11 < x3)
        )
        if len(x9) == ZERO:
            continue
        x10 = all(x11 not in x1 for x11 in x9)
        if not x10:
            continue
        for x11 in x9:
            x0[x11[0]][x11[1]] = noise
            x1.add(x11)
        x4 += len(x9)
    return tuple(tuple(x12) for x12 in x0), frozenset(x1)
