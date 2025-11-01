# Text Alignment Problem

### Leetcode Adjacent Problem Link: [https://leetcode.com/problems/text-justification/](https://leetcode.com/problems/text-justification/)

### Problem: Multi-Paragraph Text Formatting with Individual Alignments

Given a 2D array where each sub-array represents a paragraph containing individual words, format the text with a maximum line width. Each paragraph has its own alignment specification. Words that would cause a line to exceed the width limit must wrap to the next line within the same paragraph.

### Input:

- **paragraphs**: A 2D array where each element is an array of words
  - Example: `[["hello", "world"], ["other", "long", "sentence", "here", "too", "long"]]`
- **width**: Maximum number of characters allowed per line (integer)
- **align**: An array of alignment directives corresponding to each paragraph
  - Example: `["right", "left"]` for 2 paragraphs. Each element is either "left" or "right"

### Output:

A single array of formatted strings where each string represents a line. Lines are padded with spaces according to alignment. Paragraphs are concatenated in order.

### Rules:

- Words are separated by single spaces when calculating line width
- A word that would exceed the width limit moves to the next line
- Lines are padded with spaces according to alignment:
  - **"left"**: Text starts from the left edge, padded with spaces on the right
  - **"right"**: Text padded with spaces on the left to reach the right edge
- All lines must be exactly width characters long (padded with spaces)
- Empty paragraphs are skipped

### Example:

Input:
```python
paragraphs = [["hello", "world", "from", "here"], 
              ["this", "is", "a", "very", "long", "sentence"]]
width = 12
align = ["right", "left"]
```

Output:
```python
[
  " hello world",  # right-aligned (1 space + text = 12 chars)
  "   from here",  # right-aligned (3 spaces + text = 12 chars)  
  "this is a   ",  # left-aligned (text + 3 spaces = 12 chars)
  "very long   ",  # left-aligned (text + 3 spaces = 12 chars)
  "sentence    "   # left-aligned (text + 4 spaces = 12 chars)
]
```
