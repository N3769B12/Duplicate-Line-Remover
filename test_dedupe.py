import unittest
from dedupe import remove_duplicates


class RemoveDuplicatesTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(remove_duplicates("a\nb\na\nc\nb"), ("a\nb\nc", 2, 3))

    def test_case_sensitive_by_default(self):
        self.assertEqual(remove_duplicates("Apple\napple")[1], 0)

    def test_ignore_case_keeps_first(self):
        self.assertEqual(remove_duplicates("Apple\napple", ignore_case=True), ("Apple", 1, 1))

    def test_trim_spaces(self):
        self.assertEqual(remove_duplicates("cat\n  cat  ", trim_spaces=True), ("cat", 1, 1))
        self.assertEqual(remove_duplicates("cat\n  cat  ")[1], 0)

    def test_sort(self):
        self.assertEqual(remove_duplicates("pear\nApple\nfig\npear", sort_az=True)[0], "Apple\nfig\npear")

    def test_empty(self):
        self.assertEqual(remove_duplicates(""), ("", 0, 0))


if __name__ == "__main__":
    unittest.main()
