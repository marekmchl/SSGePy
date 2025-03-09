from textnode import TextType, TextNode
from extract_markdown import extract_markdown_links

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links_list = extract_markdown_links(node.text)
        if links_list == []:
            new_nodes.append(node)
            continue

        text = node.text
        for link_tuple in links_list:
            left_index = text.find("[")
            new_nodes.append(TextNode(text[:left_index], TextType.TEXT))
            new_nodes.append(TextNode(link_tuple[0], TextType.LINK, link_tuple[1]))
            # From the end of the current link to the end of the original text
            text = text[left_index + 4 + len(link_tuple[0]) + len(link_tuple[1]):]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
