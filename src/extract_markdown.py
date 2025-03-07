import re

# Takes a Markdown string with an image and returns a list of (alt_text, URL) tuples
def extract_markdown_images(text):
    return re.findall(r"\!\[(.+?)\]\((.*?)\)", text)

# Takes a Markdown string with a link and returns a list of (anchor_text, URL) tuples
def extract_markdown_links(text):
    return re.findall(r"[^\!]\[(.+?)\]\((.*?)\)", text)
