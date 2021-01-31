import subprocess

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

# For sorting blogs by creation date
sort_blog_by_cd_lambda = lambda x:x["meta_data"]["creation_date"]

def process_sass_files():
    # Transpile sass files
    # npx node-sass sass/main.scss dist/css/main.css
    subprocess.run(['npx', 'node-sass', 'sass/main.scss', 'dist/css/main.css'], shell=True)
    subprocess.run(['npx', 'node-sass', 'sass/blog.scss', 'dist/css/blog.css'], shell=True)
    
    # Minify main css file
    # npx csso dist/css/main.css -o dist/css/main.min.css
    subprocess.run(['npx', 'csso', 'dist/css/main.css', '-o', 'dist/css/main.min.css'], shell=True)
    subprocess.run(['npx', 'csso', 'dist/css/blog.css', '-o', 'dist/css/blog.min.css'], shell=True)