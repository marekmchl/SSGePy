from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"\nGenerating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path)
    markdown_text = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path)
    template_text = template_file.read()
    template_file.close()

    markdown_html_node = markdown_to_html_node(markdown_text)
    markdown_html = markdown_html_node.to_html()

    title = extract_title(markdown_text)

    content = template_text.replace("{{ Title }}", title).replace("{{ Content }}", markdown_html)
    content = content.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    dest_file = open(dest_path, "w")
    dest_file.write(content)
    dest_file.close()
