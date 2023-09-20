#!/usr/bin/python3
"""markdown2html"""
import sys
import os
import markdown

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    sys.stderr.write(f"Missing {input_file}\n")
    sys.exit(1)

with open(input_file, 'r') as f:
    markdown_content = f.read()

html_content = markdown.markdown(markdown_content)

with open(output_file, 'w') as f:
    f.write(html_content)

# Exit with a success code
sys.exit(0)
