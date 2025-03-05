import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("Text", TextType.LINK, "www.example.com/something/else")
        node2 = TextNode("Text", TextType.LINK, "www.example.com/something/else")
        self.assertEqual(node, node2)

    def test_neq_text_no_url(self):
        node = TextNode("Text1", TextType.ITALIC)
        node2 = TextNode("Text2", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_neq_text_with_url(self):
            node = TextNode("Text1", TextType.ITALIC, "www.example.com/something/else")
            node2 = TextNode("Text2", TextType.ITALIC, "www.example.com/something/else")
            self.assertNotEqual(node, node2)

    def test_neq_texttype_no_url(self):
            node = TextNode("Text", TextType.ITALIC)
            node2 = TextNode("Text", TextType.BOLD)
            self.assertNotEqual(node, node2)

    def test_neq_texttype_with_url(self):
                node = TextNode("Text", TextType.ITALIC, "www.example.com/something/else")
                node2 = TextNode("Text", TextType.BOLD, "www.example.com/something/else")
                self.assertNotEqual(node, node2)

    def test_neq_url_1(self):
            node = TextNode("Text", TextType.LINK, "www.example.com/something/else/1")
            node2 = TextNode("Text", TextType.LINK, "www.example.com/something/else/2")
            self.assertNotEqual(node, node2)

    def test_neq_url_2(self):
                node = TextNode("Text", TextType.LINK, "www.example.com/something/else/1")
                node2 = TextNode("Text", TextType.LINK)
                self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
