import unittest

from textnode import TextNode
from node_functions import split_nodes_link

class TestSplitNodesImage(unittest.TestCase):
  def test_links_in_the_middle(self):
    node = TextNode(
      "This is text with an [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
      "text"
    )
    new_nodes = split_nodes_link([node])
    self.assertEqual(new_nodes, [
      TextNode("This is text with an ", "text"),
      TextNode("image", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
      TextNode(" and another ", "text"),
      TextNode("second image", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
    ])

  def test_link_at_the_beginning(self):
    node = TextNode(
      "[image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
      "text"
    )
    new_nodes = split_nodes_link([node])
    self.assertEqual(new_nodes, [
      TextNode("image", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
      TextNode(" and ", "text"),
      TextNode("image", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    ])

  def test_no_image_in_string(self):
    node = TextNode(
      "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png and https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
      "text"
    )
    new_nodes = split_nodes_link([node])
    self.assertEqual(new_nodes, [
      TextNode(
        "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png and https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
        "text"
      )
    ])

if __name__ == "__main__":
  unittest.main()
