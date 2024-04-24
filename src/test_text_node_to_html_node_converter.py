import unittest

from textnode import TextNode
from leafnode import LeafNode
from main import text_node_to_html_node

class TestLeafNode(unittest.TestCase):
  def test_text_type_text(self):
    node = TextNode("This is a text node", "text_type_text", "www.abc.com")
    leaf_node = text_node_to_html_node(node)
    self.assertEqual(leaf_node.tag, None)
    self.assertEqual(leaf_node.value, "This is a text node")
    self.assertEqual(leaf_node.children, None)
    self.assertEqual(leaf_node.props, None)

  def test_text_type_bold(self):
    node = TextNode("This is a text node", "text_type_bold", "www.abc.com")
    leaf_node = text_node_to_html_node(node)
    self.assertEqual(leaf_node.tag, 'b')
    self.assertEqual(leaf_node.value, "This is a text node")
    self.assertEqual(leaf_node.children, None)
    self.assertEqual(leaf_node.props, None)

  def test_text_type_italic(self):
    node = TextNode("This is a text node", "text_type_italic", "www.abc.com")
    leaf_node = text_node_to_html_node(node)
    self.assertEqual(leaf_node.tag, 'i')
    self.assertEqual(leaf_node.value, "This is a text node")
    self.assertEqual(leaf_node.children, None)
    self.assertEqual(leaf_node.props, None)

  def test_text_type_code(self):
    node = TextNode("This is a text node", "text_type_code", "www.abc.com")
    leaf_node = text_node_to_html_node(node)
    self.assertEqual(leaf_node.tag, 'code')
    self.assertEqual(leaf_node.value, "This is a text node")
    self.assertEqual(leaf_node.children, None)
    self.assertEqual(leaf_node.props, None)

  def test_text_type_link(self):
    node = TextNode("This is a text node", "text_type_link", "www.abc.com")
    leaf_node = text_node_to_html_node(node)
    self.assertEqual(leaf_node.tag, 'a')
    self.assertEqual(leaf_node.value, "This is a text node")
    self.assertEqual(leaf_node.children, None)
    self.assertEqual(leaf_node.props, { "href": "www.abc.com" })

  def test_text_type_image(self):
    node = TextNode("This is a text node", "text_type_image", "www.abc.com")
    leaf_node = text_node_to_html_node(node)
    self.assertEqual(leaf_node.tag, 'img')
    self.assertEqual(leaf_node.value, None)
    self.assertEqual(leaf_node.children, None)
    self.assertEqual(leaf_node.props, { "src": "www.abc.com", "alt": "This is a text node" })

  def test_invalid_text_type_err(self):
    with self.assertRaises(Exception) as err:
      node = TextNode("This is a text node", "aaa", "www.abc.com")
      text_node_to_html_node(node)
      self.assertEqual(err.msg, "Invalid text_type")
    

if __name__ == "__main__":
  unittest.main()
