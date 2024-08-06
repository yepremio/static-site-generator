
markdown_path = "content/index.md"
markdown = get_markdown(markdown_path)


def get_markdown(path):
    with open(path) as f:
        return f.read()




def extract_title(markdown):



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")


