class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        result_string = ""
        if self.props == None:
            return result_string
        else:
            for key in self.props:
                result_string += f' {key}="{self.props[key]}"'

        return result_string

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.tag == None:
            return f'{self.value}'
        elif self.tag == "img":
            return f'<img{self.props_to_html()}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("missing tag")

        if self.children == None or self.children == []:
            raise ValueError("missing children")

        string = f"<{self.tag}>"
        for child in self.children:
            string += child.to_html()
        string += f"</{self.tag}>"
        return string
