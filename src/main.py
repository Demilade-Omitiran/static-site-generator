from copy_static_to_public import copy_static_to_public
from markdown_to_html import generate_pages_recursive

def main():
  copy_static_to_public()
  generate_pages_recursive("content", "template.html", "public")

main()