# External Libs
import sys
import subprocess

# Internal Libs
from blog_generator import BlogGenerator
from site_generator import SiteGenerator
from project_generator import ProjectGenerator

if len(sys.argv) < 2:
    print("Enter atleast one argument")
    exit(0)

if sys.argv[1] == "new":
    if sys.argv[2] == "blog":
        blog_gen = BlogGenerator()
        blog_gen.generate()
    elif sys.argv[2] == "project":
        project_gen = ProjectGenerator()
        project_gen.generate()
    else:
        print("Invalid 2nd argument with 'new'. Try Again!")

elif sys.argv[1] == "gen":
    site_gen = SiteGenerator()
    site_gen.generate()

    # Transpile sass files
    subprocess.run(['npm', 'run', 'compile-sass'], shell=True)
    # Minify main css file
    subprocess.run(['npm', 'run', 'minify-css'], shell=True)