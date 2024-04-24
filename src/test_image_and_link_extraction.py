import unittest

from node_functions import (
  extract_markdown_images,
  extract_markdown_links
)

class TestSplitNodesDelimiter(unittest.TestCase):
  def test_extract_markdown_images(self):
    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    self.assertEqual(
      extract_markdown_images(text),
      [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
    )

  def test_extract_markdown_links(self):
    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    self.assertEqual(
      extract_markdown_links(text),
      [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
    )

  def test_invalid_image_markdown(self):
    self.assertEqual(extract_markdown_images("[image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"), [])

  def test_invalid_link_markdown(self):
    self.assertEqual(extract_markdown_links("abc"), [])
    

if __name__ == "__main__":
  unittest.main()
