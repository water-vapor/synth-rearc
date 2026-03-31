`e87109e9` is a k-by-k block-ray tracing task.

- The top 6-row legend maps each color to a turn rule.
- In the lower grid, color `8` is the seed block and the other colored rectangles are obstacles.
- From the seed, trace k-thick rays in the four cardinal directions.
- When a ray hits a colored rectangle, turn clockwise or counterclockwise according to that rectangle's legend marker and continue.
- Stop when the next shifted k-by-k block would leave the grid or hit multiple objects.
