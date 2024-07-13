class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
    # Str representing the HTML tag name ("p", "h1")
        self.tag = tag
    # Str representing the value of the HTML tag - (text inside paragraph) 
        self.value = value
    # List of HTML objects representing the children of this node
        self.children = children
    # A dictionary of key-value pairs representing the attributes of the
    # HTML Tag for e.g. link <a> might have {"href": "https://www.google.com"}
        self.props = props
 
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
       # This method should return a string that represents the HTML attributes of the node.
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children='{self.children}', props='{self.props}')"
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
   
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Error: missing children")

        children_html = ""

        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, childre:{self.children}, {self.props})"

testig plz delete




    
