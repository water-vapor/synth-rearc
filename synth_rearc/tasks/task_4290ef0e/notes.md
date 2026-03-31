`4290ef0e` builds a centered four-way symmetric composition from several disconnected same-color parts in the input.

- Each foreground color in the input corresponds to one nested layer in the output.
- If one color appears as a singleton in the input, it becomes the center pixel of the output.
- The generator samples nested top-left corner motifs, mirrors them into the full target, then scatters the per-color partitions into a larger background canvas.
