import re

valid_metadata_fields: list[str] = ['author', 'institute', 'date', 'uv', 'semester']

def extract_metadata_from_md(file_path) -> dict:

    metadata = {}
    title = None
    metadata_pattern = re.compile(r'^\$meta-(\w+)=(.*)$')
    title_pattern = re.compile(r'^#\s+(.+)$') 

    with open(file_path, 'r') as file:
        for line in file:
            stripped_line = line.strip()

            match = metadata_pattern.match(stripped_line)
            if match:
                key, value = match.groups()
                if key in valid_metadata_fields:
                    metadata[key] = value.strip()
                else:
                    raise ValueError(f'{key} is not a valid metadata field! (valid: {", ".join(valid_metadata_fields)})')
            
            title_match = title_pattern.match(stripped_line)
            if title_match:
                if title is None:
                    title = title_match.group(1).strip() 
                else:
                    print(key)
                    raise ValueError("Multiple titles found! Only one title is allowed.")
    
    if title is not None:
        metadata['title'] = title
    else:
        raise ValueError("No title found in the file!")

    return metadata

def extract_frames_from_md(file_path) -> list:
    frames = []
    frame_title = None
    content_buffer = []
    frame_pattern = re.compile(r'^##\s+(.+)$')
    metadata_pattern = re.compile(r'^\$meta-')

    with open(file_path, 'r') as file:
        for line in file:
            stripped_line = line.strip()

            if metadata_pattern.match(stripped_line) or stripped_line.startswith('# '):
                continue

            frame_match = frame_pattern.match(stripped_line)
            if frame_match:
                if frame_title:
                    frames.append((frame_title, "\n".join(content_buffer).strip()))
                    content_buffer = []

                frame_title = frame_match.group(1).strip()

            else:
                content_buffer.append(stripped_line)

        if frame_title:
            frames.append((frame_title, "\n".join(content_buffer).strip()))

    if not frames:
        raise ValueError("No frames (## title) found in the file!")

    return frames

