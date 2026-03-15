# DSL Quick Reference

High-level index for [`dsl.py`](./dsl.py). Read this file first, then open the source for any primitive you plan to use in real code, especially the more geometric or object-extraction primitives.

Conventions:
- `Grid` is a tuple of tuple rows of color integers.
- `Object` is a `frozenset` of `(color, (row, col))` cells.
- `Patch` means either a plain index set or a colored object.
- Line numbers below point to the definition start in `dsl.py`.

## Scalar, Boolean, and Vector Primitives

- `identity(x: Any) -> Any` (`L75`): Identity function.
- `add(a: Numerical, b: Numerical) -> Numerical` (`L82`): Adds integers or performs elementwise/broadcast addition when one or both inputs are 2-tuples.
- `subtract(a: Numerical, b: Numerical) -> Numerical` (`L96`): Subtracts integers or performs elementwise/broadcast subtraction for 2-tuples.
- `multiply(a: Numerical, b: Numerical) -> Numerical` (`L110`): Multiplies integers or performs elementwise/broadcast multiplication for 2-tuples.
- `divide(a: Numerical, b: Numerical) -> Numerical` (`L124`): Floor-divides integers or performs elementwise/broadcast floor division for 2-tuples.
- `invert(n: Numerical) -> Numerical` (`L138`): Additive inverse: negates an integer or both components of a 2-tuple.
- `even(n: Integer) -> Boolean` (`L145`): Evenness.
- `double(n: Numerical) -> Numerical` (`L152`): Scaling by two.
- `halve(n: Numerical) -> Numerical` (`L159`): Scaling by one half.
- `flip(b: Boolean) -> Boolean` (`L166`): Logical not.
- `equality(a: Any, b: Any) -> Boolean` (`L173`): Equality.
- `contained(value: Any, container: Container) -> Boolean` (`L181`): Membership test: returns whether `value` appears in `container`.
- `combine(a: Container, b: Container) -> Container` (`L189`): Type-preserving concatenation/union. For tuples it concatenates in order; for sets/frozensets duplicates collapse naturally.
- `intersection(a: FrozenSet, b: FrozenSet) -> FrozenSet` (`L197`): Returns the intersection of two containers.
- `difference(a: Container, b: Container) -> Container` (`L205`): Keeps items from `a` that are not present in `b`, preserving the outer container type.
- `dedupe(iterable: Tuple) -> Tuple` (`L213`): Removes duplicate entries from a tuple while keeping first-occurrence order.
- `order(container: Container, compfunc: Callable) -> Tuple` (`L220`): Order container by custom key.
- `repeat(item: Any, num: Integer) -> Tuple` (`L228`): Builds a tuple containing `item` repeated `num` times.
- `greater(a: Integer, b: Integer) -> Boolean` (`L236`): Greater.
- `size(container: Container) -> Integer` (`L244`): Cardinality.
- `merge(containers: ContainerContainer) -> Container` (`L251`): Flattens one container of containers into a single container of the same outer type.
- `maximum(container: IntegerSet) -> Integer` (`L258`): Maximum.
- `minimum(container: IntegerSet) -> Integer` (`L265`): Minimum.
- `valmax(container: Container, compfunc: Callable) -> Integer` (`L272`): Maximum by custom function.
- `valmin(container: Container, compfunc: Callable) -> Integer` (`L280`): Minimum by custom function.
- `argmax(container: Container, compfunc: Callable) -> Any` (`L288`): Largest item by custom order.
- `argmin(container: Container, compfunc: Callable) -> Any` (`L296`): Smallest item by custom order.
- `mostcommon(container: Container) -> Any` (`L304`): Most common item.
- `leastcommon(container: Container) -> Any` (`L311`): Least common item.
- `initset(value: Any) -> FrozenSet` (`L318`): Initialize container.
- `both(a: Boolean, b: Boolean) -> Boolean` (`L325`): Logical and.
- `either(a: Boolean, b: Boolean) -> Boolean` (`L333`): Logical or.
- `increment(x: Numerical) -> Numerical` (`L341`): Incrementing.
- `decrement(x: Numerical) -> Numerical` (`L348`): Decrementing.
- `crement(x: Numerical) -> Numerical` (`L355`): Moves each component one step away from zero: positive values increase, negative values decrease, zero stays zero.
- `sign(x: Numerical) -> Numerical` (`L367`): Sign.
- `positive(x: Integer) -> Boolean` (`L379`): Positive.
- `toivec(i: Integer) -> IntegerTuple` (`L386`): Vector pointing vertically.
- `tojvec(j: Integer) -> IntegerTuple` (`L393`): Vector pointing horizontally.

