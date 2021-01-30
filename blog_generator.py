# External Libs
import yaml
from typing import Dict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

# Internal Libs
from utils import slugify_title

@dataclass 
class Blog:
    title: str = ''
    subtitle: str = ''
    author: str = ''
    creation_date: datetime = None

class BlogGenerator:
    def __init__(self) -> None:
        self.meta_data = Blog()

    def get_blog_meta(self) -> Dict:
        self.meta_data.title = input("title: ")
        self.meta_data.subtitle = input("sub title: ")
        self.meta_data.author = input("author: ")
        self.meta_data.creation_date = datetime.now()

    def write_meta_yaml(self, meta_file_path: Path) -> None:
        with meta_file_path.open('w') as meta_file:
            yaml.dump(
                self.meta_data.__dict__, meta_file, 
                Dumper=yaml.CDumper
            )

    def generate(self) -> None:
        # Get metadata from user
        self.get_blog_meta()
        slugged_title = slugify_title(self.meta_data.title)

        # Create blog folder
        new_blog_path = 'blogs' / Path(slugged_title)
        new_blog_path.mkdir()
        
        # Create file paths
        markdown_file = new_blog_path / (slugged_title + '.md')
        meta_file = new_blog_path / 'meta.yaml'

        # Create files
        markdown_file.touch()
        meta_file.touch()

        # Write meta data as YAML
        self.write_meta_yaml(meta_file)