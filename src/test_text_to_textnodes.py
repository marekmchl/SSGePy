import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes_empty_1(self):
        text = ""
        nodes = text_to_textnodes(text)
        control = []
        self.assertEqual(nodes, control)

    def test_text_to_textnodes_1(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        control = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, control)

    def test_text_to_textnodes_all_bold_1(self):
        text = "First normal **first bold** second normal **second bold** third normal **contains * star** normal * star **end bold**"
        nodes = text_to_textnodes(text)
        control = [
            TextNode("First normal ", TextType.TEXT),
            TextNode("first bold", TextType.BOLD),
            TextNode(" second normal ", TextType.TEXT),
            TextNode("second bold", TextType.BOLD),
            TextNode(" third normal ", TextType.TEXT),
            TextNode("contains * star", TextType.BOLD),
            TextNode(" normal * star ", TextType.TEXT),
            TextNode("end bold", TextType.BOLD),
        ]
        self.assertEqual(nodes, control)

    def test_text_to_textnodes_all_code_1(self):
        text = "First normal `first code` second normal `second code` third normal `end code`"
        nodes = text_to_textnodes(text)
        control = [
            TextNode("First normal ", TextType.TEXT),
            TextNode("first code", TextType.CODE),
            TextNode(" second normal ", TextType.TEXT),
            TextNode("second code", TextType.CODE),
            TextNode(" third normal ", TextType.TEXT),
            TextNode("end code", TextType.CODE),
        ]
        self.assertEqual(nodes, control)

    def test_text_to_textnodes_all_italic_1(self):
        text = "First normal _first italic_ second normal _second italic_ third normal _end italic_"
        nodes = text_to_textnodes(text)
        control = [
            TextNode("First normal ", TextType.TEXT),
            TextNode("first italic", TextType.ITALIC),
            TextNode(" second normal ", TextType.TEXT),
            TextNode("second italic", TextType.ITALIC),
            TextNode(" third normal ", TextType.TEXT),
            TextNode("end italic", TextType.ITALIC),
        ]
        self.assertEqual(nodes, control)

    def test_text_to_textnodes_all_images_1(self):
        text = "First normal ![first image](path/to/image/img1.png) second normal ![second image](path/to/image/img2.png) third normal ![end image](path/to/image/imgend.png)"
        nodes = text_to_textnodes(text)
        control = [
            TextNode("First normal ", TextType.TEXT),
            TextNode("first image", TextType.IMAGE, "path/to/image/img1.png"),
            TextNode(" second normal ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "path/to/image/img2.png"),
            TextNode(" third normal ", TextType.TEXT),
            TextNode("end image", TextType.IMAGE, "path/to/image/imgend.png"),
        ]
        self.assertEqual(nodes, control)

    def test_text_to_textnodes_all_links_1(self):
        text = "First normal [first link](https://www.example1.com) second normal [second link](https://www.example2.com) third normal [end link](https://www.exampleend.com)"
        nodes = text_to_textnodes(text)
        control = [
            TextNode("First normal ", TextType.TEXT),
            TextNode("first link", TextType.LINK, "https://www.example1.com"),
            TextNode(" second normal ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://www.example2.com"),
            TextNode(" third normal ", TextType.TEXT),
            TextNode("end link", TextType.LINK, "https://www.exampleend.com"),
        ]
        self.assertEqual(nodes, control)
