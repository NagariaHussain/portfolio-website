def slugify_title(title: str) -> str:
    '''returns a sluggified version of the given `title`'''
    slugged_title = ""
    for c in title:
        if c.isalnum():
            slugged_title += c.lower()
        if c.isspace():
            slugged_title += '-'

    return slugged_title


# Testing util functions
from unittest import TestCase, main
import unittest

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

# Run the tests
unittest.main()