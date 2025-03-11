import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_1(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_2(self):
        md = """# This is a heading

## This is a second heading

- This is a list
- with items

This is a paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is another a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "## This is a second heading",
                "- This is a list\n- with items",
                "This is a paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is another a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty_input_1(self):
        blocks = markdown_to_blocks("")
        control = []
        self.assertEqual(blocks, control)

    def test_markdown_to_blocks_one_line_1(self):
        blocks = markdown_to_blocks("""
# One line
""")
        control = ["# One line"]
        self.assertEqual(blocks, control)

    def test_markdown_to_blocks_trailing_whitespace_1(self):
        blocks = markdown_to_blocks("""
Paragraph
""")
        control = ["Paragraph"]
        self.assertEqual(blocks, control)

    def test_markdown_to_blocks_leading_whitespace_1(self):
        blocks = markdown_to_blocks("""
 		 		 Paragraph
""")
        control = ["Paragraph"]
        self.assertEqual(blocks, control)

    def test_markdown_to_blocks_excess_newlines_1(self):
        blocks = markdown_to_blocks("""
One line








Two line
""")
        control = ["One line", "Two line"]
        self.assertEqual(blocks, control)
