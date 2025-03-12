import os
import shutil

def copy_dir_contents(src_dir_path, dst_dir_path, parent_dir_contents=None):
    if parent_dir_contents == []:
        print("\nReached end... Returning from recursion...")
        return

    if not os.path.exists(src_dir_path):
        raise Exception("Invalid source path - source doesn't exist!")

    if not os.path.exists(dst_dir_path):
        print("\nDirectory is missing... Creating the directory...")
        os.mkdir(dst_dir_path)
    elif parent_dir_contents == None and os.listdir(dst_dir_path) != []:
        print("\nFirst call... Directory has contents... Removing...")
        shutil.rmtree(dst_dir_path)
        os.mkdir(dst_dir_path)

    if parent_dir_contents == None:
        parent_dir_contents = os.listdir(src_dir_path)

    next_item = parent_dir_contents.pop()
    new_src_path = os.path.join(src_dir_path, next_item)
    new_dst_path = os.path.join(dst_dir_path, next_item)

    if os.path.isfile(new_src_path):
        print(f"\nCopying a file...\n\tSrc: {new_src_path}\n\tDst: {new_dst_path}")
        tmp = shutil.copy2(new_src_path, new_dst_path)
        print(f"\nDone copying...\n\tResult: {tmp}")
        return copy_dir_contents(src_dir_path, dst_dir_path, parent_dir_contents)
    else:
        print(f"\nCrawling into a directory...\n\tSrc: {new_src_path}\n\tDst: {new_dst_path}")
        return copy_dir_contents(new_src_path, new_dst_path, os.listdir(new_src_path))
