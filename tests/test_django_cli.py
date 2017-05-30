#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import unittest
from collections import namedtuple

from click.testing import CliRunner

from python_vuejs import cli
from python_vuejs.vuejs import VueJsBuilder

try:
    from mock import patch
except ImportError:
    from unittest.mock import patch


class TestDjangoCli(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_djbuild(self):
        with self.runner.isolated_filesystem():
            # Given
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
            # When
            self.runner.invoke(cli.cli, ['djbuild', 'myapp'])
            # Then
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

    def test_djangofy(self):
        from python_vuejs.django import URLS_TEMPLATE

        with self.runner.isolated_filesystem():
            # Given
            os.makedirs('myapp/config')
            with open('myapp/package.json', 'w') as f:
                package_json = {
                    "scripts": {
                        "dev": "node build/dev-server.js",
                        "start": "node build/dev-server.js",
                        "build": "node build/build.js",
                        "unit": "cross-env BABEL_ENV=test karma start test/unit/karma.conf.js --single-run",
                        "e2e": "node test/e2e/runner.js",
                        "test": "npm run unit && npm run e2e",
                        "lint": "eslint --ext .js,.vue src test/unit/specs test/e2e/specs"
                    }
                }
                f.write(json.dumps(package_json))

            with open('myapp/config/index.js', 'w') as f:
                f.write("""
                module.exports = {
                    build: {
                        index: path.resolve(__dirname, '../dist/index.html'),
                        assetsRoot: path.resolve(__dirname, '../dist'),
                        assetsSubDirectory: 'static',
                    }
                }
                """)
            # When
            result = self.runner.invoke(cli.cli, ['djangofy', 'myapp'])
            # Then
            self.assertTrue(os.path.isfile('myapp/__init__.py'), "__init__.py not found")
            self.assertTrue(os.path.isfile('myapp/urls.py'), "urls.py not found")
            with open('myapp/urls.py') as f:
                self.assertEqual(''.join(f.readlines()), URLS_TEMPLATE.format(project='myapp'))
            with open('myapp/package.json', 'r') as f:
                actual = json.loads(''.join(f.readlines()))
                self.assertEqual('node build/build.js && pyvue djbuild myapp', actual['scripts']['build'])
            expected = """
                module.exports = {
                    build: {
                        index: path.resolve(__dirname, '../templates/myapp/index.html'),
                        assetsRoot: path.resolve(__dirname, '../static'),
                        assetsSubDirectory: 'myapp',
                    }
                }
                """
            with open('myapp/config/index.js') as f:
                self.assertEqual(expected, ''.join(f.readlines()))
            self.assertEqual('Making Vue.js myapp into django app\nEnjoy!\n', result.output)

    def test_djangofy_already_executed(self):
        with self.runner.isolated_filesystem():
            # Given
            os.makedirs('myapp/templates/myapp')
            open('myapp/templates/myapp/index.html', 'a').close()
            # When
            result = self.runner.invoke(cli.cli, ['djangofy', 'myapp'])
            # Then
            self.assertEqual('Making Vue.js myapp into django app\nCommand already executed\n', result.output)

    @patch('python_vuejs.django.djangofy')
    def test_djstartvueapp_django_ok(self, mock_djangofy):
        with self.runner.isolated_filesystem():
            # Given
            open('manage.py', 'a').close()
            nt = namedtuple('Result', ['status', 'message', 'color'])
            return_value = nt(True, 'Application and dependencies installed\n', 'green')

            with patch.object(VueJsBuilder, 'startproject', return_value=return_value) as mock_vuejsbuilder:
                # When
                result = self.runner.invoke(cli.cli, ['djstartvueapp', 'myapp'])
                # Then
                mock_vuejsbuilder.assert_called_once()
                mock_djangofy.assert_called_once()
                self.assertEqual('Creating myapp\n', result.output)

    def test_djstartvueapp_django_ko(self):
        result = self.runner.invoke(cli.cli, ['djstartvueapp', 'myapp'])
        self.assertEqual('Creating myapp\nInvalid django project directory\n', result.output)
