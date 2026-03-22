The summary hints were only partly useful and I treated them as untrusted.

The Sonnet summary is materially wrong: the official examples are not a generic "corner redistribution" over all 5-objects. The stable rule is column-based:

- The top 3x3 marker block always has two full `9` rows.
- Each of its three columns moves independently.
- A `9,9,1` column drops in the same column and stops immediately above the first `5` encountered below it.
- A `9,9,9` column falls to the bottom of the grid; one official example shifts the rightmost all-`9` column one step right to match a two-cell bottom support, and another trims two cells from a long bottom bar after the landing.

The Opus summary was directionally closer than the Sonnet summary because it at least separated the `...1` columns from the all-`9` columns, but it was still too vague about the actual placement mechanics and did not capture the pair-2 cleanup behavior.
