import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
  def test_attr(self):
    node1 = LeafNode("a", "link", { "href": "www.abc.com" })
    node2 = ParentNode("div", [node1], { "width": 20 })
    self.assertEqual(node2.tag, "div")
    self.assertEqual(node2.value, None)
    self.assertEqual(node2.children, [node1])
    self.assertEqual(node2.props, { "width": 20 })

  def test_to_html_leaf_children(self):
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

  def test_to_html_nested_parents(self):
    node = ParentNode(
      "div",
      [
        ParentNode(
          "p",
          [
              LeafNode("b", "Bold text"),
              LeafNode(None, "Normal text"),
              LeafNode("i", "italic text"),
              LeafNode(None, "Normal text"),
          ],
        )
      ]
    )
    self.assertEqual(node.to_html(), "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>")

  def test_to_html_multiple_nested_parents(self):
    node = ParentNode(
      "html",
      [
        ParentNode(
          "head",
          [
            LeafNode("title", "Title")
          ]
        ),
        ParentNode(
          "body",
          [
            ParentNode(
              "div",
              [
                ParentNode(
                  "p",
                  [
                      LeafNode("b", "Bold text"),
                      LeafNode(None, "Normal text"),
                      LeafNode("i", "italic text"),
                      LeafNode(None, "Normal text"),
                  ],
                )
              ]
            )
          ]
        )
      ]
    )
    self.assertEqual(node.to_html(), "<html><head><title>Title</title></head><body><div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div></body></html>")

  def test_tag_err(self):
    with self.assertRaises(ValueError) as err:
      node = ParentNode(None, [], None)
      node_to_html = node.to_html()
      self.assertEqual(err.msg, "tag is required")

  def test_empty_children_err(self):
    with self.assertRaises(ValueError) as err:
      node = ParentNode('a', [], None)
      node_to_html = node.to_html()
      self.assertEqual(err.msg, "children list is required")

  def test_no_children_err(self):
    with self.assertRaises(ValueError) as err:
      node = ParentNode('a', None, None)
      node_to_html = node.to_html()
      self.assertEqual(err.msg, "children list is required")
    

if __name__ == "__main__":
  unittest.main()
