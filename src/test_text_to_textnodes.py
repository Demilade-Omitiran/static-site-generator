import unittest

from textnode import TextNode
from leafnode import LeafNode
from node_functions import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
  def test_all_tags(self):
    nodes = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)")
    self.assertEqual(
      nodes,
      [
          TextNode("This is ", "text"),
          TextNode("text", "bold"),
          TextNode(" with an ", "text"),
          TextNode("italic", "italic"),
          TextNode(" word and a ", "text"),
          TextNode("code block", "code"),
          TextNode(" and an ", "text"),
          TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
          TextNode(" and a ", "text"),
          TextNode("link", "link", "https://boot.dev")
      ]
    )

if __name__ == "__main__":
  unittest.main()
