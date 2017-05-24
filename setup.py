#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python-vuejs
-------------
Gluing Python and Vue.js with a set of scripts in order to automate project and app builds
"""

from setuptools import setup

import codecs

with codecs.open('README.rst', 'r', 'utf-8') as readme_file:
    readme = readme_file.read()

with codecs.open('HISTORY.rst', 'r', 'utf-8') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'colorama',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='python_vuejs',
    version='0.0.2',
    description="Gluing Python and Vue.js with a set of scripts in order to automate project and app builds",
    long_description=readme + '\n\n' + history,
    author="Christian Strappazzon",
    author_email='lab@strap.it',
    url='https://github.com/cstrap/python-vuejs',
    packages=[
        'python_vuejs',
    ],
    package_dir={'python_vuejs':
                 'python_vuejs'},
    entry_points={
        'console_scripts': [
            'checkenv=python_vuejs.vuejs:check_env',
            'vuecli=python_vuejs.vuejs:install_vue_cli',
            'startvueapp=python_vuejs.vuejs:startvueapp',
            'vuedev=python_vuejs.vuejs:vuedev',
            'vuebuild=python_vuejs.vuejs:vuebuild',
            'djbuild=python_vuejs.django:django_build',
            'djvue=python_vuejs.django:djangofy_vue_project',
            'djstartvueapp=python_vuejs.django:django_start_vue_app'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='python_vuejs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
