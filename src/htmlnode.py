
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        text = ""
        if isinstance(self.props, dict):
            for key, value in self.props.items():
                text += f' {key}="{value}"'
        return text

    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag")
        elif self.children == None:
            raise ValueError("no child")
        html_string = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            child_html_string = child.to_html()
            html_string += child_html_string
        html_string += f'</{self.tag}>'
        return html_string