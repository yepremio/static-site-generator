import os
from markdown_blocks import markdown_to_html_node 

def extract_title(markdown):
    split_markdown = markdown.splitlines()
    for line in split_markdown:
        if line.startswith("# "):
            return line[2:]
    else:
        raise ValueError("Missing h1 header")

# write the generative pages recursively function below
# Additional notes as needed.
#
# New functio
# testn
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
 
    def open_file(path):
        with open(path) as f:
            return f.read()

    markdown = open_file(from_path)
    template = open_file(template_path)

    node = markdown_to_html_node(markdown)
    html = node.to_html()


    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    to_file = open(dest_path, 'w')
    to_file.write(template)

