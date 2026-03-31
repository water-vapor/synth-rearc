Rule sketch for `e376de54`:

- The foreground decomposes into straight monochrome segments of one shared orientation.
- One endpoint of every segment already lies on a common support line.
- The segment ordered at the median position along that support line gives the canonical length.
- The output keeps the aligned endpoint fixed for every segment and extends or trims each segment to that canonical length.

Generator sketch:

- Sample a 16x16 background-7 grid.
- Place 3 or 5 horizontal, vertical, or anti-diagonal segments with aligned anchor endpoints.
- Keep the median anchor-position segment at the canonical length and perturb the others shorter or longer.
- Use 1 to 3 contiguous color runs along the ordered segment family to mimic the official task layouts.
