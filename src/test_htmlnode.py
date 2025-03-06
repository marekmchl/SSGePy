import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_eq(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        string1 = node.props_to_html()
        string2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(string1, string2)

    def test_props_to_html_neq(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        string1 = node.props_to_html()
        string2 = 'href="https://www.google.com" target="_blank"'
        self.assertNotEqual(string1, string2)

    def test_repr_eq(self):
        node = HTMLNode("h1", "Title", [], {"href": "https://www.example.com"})
        string1 = str(node)
        string2 = "HTMLNode(tag=h1, value=Title, children=[], props={'href': 'https://www.example.com'}"
        self.assertEqual(string1, string2)

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_children(self):
        node = LeafNode("p", "This is a paragraph of text.")
        children1 = node.children
        children2 = []
        self.assertEqual(children1, children2)

    def test_leaf_node_to_html_1(self):
        node = LeafNode("p", "This is a paragraph of text.")
        html_1 = node.to_html()
        html_2 = "<p>This is a paragraph of text.</p>"
        self.assertEqual(html_1, html_2)

    def test_leaf_node_to_html_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        html_1 = node.to_html()
        html_2 = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(html_1, html_2)

    def test_leaf_node_to_html_3(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

class TestParentNode(unittest.TestCase):
    def test_parent_node_to_html_1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        html_1 = node.to_html()
        html_2 = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(html_1, html_2)

    def test_parent_node_to_html_2(self):
        node_1 = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"),])
        node_2 = ParentNode("p", [LeafNode("b", "Bold text"), node_1, LeafNode("i", "italic text"), LeafNode(None, "Normal text"),])
        node_3 = ParentNode("p", [LeafNode("b", "Bold text"), node_2, LeafNode("i", "italic text"), LeafNode(None, "Normal text"),])

        html_1 = node_3.to_html()
        html_2 = "<p><b>Bold text</b><p><b>Bold text</b><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i>Normal text</p><i>italic text</i>Normal text</p>"
        self.assertEqual(html_1, html_2)

    def test_parent_node_to_html_3(self):
        node_1 = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"),])
        node_2 = ParentNode("p", [node_1, node_1, node_1])

        html_1 = node_2.to_html()
        html_2 = "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>"
        self.assertEqual(html_1, html_2)

    def test_parent_node_no_children_eq_1(self):
        try:
            test = ParentNode("p", None, {}).to_html()
        except ValueError as e:
            self.assertEqual(str(e), "missing children")

    def test_parent_node_no_children_neq_1(self):
        try:
            test = ParentNode("p", None, {}).to_html()
        except ValueError as e:
            self.assertNotEqual(str(e), "missing tag")

    def test_parent_node_no_children_eq_2(self):
        try:
            test = ParentNode("p", [], {}).to_html()
        except ValueError as e:
            self.assertEqual(str(e), "missing children")

    def test_parent_node_no_children_neq_2(self):
        try:
            test = ParentNode("p", [], {}).to_html()
        except ValueError as e:
            self.assertNotEqual(str(e), "missing tag")

    def test_parent_node_no_tag_eq_1(self):
        try:
            child = LeafNode(None, "Some text", None)
            test = ParentNode(None, [child,], {}).to_html()
        except ValueError as e:
            self.assertEqual(str(e), "missing tag")

    def test_parent_node_no_tag_neq_1(self):
        try:
            child = LeafNode(None, "Some text", None)
            test = ParentNode(None, [child,], {}).to_html()
        except ValueError as e:
            self.assertNotEqual(str(e), "missing children")

    def test_parent_node_no_tag_eq_2(self):
        try:
            child = LeafNode(None, "Some text", None)
            test = ParentNode("", [child,], {}).to_html()
        except ValueError as e:
            self.assertEqual(str(e), "missing tag")

    def test_parent_node_no_tag_neq_2(self):
        try:
            child = LeafNode(None, "Some text", None)
            test = ParentNode("", [child,], {}).to_html()
        except ValueError as e:
            self.assertNotEqual(str(e), "missing children")
