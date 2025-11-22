dict_promptmode_to_prompt = {
    # prompt_layout_all_en: parse all layout info in json format.
    "prompt_layout_all_en": """Please output the layout information from the PDF image, including each layout element's bbox, its category, and the corresponding text content within the bbox.

1. Bbox format: [x1, y1, x2, y2]

2. Layout Categories: The possible categories are ['Caption', 'Footnote', 'Formula', 'List-item', 'Page-footer', 'Page-header', 'Picture', 'Section-header', 'Table', 'Text', 'Title'].

3. Text Extraction & Formatting Rules:
    - Picture: For the 'Picture' category, the text field should be omitted.
    - Formula: Format its text as LaTeX.
    - Table: Format its text as HTML.
    - All Others (Text, Title, etc.): Format their text as Markdown.

4. Constraints:
    - The output text must be the original text from the image, with no translation.
    - All layout elements must be sorted according to human reading order.

5. Final Output: The entire output must be a single JSON object.
""",

    # prompt_layout_only_en: layout detection
    "prompt_layout_only_en": """Please output the layout information from this PDF image, including each layout's bbox and its category. The bbox should be in the format [x1, y1, x2, y2]. The layout categories for the PDF document include ['Caption', 'Footnote', 'Formula', 'List-item', 'Page-footer', 'Page-header', 'Picture', 'Section-header', 'Table', 'Text', 'Title']. Do not output the corresponding text. The layout result should be in JSON format.""",

    # prompt_layout_with_orientation_en: layout detection with orientation
    "prompt_layout_with_orientation_en": """Output ONLY a JSON array with layout detection results. Each element must have exactly 3 fields: bbox, category, and orientation.

**Required Output Format:**
```json
[
    {
        "bbox": [x1, y1, x2, y2],
        "category": "category_name",
        "orientation": "orientation_value"
    }
]
```

**Field Specifications:**

1. **bbox**: Bounding box coordinates as [x1, y1, x2, y2] where (x1, y1) is top-left, (x2, y2) is bottom-right.

2. **category**: Must be one of: 'Caption', 'Footnote', 'Formula', 'List-item', 'Page-footer', 'Page-header', 'Picture', 'Section-header', 'Table', 'Text', 'Title'.

3. **orientation**: Text/content orientation relative to normal reading direction. Must be one of:
   - 'up': Normal upright text (0°)
   - 'right': Rotated 90° clockwise
   - 'down': Upside down (180°)
   - 'left': Rotated 90° counter-clockwise (270°)

**Critical Rules:**
- Output ONLY bbox, category, and orientation fields
- DO NOT include any "text" field
- DO NOT extract or output text content
- Output must be valid JSON array format
""",

    # prompt_ocr: parse ocr text except the Page-header and Page-footer
    "prompt_ocr": """Extract the text content from this image.""",

    # prompt_grounding_ocr: extract text content in the given bounding box
    "prompt_grounding_ocr": """Extract text from the given bounding box on the image (format: [x1, y1, x2, y2]).\nBounding Box:\n""",

    # "prompt_table_html": """Convert the table in this image to HTML.""",
    # "prompt_table_latex": """Convert the table in this image to LaTeX.""",
    # "prompt_formula_latex": """Convert the formula in this image to LaTeX.""",
}
