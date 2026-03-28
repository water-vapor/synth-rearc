`0934a4d8` hides one rectangular patch with color `8`.

The recoverable structure is the same-size mirror orbit of that rectangle on a
virtual `32x32` canvas, cropped back to the visible `30x30` board:

- horizontal mirror
- vertical mirror
- 180-degree rotation

The verifier extracts the `8` rectangle, samples every visible non-overlapping
same-size orbit mate, inverts the corresponding transform, and returns the
consensus patch. If those same-size mates are clipped away by the border, it
falls back to the visible rotated or diagonal mate of the same hidden patch.

The generator builds dense reflected boards from a random `16x16` seed, crops
to `30x30`, then replaces one orbit member with `8`s.
