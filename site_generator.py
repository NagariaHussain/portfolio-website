# External Libs
import yaml
import markdown
from pathlib import Path
from yaml import CLoader

# Internal Libs
from blog_generator import Blog
from utils import sort_blog_by_cd_lambda

class SiteGenerator:
    def __init__(self) -> None:
        self.blogs = []
    
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
            with blog["md_file"].open('r') as f:
                html = markdown.markdown(f.read())
                out_path: Path = Path('dist/pages/blogs') / blog["md_file"].stem
                out_path.with_suffix('.html').write_text(html)




    def generate_blog_list_page(self) -> None:
        pass

    def generate(self) -> None:
        # Load blogs into memory
        self.load_blogs()

        # Sort blogs by creation date
        self.sort_blogs()

        # Parse markdown and Generate HTML 
        self.generate_blog_html_files()

        # Generate Blog list HTML page
        self.generate_blog_list_page()

site_gen = SiteGenerator()
site_gen.generate()