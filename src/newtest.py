from markdown_blocks import markdown_to_html_node


def test_markdown_conversion():
    markdown_text = "_didn't ruin it_"
    html_node = markdown_to_html_node(markdown_text)
    html_string = html_node.to_html()
    print(html_string)
    
test_markdown_conversion()
