# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import click
import os
from .utils import touch, cd
import json
from collections import OrderedDict


@click.command()
@click.argument('project')
def django_build(project):
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
def djangofy_vue_project(project):
    """
    Convert Vue.js webpack project into a django app
    """

    urls_py = """# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^{project}/$', TemplateView.as_view(template_name='{project}/index.html'), name='vue_index'),
]

""".format(project=project)
    try:
        os.makedirs('{project}/templates/{project}/'.format(project=project))
    except FileExistsError:
        pass
    with cd(project):
        touch('__init__.py')
        touch('index.html', 'templates/{project}/'.format(project=project))
        with open('urls.py', 'w') as f:
            f.write(urls_py)
        with open('package.json', 'r+') as f:
            pakckage_json = json.loads(''.join(f.readlines()), object_pairs_hook=OrderedDict)
            pakckage_json['scripts']['build'] += ' && djbuild'
            f.seek(0)
            f.write(json.dumps(pakckage_json, indent=2))
        with cd('config'):
            with open('index.js', 'r+'):
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    f.write(line.replace('../dist/index.html', './templates/{project}/index.html'.format(project=project))
                            .replace('', '../static')
                            .replace("assetsSubDirectory: 'static'",
                                     "assetsSubDirectory: '{project}'".format(project=project)))
