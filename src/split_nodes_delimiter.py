import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        match delimiter:
            case "**":
                blocks_list = re.findall(r"\*\*(.+?)\*\*", text)
            case "`":
                blocks_list = re.findall(r"`(.+?)`", text)
            case "_":
                blocks_list = re.findall(r"_(.+?)_", text)
            case _:
                raise Exception("invalid delimiter")

        if blocks_list == []:
            new_nodes.append(node)
            continue

        for block in blocks_list:
            left_index = text.find(delimiter)
            new_nodes.append(TextNode(text[:left_index], TextType.TEXT))
            new_nodes.append(TextNode(block, text_type, None))
            # From the end of the current link to the end of the original text
            text = text[left_index + 2*len(delimiter) + len(block):]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