## Container and Functional Utilities

- `sfilter(container: Container, condition: Callable) -> Container` (`L400`): Keep elements in container that satisfy condition.
- `mfilter(container: Container, function: Callable) -> FrozenSet` (`L408`): Filter and merge.
- `extract(container: Container, condition: Callable) -> Any` (`L416`): First element of container that satisfies condition.
- `totuple(container: FrozenSet) -> Tuple` (`L424`): Conversion to tuple.
- `first(container: Container) -> Any` (`L431`): First item of container.
- `last(container: Container) -> Any` (`L438`): Last item of container.
- `insert(value: Any, container: FrozenSet) -> FrozenSet` (`L445`): Insert item into container.
- `remove(value: Any, container: Container) -> Container` (`L453`): Remove item from container.
- `other(container: Container, value: Any) -> Any` (`L461`): Returns the first element different from `value`; most useful when the container is known to have exactly two possibilities.
- `interval(start: Integer, stop: Integer, step: Integer) -> Tuple` (`L469`): Range.
- `astuple(a: Integer, b: Integer) -> IntegerTuple` (`L478`): Constructs a tuple.
- `product(a: Container, b: Container) -> FrozenSet` (`L486`): Cartesian product; returns all ordered pairs `(i, j)` with `i in a` and `j in b`.
- `pair(a: Tuple, b: Tuple) -> TupleTuple` (`L494`): Zip for tuples; truncates to the shorter input like Python `zip`.
- `branch(condition: Boolean, if_value: Any, else_value: Any) -> Any` (`L502`): If else branching.
- `compose(outer: Callable, inner: Callable) -> Callable` (`L511`): Function composition.
- `chain(h: Callable, g: Callable, f: Callable) -> Callable` (`L519`): Function composition with three functions.
- `matcher(function: Callable, target: Any) -> Callable` (`L528`): Builds a predicate `lambda x: function(x) == target`.
- `rbind(function: Callable, fixed: Any) -> Callable` (`L536`): Partially applies the rightmost argument of a 2-, 3-, or 4-argument function.
- `lbind(function: Callable, fixed: Any) -> Callable` (`L550`): Partially applies the leftmost argument of a 2-, 3-, or 4-argument function.
- `power(function: Callable, n: Integer) -> Callable` (`L564`): Composes a unary function with itself `n` times.
- `fork(outer: Callable, a: Callable, b: Callable) -> Callable` (`L574`): Builds `lambda x: outer(a(x), b(x))`; a common RE-ARC combinator pattern.
- `apply(function: Callable, container: Container) -> Container` (`L583`): Maps a function over a container and preserves the container type when possible.
- `rapply(functions: Container, value: Any) -> Container` (`L591`): Applies each function in a container to the same value.
- `mapply(function: Callable, container: ContainerContainer) -> FrozenSet` (`L599`): Maps then merges: applies a function to each inner container and unions/concatenates the results.
- `papply(function: Callable, a: Tuple, b: Tuple) -> Tuple` (`L607`): Pairwise map across two tuples using `zip`, not Cartesian product.
- `mpapply(function: Callable, a: Tuple, b: Tuple) -> Tuple` (`L616`): Pairwise map across two tuples and then merge the mapped outputs.
- `prapply(function: Callable, a: Container, b: Container) -> FrozenSet` (`L625`): Applies a function over the Cartesian product of two containers.

## Color, Shape, and Index Queries

