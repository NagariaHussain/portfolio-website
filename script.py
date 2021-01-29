from pathlib import Path
from typing import Dict
from datetime import datetime

import sys
import yaml

from utils import slugify_title

if len(sys.argv) < 2:
    print("Enter atleast one argument")
    exit(0)

def write_meta_yaml(meta_file_path: Path, meta_data: Dict) -> None:
    yaml.dump(meta_data, meta_file_path.open('w'))

def get_blog_meta() -> Dict:
    meta_data = {}
    meta_data["title"] = input("title: ")
    meta_data["subtitle"] = input("sub title: ")
    meta_data["author"] = input("author: ")
    meta_data["creation_date"] = datetime.now()
    return meta_data

def create_new_blog() -> None:
    meta_data = get_blog_meta()
    slugged_title = slugify_title(meta_data["title"])

    # Create blog folder
    new_blog_path = 'blogs' / Path(slugged_title)
    new_blog_path.mkdir()
    
    # Create file paths
    markdown_file = new_blog_path / (slugged_title + '.md')
    meta_file = new_blog_path / 'meta.yaml'

    # Create files
    markdown_file.touch()
    meta_file.touch()

    write_meta_yaml(meta_file, meta_data)


if sys.argv[1] == "new":
    create_new_blog()
