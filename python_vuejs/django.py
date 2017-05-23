# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import click
import os


@click.command()
@click.argument('project')
def djangobuild(project):
    """
    Called inside `package.json`
    """
    template_file = 'templates/{project}/index.html'.format(project=project)
    with open(template_file, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        lines.insert(0, "{% load staticfiles %}\n")
        for line in lines:
            f.write(line.replace('href=/', "href={% static '/")
                    .replace('.css', ".css' %}")
                    .replace('src=/', "src={% static '/")
                    .replace('.js', ".js' %}"))


@click.command()
@click.argument('project')
def djangofy(project):
    """
    Convert Vue.js webpack project into a django app
    """
    os.makedirs('{project}/templates/{project}/'.format(project=project))
    # TODO:
    # create urls.py
    # create __init__.py
    # create empty index.html under templates/project
    # edit `index.json` build
    # edit `package.json` build
