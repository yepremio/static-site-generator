from textnode import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def markdown_to_blocks(markdown):
    block_list = []
    split_str = markdown.split('\n\n')
    for str in split_str:
        if str != '\n\n':
            block_list.append(str)
    clean_list = [s for s in block_list if s.strip()]
    return clean_list

def block_to_block_type(markdown):
    if markdown.startswith("#"):
        count_hashes = 0
        for char in markdown:
            if char == "#":
                count_hashes += 1
            else:
                break
        if count_hashes <= 6 and markdown[count_hashes] == " ":
            return "heading"

    elif markdown.startswith("```") and markdown.endswith("```"):
        return text_type_code 
        
    elif all(line.startswith(">") for line in markdown.split("\n")):
        return "quote"
        
    elif all(line.startswith("* ") or line.startswith("- ") for line in markdown.split("\n")):
        return "unordered list"
        
    elif all(line.split(". ")[0].isdigit() and line.startswith(str(index) + ". ") for index, line in enumerate(markdown.split("\n"), start=1)):
        return "ordered_list"
    else:
        return "paragraph"
