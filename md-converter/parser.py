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