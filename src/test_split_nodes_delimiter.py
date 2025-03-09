import unittest
from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_delimiter_valid_code_1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_delimiter_valid_bold_1(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_delimiter_valid_italic_1(self):
        node = TextNode("This is text with an _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_delimiter_badly_used_delimiter_1(self):
        node = TextNode("This is text with a **bold block word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a **bold block word.", TextType.TEXT), ])

    def test_split_delimiter_badly_used_delimiter_2(self):
        node = TextNode("This is text with a _italic block word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with a _italic block word.", TextType.TEXT), ])

    def test_split_delimiter_badly_used_delimiter_3(self):
        node = TextNode("This is text with a `code block word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a `code block word.", TextType.TEXT), ])

    def test_split_delimiter_badly_used_delimiter_4(self):
        node = TextNode("This is text with a bold** block word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a bold** block word.", TextType.TEXT), ])

    def test_split_delimiter_badly_used_delimiter_5(self):
        node = TextNode("This is text with a italic_ block word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with a italic_ block word.", TextType.TEXT), ])

    def test_split_delimiter_badly_used_delimiter_6(self):
        node = TextNode("This is text with a code` block word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a code` block word.", TextType.TEXT), ])

    def test_split_delimiter_invalid_delimiter_1(self):
        try:
            node = TextNode("This is text with a `code block word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "'", TextType.CODE)
        except Exception as e:
            self.assertEqual(str(e), "invalid delimiter")

    def test_split_delimiter_invalid_delimiter_2(self):
        try:
            node = TextNode("This is text with a `code block word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "-", TextType.CODE)
        except Exception as e:
            self.assertEqual(str(e), "invalid delimiter")

    def test_split_delimiter_invalid_delimiter_3(self):
        try:
            node = TextNode("This is text with a `code block word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "'", TextType.CODE)
        except Exception as e:
            self.assertNotEqual(str(e), "invalid elimiter")

    def test_split_delimiter_invalid_delimiter_4(self):
        try:
            node = TextNode("This is text with a `code block word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "'", TextType.CODE)
        except Exception as e:
            self.assertNotEqual(str(e), "invalid elimiter")
