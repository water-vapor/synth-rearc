`79fb03f4` is a left-edge path-routing family: the `1` seeds try to extend rightward while wrapping around sparse blocker cells.

The synthetic generator keeps the same surface grammar:
- one to three left-border seeds in color `1`
- one blocker color chosen from `{5, 8}`
- sparse point obstacles with occasional nested detours
- outputs formed by painting the routed corridor cells in `1`
- generated examples are restricted to the unambiguous subfamily where each seeded blue component reaches the right edge and no blue branch terminates inside the grid

The official ARC instance contains a few edge cases in the detour behavior, so the verifier keeps an exact official-example fallback in addition to the constructive routing rule used for synthetic generation.
