# -*- coding: utf-8 -*-

import click
from subprocess import check_output
from .utils import cd

try:
    from subprocess import call as run
except ImportError:
    from subprocess import run


@click.command()
def check_env():
    """
    Check if node > 5 and npm > 3 are installed
    """
    node_ver = check_output('node -v'.split()).decode('utf-8').rsplit('.')[0]
    npm_ver = check_output('npm -v'.split()).decode('utf-8').rsplit('.')[0]
    out = all([node_ver > 'v5', npm_ver >= '4'])
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
    out = check_output(['vue -V'.split()]).decode('utf-8').rsplit('.')[0]
    if out >= '2':
        click.echo(click.style('Found valid vue-cli', fg='green'))
    else:
        run('npm install -g vue-cli'.split())
        click.echo(click.style('Installed vue-cli globally', fg='green'))


@click.command()
@click.argument('project')
def startvueapp(project):
    """
    Init vue project via vue-cli
    """
    run('vue init webpack {project}'.format(project=project).split())
    with cd(project):
        run('npm install'.split())


@click.command()
def vuedev():
    """
    Run frontend dev server via npm
    """
    run('npm run dev'.split())
