import re

def process_frames(frames: list) -> list:
    processed_frames = []
    processing_functions = [process_title, process_content]

    for title, content in frames:
        for func in processing_functions:
            if func == process_title:
                title = func(title)
            else:
                content = func(content)
        
        processed_frames.append((title, content))
    
    return processed_frames

def process_title(title: str) -> str:
    return f"\\begin{{frame}}{{{title}}}"

def process_content(content: str) -> str:
    return process_lists(content)

def process_lists(content: str) -> str:
    lines = content.splitlines()
    processed_lines = []

    for line in lines:
        if line.startswith('* '):
            processed_lines.append(f"        \\item {line[2:]}")
        else:
            processed_lines.append(f"        {line}")

    return "\\begin{itemize}\n" + "\n".join(processed_lines) + "\n    \\end{itemize}"

def finalize_frames(processed_frames: list) -> str:
    final_output = []
    for title, content in processed_frames:
        final_output.append(f"{title}\n    {content}\n\\end{{frame}}")
    return "\n\n".join(final_output)
