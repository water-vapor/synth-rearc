`arc2_opus46_summary.json` was only partially useful. It correctly points to connected objects with square bounding boxes larger than `1x1`, but it says to place four diagonal corner marks. The official examples instead add eight `2` cells: the direct-neighbor cells on the outer border adjacent to each bounding-box corner.

`arc2_sonnet45_summary.jsonl` was rejected. It describes symmetry detection and a full outside border, but the official examples mark square-bounded objects regardless of symmetry and only place the eight corner-adjacent outbox cells, not an entire perimeter.
