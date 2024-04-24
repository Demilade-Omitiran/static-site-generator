from htmlnode import HtmlNode

class ParentNode(HtmlNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag == None:
      raise ValueError("tag is required")
    
    if self.children == None or len(self.children) == 0:
      raise ValueError("children list is required")
    
    html_string = f"<{self.tag}{self.props_to_html()}>"

    for child in self.children:
      html_string += child.to_html()

    return html_string + f"</{self.tag}>"