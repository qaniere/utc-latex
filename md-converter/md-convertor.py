import os
import jinja2
from parser import extract_metadata_from_md, extract_frames_from_md
from frame import process_frames, finalize_frames  # Import des fonctions de frame.py

metadata: dict = extract_metadata_from_md('example.md')
frames: list = extract_frames_from_md('example.md')  # Assurez-vous que cela renvoie une liste

processed_frames = process_frames(frames)  # Traiter chaque frame dans la liste
final_frames_output = finalize_frames(processed_frames)  # Finaliser les frames traitées

with open('utc-beamer.tpl.tex', 'r') as file: 
    beamer_template: str = file.read()

ejs_env = jinja2.Environment(
    block_start_string='<$', 
    block_end_string='$>',
    variable_start_string='<$=',
    variable_end_string='$>',
    autoescape=False  
)

template = ejs_env.from_string(beamer_template)
rendered_latex = template.render(metadata=metadata, content=final_frames_output)

with open('result.tex', 'w') as file:
    file.write(rendered_latex)

os.system("pdflatex -interaction=nonstopmode -halt-on-error result.tex")