- `mostcolor(element: Element) -> Integer` (`L634`): Most common color.
- `leastcolor(element: Element) -> Integer` (`L642`): Least common color.
- `height(piece: Piece) -> Integer` (`L650`): For grids, number of rows. For patches/objects, height of the bounding box.
- `width(piece: Piece) -> Integer` (`L661`): For grids, number of columns. For patches/objects, width of the bounding box.
- `shape(piece: Piece) -> IntegerTuple` (`L672`): Returns `(height(piece), width(piece))`.
- `portrait(piece: Piece) -> Boolean` (`L679`): Whether height is greater than width.
- `colorcount(element: Element, value: Integer) -> Integer` (`L686`): Number of cells with color.
- `colorfilter(objs: Objects, value: Integer) -> Objects` (`L696`): Filter objects by color.
- `sizefilter(container: Container, n: Integer) -> FrozenSet` (`L704`): Keeps only items whose `len(item)` equals `n`.
- `asindices(grid: Grid) -> Indices` (`L712`): Indices of all grid cells.
- `ofcolor(grid: Grid, value: Integer) -> Indices` (`L719`): Indices of all grid cells with value.
- `ulcorner(patch: Patch) -> IntegerTuple` (`L727`): Index of upper left corner.
- `urcorner(patch: Patch) -> IntegerTuple` (`L734`): Index of upper right corner.
- `llcorner(patch: Patch) -> IntegerTuple` (`L741`): Index of lower left corner.
- `lrcorner(patch: Patch) -> IntegerTuple` (`L748`): Index of lower right corner.
- `crop(grid: Grid, start: IntegerTuple, dims: IntegerTuple) -> Grid` (`L755`): Subgrid specified by start and dimension.
- `toindices(patch: Patch) -> Indices` (`L764`): Converts either a colored object or an index patch into a plain set of indices.
- `recolor(value: Integer, patch: Patch) -> Object` (`L775`): Turns an index patch into a colored object by assigning the same color to every cell.
- `shift(patch: Patch, directions: IntegerTuple) -> Patch` (`L783`): Translates every cell in a patch/object by `(di, dj)`; supports both colored and uncolored patches.
- `normalize(patch: Patch) -> Patch` (`L796`): Shifts a patch so its upper-left occupied cell lands at the origin `(0, 0)`.
- `dneighbors(loc: IntegerTuple) -> Indices` (`L805`): Directly adjacent indices.
- `ineighbors(loc: IntegerTuple) -> Indices` (`L812`): Diagonally adjacent indices.
- `neighbors(loc: IntegerTuple) -> Indices` (`L819`): Adjacent indices.
- `objects(grid: Grid, univalued: Boolean, diagonal: Boolean, without_bg: Boolean) -> Objects` (`L826`): Connected-component extractor. `univalued` requires each object to stay single-color, `diagonal` switches between 4- and 8-connectivity, and `without_bg` skips the most common color as background.
- `partition(grid: Grid) -> Objects` (`L862`): Groups all cells of the same color into one object, ignoring connectivity.
- `fgpartition(grid: Grid) -> Objects` (`L873`): Like `partition`, but excludes the most common background color.
- `uppermost(patch: Patch) -> Integer` (`L884`): Row index of uppermost occupied cell.
- `lowermost(patch: Patch) -> Integer` (`L891`): Row index of lowermost occupied cell.
- `leftmost(patch: Patch) -> Integer` (`L898`): Column index of leftmost occupied cell.
- `rightmost(patch: Patch) -> Integer` (`L905`): Column index of rightmost occupied cell.
- `square(piece: Piece) -> Boolean` (`L912`): For grids checks rectangular square shape; for patches checks both square bounding box and full occupancy.
- `vline(patch: Patch) -> Boolean` (`L919`): Whether the piece forms a vertical line.
- `hline(patch: Patch) -> Boolean` (`L926`): Whether the piece forms a horizontal line.
- `hmatching(a: Patch, b: Patch) -> Boolean` (`L933`): True when the two patches occupy at least one common row index.
- `vmatching(a: Patch, b: Patch) -> Boolean` (`L941`): True when the two patches occupy at least one common column index.
- `manhattan(a: Patch, b: Patch) -> Integer` (`L949`): Minimum Manhattan distance between any cell in `a` and any cell in `b`.
- `adjacent(a: Patch, b: Patch) -> Boolean` (`L957`): True exactly when the minimum Manhattan distance is 1.
- `bordering(patch: Patch, grid: Grid) -> Boolean` (`L965`): Whether a patch is adjacent to a grid border.
- `centerofmass(patch: Patch) -> IntegerTuple` (`L973`): Integer center of mass obtained by averaging row and column indices separately with floor division.
- `palette(element: Element) -> IntegerSet` (`L980`): Colors occurring in object or grid.
- `numcolors(element: Element) -> IntegerSet` (`L989`): Returns the count of distinct colors. Note: the source annotation says `IntegerSet`, but the runtime value is an integer.
- `color(obj: Object) -> Integer` (`L996`): Returns the color of a nonempty object; assumes the object is effectively single-colored.

