#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

from click.testing import CliRunner

from python_vuejs import cli


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
