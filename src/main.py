from copy_static_to_public import copy_static_to_public
from markdown_to_html import generate_page

def main():
  copy_static_to_public()
  generate_page("content/index.md", "template.html", "public/index.html")

main()