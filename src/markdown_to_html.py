import re
import os
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

  top_level_html_node = ParentNode("div", top_level_html_node_children)
  return top_level_html_node.to_html()

def create_blockquote_html(block):
  block_lines = block.split("\n")
  inline_nodes = []

  for line in block_lines:
    text_nodes = text_to_textnodes(line[2:])
    html_nodes = list(map(lambda node: text_node_to_html_node(node), text_nodes))
    inline_nodes += html_nodes

  return ParentNode("blockquote", inline_nodes)

def create_paragraph_html(block):
  return ParentNode("p", create_block_inline_nodes(block))

def create_heading_html(block):
  block_without_the_heading = " ".join((block.split(" "))[1:])
  number_of_h_tag = (block.split(" ")[0]).count("#")
  return LeafNode(f"h{number_of_h_tag}", block_without_the_heading)

def create_unordered_list_html(block):
  block_lines = block.split("\n")
  inline_nodes = []

  for line in block_lines:
    text_nodes = text_to_textnodes(line[2:])
    html_nodes = list(map(lambda node: text_node_to_html_node(node), text_nodes))
    inline_nodes.append(
      ParentNode("li", html_nodes)
    )
  
  return ParentNode("ul", inline_nodes)

def create_ordered_list_html(block):
  block_lines = block.split("\n")
  inline_nodes = []

  for line in block_lines:
    text_nodes = text_to_textnodes(line[3:])
    html_nodes = list(map(lambda node: text_node_to_html_node(node), text_nodes))
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
    html_nodes = list(map(lambda node: text_node_to_html_node(node), text_nodes))
    inline_nodes += html_nodes

  return inline_nodes

def extract_title(markdown):
  match = re.match(r"^\# ", markdown)
  if match == None:
    raise Exception("document must have a heading")
  return match.string.split("\n")[0]

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  with open(from_path, "r") as file:
    markdown = file.read()
  with open(template_path, "r") as file:
    template = file.read()
  markdown_html = markdown_to_html(markdown)
  title = extract_title(markdown)
  template = template.replace("{{ Title }}", title)
  template = template.replace("{{ Content }}", markdown_html)
  writer = open(dest_path, "w")
  writer.write(template)
  writer.close()
  
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  dir_contents = os.listdir(dir_path_content)

  for content in dir_contents:
    path_to_content = os.path.join(dir_path_content, content)
    if os.path.isfile(path_to_content):
      if os.path.isfile(dest_dir_path):
        new_dest_dir_path = dest_dir_path
      else:
        new_dest_dir_path = os.path.join(dest_dir_path, "index.html")
      generate_page(
        path_to_content,
        template_path,
        new_dest_dir_path
      )
    else:
      new_dest_dir_path = os.path.join(dest_dir_path, content)
      os.mkdir(new_dest_dir_path)
      generate_pages_recursive(
        path_to_content,
        template_path,
        new_dest_dir_path
      )