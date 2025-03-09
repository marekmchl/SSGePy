import unittest
from textnode import TextNode, TextType
from split_nodes_link import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
    def test_split_links_two_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_three_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png) and another [third link](https://www.example.com/img.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "third link", TextType.LINK, "https://www.example.com/img.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_one_link(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_links_one_link_and_aftertext(self):
            node = TextNode(
                "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) aftertext!!!!",
                TextType.TEXT,
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" aftertext!!!!", TextType.TEXT)
                ],
                new_nodes,
            )

    def test_split_links_with_image(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and an image ![image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and an image ![image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_no_link(self):
            node = TextNode(
                "This is no link here!",
                TextType.TEXT,
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This is no link here!", TextType.TEXT),
                ],
                new_nodes,
            )

    # def test_split_links_invalid_syntax(self):
    #         node = TextNode(
    #             "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and a a few invalid ones: [) [] () and another [second link](https://i.imgur.com/3elNhQu.png) and another [third link](https://www.example.com/img.png)",
    #             TextType.TEXT,
    #         )
    #         new_nodes = split_nodes_link([node])
    #         print(f"\n\n!!! HERE: {new_nodes} !!!\n\n")
    #         self.assertListEqual(
    #             [
    #                 TextNode("This is text with a ", TextType.TEXT),
    #                 TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
    #                 TextNode(
    #                     " and a a few invalid ones: [) [] () and another ",
    #                     TextType.TEXT
    #                 ),
    #                 TextNode(
    #                     "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
    #                 ),
    #                 TextNode(" and another ", TextType.TEXT),
    #                 TextNode(
    #                     "third image", TextType.LINK, "https://www.example.com/img.png"
    #                 ),
    #             ],
    #             new_nodes,
    #         )
