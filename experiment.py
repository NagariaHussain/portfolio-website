import markdown

# Generate HTML from markdown
print(markdown.markdown("# Hello \n## bYe"))

# Reading and writing YAML files
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

with open('meta.yaml', 'r') as config_file:
    print(yaml.load(config_file, Loader=Loader))

from datetime import datetime

with open('meta.yaml', 'w') as config_fig:
    yaml.dump({
        "title": "My Second blog title", 
        "creation_date": datetime.now(),
        "subtitle": "This is my sub title!",
        "author": "Mohammad Hussain"
    }, config_fig)

# String template
from string import Template

head_template_file = open('partials/head.html', 'r')
config_file = open('meta.yaml', 'r')

head_template = Template(head_template_file.read())

print(head_template.substitute(yaml.load(config_file)))

config_file.close()
head_template_file.close()