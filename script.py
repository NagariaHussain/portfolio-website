# External Libs
import argparse
from utils import process_sass_files

# Internal Libs
import watcher
from blog_generator import BlogGenerator
from site_generator import SiteGenerator
from project_generator import ProjectGenerator

# Parsing command line arguments
parser = argparse.ArgumentParser()

# For creation of new site content
parser.add_argument("--new", "-n", choices=["blog", "project"], help="generate new site content")

# For watching file changes
parser.add_argument("--watch", "-w", help="watch for file changes", action="store_true")

# Parse arguments
args = parser.parse_args()

# Based on --new flag
if args.new == "blog":
    # Generate a new blog boiler plate
    blog_gen = BlogGenerator()
    blog_gen.generate()
elif args.new == "project":
    # Generate a new project boiler plate
    project_gen = ProjectGenerator()
    project_gen.generate()

# Generate site
site_gen = SiteGenerator()
site_gen.generate()

# Process SASS files
process_sass_files()

# To watch for file changes
if args.watch:
    print("watching for file changes...")
    watcher.start_watching()