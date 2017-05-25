#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_vuejs
----------------------------------

Tests for `python_vuejs` module.

"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

try:
    from mock import patch
except ImportError:
    from unittest.mock import patch

from python_vuejs import cli
from python_vuejs.vuejs import VueJs


class TestMainCli(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_main_cli_interface(self):
        result = self.runner.invoke(cli.cli)
        self.assertEqual(0, result.exit_code)
        help_result = self.runner.invoke(cli.cli, ['--help'])
        self.assertEqual(0, help_result.exit_code)
        self.assertIn('--help  Show this message and exit.', help_result.output, 'message')

    def test_main_cli_interface_commands(self):
        commands_result = self.runner.invoke(cli.cli, ['--help'])
        commands_list = ['vuecheck', 'startvueapp', 'vuebuild', 'vuedev', 'installvuecli',
                         'djangofy', 'djbuild', 'djstartvueapp']
        for command in commands_list:
            self.assertIn(command, commands_result.output)


class TestVueJsCli(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    @patch('python_vuejs.vuejs.VueJs.node_check')
    def test_check_node_environment_ok(self, mocked):
        mocked.return_value = True
        result = self.runner.invoke(cli.cli, ['vuecheck'])
        self.assertEqual(0, result.exit_code)
        self.assertIn('Found node and npm', result.output)

    @patch('python_vuejs.vuejs.VueJs.node_check')
    def test_check_node_environment_ok(self, mocked):
        mocked.return_value = False
        result = self.runner.invoke(cli.cli, ['vuecheck'])
        self.assertEqual(0, result.exit_code)
        self.assertIn('Missing node and npm installation', result.output)
