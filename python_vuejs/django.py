# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import click
import os
from .utils import touch, cd


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
    # TODO:
    # edit `index.json` build
    # edit `package.json` build