from os import getcwd
from os.path import join
from copy_dir_contents import copy_dir_contents
from generate_page import generate_page

def main():
    src = join(getcwd(), "static")
    dst = join(getcwd(), "public")
    copy_dir_contents(src, dst)

    from_path = join(join(getcwd(), "content"), "index.md")
    template_path = join(getcwd(), "template.html")
    dest_path = join(join(getcwd(), "public"), "index.html")

    generate_page(from_path, template_path, dest_path)

main()
