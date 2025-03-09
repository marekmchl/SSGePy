from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_link import split_nodes_link
from split_nodes_image import split_nodes_image

def text_to_textnodes(text_string):
    if text_string == "":
        return []

    node_list = [TextNode(text_string, TextType.TEXT, None), ]
    node_list = split_nodes_delimiter(node_list, "**", TextType.BOLD)
    node_list = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
    node_list = split_nodes_delimiter(node_list, "`", TextType.CODE)
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)
    return node_list
