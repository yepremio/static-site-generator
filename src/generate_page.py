
markdown_path = "content/index.md"
markdown = get_markdown(markdown_path)


def get_markdown(path):
    with open(path) as f:
        return f.read()




def extract_title(markdown):



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

#read markdown from_path and store in variable
#read template file at template_path and store in variable
# markdown_to_html_node and .to_html() method to convert markdown file to an html string
# use extract_title function to grab the title of the page.
# replace the {{ Title }} and {{ Content }} placeholders with the html generated
# write the new full HTML page to a file at dest_path
#
