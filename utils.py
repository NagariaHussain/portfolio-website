import subprocess
from pathlib import Path

# ---------
# Functions
# ---------
# For creating a slug string
def slugify_title(title: str) -> str:
    '''returns a sluggified version of the given `title`'''
    slugged_title = ""
    for c in title:
        if c.isalnum():
            slugged_title += c.lower()
        if c.isspace():
            slugged_title += '-'

    return slugged_title

# For processing sass files
def process_sass_files():
    for path in Path('sass').iterdir():
        if path.is_file() and path.suffix == ".scss":
            sass_path_string = str(path)
            css_path_string =  Path("dist/css") / (path.stem + ".css")
            mincss_path_string =  Path("dist/css") / (path.stem + ".min.css")

            subprocess.run(
                ['npx', 'node-sass', sass_path_string, css_path_string], 
                shell=True
            )
        
            subprocess.run(
                ['npx', 'csso', css_path_string, '-o', mincss_path_string]
                , shell=True
            )

# -------
# LAMBDAS
# -------
# For sorting blogs by creation date
sort_blog_by_cd_lambda = lambda x:x["meta_data"]["creation_date"]
