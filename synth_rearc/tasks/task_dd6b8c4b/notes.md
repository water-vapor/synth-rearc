`dd6b8c4b` centers on the fixed `3/2` motif. The output count is the number of movable `9`s, written back into the motif in row-major order.

The verifier uses a two-stage reconstruction that matches the official examples:

1. Start from the non-`6` cells on the 5x5 ring around the motif.
2. For each opener, flood through non-`6` cells inside the strip or orthant implied by that opener.
3. Every `9` already inside that union is movable.
4. If one more outside `9` is nearest to the flooded region through a `7` corridor, it is also movable.

For generation, I stay close to the reference family by reusing `9`-stripped versions of the official layouts as scaffolds, then:

- place the movable `9`s only inside the base flooded region
- place any persistent noise only in `7` pockets disconnected from that region

That keeps the generated examples consistent with the verifier while preserving the official look.
