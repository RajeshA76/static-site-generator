import unittest
from htmlnode import HTMLNode,LeafNode


"""
An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes

"""

class TestHTMLNode(unittest.TestCase):
    def test_empty_tag(self):
        node = HTMLNode(tag=None,value="raw text",children=None,props=None)
        self.assertIsNone(node.tag)
        self.assertEqual(node.value,"raw text")

    def test_empty_value(self):
        child = HTMLNode("span","child text")
        node = HTMLNode(tag="div",value=None,children=[child])
        self.assertIsNone(node.value)
        self.assertEqual(node.children,[child])

    def test_empty_children(self):
        node = HTMLNode(tag="p",value="some text")
        self.assertIsNone(node.children)
        self.assertEqual(node.value,"some text")

    def test_empty_props(self):
        node = HTMLNode(tag="p",value="some text")
        self.assertIsNone(node.props)
        self.assertEqual(node.props_to_html(),"")

    def test_empty_props_dict(self):
        node = HTMLNode(tag="p",value="some text",props={})
        self.assertEqual(node.props_to_html(),"")

    def test_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html_single(self):
        node = HTMLNode("a","link",props={"href":"https://www.google.com"})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode("a","link",props={"href":"https://www.google.com","target":"_blank"})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_to_html_not_implemented(self):
        node = HTMLNode("p","some text")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        node = HTMLNode("p","some text",None,{"class":"intro"})
        self.assertEqual(repr(node),"HTMLNode(p,some text,None,{'class': 'intro'})")

class TestLeafNode(unittest.TestCase):
    def test_empty_value(self):
        node = LeafNode(tag="p",value=None)
        self.assertIsNone(node.value)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_empty_tag(self):
        node = LeafNode(tag=None,value="no tag in this text")
        self.assertIsNone(node.tag)
        self.assertEqual(node.to_html(),node.value)


        



if __name__ == "__main__":
    unittest.main()
