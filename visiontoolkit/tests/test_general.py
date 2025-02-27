"""Test suite for the VISION Toolkit."""

import unittest
from unittest.mock import patch

import sys
from io import StringIO

import visiontoolkit


class TestApp(unittest.TestCase):
    """TODO."""
    @patch("sys.stdout", new_callable=StringIO)
    @patch("sys.argv", new=["visiontoolkit.py"])
    def test_no_arguments(self, mock_stdout):
        visiontoolkit.main()

        # Capture the printed output and test it
        output = mock_stdout.getvalue().strip()
        print("test_no_arguments output is:", output)

    @patch("sys.stdout", new_callable=StringIO)
    @patch("sys.argv", new=["visiontoolkit.py", "--help"])
    def test_argument(self, mock_stdout):
        visiontoolkit.main()

        # Capture STDOUT
        output = mock_stdout.getvalue().strip()
        print("test_argument output is:", output)


if __name__ == "__main__":
    unittest.main()
