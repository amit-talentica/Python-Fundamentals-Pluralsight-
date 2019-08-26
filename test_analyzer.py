import unittest
import os


def analyze_text(filename):
    """ Calculate the numbers of line """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return lines, chars


class TextAnalysisTests(unittest.TestCase):
    """ Tests for the analyze_text() function
    """

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Python is a programming language\n'
                    'Declare variables not war\n'
                    'Machine Learning is trending')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods"""
        try:
            os.remove()
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test": does the function run""
        """
        analyze_text(self.filename)

    def test_line_count(self):
        """Test the line count"""
        self.assertEqual(analyze_text(self.filename)[0], 3)

    def test_character_count(self):
        """Total  number of characters in a file"""
        self.assertEqual(analyze_text(self.filename)[1], 87)

    def test_no_such_file(self):
        """check file name"""
        with self.assertRaises(IOError):
            analyze_text("abcd")

    def test_no_deletion(self):
        """check that function doesn't delete file """
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()