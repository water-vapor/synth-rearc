Used `arc2_opus46_summary.json` as the starting hypothesis, but corrected both hints after checking the official examples.

- Both summaries are broadly right that the input is a crossing row and column and that the output is rebuilt as a compact block.
- They miss an important detail: the alternating "separator" rows are not always fully solid. When the intersection carries the column-majority color, those rows alternate `row-majority / intersection-color` across the width instead.
- They also miss a second detail shown by official example 1: if the column accent nearest the intersection lands on the patterned-row parity, that specific row alternates `column-accent / intersection-color`, while the farther column-accent rows alternate `column-accent / column-majority`.

Confirmed rule:

- Find the densest nonzero row and the densest nonzero column.
- In the row, the repeated non-majority color determines the horizontal span: from its first occurrence to its second occurrence.
- In the column, the repeated non-majority color determines the vertical span: from the intersection to the farther accent if the accents are below, or from the farther accent up to the intersection if the accents are above.
- Within that rectangle, rows alternate between patterned rows and separator rows starting with a patterned row at the span start.
- Patterned rows nearest the intersection use the row accent, patterned rows farther from the intersection use the column accent, and the near accent row uses the intersection color on its odd columns when it falls on the patterned parity.