## Object Conversion and Geometric Transforms

- `toobject(patch: Patch, grid: Grid) -> Object` (`L1003`): Attaches grid colors to a patch and clips any out-of-bounds cells.
- `asobject(grid: Grid) -> Object` (`L1012`): Converts the full grid into one colored object containing every cell.
- `rot90(grid: Grid) -> Grid` (`L1019`): Quarter clockwise rotation.
- `rot180(grid: Grid) -> Grid` (`L1026`): Half rotation.
- `rot270(grid: Grid) -> Grid` (`L1033`): Quarter anticlockwise rotation.
- `hmirror(piece: Piece) -> Piece` (`L1040`): Mirrors a grid or patch across the horizontal axis of its own bounding box.
- `vmirror(piece: Piece) -> Piece` (`L1052`): Mirrors a grid or patch across the vertical axis of its own bounding box.
- `dmirror(piece: Piece) -> Piece` (`L1064`): Mirrors a grid or patch across the main diagonal of its own bounding box.
- `cmirror(piece: Piece) -> Piece` (`L1076`): Mirrors a grid or patch across the counterdiagonal of its own bounding box.

## Painting, Scaling, and Grid Composition

- `fill(grid: Grid, value: Integer, patch: Patch) -> Grid` (`L1085`): Writes one color into the given indices, clipping silently to grid bounds.
- `paint(grid: Grid, obj: Object) -> Grid` (`L1099`): Writes a colored object onto a grid, clipping silently to grid bounds.
- `underfill(grid: Grid, value: Integer, patch: Patch) -> Grid` (`L1112`): Like `fill`, but only overwrites cells that currently equal the grid background (`mostcolor(grid)`).
- `underpaint(grid: Grid, obj: Object) -> Grid` (`L1128`): Like `paint`, but only writes onto current background cells.
- `hupscale(grid: Grid, factor: Integer) -> Grid` (`L1143`): Upscale grid horizontally.
- `vupscale(grid: Grid, factor: Integer) -> Grid` (`L1157`): Upscale grid vertically.
- `upscale(element: Element, factor: Integer) -> Element` (`L1168`): For grids, repeats each cell into a `factor x factor` block. For objects, expands each colored cell into a block in normalized coordinates and shifts back.
- `downscale(grid: Grid, factor: Integer) -> Grid` (`L1195`): Keeps every `factor`th row and column; this is subsampling, not averaging.
- `hconcat(a: Grid, b: Grid) -> Grid` (`L1216`): Concatenate two grids horizontally.
- `vconcat(a: Grid, b: Grid) -> Grid` (`L1224`): Concatenate two grids vertically.
- `subgrid(patch: Patch, grid: Grid) -> Grid` (`L1232`): Returns the smallest rectangular crop that contains the patch/object bounding box.
- `hsplit(grid: Grid, n: Integer) -> Tuple` (`L1240`): Splits a grid into `n` vertical slices (left-to-right). If width is not divisible by `n`, the extra columns are distributed via a one-cell offset between slices.
- `vsplit(grid: Grid, n: Integer) -> Tuple` (`L1250`): Splits a grid into `n` horizontal slices (top-to-bottom). If height is not divisible by `n`, the extra rows are distributed via a one-cell offset between slices.
- `cellwise(a: Grid, b: Grid, fallback: Integer) -> Grid` (`L1260`): Keeps a cell value where two grids agree; otherwise inserts `fallback`.
- `replace(grid: Grid, replacee: Integer, replacer: Integer) -> Grid` (`L1278`): Color substitution.
- `switch(grid: Grid, a: Integer, b: Integer) -> Grid` (`L1287`): Swaps two colors everywhere in the grid and leaves all others unchanged.

