#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_vuejs
----------------------------------

Tests for `python_vuejs` module.



import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from python_vuejs import python_vuejs
from python_vuejs import cli


class TestPython_vuejs(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'python_vuejs.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

"""
