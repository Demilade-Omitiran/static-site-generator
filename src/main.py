from textnode import TextNode
from leafnode import LeafNode

def main():
  node = TextNode("This is text with a `code block` word", "bold", "https://www.boot.dev")
  print(node)
  print(node.text.split("`"))

main()