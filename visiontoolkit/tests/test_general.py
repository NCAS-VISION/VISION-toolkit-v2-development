"""Test suite for the VISION Toolkit."""

import sys

import pytest
from unittest.mock import patch  # Only using patch, not unittest

import visiontoolkit


class TestGeneral:
    def test_help(self, capsys):
        """Test the `$ visiontoolkit --help` command."""
        # Setup to run command
        with patch.object(sys, "argv", ["visiontoolkit.py", "--help"]):
            with pytest.raises(SystemExit) as excinfo:
                visiontoolkit.main()  # Run command
                
        captured = capsys.readouterr().out

        # Actual testing statements
        assert captured != ""
        assert "usage: VISION TOOLKIT" in captured
        


if __name__ == "__main__":
    pytest.main()
