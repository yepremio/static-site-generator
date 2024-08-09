from markdown_blocks import markdown_to_html_node 
import htmlnode 

def open_file(path):
    with open(path) as f:
        return f.read()

markdown_path = "content/index.md"
markdown = open_file(markdown_path)

template_path = "template.html"
template = open_file(template_path)

def extract_title(markdown):
    split_markdown = markdown.splitlines()
    for line in split_markdown:
        if line.startswith("#"):
            new_line = line.replace("#", '')
            return new_line.strip()
    else:
        raise Exception("Missing h1 header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
 
    def open_file(path):
        with open(path) as f:
            return f.read()

    markdown = open_file(from_path)
    template = open_file(template_path)

    converted_markdown = markdown_to_html_node(markdown)
    title = extract_title(markdown)

    new_template = template.replace("{{ Title }}", title)
    new_template = new_template.replace("{{ Content }}", converted_markdown)
    
    with open(dest_path, 'w') as f:
        f.write(new_template)

