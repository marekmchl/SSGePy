from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from htmlnode import ParentNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType

def text_to_children(text):
    children = text_to_textnodes(text)
    html_children = []
    for child in children:
        html_children.append(text_node_to_html_node(child))

    return html_children

def make_a_paragraph(text):
    return ParentNode("p", text_to_children(text.replace("\n", " ")))

def make_a_heading(markdown_line):
    words = markdown_line.split(" ")
    heading_level = words[0].count("#")
    return ParentNode(f"h{heading_level}", text_to_children(" ".join(words[1:])))

def make_a_code(text):
    stripped_text = text[3:-3].lstrip("\n")
    node = TextNode(stripped_text, TextType.CODE, None)
    node = text_node_to_html_node(node)
    return ParentNode("pre", [node, ])

def make_a_quote(text):
    lines = text.split("\n")
    stripped_lines = []
    for line in lines:
        stripped_lines.append(line.lstrip(">"))
    quote_block = "\n".join(stripped_lines)
    return ParentNode("blockquote", text_to_children(quote_block))

def make_unordered_list(data):
    rows_text = data.split("\n")
    rows_nodes = []
    for row in rows_text:
        children = text_to_children(" ".join(row.split(" ")[1:]))
        rows_nodes.append(ParentNode("li", children))

    return ParentNode("ul", rows_nodes)

def make_ordered_list(data):
    rows_text = data.split("\n")
    rows_nodes = []
    for row in rows_text:
        children = text_to_children(" ".join(row.split(" ")[1:]))
        rows_nodes.append(ParentNode("li", children))

    return ParentNode("ol", rows_nodes)

def markdown_to_html_node(markdown_string):
    markdown_blocks = markdown_to_blocks(markdown_string)
    html_children = []
    for block in markdown_blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                html_children.append(make_a_paragraph(block))

            case BlockType.HEADING:
                html_children.append(make_a_heading(block))

            case BlockType.CODE:
                html_children.append(make_a_code(block))

            case BlockType.QUOTE:
                html_children.append(make_a_quote(block))

            case BlockType.UNORDERED_LIST:
                html_children.append(make_unordered_list(block))

            case BlockType.ORDERED_LIST:
                html_children.append(make_ordered_list(block))

    return ParentNode("div", html_children, None)
