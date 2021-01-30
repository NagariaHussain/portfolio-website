from pathlib import Path
from blog_generator import Blog
from utils import sort_blog_by_cd_lambda
import yaml
from yaml import CLoader


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

    def generate(self) -> None:
        self.load_blogs()
        self.sort_blogs()

site_gen = SiteGenerator()
site_gen.generate()