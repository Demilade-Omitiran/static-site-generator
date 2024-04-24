import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
  def test_attr(self):
    node = HtmlNode("a", "link", None, { "href": "www.abc.com" })
    node2 = HtmlNode("div", "Here", [node], { "colour": "AABBCC" })
    self.assertEqual(node.tag, "a")
    self.assertEqual(node.value, "link")
    self.assertEqual(node.children, None)
    self.assertEqual(node.props, { "href": "www.abc.com" })
    self.assertEqual(node2.tag, "div")
    self.assertEqual(node2.value, "Here")
    self.assertEqual(node2.children, [node])
    self.assertEqual(node2.props, { "colour": "AABBCC" })

  def test_props_to_html(self):
    node = HtmlNode("a", "link", None, { "href": "www.abc.com", "height": 10 })
    node_html_props = node.props_to_html()
    self.assertEqual(node_html_props, " href=\"www.abc.com\" height=10")

  def test_no_props_to_html(self):
    node = HtmlNode("a", "link", None, None)
    node_html_props = node.props_to_html()
    self.assertEqual(node_html_props, "")

  def test_empty_props_to_html(self):
    node = HtmlNode("a", "link", None, {})
    node_html_props = node.props_to_html()
    self.assertEqual(node_html_props, "")

  def test_repr(self):
    node = HtmlNode("a", "link", None, { "href": "www.abc.com" })
    node2 = HtmlNode("div", "Here", [node], { "colour": "AABBCC" })
    node2_to_str_lines = str(node2).split("\n")

    self.assertEqual(node2_to_str_lines[0], "")
    self.assertEqual(node2_to_str_lines[1].strip(), f"tag: {node2.tag},")
    self.assertEqual(node2_to_str_lines[2].strip(), f"value: {node2.value},")
    self.assertEqual(node2_to_str_lines[3].strip(), "children: [")
    self.assertEqual(node2_to_str_lines[4].strip(), f"tag: {node.tag},")
    self.assertEqual(node2_to_str_lines[5].strip(), f"value: {node.value},")
    self.assertEqual(node2_to_str_lines[6].strip(), f"children: {node.children},")
    self.assertEqual(node2_to_str_lines[7].strip(), f"props: {node.props}")
    self.assertEqual(node2_to_str_lines[8].strip(), "],")
    self.assertEqual(node2_to_str_lines[9].strip(), f"props: {node2.props}")
    self.assertEqual(node2_to_str_lines[10].strip(), "")


if __name__ == "__main__":
  unittest.main()
