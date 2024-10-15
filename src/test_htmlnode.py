import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>", None, [1,2], None)
        node2 = HTMLNode("<a>", None, [1,2], None)
        self.assertEqual(node, node2)

    def test_value_and_children_none(self):
        node = HTMLNode("<a>", None, [1,2], None)
        self.assertNotEqual(node.value, node.children)

    def test_prop_to_html(self):
        node = HTMLNode("<a>", None, [1,2], {"href": "https://www.google.com", "target": "_blank",})
        attribute = f"{node.props_to_html}"
        attribute2 = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(attribute, attribute2)
