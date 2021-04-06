import unittest

from dextractor import analyze

class TestAnalysis(unittest.TestCase):
    def test_single_file(self):
        """
        Test using a singular file. Returning `True` means it's a single file.
        """
        singleFilePath = "/this/is/a/single/file.txt"
        self.assertTrue(analyze(singleFilePath))
    def test_directory(self):
        """
        Test using a directory path. Returning `False` means it's a directory.
        """
        directoryPath = "this/is/a/directory"
        self.assertFalse(analyze(directoryPath))

if __name__ == '__main__':
    unittest.main()