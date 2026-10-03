import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("this is text node with url",TextType.LINK,"https://www.google.co.in")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node,node2)

    def test_diff_type(self):
        with self.assertRaises(ValueError):
            TextNode("this is diff text type node","url","https://www.google.co.in")



if __name__ == "__main__":
    unittest.main()


