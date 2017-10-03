# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import json
import os
import sys
from collections import OrderedDict

import click

from .utils import cd, touch
from .vuejs import VueJsBuilder


URLS_TEMPLATE = """# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^{project}/$', TemplateView.as_view(template_name='{project}/index.html'), name='vue_index'),
]

"""


@click.group()
def cli():
    """
    Click entry point: django-cli commands group
    By convention all new cli has a cli function with a pass statement
    """
    pass


@cli.command()
@click.argument('project')
def djbuild(project):
    """
    Called inside `package.json`
    """
    template_file = 'templates/{project}/index.html'.format(project=project)
    with open(template_file, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        lines.insert(0, "{% load staticfiles %}\n")
        for line in lines:
            f.write(line.replace('href=/', "href=\"{% static '")
                    .replace('.css', ".css' %}\"")
                    .replace('src=/', "src=\"{% static '")
                    .replace('.js', ".js' %}\""))


@cli.command()
@click.argument('project')
def djangofy(project):
    """
    Convert Vue.js webpack project into a django app
    """
    click.echo(click.style('Making Vue.js {project} into django app'.format(project=project), bg='blue', fg='white'))
    urls_py = URLS_TEMPLATE.format(project=project)
    try:
        os.makedirs('{project}/templates/{project}/'.format(project=project))
    except OSError:
        click.echo(click.style('Command already executed', fg='red'))
        sys.exit(0)
    with cd(project):
        touch('__init__.py')
        touch('index.html', 'templates/{project}/'.format(project=project))
        with open('urls.py', 'w') as f:
            f.write(urls_py)
        with open('package.json', 'r+') as f:
            pakckage_json = json.loads(''.join(f.readlines()), object_pairs_hook=OrderedDict)
            pakckage_json['scripts']['build'] += ' && pyvue djbuild {project}'.format(project=project)
            f.seek(0)
            f.write(json.dumps(pakckage_json, indent=2))
        with cd('config'):
            with open('index.js', 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    f.write(line
                            .replace('../dist/index.html', '../templates/{project}/index.html'.format(project=project))
                            .replace('../dist', '../static')
                            .replace("assetsSubDirectory: 'static'",
                                     "assetsSubDirectory: '{project}'".format(project=project)))

    click.echo(click.style('Enjoy!', fg='green'))


@cli.command()
@click.argument('project')
@click.pass_context
def djstartvueapp(ctx, project):
    """
    Run click commands on bash.
    """
    click.echo(click.style('Creating {project}'.format(project=project), fg='green'))
    if os.path.isfile('manage.py') and VueJsBuilder.startproject(project).status:
        ctx.forward(djangofy)
        ctx.invoke(djangofy, project=project)
    else:
        click.echo(click.style('Invalid django project directory. `manage.py` not found.', fg='red'))
