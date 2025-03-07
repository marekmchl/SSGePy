import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_valid_image_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)."
        matches = extract_markdown_images(text)
        control = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(matches, control)

    def test_valid_image_and_link_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and link [to youtube](https://www.youtube.com/@bootdotdev)."
        matches = extract_markdown_images(text)
        control = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(matches, control)

    def test_no_images_1(self):
        text = "This text has no images."
        matches = extract_markdown_images(text)
        control = []
        self.assertEqual(matches, control)


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_two_links_1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        control = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(matches, control)

    def test_one_link_1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and an image ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)."
        matches = extract_markdown_links(text)
        control = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(matches, control)

    def test_no_link_1(self):
        text = "This is text with no links."
        matches = extract_markdown_links(text)
        control = []
        self.assertEqual(matches, control)
