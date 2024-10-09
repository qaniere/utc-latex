import os
import jinja2

from parser import extract_metadata_from_md


metadata = extract_metadata_from_md('example.md')

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
rendered_latex = template.render(metadata)

with open('result.tex', 'w') as file:
    file.write(rendered_latex)

os.system("pdflatex -interaction=nonstopmode -halt-on-error result.tex")
