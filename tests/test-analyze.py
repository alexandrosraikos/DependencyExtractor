import unittest
import os

from dextractor import analyze

if (os.getcwd().endswith("dependency-extractor") == False):
    raise Exception("Please launch the script from the root directory of the package.")
else:
    print("\nTesting sequence launched from: "+ os.getcwd()+"\n")

class TestAnalysis(unittest.TestCase):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    def test_single_file(self):
        """
        Test using a singular file.
        """
        filePath = "/tests/data/cpp/main.cpp"
        self.assertEqual("File!", analyze(os.getcwd()+filePath))
    def test_directory(self):
        """
        Test using a directory path.
        """
        directoryPath = "/tests/data/cpp"
        self.assertEqual("Directory!", analyze(os.getcwd()+directoryPath))

if __name__ == '__main__':
    unittest.main()