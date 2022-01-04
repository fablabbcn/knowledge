import os
import re
import yaml
from jinja2 import Environment, FileSystemLoader

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """

    @env.macro
    def include_tags(filename, tag = 'all'):
        """
        Include a file, optionally indicating start_line and end_line
        (start counting from 0)
        The path is relative to the top directory of the documentation
        project.
        """

        full_filename = os.path.join(env.project_dir, filename)
        with open(full_filename, 'r') as f:
            lines = f.readlines()

        klines = dict()

        pattern_tag = re.compile("(?<=>)(.*)(?=<)")

        for line in lines[4:]:

            if line.startswith('# ') or line.startswith('---'): continue
            if line.startswith('## '):

                ctag = ''.join(pattern_tag.findall(line))
                klines[ctag] = dict()
                continue

            if '*' not in line: continue
            if 'index' in line: continue

            desc = line[line.index("[")+1:line.index("]")]
            link = line[line.index("(")+1:line.index(")")]

            frontmatter = get_meta(link)

            description = ''
            if 'description' in frontmatter:
                description = frontmatter['description']

            date = ''
            if 'date' in frontmatter:
                date = frontmatter['date']

            author = ''
            if 'author' in frontmatter:
                author = frontmatter['author']

            klines[ctag][desc]= [link.replace('.md', ''),
                 description,
                 date,
                 author]

        if tag != 'all': klines = klines[tag]

        return klines

    @env.macro
    def get_meta(filename):
        full_filename = os.path.join(env.project_dir, 'docs', filename)

        with open(full_filename, 'r') as f:
            lines = f.readlines()

        frontmatter = yaml.load('\n'.join(lines[1:lines[1:].index('---\n')+1]),
            Loader=yaml.SafeLoader)

        return frontmatter

    @env.macro
    def get_cards(template = 'tag_cards.html', tags = 'all', full = True):

        file_loader = FileSystemLoader('templates')

        jenv = Environment(loader=file_loader)
        template = jenv.get_template(template)

        return template.render(tags=include_tags('aux/tags.md', tags), full=full)


