import re

def process_frames(frames: list) -> list:
    processed_frames = []
    for title, content in frames:
        title = process_title(title)
        content = process_content(content)
        processed_frames.append((title, content))
    return processed_frames

def process_title(title: str) -> str:
    return f"\\begin{{frame}}{{{title}}}"

def process_content(content: str) -> str:
    content = process_images(content)
    content = process_notes(content)
    content = process_lists(content)
    content = process_text_styles(content)
    return content

def process_images(content: str) -> str:
    image_pattern = re.compile(r"!\[(.*?)\]\((.*?)\)(?:\{(.*?)\})?")
    lines = content.splitlines()
    processed_lines = []

    for line in lines:
        match = image_pattern.search(line)
        if match:
            alt_text = match.group(1)
            image_path = match.group(2)
            size_options = match.group(3) if match.group(3) else "width=\\textwidth"
            processed_lines.append(
                f"\\begin{{center}}\n    \\includegraphics[{size_options}]{{{image_path}}} % {alt_text}\n\\end{{center}}"
            )
        else:
            processed_lines.append(line)
    
    return "\n".join(processed_lines)

def process_notes(content: str) -> str:
    note_pattern = re.compile(r"^>\s*(\((.*?)\))?\s*(.*)")
    lines = content.splitlines()
    processed_lines = []

    for line in lines:
        match = note_pattern.match(line)
        if match:
            block_title = match.group(2) or "Note"
            block_content = match.group(3)
            processed_lines.append(
                f"\\begin{{block}}{{{block_title}}}\n    {block_content}\n\\end{{block}}"
            )
        else:
            processed_lines.append(line)
    
    return "\n".join(processed_lines)

def process_lists(content: str) -> str:
    lines = content.splitlines()
    processed_lines = []
    inside_list = False

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.startswith('* '):
            if not inside_list:
                processed_lines.append("\\begin{itemize}")
                inside_list = True
            processed_lines.append(f"    \\item {stripped_line[2:]}")
        else:
            if inside_list:
                processed_lines.append("\\end{itemize}")
                inside_list = False
            processed_lines.append(line)

    if inside_list:
        processed_lines.append("\\end{itemize}")

    return "\n".join(processed_lines)

def process_text_styles(content: str) -> str:
    content = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', content)
    content = re.sub(r'\*(.*?)\*', r'\\textit{\1}', content)
    content = re.sub(r'__(.*?)__', r'\\underline{\1}', content)
    return content

def finalize_frames(processed_frames: list) -> str:
    final_output = []
    for title, content in processed_frames:
        final_output.append(f"{title}\n    {content}\n\\end{{frame}}")
    return "\n\n".join(final_output)
