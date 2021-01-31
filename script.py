# External Libs
import sys
from utils import process_sass_files

# Internal Libs
import watcher
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
    # Generate site
    site_gen = SiteGenerator()
    site_gen.generate()

    # Process SASS files
    process_sass_files()

if __name__ == "__main__":
    watcher.start_watching()