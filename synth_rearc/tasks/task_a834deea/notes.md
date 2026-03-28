`arc2_opus46_summary.json` is correct for `a834deea`.

`arc2_sonnet45_summary.jsonl` overfits to connected 0-components and to existing interior 8s as "anchors". That fails on the official test-style bottom-left motif, whose 5x5 box contains a disconnected singleton 0 in the interior but still receives the same fixed stencil.

Correct rule:
- Find every 5x5 box whose outer border is all 0.
- Treat the box's top-left corner as the anchor.
- Overlay the fixed interior stencil
  `1 7 6`
  `4 0 5`
  `2 9 3`
  one cell down and one cell right from that anchor.
- Only write labels into positions that are 0 in the input; keep interior 8s unchanged.
