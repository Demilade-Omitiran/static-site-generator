import unittest

from textnode import TextNode
from node_functions import split_nodes_image

class TestSplitNodesImage(unittest.TestCase):
  def test_images_in_the_middle(self):
    node = TextNode(
      "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
      "text"
    )
    new_nodes = split_nodes_image([node])
    self.assertEqual(new_nodes, [
      TextNode("This is text with an ", "text"),
      TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
      TextNode(" and another ", "text"),
      TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
    ])

  def test_image_at_the_beginning(self):
    node = TextNode(
      "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
      "text"
    )
    new_nodes = split_nodes_image([node])
    self.assertEqual(new_nodes, [
      TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
      TextNode(" and ", "text"),
      TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    ])

  def test_no_image_in_string(self):
    node = TextNode(
      "[image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
      "text"
    )
    new_nodes = split_nodes_image([node])
    self.assertEqual(new_nodes, [
      TextNode(
        "[image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
        "text"
      )
    ])

if __name__ == "__main__":
  unittest.main()