## Positioning, Construction, and Motion

- `center(patch: Patch) -> IntegerTuple` (`L1296`): Returns the integer center of a patch bounding box, not the average of occupied cells.
- `position(a: Patch, b: Patch) -> IntegerTuple` (`L1303`): Returns a coarse direction from patch `a` to patch `b` based on bounding-box centers: horizontal, vertical, or diagonal unit step.
- `index(grid: Grid, loc: IntegerTuple) -> Integer` (`L1320`): Returns the grid value at `loc`, or `None` if `loc` is out of bounds.
- `canvas(value: Integer, dimensions: IntegerTuple) -> Grid` (`L1332`): Grid construction.
- `corners(patch: Patch) -> Indices` (`L1340`): Returns the four bounding-box corners of a patch/object.
- `connect(a: IntegerTuple, b: IntegerTuple) -> Indices` (`L1347`): Returns the discrete segment between two points when they are horizontally aligned, vertically aligned, or on a 45-degree diagonal; otherwise returns an empty set.
- `cover(grid: Grid, patch: Patch) -> Grid` (`L1369`): Removes a patch/object from a grid by filling its cells with the grid background (`mostcolor(grid)`).
- `trim(grid: Grid) -> Grid` (`L1377`): Trim border of grid.
- `move(grid: Grid, obj: Object, offset: IntegerTuple) -> Grid` (`L1384`): Implements move as `paint(cover(grid, obj), shift(obj, offset))`.

## Grid Slices, Frontiers, Boxes, and Pattern Search

- `tophalf(grid: Grid) -> Grid` (`L1393`): Upper half of grid.
- `bottomhalf(grid: Grid) -> Grid` (`L1400`): Lower half of grid.
- `lefthalf(grid: Grid) -> Grid` (`L1407`): Left half of grid.
- `righthalf(grid: Grid) -> Grid` (`L1414`): Right half of grid.
- `vfrontier(location: IntegerTuple) -> Indices` (`L1421`): Returns the full 30-cell vertical line through the given column index.
- `hfrontier(location: IntegerTuple) -> Indices` (`L1428`): Returns the full 30-cell horizontal line through the given row index.
- `backdrop(patch: Patch) -> Indices` (`L1435`): Returns every index inside the patch/object bounding box, including the patch itself.
- `delta(patch: Patch) -> Indices` (`L1447`): Returns the bounding box minus the patch/object cells.
- `gravitate(source: Patch, destination: Patch) -> IntegerTuple` (`L1456`): Computes the offset that moves `source` step by step toward `destination` until they become adjacent, preferring vertical motion when they share a column band and horizontal motion otherwise.
- `inbox(patch: Patch) -> Indices` (`L1480`): Returns the inner perimeter one cell inside the patch bounding box.
- `outbox(patch: Patch) -> Indices` (`L1493`): Returns the outer perimeter one cell outside the patch bounding box.
- `box(patch: Patch) -> Indices` (`L1506`): Returns the perimeter of the patch bounding box itself.
- `shoot(start: IntegerTuple, direction: IntegerTuple) -> Indices` (`L1521`): Extends a ray from `start` in `direction` by calling `connect` toward a far-away point.
- `occurrences(grid: Grid, obj: Object) -> Indices` (`L1529`): Searches for all top-left placements where a normalized object appears exactly in the grid.
- `frontiers(grid: Grid) -> Objects` (`L1553`): Returns every uniform-color full row or full column as an object.
- `compress(grid: Grid) -> Grid` (`L1565`): Deletes every uniform-color full row and every uniform-color full column.
- `hperiod(obj: Object) -> Integer` (`L1574`): Smallest positive horizontal shift whose truncated overlap stays a subset of the normalized object; returns width if no shorter period exists.
- `vperiod(obj: Object) -> Integer` (`L1588`): Smallest positive vertical shift whose truncated overlap stays a subset of the normalized object; returns height if no shorter period exists.
