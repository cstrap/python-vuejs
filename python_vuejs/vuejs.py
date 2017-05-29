# -*- coding: utf-8 -*-

from collections import namedtuple
from subprocess import check_output

import click

from .utils import cd

try:
    from subprocess import call as run
except ImportError:
    from subprocess import run


class VueJs(object):
    """
    Provide subprocess call to `npm` and `vue-cli`
    """

    @staticmethod
    def node_check():
        """
        Node and npm version checker
        """
        node_ver = check_output('node -v'.split()).decode('utf-8').rsplit('.')[0]
        npm_ver = check_output('npm -v'.split()).decode('utf-8').rsplit('.')[0]
        return all([node_ver > 'v5', npm_ver >= '4'])

    @staticmethod
    def vue_cli_check():
        """
        vue-cli version checker
        """
        try:
            return check_output('vue -V'.split()).decode('utf-8').rsplit('.')[0]
        except OSError:
            return False

    @staticmethod
    def install_cli():
        run('npm install -g vue-cli'.split())

    @staticmethod
    def project_setup(project):
        run('vue init webpack {project}'.format(project=project).split())

    @staticmethod
    def install_dependencies(project):
        with cd(project):
            run('npm install'.split())

    @staticmethod
    def dev():
        run('npm run dev'.split())

    @staticmethod
    def build():
        run('npm run build'.split())


class VueJsBuilder(object):
    @staticmethod
    def startproject(project):
        nt = namedtuple('Result', ['status', 'message', 'color'])
        if VueJs.vue_cli_check():
            VueJs.project_setup(project)
            VueJs.install_dependencies(project)
            return nt(True, 'Application and dependencies installed\n', 'green')
        else:
            return nt(False, 'Please install vue-cli via `vuecli` command', 'red')


@click.group()
def vuecli():
    pass


@vuecli.command()
def vuecheck():
    """
    Check if node > 5 and npm > 3 are installed
    """
    if VueJs.node_check():
        click.echo(click.style('Found node and npm', fg='green'))
    else:
        click.echo(click.style('Missing node and npm installation', fg='red'))


@vuecli.command()
def installvuecli():
    """
    Install vue-cli
    """
    if VueJs.vue_cli_check():
        click.echo(click.style('Found valid vue-cli', fg='green'))
    else:
        VueJs.install_cli()
        click.echo(click.style('Installed vue-cli globally', fg='green'))


@vuecli.command()
@click.argument('project')
def startvueapp(project):
    """
    Init vue project via vue-cli
    """
    result = VueJsBuilder.startproject(project)
    click.echo(click.style(result.message, fg=result.color))


@vuecli.command()
def vuedev():
    """
    Run frontend dev server via npm
    """
    VueJs.dev()


@vuecli.command()
def vuebuild():
    """
    Build Vue.js project via npm
    """
    VueJs.build()
