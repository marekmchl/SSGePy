from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images_list = extract_markdown_images(node.text)
        if images_list == []:
            new_nodes.append(node)
            continue

        text = node.text
        for image_tuple in images_list:
            left_index = text.find(f"![{image_tuple[0]}]({image_tuple[1]})")
            new_nodes.append(TextNode(text[:left_index], TextType.TEXT))
            new_nodes.append(TextNode(image_tuple[0], TextType.IMAGE, image_tuple[1]))
            # From the end of the current image to the end of the original text
            text = text[left_index + 5 + len(image_tuple[0]) + len(image_tuple[1]):]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
