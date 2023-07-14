#!/usr/bin/python3

"""
A script that converts Markdown to HTML.
"""

import sys
import os.path
import markdown


def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    # Check if the Markdown file exists
    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    with open(input_file, 'r') as file:
        markdown_content = file.read()

    html_content = markdown.markdown(markdown_content)

    with open(output_file, 'w') as file:
        file.write(html_content)


if __name__ == '__main__':
    # Check the number of arguments
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
