`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded because it describes overlaying multiple rectangles into one composite output. The official examples instead have a single selected object whose bounding-box gaps are matched by separate external components of the same shapes, and the output is just that object's cropped bounding box with those gaps recolored.
