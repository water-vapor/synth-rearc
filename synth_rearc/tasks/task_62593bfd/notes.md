Rule summary:
- Extract diagonal-connected monochrome objects.
- Objects of size `3`, `7`, or `9` move straight up until they touch the top border.
- The remaining official-family objects move straight down until they touch the bottom border.

Generator summary:
- Samples only motif templates observed in the official task family, plus mirrored/transposed variants.
- Places top-family motifs on the output ceiling and bottom-family motifs on the output floor first, then samples interior input rows that preserve the same columns.
