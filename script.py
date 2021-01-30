import sys
from blog_generator import BlogGenerator
from site_generator import SiteGenerator

if len(sys.argv) < 2:
    print("Enter atleast one argument")
    exit(0)

if sys.argv[1] == "new":
    blog_gen = BlogGenerator()
    blog_gen.generate()
elif sys.argv[1] == "gen":
    site_gen = SiteGenerator()
    site_gen.generate()