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
                
        cmd_stdout = capsys.readouterr().out
        cmd_stdout_ignore_newlines = cmd_stdout.replace("\n", " ")

        # Actual testing statements
        # 1. Assert something emerges to STDOUT
        assert cmd_stdout != ""

        # 2. Assert basic text including summary appears
        assert "usage: VISION TOOLKIT" in cmd_stdout
        assert (
            "Virtual Integration of Satellite and In-Situ Observation "
            "Networks (VISION) toolkit flight simulator"
        ) in cmd_stdout_ignore_newlines

        # 3. Assert ASCII project symbol appears
        # Just test this via first line to avoid having to wrestle against
        # newlines and whitespace line splitting
        assert ".______________________________________________." in cmd_stdout

        # 4. Assert some CLI argument help descriptions appear.
        # Don't want to test on any specific option since thes might change
        # with a CLI change, but this 'help' command is guaranteed to be there
        # so check the description of that appears.
        assert "options:" in cmd_stdout
        assert (
            "-h, --help            show this help message and exit"
        ) in cmd_stdout_ignore_newlines


if __name__ == "__main__":
    pytest.main()
