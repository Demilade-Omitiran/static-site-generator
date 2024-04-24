from textnode import TextNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
  converter_function_dict = {
    "text_type_text": lambda node: LeafNode(None, node.text),
    "text_type_bold": lambda node: LeafNode("b", node.text),
    "text_type_italic": lambda node: LeafNode("i", node.text),
    "text_type_code": lambda node: LeafNode("code", node.text),
    "text_type_link": lambda node: LeafNode("a", node.text, { "href": node.url }),
    "text_type_image": lambda node: LeafNode("img", None, { "src": node.url, "alt": node.text })
  }
  
  if text_node.text_type not in converter_function_dict:
    raise Exception("Invalid text_type")
  
  converter_function = converter_function_dict[text_node.text_type]
  return converter_function(text_node)

def main():
  node = TextNode("This is a text node", "bold", "https://www.boot.dev")
  print(node)

main()