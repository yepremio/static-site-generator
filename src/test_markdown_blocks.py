import unittest

from markdown_blocks import markdown_to_blocks

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        nodes = markdown_to_blocks(
            "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        )
        expected_nodes = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()
