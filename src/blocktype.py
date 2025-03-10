from re import match
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block_string):
    if block_string == "" or not isinstance(block_string, str):
        return

    if match(r"(?<!.)#{1,6} .+", block_string): # Headings
        return BlockType.HEADING

    if block_string[:3] == "```" and block_string[-3:] == "```":
        return BlockType.CODE

    block_lines_list = block_string.split("\n")
    quote = True
    unordered_list = True
    ordered_list = True
    for line_num, line in enumerate(block_lines_list):
        if line[0] != ">":
            quote = False
        if line[:2] != "- ":
            unordered_list = False
        if line.split(" ")[0] != f"{line_num + 1}.":
            ordered_list = False

    if quote:
        return BlockType.QUOTE

    if unordered_list:
        return BlockType.UNORDERED_LIST

    if ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
