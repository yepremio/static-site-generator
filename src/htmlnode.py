class HTMLNode():
    def __init__(self, tag, value, children, props):
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
        raise NotImplementedError

    def props_to_html(self):
        return f""
    
    def __repr__(self):
        print() 

        
