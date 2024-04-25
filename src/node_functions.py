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

def split_nodes_image(old_nodes):
  new_nodes = []

  for node in old_nodes:
    if node.text_type != "text":
      new_nodes.append(node)
      continue
    images_in_node = extract_markdown_images(node.text)
    if len(images_in_node) == 0:
      new_nodes.append(node)
      continue
    node_text = node.text
    current_index = 0
    for image in images_in_node:
      image_index = node_text[current_index:].find(f"![{image[0]}]({image[1]})")
      if image_index != 0:
        new_nodes.append(TextNode(node_text[current_index:current_index + image_index], "text"))
        new_nodes.append(TextNode(image[0], "image", image[1]))
      else:
        new_nodes.append(TextNode(image[0], "image", image[1]))
      current_index += image_index + len(f"![{image[0]}]({image[1]})")
    if current_index != (len(node_text) - 1) and node_text[current_index:].strip() != "":
      new_nodes.append(TextNode(node_text[current_index:], "text"))
  
  return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = []

  for node in old_nodes:
    if node.text_type != "text":
      new_nodes.append(node)
      continue
    links_in_node = extract_markdown_links(node.text)
    if len(links_in_node) == 0:
      new_nodes.append(node)
      continue
    node_text = node.text
    current_index = 0
    for link in links_in_node:
      link_index = node_text[current_index:].find(f"[{link[0]}]({link[1]})")
      if link_index != 0:
        new_nodes.append(TextNode(node_text[current_index:current_index + link_index], "text"))
        new_nodes.append(TextNode(link[0], "link", link[1]))
      else:
        new_nodes.append(TextNode(link[0], "link", link[1]))
      current_index += link_index + len(f"[{link[0]}]({link[1]})")
    if current_index != (len(node_text) - 1) and node_text[current_index:].strip() != "":
        new_nodes.append(TextNode(node_text[current_index:], "text"))
  
  return new_nodes
  
def text_to_textnodes(text):
  nodes = split_nodes_delimiter(
    [TextNode(text, "text")],
    "**",
    "bold"
  )
  nodes = split_nodes_delimiter(nodes, "*", "italic")
  nodes = split_nodes_delimiter(nodes, "`", "code")
  nodes = split_nodes_image(nodes)
  nodes = split_nodes_link(nodes)
  return nodes
