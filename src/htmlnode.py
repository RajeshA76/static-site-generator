

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        result = ""
        for k,v in self.props.items():
            result += f' {k}="{v}"'
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"


class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        self.tag = tag
        self.value = value
        self.props = props
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        props = self.props_to_html()
        if not self.tag:
            return self.value
        else:
            return f"<{tag}{props}>{value}</{tag}>"
