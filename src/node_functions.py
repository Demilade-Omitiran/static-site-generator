import re
from textnode import TextNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
  converter_function_dict = {
    "text": lambda node: LeafNode(None, node.text),
    "bold": lambda node: LeafNode("b", node.text),
    "italic": lambda node: LeafNode("i", node.text),
    "code": lambda node: LeafNode("code", node.text),
    "link": lambda node: LeafNode("a", node.text, { "href": node.url }),
    "image": lambda node: LeafNode("img", None, { "src": node.url, "alt": node.text })
  }
  if text_node.text_type not in converter_function_dict:
    raise Exception("Invalid text_type") 
  converter_function = converter_function_dict[text_node.text_type]
  return converter_function(text_node)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []

  for node in old_nodes:
    if node.text_type != "text":
      new_nodes.append(node)
      continue
    delimited_strings = node.text.split(delimiter)
    if len(delimited_strings) % 2 == 0:
      raise Exception("Invalid markdown")
    
    for i in range(0, len(delimited_strings)):
      if i % 2 == 1:
        new_nodes.append(TextNode(delimited_strings[i], text_type))
      else:
        new_nodes.append(TextNode(delimited_strings[i], "text"))
  
  return new_nodes

def extract_markdown_images(text):
  matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
  return matches

def extract_markdown_links(text):
  matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
  return matches