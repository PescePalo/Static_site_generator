import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")        
        self.assertEqual(node, node2)

    def test_correct_format(self):
        node = TextNode("test", "italic", "https://www.boot.dev")
        node2 = TextNode("test", "italic", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_correct_url(self):
        node = TextNode("test", "bold")
        node2 = TextNode("test","bold")
        self.assertEqual(node, node2)

    def test_same_text_type(self):
        node = TextNode("test", "bold")
        node2 = TextNode("test", "bold")
        self.assertEqual(node, node2)

    def test_text_text_node(self):
        text_text_node = TextNode("test only text", "text", None)
        node = text_node_to_html_node(text_text_node)
        self.assertEqual("test only text", node.to_html())

    def test_bold_text_node(self):
        bold_text_node = TextNode("bold text", "bold", None)
        self.assertEqual("<b>bold text</b>", text_node_to_html_node(bold_text_node).to_html())

    def test_italic_text_node(self):
        italic_text_node = TextNode("italic text", "italic", None)
        self.assertEqual("<i>italic text</i>", text_node_to_html_node(italic_text_node).to_html())

    def test_code_text_node(self):
        code_text_node = TextNode("code text", "code", None)
        self.assertEqual("<code>code text</code>", text_node_to_html_node(code_text_node).to_html())

    def test_link_text_node(self):
        link_text_node = TextNode("link", "link", "https://www.google.com")
        self.assertEqual('<a href="https://www.google.com">link</a>', text_node_to_html_node(link_text_node).to_html())

    def test_img_text_node(self):
        img_text_node = TextNode("img text", "image", "https://www.google.com")
        self.assertEqual('<img src="https://www.google.com" alt="img text">', text_node_to_html_node(img_text_node).to_html())
        
if __name__ == "__main__":
    unittest.main()