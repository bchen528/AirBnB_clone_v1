#!/usr/bin/python3
"""Unit tests for console"""
import unittest
import os
import pep8
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """testing console"""
    @classmethod
    def setUpClass(cls):
        """setup instance"""
        cls.c1 = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """tear down class after test"""
        del cls.c1

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """test pep8 compliant"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docstrings_in_console(self):
        """check for docstrings indicating function existence"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)

    def test_emptyline(self):
        """test newline"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.c1.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """test quit command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.c1.onecmd("quit")
            self.assertEqual('', f.getvalue())

if __name__ == '__main__':
    unittest.main()
