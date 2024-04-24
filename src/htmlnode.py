class HtmlNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError()
  
  def props_to_html(self):
    if self.props == None or len(self.props) == 0:
      return ""
    
    html_props = []
    for key in self.props:
      prop_string = f"{key}="
      if type(self.props[key]) == str:
        prop_string += f"\"{self.props[key]}\""
      else:
        prop_string += f"{self.props[key]}"
      html_props.append(prop_string)
    
    return " " + " ".join(html_props)
  
  def __repr__(self):
    return f"""
      tag: {self.tag},
      value: {self.value},
      children: {self.children},
      props: {self.props}
    """