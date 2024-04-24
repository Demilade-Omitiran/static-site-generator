import unittest

from textnode import TextNode
from leafnode import LeafNode
from node_functions import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
  def test_no_delimiters(self):
    node = TextNode("This is a text node", "text")
    new_nodes = split_nodes_delimiter([node], '`', "code")
    self.assertEqual(new_nodes, [node])

  def test_delimiter(self):
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], '`', "code")
    self.assertEqual(new_nodes, [
      TextNode("This is text with a ", "text"),
      TextNode("code block", "code"),
      TextNode(" word", "text"),
    ])

  def test_multiple_delimiters(self):
    node = TextNode("This is text with a `code block` word, an *italic block* word and a **bold block** word", "text")
    new_nodes = split_nodes_delimiter([node], '`', "code")
    new_nodes = split_nodes_delimiter(new_nodes, '**', "bold")
    new_nodes = split_nodes_delimiter(new_nodes, '*', "italic")
    self.assertEqual(new_nodes, [
      TextNode("This is text with a ", "text"),
      TextNode("code block", "code"),
      TextNode(" word, an ", "text"),
      TextNode("italic block", "italic"),
      TextNode(" word and a ", "text"),
      TextNode("bold block", "bold"),
      TextNode(" word", "text"),
    ])

  def test_invalid_markdown(self):
    with self.assertRaises(Exception) as err:
      node = TextNode("This is a `text node", "text")
      split_nodes_delimiter([node], '`', "code")
      self.assertEqual(err.msg, "Invalid text_type")
    

if __name__ == "__main__":
  unittest.main()
