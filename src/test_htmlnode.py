import unittest
from htmlnode import HTMLNode, LeafNode

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
