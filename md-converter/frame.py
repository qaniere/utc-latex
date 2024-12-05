import re

def process_frames(frames: list) -> list:
    """
    Process frames by applying title and content processing.
    """
    processed_frames = []
    for title, content in frames:
        title = process_title(title)
        content = process_content(content)
        processed_frames.append((title, content))
    return processed_frames

def process_title(title: str) -> str:
    """
    Process the title for a frame.
    """
    return f"\\begin{{frame}}{{{title}}}"

def process_content(content: str) -> str:
    """
    Process the content of a Markdown frame.
    Detects and processes images, lists, notes, and plain text.
    """
    content = process_images(content)
    content = process_notes(content)
    content = process_lists(content)
    return content

def process_images(content: str) -> str:
    """
    Converts Markdown image syntax to LaTeX, supporting size configuration.
    """
    # ![alt_text](path/to/image){width=...}
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
    """
    Detects and converts Markdown notes (lines starting with '>') to LaTeX blocks.
    """
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
    """
    Converts Markdown syntax into LaTeX, supporting multiple independent lists 
    and text blocks on the same frame.
    """
    lines = content.splitlines()
    processed_lines = []
    inside_list = False  # Tracks if we're currently inside a list

    for line in lines:
        stripped_line = line.strip()

        # Detect list item
        if stripped_line.startswith('* '):
            # Open a new list if not already inside one
            if not inside_list:
                processed_lines.append("\\begin{itemize}")
                inside_list = True
            # Add the list item
            processed_lines.append(f"    \\item {stripped_line[2:]}")
        else:
            # Handle non-list lines (e.g., plain text or titles between lists)
            if inside_list:
                # Close the list environment
                processed_lines.append("\\end{itemize}")
                inside_list = False
            processed_lines.append(line)  # Add the plain text

    # Close any remaining open list
    if inside_list:
        processed_lines.append("\\end{itemize}")

    return "\n".join(processed_lines)





def finalize_frames(processed_frames: list) -> str:
    """
    Wraps the processed frames into LaTeX `frame` environments.
    """
    final_output = []
    for title, content in processed_frames:
        final_output.append(f"{title}\n    {content}\n\\end{{frame}}")
    return "\n\n".join(final_output)
