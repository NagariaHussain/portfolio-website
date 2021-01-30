# External Libs
import yaml
from typing import Dict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from yaml.cyaml import CDumper

# Internal Libs
from utils import slugify_title

class ProjectGenerator:
    def __init__(self) -> None:
        self.data = {}

    def get_project_details(self) -> None:
        # Entered by the user
        self.data["name"] = input("project name: ")
        self.data["tech_stack"] = input("tech stack (separated by ','): ").split(",")
        self.data["programming_languages"] = input("programming languages (separated by ','): ").split(",")
        self.data["summary"] = input("project summary: ")
        self.data["project_type"] = input("project type: ")

        # Place holders
        self.data["screenshots"] = {
            "caption1": "url1", 
            "caption2": "url2"
        }

        self.data["body"] = "|"


    def write_data_yaml(self) -> None:
        project_name = slugify_title(self.data["name"]) + ".yaml"
        project_file = Path('projects') / project_name

        with project_file.open('w') as f:
            yaml.dump(self.data, f, Dumper=CDumper)

    def generate(self) -> None:
        self.get_project_details()
        self.write_data_yaml()
        
        print("Go ahead and add some content to project body!")
