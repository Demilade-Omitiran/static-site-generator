import unittest

from textnode import TextNode
from node_functions import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_headings(self):
      block1 = "# This is a header"
      block2 = "### This is also a header"
      block3 = "###### This is also a header"

      self.assertEqual(
        block_to_block_type(block1),
        "heading"
      )
      self.assertEqual(
        block_to_block_type(block2),
        "heading"
      )
      self.assertEqual(
        block_to_block_type(block3),
        "heading"
      )

    def test_code_block(self):
      block = "```This is a code block```"
      self.assertEqual(
        block_to_block_type(block),
        "code"
      )

    def test_quotes(self):
      block1 = "> This is a quote"
      block2 = "> This is another quote\n> Here is yet another quote\n> And another"
      self.assertEqual(
        block_to_block_type(block1),
        "quote"
      )
      self.assertEqual(
        block_to_block_type(block2),
        "quote"
      )

    def test_unordered_list(self):
      block1 = "* This is an unordered list"
      block2 = "- This is an unordered list"
      block3 = "* This is another unordered list\n* And again \n* Again too"
      block4 = "- This is another unordered list\n- And again \n- Again too"
      self.assertEqual(
        block_to_block_type(block1),
        "unordered_list"
      )
      self.assertEqual(
        block_to_block_type(block2),
        "unordered_list"
      )
      self.assertEqual(
        block_to_block_type(block3),
        "unordered_list"
      )
      self.assertEqual(
        block_to_block_type(block4),
        "unordered_list"
      )

    def test_ordered_list(self):
      block1 = "1. This is an ordered list"
      block2 = "1. This is another quote\n2. Here is yet another quote\n3. And another"
      self.assertEqual(
        block_to_block_type(block1),
        "ordered_list"
      )
      self.assertEqual(
        block_to_block_type(block2),
        "ordered_list"
      )

    def test_paragraph(self):
      block1 = "This is a paragraph"
      block2 = "This is another paragraph\nAnd another"
      self.assertEqual(
        block_to_block_type(block1),
        "paragraph"
      )
      self.assertEqual(
        block_to_block_type(block2),
        "paragraph"
      )

    def test_invalid_headings(self):
      block1 = "#This is an invalid heading"
      block2 = "######## This is another invalid heading"
      self.assertEqual(
        block_to_block_type(block1),
        "paragraph"
      )
      self.assertEqual(
        block_to_block_type(block2),
        "paragraph"
      )

    def test_invalid_code_block(self):
      block1 = "```This is an invalid code block"
      block2 = "```This is another invalid code block``"
      self.assertEqual(
        block_to_block_type(block1),
        "paragraph"
      )
      self.assertEqual(
        block_to_block_type(block2),
        "paragraph"
      )

    def test_invalid_quotes(self):
      block = "> This is a valid quote\n> Here is yet another quote\n>But this is invalid"
      self.assertEqual(
        block_to_block_type(block),
        "paragraph"
      )

    def test_invalid_unordered_list(self):
      block1 = "* This is a valid unordered list\n* And again \n>But this is invalid"
      block2 = "- This is a valid unordered list\n- And again \n>But this is invalid"
      self.assertEqual(
        block_to_block_type(block1),
        "paragraph"
      )
      self.assertEqual(
        block_to_block_type(block2),
        "paragraph"
      )

    def test_invalid_ordered_list(self):
      block1 = "1. This is a valid unordered list\n2. And again \n4. But this is invalid"
      block2 = "1. This is a valid unordered list\n3. And again \n4. But this is invalid"
      self.assertEqual(
        block_to_block_type(block1),
        "paragraph"
      )
      self.assertEqual(
        block_to_block_type(block2),
        "paragraph"
      )

if __name__ == "__main__":
  unittest.main()
