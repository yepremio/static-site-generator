import shutil
import os


def copy_static_contents(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
        
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)
        print(f"* {src_item} -> {dst_item}")

        if os.path.isfile(src_item):
            shutil.copy(src_item, dst_item)
        else:
            copy_static_contents(src_item, dst_item)

