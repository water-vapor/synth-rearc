Rule sketch for `135a2760`:

- The grid is split by full-background separator rows or columns into framed panels.
- Each panel contains a single foreground color on the global background color, with one of a small fixed family of periodic motifs.
- The input is a locally corrupted version of that motif; the output restores the closest valid motif for each panel independently.

Synthetic generator choices:

- Preserve the official layouts: one small horizontal panel, four stacked horizontal panels, or four side-by-side vertical panels.
- Use the observed horizontal and vertical motif families directly.
- Corrupt only interior foreground/background cells, then reject any corruption that the verifier would not repair back to the source panel.
