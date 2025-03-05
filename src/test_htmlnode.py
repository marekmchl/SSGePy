import unittest
from htmlnode import HTMLNode

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
