import os
import shutil
from generate_page import generate_page
from copystatic import copy_static_contents

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting Public Directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_static_contents(dir_path_static, dir_path_public)

    generate_page('content/index.md', 'template.html', 'public/index.html')
    
if __name__ == "__main__": main()

