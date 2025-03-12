import re

def extract_title(markdown_file_string):
    titles = re.findall(r"(?<!.)# (.+)", markdown_file_string)
    if titles == []:
        raise Exception("No title found!")
    else:
        return titles[0].lstrip().rstrip()
