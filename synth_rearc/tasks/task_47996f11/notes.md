`47996f11` is a diagonal-completion task.

- The latent output is symmetric across the main diagonal.
- The input is formed by overwriting several rectangular strips with color `6`.
- Most masked cells are recovered directly from their transposed counterpart.
- The official ARC training set includes three overlap cases where the mask intersects its own transpose.

The synthetic generator avoids transpose-overlap entirely and focuses on dense, tapestry-like diagonal-symmetric mosaics so the produced previews stay close to the visual character of the original task family.
