from os import getcwd
from os.path import join
from copy_dir_contents import copy_dir_contents
from generate_pages_recursive import generate_pages_recursive

def main():
    src = join(getcwd(), "static")
    dst = join(getcwd(), "public")
    copy_dir_contents(src, dst)

    from_path = join(getcwd(), "content")
    template_path = join(getcwd(), "template.html")
    dest_path = join(getcwd(), "public")

    generate_pages_recursive(from_path, template_path, dest_path)

main()
