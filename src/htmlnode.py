
class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        attribute = ""
        for prop in self.props:
            attribute += f' {prop}="{self.props[prop]}"'
        return attribute
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children:{self.children},{self.props_to_html()})"
    
class LeafNode(HTMLNode):
    def __init__(self, value:str, props:dict, tag:str=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"