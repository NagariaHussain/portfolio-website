
# For Testing util functions
from utils import slugify_title, sort_blog_by_cd_lambda
from datetime import datetime

# For testing blog generation
from blog_generator import BlogGenerator
from pathlib import Path
import yaml
from yaml import CLoader

from unittest import TestCase, loader, main
from unittest.mock import patch, Mock

class TestUtilities(TestCase):
    def test_slug_generation(self):
        # Test 1
        self.assertEqual(
            slugify_title('My First Blog!'), 'my-first-blog'
        )

        # Test 2
        self.assertEqual(
            slugify_title('The circular import string.py fatigue?!'), 'the-circular-import-stringpy-fatigue'
        )

        # Test 3
        self.assertEqual(
            slugify_title('Yet another test with 1234 Numbers, yes.'), 'yet-another-test-with-1234-numbers-yes'
        )

    def test_sort_lambda(self):
        unsorted_test_data = [
            {
                "meta_data": {
                    "title": "Hello 1",
                    "creation_date": datetime(2021, 12, 12)
                }
            },
            {
                "meta_data": {
                    "title": "Hello 2",
                    "creation_date": datetime(2021, 1, 26)
                }
            },
            {
                "meta_data": {
                    "title": "Hello 3",
                    "creation_date": datetime(2021, 1, 1)
                }
            }
        ]

        sorted_test_data = [
            {
                "meta_data": {
                    "title": "Hello 3",
                    "creation_date": datetime(2021, 1, 1)
                }
            },
            {
                "meta_data": {
                    "title": "Hello 2",
                    "creation_date": datetime(2021, 1, 26)
                }
            },
            {
                "meta_data": {
                    "title": "Hello 1",
                    "creation_date": datetime(2021, 12, 12)
                }
            },
        ]

        unsorted_test_data.sort(key=sort_blog_by_cd_lambda)

        self.assertListEqual(sorted_test_data, unsorted_test_data)

class TestBlogGenerator(TestCase):
    TEST_TITLE = 'some-super-title'

    @patch('builtins.input')
    def setUp(self, mock_inp: Mock) -> None:
        self.blog_gen = BlogGenerator()
        mock_inp.side_effect = ['Some Super Title!?', 'Some subtitle', 'John Doe']
        self.blog_gen.generate()

    def test_blog_boiler_plate_gen(self):
        new_blog_path = Path(f'blogs/{self.TEST_TITLE}')
        # Assert folder creation
        self.assertTrue(new_blog_path.exists())

        meta_file_path = new_blog_path / 'meta.yaml'
        blog_file = new_blog_path / f'{self.TEST_TITLE}.md'
        # Assert Files creation
        self.assertTrue(meta_file_path.exists())
        self.assertTrue(blog_file.exists())

        # Assert meta data
        with meta_file_path.open('r') as meta_file:
            meta_data = yaml.load(meta_file, Loader=CLoader)
            self.assertEqual(meta_data['title'], 'Some Super Title!?')
            self.assertEqual(meta_data['subtitle'], 'Some subtitle')
            self.assertEqual(meta_data['author'], 'John Doe')

    def tearDown(self) -> None:
        # Delete generated files
        Path(f'blogs/{self.TEST_TITLE}/meta.yaml').unlink()
        Path(f'blogs/{self.TEST_TITLE}/{self.TEST_TITLE}.md').unlink()
        # Remove generated folder
        Path(f'blogs/{self.TEST_TITLE}').rmdir()
        
# Run the tests
main()