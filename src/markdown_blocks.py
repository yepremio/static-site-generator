from htmlnode import HTMLNode


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    block_list = []
    split_str = markdown.split('\n\n')
    for str in split_str:
        if str != '\n\n':
            block_list.append(str)
    clean_list = [s for s in block_list if s.strip()]
    return clean_list

def block_to_block_type(markdown):
    if markdown.startswith("#"):
        count_hashes = 0
        for char in markdown:
            if char == "#":
                count_hashes += 1
            else:
                break
        if count_hashes <= 6 and markdown[count_hashes] == " ":
            return "heading"
    elif markdown.startswith("```") and markdown.endswith("```"):
        return block_type_code
    elif all(line.startswith(">") for line in markdown.split("\n")):
        return "quote"
    elif all(line.startswith("* ") or line.startswith("- ") for line in markdown.split("\n")):
        return block_type_ulist 
    elif all(line.split(". ")[0].isdigit() and line.startswith(str(index) + ". ") for index, line in enumerate(markdown.split("\n"), start=1)):
        return block_type_olist
    else:
        return "paragraph"

def text_to_children(text):
    if text 



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == block_type_paragraph:
            node = HTMLNode("p")
            node.children = text_to_children(block)
        
        elif block_type == block_type_heading:
            node = HTMLNode("h")
            node.children = text_to_children(block)

        elif block_type == block_type_code:
            node = HTMLNode("code")
            node.children = text_to_children(block)

        elif block_type == block_type_quote:
            node = HTMLNode("blockquote")
            node.children = text_to_children(block)

        elif block_type == block_type_olist:
            node = HTMLNode("ol")
            node.children = text_to_children(block)

        elif block_type == block_type_ulist:
            node = HTMLNode("ul")
            node.children = text_to_children(block)

        else:

        nodes.append(node)

        parent_node = HTMLNode("div")
        parent_node.children = nodes

        return parent_node












