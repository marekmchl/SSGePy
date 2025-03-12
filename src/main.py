from os import getcwd
from os.path import join
from copy_dir_contents import copy_dir_contents

def main():
    src = join(getcwd(), "static")
    dst = join(getcwd(), "public")
    copy_dir_contents(src, dst)

main()
