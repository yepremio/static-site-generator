import shutil
import os

def main():

    def copy_static_contents(src, dst):
        # Check to see if destination exists.
        
        if os.path.exists(dst):
        # Remove dir and contents 

            shutil.rmtree(dst)

        # Create destination dir.

        os.mkdir(dst)

        # recursive logic 

        if not os.path.exists(src):
            return src
        
        # logic
        for item in os.listdir(src):
            src_item = os.path.join(src, item)
            dst_item = os.path.join(dst, item)

            if os.path.isdir(src_item):
                copy_static_contents(src_item, dst_item)
            else:
                shutil.copy(src_item, dst_item)
                print(f"Copied {src_item} to {dst_item}")

main()











