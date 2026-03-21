The summary hints were directionally useful but needed a correction.

The misleading part is the phrase "nearest side". In the official examples, the
projection axis is determined by alignment with the block, not by generic geometric
proximity: if a marker's row intersects the `1` block, it projects horizontally to the
left or right face; otherwise it projects vertically to the top or bottom face. The
second training pair shows this most clearly, because the right-hand `9` is closer to
the top/bottom faces in absolute distance but still moves horizontally.

The distance threshold is also strict: a marker lands on the block edge only when its
distance to that face is less than the block size on that axis. When the distance is
equal to or greater than that size, it lands one cell outside the block instead.
