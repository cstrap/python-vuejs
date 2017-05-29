#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from click.testing import CliRunner
from python_vuejs import cli
from python_vuejs.vuejs import VueJs, VueJsBuilder

try:
    from mock import patch
except ImportError:
    from unittest.mock import patch


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

    @patch('python_vuejs.vuejs.VueJs.vue_cli_check')
    def test_find_valid_vue_no_install_vuecli(self, mocked):
        mocked.return_value = True
        result = self.runner.invoke(cli.cli, ['installvuecli'])
        self.assertEqual(0, result.exit_code)
        self.assertIn('Found valid vue-cli', result.output)

    @patch('python_vuejs.vuejs.VueJs.install_cli')
    @patch('python_vuejs.vuejs.VueJs.vue_cli_check')
    def test_no_vuecli_install(self, mock_check, mock_install):
        mock_check.return_value = False
        result = self.runner.invoke(cli.cli, ['installvuecli'])
        self.assertEqual(0, result.exit_code)
        mock_install.assert_called_once()
        self.assertIn('Installed vue-cli globally', result.output)

    @patch('python_vuejs.vuejs.VueJsBuilder.startproject')
    def test_start_vue_app(self, mock_startproject):
        result = self.runner.invoke(cli.cli, ['startvueapp', 'myapp'])
        self.assertEqual(-1, result.exit_code)
        mock_startproject.assert_called_once()

    def test_builder_startproject_ko(self):
        with patch.object(VueJs, 'vue_cli_check', return_value=False) as mock_method:
            result = VueJsBuilder.startproject('project')
            self.assertFalse(result.status)
            mock_method.assert_called_once()

    def test_builder_startproject_ok(self):
        with patch.object(VueJs, 'vue_cli_check', return_value=True) as mock_vuecli:
            with patch.object(VueJs, 'project_setup') as mock_setup:
                with patch.object(VueJs, 'install_dependencies') as mock_installdep:
                    result = VueJsBuilder.startproject('project')
                    mock_vuecli.assert_called_once()
                    mock_setup.assert_called_once()
                    mock_installdep.assert_called_once()
                    self.assertTrue(result.status)

    @patch('python_vuejs.vuejs.VueJs.dev')
    def test_call_vuedev(self, mock_dev):
        result = self.runner.invoke(cli.cli, ['vuedev'])
        mock_dev.assert_called_once()
        self.assertEqual(0, result.exit_code)

    @patch('python_vuejs.vuejs.VueJs.build')
    def test_call_vuedev(self, mock_build):
        result = self.runner.invoke(cli.cli, ['vuebuild'])
        mock_build.assert_called_once()
        self.assertEqual(0, result.exit_code)


class TestDjangoCli(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_djbuild(self):
        with self.runner.isolated_filesystem():
            os.makedirs('templates/myapp')
            with open(os.path.join('templates/myapp', 'index.html'), 'w') as f:
                f.write("""<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8>
<title>myapp</title>
<link href=/static/css/app.8dec12ac5345f90e222a6effb448e777.css rel=stylesheet>
</head>
<body>
<div id=app></div>
<script type=text/javascript src=/static/js/manifest.77925171db9c5dd326bf.js></script>
<script type=text/javascript src=/static/js/vendor.10682ac638c1f430abfc.js></script>
<script type=text/javascript src=/static/js/app.5f58654c7e43b3645479.js></script>
</body>
</html>""")
            self.runner.invoke(cli.cli, ['djbuild', 'myapp'])
            with open(os.path.join('templates/myapp', 'index.html')) as f:
                sut = f.readlines()
                self.assertEqual('{% load staticfiles %}\n', sut[0])
                expected = """<link href="{% static '/static/css/app.8dec12ac5345f90e222a6effb448e777.css' %}" rel=stylesheet>\n"""  # noqa
                self.assertEqual(expected, sut[6])
                expected = """<script type=text/javascript src="{% static '/static/js/manifest.77925171db9c5dd326bf.js' %}"></script>\n"""  # noqa
                self.assertEqual(expected, sut[10])
                expected = """<script type=text/javascript src="{% static '/static/js/vendor.10682ac638c1f430abfc.js' %}"></script>\n"""  # noqa
                self.assertEqual(expected, sut[11])
                expected = """<script type=text/javascript src="{% static '/static/js/app.5f58654c7e43b3645479.js' %}"></script>\n"""  # noqa
                self.assertEqual(expected, sut[12])
