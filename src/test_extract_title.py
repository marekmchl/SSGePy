import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_valid_1(self):
        title = extract_title("""


# Hello

""")
        control = "Hello"
        self.assertEqual(control, title)

    def test_extract_title_whitespaces_1(self):
        title = extract_title("""


#  \t\t   \t  \tHello\t   \t\t


""")
        control = "Hello"
        self.assertEqual(control, title)

    def test_extract_title_more_md_1(self):
        title = extract_title("""

## Bad Hello!

### Badder Hello?

# \t\t\t   \t Hello\t   \t\t


""")
        control = "Hello"
        self.assertEqual(control, title)
