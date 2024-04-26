from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode
from node_functions import (
  markdown_to_blocks,
  text_node_to_html_node,
  text_to_textnodes,
  block_to_block_type
)

def markdown_to_html(markdown):
  blocks = markdown_to_blocks(markdown)
  block_type_function_dict = {
    "quote": create_blockquote_html,
    "paragraph": create_paragraph_html,
    "heading": create_heading_html,
    "code": create_code_html,
    "unordered_list": create_unordered_list_html,
    "ordered_list": create_ordered_list_html
  }
  top_level_html_node_children = []

  for block in blocks:
    block_type = block_to_block_type(block)
    block_type_function = block_type_function_dict[block_type]
    top_level_html_node_children.append(block_type_function(block))

  return ParentNode("div", top_level_html_node_children)


def create_blockquote_html(block):
  block_lines = block.split("\n")
  inline_nodes = []

  for line in block_lines:
    text_nodes = text_to_textnodes(line[1:])
    html_nodes = map(lambda node: text_node_to_html_node(node), text_nodes)
    inline_nodes.append(html_nodes)

  return ParentNode("blockquote", inline_nodes)

def create_paragraph_html(block):
  return ParentNode("p", create_block_inline_nodes(block))

def create_heading_html(block):
  block_without_the_heading = " ".join((block.split(" "))[1:])
  number_of_h_tag = (block.split(" ")[0]).count("#")
  return ParentNode(f"h{number_of_h_tag}", create_block_inline_nodes(block_without_the_heading))

def create_unordered_list_html(block):
  block_lines = block.split("\n")
  inline_nodes = []

  for line in block_lines:
    text_nodes = text_to_textnodes(line[2:])
    html_nodes = map(lambda node: text_node_to_html_node(node), text_nodes)
    inline_nodes.append(
      ParentNode("li", html_nodes)
    )
  
  return ParentNode("ul", inline_nodes)

def create_ordered_list_html(block):
  block_lines = block.split("\n")
  inline_nodes = []

  for line in block_lines:
    text_nodes = text_to_textnodes(line[3:])
    html_nodes = map(lambda node: text_node_to_html_node(node), text_nodes)
    inline_nodes.append(
      ParentNode("li", html_nodes)
    )
  
  return ParentNode("ol", inline_nodes)

def create_code_html(block):
  block_text = block.split("```")[1]

  return ParentNode("pre", [
    LeafNode("code", block_text)
  ])


def create_block_inline_nodes(block):
  block_lines = block.split("\n")
  inline_nodes = []

  for line in block_lines:
    text_nodes = text_to_textnodes(line)
    html_nodes = map(lambda node: text_node_to_html_node(node), text_nodes)
    inline_nodes.append(html_nodes)

  return inline_nodes
