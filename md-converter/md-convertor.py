#!/usr/bin/python3

import os
import argparse
import jinja2

from parser import extract_metadata_from_md, extract_frames_from_md
from frame import process_frames, finalize_frames

parser = argparse.ArgumentParser(description="Generate a Beamer PDF from a Markdown file.")
parser.add_argument("input_file", type=str, help="Path to the input Markdown file.")
parser.add_argument("--output_file", type=str, default="result.pdf", help="Path to the output PDF file.")
parser.add_argument(
    "--template", type=str, default="utc-beamer.tpl.tex",
    help="Path to the LaTeX Beamer template file (default: utc-beamer.tpl.tex)."
)
args = parser.parse_args()

metadata: dict = extract_metadata_from_md(args.input_file)
frames: list = extract_frames_from_md(args.input_file)

processed_frames = process_frames(frames)
final_frames_output = finalize_frames(processed_frames)

with open(args.template, 'r') as file:
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

output_tex_file = args.output_file.replace('.pdf', '.tex')
with open(output_tex_file, 'w') as file:
    file.write(rendered_latex)

os.system(f"pdflatex -interaction=nonstopmode -halt-on-error {output_tex_file}")
