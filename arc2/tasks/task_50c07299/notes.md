`arc2_sonnet45_summary.jsonl` had no entry for `50c07299`.

`arc2_opus46_summary.json` was not fully trustworthy. It described the new diagonal as moving up-left from the input's upper-right endpoint, but the official examples show the opposite horizontal direction.

Correct rule:
- The input is a single anti-diagonal segment on the grid's main counterdiagonal.
- If the input segment has length `n`, the output is the immediately preceding segment on that same counterdiagonal, shifted up-right so it touches the input diagonally, and its length is `n + 1`.
