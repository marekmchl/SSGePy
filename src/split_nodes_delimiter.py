from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        text = node.text
        index_left = text.find(delimiter)
        if index_left == -1:
            raise Exception("invalid Markdown syntax - no delimeter found")

        index_right = text.rfind(delimiter)
        if index_right == -1:
            raise Exception("invalid Markdown syntax - no closing delimiter")

        new_nodes.append(TextNode(text[:index_left], node.text_type))
        new_nodes.append(TextNode(text[index_left+len(delimiter):index_right], text_type))
        new_nodes.append(TextNode(text[index_right+len(delimiter):], node.text_type))

    return new_nodes
