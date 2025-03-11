def markdown_to_blocks(markdown):
    if markdown == "":
        return []

    full_block_list = markdown.split("\n\n")
    cleaned_block_list = []
    for block in full_block_list:
        if block == "":
            continue
        else:
            block = block.lstrip().rstrip()
            cleaned_block_list.append(block)

    return cleaned_block_list
