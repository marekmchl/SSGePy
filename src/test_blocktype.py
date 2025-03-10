import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_block_to_blocktype_paragraph_1(self):
        block = "This is a paragraph!"
        blocktype = block_to_block_type(block)
        control = BlockType.PARAGRAPH
        self.assertEqual(control, blocktype)

    def test_block_to_blocktype_paragraph_2(self):
        block = "This \nis \nstill \na \nparagraph!"
        blocktype = block_to_block_type(block)
        control = BlockType.PARAGRAPH
        self.assertEqual(control, blocktype)

    def test_block_to_blocktype_heading_1(self):
        block = "# This is a heading!"
        blocktype = block_to_block_type(block)
        control = BlockType.HEADING
        self.assertEqual(control, blocktype)

    def test_block_to_blocktype_heading_2(self):
        block = "## This is also a heading!"
        blocktype = block_to_block_type(block)
        control = BlockType.HEADING
        self.assertEqual(control, blocktype)

    def test_block_to_blocktype_heading_3(self):
        block = "### This is also also a heading!"
        blocktype = block_to_block_type(block)
        control = BlockType.HEADING
        self.assertEqual(control, blocktype)

    def test_block_to_blocktype_heading_4(self):
        block = "#### This is also also also a heading!"
        blocktype = block_to_block_type(block)
        control = BlockType.HEADING
        self.assertEqual(control, blocktype)

    def test_block_to_blocktype_heading_5(self):
        block = "##### This is also also also also a heading!"
        blocktype = block_to_block_type(block)
        control = BlockType.HEADING
        self.assertEqual(control, blocktype)

    def test_block_to_blocktype_heading_6(self):
        block = "###### This is also also also also also a heading!"
        blocktype = block_to_block_type(block)
        control = BlockType.HEADING
        self.assertEqual(control, blocktype)

    def test_block_to_blocktype_heading_7(self):
        block = "####### This is not a heading!"
        blocktype = block_to_block_type(block)
        control = BlockType.HEADING
        self.assertNotEqual(control, blocktype)

    def test_block_to_blocktype_code_1(self):
        block = "```This is \na code block```"
        blocktype = block_to_block_type(block)
        control = BlockType.CODE
        self.assertEqual(control, blocktype)

    def test_block_to_blocktype_quote_1(self):
        block = ">This is a quote!\n>Also a quote!"
        blocktype = block_to_block_type(block)
        control = BlockType.QUOTE
        self.assertEqual(control, blocktype)

    def test_block_to_blocktype_un_list_1(self):
        block = "- This is a list!\n- And another item!\n- And another!\n- And a last one!"
        blocktype = block_to_block_type(block)
        control = BlockType.UNORDERED_LIST
        self.assertEqual(control, blocktype)

    def test_block_to_blocktype_or_list_1(self):
        block = "1. This is a list!\n2. Also another item!\n3. Item\n4. Item\n5. Last item!"
        blocktype = block_to_block_type(block)
        control = BlockType.ORDERED_LIST
        self.assertEqual(control, blocktype)
