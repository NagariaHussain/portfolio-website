# External Libs
import yaml
import markdown
from pathlib import Path
from yaml import CLoader
from string import Template

# Internal Libs
from blog_generator import Blog
from utils import slugify_title, sort_blog_by_cd_lambda

class SiteGenerator:
    def __init__(self) -> None:
        self.blogs = []
        self.projects = []
    
    def load_blogs(self) -> None:
        for path in Path('blogs').iterdir():
            if path.is_dir():
                meta_data_file = path / 'meta.yaml'
                md_file = path / (path.name + '.md')

                with meta_data_file.open('r') as f:
                    meta_data = yaml.load(
                        f, 
                        Loader=CLoader
                    )

                    self.blogs.append({
                        "meta_data": meta_data,
                        "md_file": md_file
                    })
           
    def sort_blogs(self) -> None:
        self.blogs.sort(key=sort_blog_by_cd_lambda)

    def generate_blog_html_files(self) -> None:
        for blog in self.blogs:
            # Generate HTML Head
            head_template_file = open('partials/blog_head.html', 'r')
            head_template = Template(head_template_file.read())

            main_template_file = open('partials/main.html', 'r')
            main_template = Template(main_template_file.read())

            blog_head = head_template.substitute(blog["meta_data"])
            
            # Parse and add markdown
            with blog["md_file"].open('r') as f:
                blog_body = markdown.markdown(f.read())
            
            html = main_template.substitute(
                {
                    **blog["meta_data"],
                    "blog_body": blog_body,
                    "blog_head": blog_head
                }
            )
            # Write output file
            out_path: Path = Path('dist/pages/blogs') / blog["md_file"].stem
            out_path.with_suffix('.html').write_text(html)

    def generate_blog_list_page(self) -> None:
        out_path: Path = Path('dist/pages') / 'blogs.html'
        html = "<ul>"
        
        for blog in self.blogs:
            blog_title = blog["meta_data"]["title"]
            blog_html_url = "/dist/pages/blogs/" + blog["md_file"].with_suffix('.html').name
            html += f'<li><a href="{blog_html_url}">{blog_title}</a></li>'

        html += "</ul>"
        out_path.write_text(html)

    def generate(self) -> None:
        # Generate Blogs
        self.generate_blogs()

        # Generate projects
        self.generate_projects()

        # Generate about page
        self.generate_about_page()

    def generate_blogs(self) -> None:
        # Load blogs into memory
        self.load_blogs()

        # Sort blogs by creation date
        self.sort_blogs()

        # Parse markdown and Generate HTML 
        self.generate_blog_html_files()

        # Generate Blog list HTML page
        self.generate_blog_list_page()

    def generate_project_html_files(self) -> None:
        for project in self.projects:
            body_html = markdown.markdown(project["body"])
            file_name = slugify_title(project["name"]) + ".html"
            out_path = Path('dist/pages/projects') / file_name
            out_path.write_text(body_html)

    def generate_projects(self) -> None:
        # Load projects into memory
        self.load_projects()

        # Generate project HTML files
        self.generate_project_html_files()

        # Generate projects list page
        self.generate_projects_list_page()

    def generate_projects_list_page(self) -> None:
        out_path: Path = Path('dist/pages') / 'projects.html'

        html = "<ul>\n"
        for proj in self.projects:
            proj_url = "projects/" + slugify_title(proj["name"]) + ".html"
            html += f'<li><a href="{proj_url}">{proj["name"]}</a></li>\n'
        html += "</ul>"

        out_path.write_text(html)

    def load_projects(self) -> None:
         for path in Path('projects').iterdir():
            if path.is_file():
                with path.open('r') as proj_file:
                    project_data = yaml.load(proj_file, Loader=CLoader)
                    self.projects.append(project_data)

    def generate_about_page(self) -> None:
        # Output HTML file path
        out_path = Path('dist/pages/about.html')

        # Load about data
        with open('about.yaml', 'r') as about_me:
            data = yaml.load(about_me, Loader=CLoader)
        
        # Get the about template string
        template_file = open('partials/about.html')
        about_template = template_file.read()
        template_file.close()

        # Create template
        about_template = Template(about_template)

        # Generate HTML for education list
        education_list_html = '<ul>'
        for education in data["education"]:
            education_list_html += f'<li>{education["degree"]}</li>'
        education_list_html += '</ul>'

        data["education"] = education_list_html

        # Render and save template
        with out_path.open('w') as out_file:
            html = about_template.safe_substitute(data)
            out_file.write(html)



        