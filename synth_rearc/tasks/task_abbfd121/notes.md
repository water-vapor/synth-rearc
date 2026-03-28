`arc2_opus46_summary.json` was usable: the task is to find the largest solid-color occluding rectangle and reconstruct the repeating wallpaper crop that lies underneath it.

`arc2_sonnet45_summary.jsonl` had the right high-level idea but a concrete mismatch on pair 4: it describes a `4`-colored rectangle as width `10`, while the official grid shows width `9` (`cols 11..19`). I used the official examples plus the Opus hint and treated the Sonnet dimensions as unreliable.
