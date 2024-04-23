import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
  def test_attr(self):
    node = TextNode("This is a text node", "bold", "www.abc.com")
    self.assertEqual(node.text, "This is a text node")
    self.assertEqual(node.text_type, "bold")
    self.assertEqual(node.url, "www.abc.com")

  def test_eq(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "bold")
    self.assertEqual(node, node2)
    self.assertEqual(node.url, None)
  
  def test_diff(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "italic")
    self.assertNotEqual(node, node2)

  def test_repr(self):
    node = TextNode("This is a text node", "bold", "www.abc.com")
    node2 = TextNode("This is a text node", "bold")
    self.assertEqual(str(node), "TextNode(This is a text node, bold, www.abc.com)")
    self.assertEqual(str(node2), "TextNode(This is a text node, bold, None)")


if __name__ == "__main__":
  unittest.main()
