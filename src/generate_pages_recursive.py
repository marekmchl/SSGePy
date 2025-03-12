import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, current_dir=None):
    print("\n\n")
    if current_dir == []:
        return

    if not os.path.exists(dir_path_content):
        raise Exception("Content directory not found!")

    if not os.path.exists(template_path):
        raise Exception("Template not found!")

    if not os.path.exists(dest_dir_path):
        print(f"Creating dir: {dest_dir_path}")
        os.mkdir(dest_dir_path)

    if current_dir == None:
        current_dir = os.listdir(dir_path_content)

    next_item = current_dir.pop()
    new_content_path = os.path.join(dir_path_content, next_item)
    new_dest_path = os.path.join(dest_dir_path, next_item)
    print(f"next_item: {next_item}\nnew_src: {new_content_path}\nnew_dst: {new_dest_path}")

    if os.path.isfile(new_content_path):
        file_html = next_item.replace(".md", ".html")
        dest_to_html = dest_dir_path + "/" + file_html
        print(f"dest_toHtml: {dest_to_html}")
        generate_page(new_content_path, template_path, dest_to_html)
        return generate_pages_recursive(dir_path_content, template_path, dest_dir_path, current_dir)
    else:
        generate_pages_recursive(new_content_path, template_path, new_dest_path, os.listdir(new_content_path))
        return generate_pages_recursive(dir_path_content, template_path, dest_dir_path, current_dir)
