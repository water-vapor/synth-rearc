The summary hints were discarded as incomplete. The Opus hint overfits the task to
"almost-complete 2x2" red motifs, but the official examples also contain single red
cells, diagonal pairs, and larger sparse subsets that do not fit that description.

The reliable rule is window-based: find every maximal 3x3 subgrid whose cells are
all 2 or 5, whose center is 5, and that contains at least one 2. In the output,
each such window becomes a 3x3 flower with center 4, original 2 cells preserved,
and every remaining 5 in that window recolored to 7.
