
class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        attribute = ""
        for prop in self.props:
            attribute += " " + prop +"=" + self.props[prop]
        return attribute
    
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props_to_html}"