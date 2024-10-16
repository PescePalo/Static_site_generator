import unittest
from textnode import TextNode

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
        
if __name__ == "__main__":
    unittest.main()