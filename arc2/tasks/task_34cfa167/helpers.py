def horizontal_cycle_34cfa167(
    length: int,
    lead: int,
    tail: int,
    bg: int,
) -> tuple[int, ...]:
    period = (lead, bg, tail, bg)
    return tuple(period[idx % 4] for idx in range(length))


def vertical_cycle_34cfa167(
    length: int,
    lead: int,
    tail: int,
    bg: int,
) -> tuple[int, ...]:
    period = (lead, bg, tail, bg)
    return tuple(period[idx % 4] for idx in range(length))
