# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import click

from .utils import cd

from subprocess import check_output

try:
    from subprocess import call as run
except ImportError:
    from subprocess import run


@click.command()
def check_env():
    """
    Check if node > 5 and npm > 3 are installed
    """
    out = all([check_output(['node -v'.split()]) > 'v5.0.0', check_output(['npm -v'.split()]) >= '4.0.0'])
    if out:
        click.echo(click.style('Found node and npm', fg='green'))
    else:
        click.echo(click.style('Missing node and npm installation', fg='red'))
    return out


@click.command()
def install_vue_cli():
    """
    Install vue-cli
    """
    out = check_output(['vue -V'.split()])
    if out >= '2.0.0.':
        click.echo(click.style('Found valid vue-cli', fg='green'))
    else:
        run(['npm install -g vue-cli'.split()])
        click.echo(click.style('Installed vue-cli globally', fg='green'))


@click.command()
@click.argument('project')
def startvueapp(project):
    run('vue init webpack {project}'.format(project=project).split())
    with cd(project):
        run(['npm install'.split()])


@click.command()
def vuedev():
    run(['npm run dev'.split()])
