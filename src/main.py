from os.path import join
from copy_dir_contents import copy_dir_contents
from generate_pages_recursive import generate_pages_recursive
from sys import argv

def main():
    if len(argv) < 2:
        basepath = "/"
    else:
        basepath = argv[1]

    src = "./static"
    dst = "./docs"
    copy_dir_contents(src, dst)

    from_path = "./content"
    template_path = "./template.html"
    dest_path = "./docs"

    generate_pages_recursive(from_path, template_path, dest_path, basepath)

main()
