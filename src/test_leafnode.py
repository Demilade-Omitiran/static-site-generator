import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_attr(self):
    node = LeafNode("a", "link", { "href": "www.abc.com", "width": 20 })
    self.assertEqual(node.tag, "a")
    self.assertEqual(node.value, "link")
    self.assertEqual(node.children, None)
    self.assertEqual(node.props, { "href": "www.abc.com", "width": 20 })

  def test_to_html(self):
    node = LeafNode("a", "link", { "href": "www.abc.com", "width": 20 })
    node_to_html = node.to_html()
    self.assertEqual(node.to_html(), "<a href=\"www.abc.com\" width=20>link</a>")


if __name__ == "__main__":
  unittest.main()
