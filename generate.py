# generate site from static pages, loosely inspired by Jekyll
# run like this:
#   ./generate.py test/source output
# the generated `output` should be the same as `test/expected_output`

import os
import logging
import jinja2
import sys
import json
import warnings

log = logging.getLogger(__name__)

def list_files(folder_path):
    for name in os.listdir(folder_path):
        if name.endswith(".rst"):
            yield os.path.join(folder_path, name)

def read_file(file_path):
    with open(file_path) as f:
        metadata, content = f.read().split('---', 1)
    return json.loads(metadata), content.strip()
    
def write_output(name, html):
    # TODO should not use sys.argv here, it breaks encapsulation
    with open(name, "w") as f:
        f.write(html)

def generate_site(folder_path, output_path):
    layout_input_path = os.path.join(folder_path, 'layout')
    
    for path, error_msg in [
        (folder_path, "Input Path does not exists: {}"),
        (layout_input_path, "Layout Input path does not exists: {}"),
        (output_path, "Output Path does not exists: {}")
    ]:
        if not os.path.exists(path):
            raise RuntimeError(error_msg.format(path))
        
    log.info("Generating site from %r", folder_path)
    jinja_env = jinja2.Environment(
                    loader=jinja2.FileSystemLoader(layout_input_path),
                    trim_blocks=True
    )
    for file_path in list_files(folder_path):                
        metadata, content = read_file(file_path)
        if not 'layout' in metadata:
            warnings.warn("The file {} is missing the layout information.".format(file_path))
            continue
        
        template_name = metadata['layout']
        template = jinja_env.get_template(template_name)
        data = dict(metadata, content=content)
        html = template.render(**data)
        name, _ = os.path.splitext(os.path.basename(file_path))
        output_file = os.path.join(output_path, name+'.html')
        write_output(output_file, html)
        log.info("Writing %r with template %r", name, template_name)


def main():
    if len(sys.argv)!=3:
        raise RuntimeError("usage: generate.py input_path output_path")
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    generate_site(input_path, output_path)

if __name__ == '__main__':
    logging.basicConfig()
    main()
