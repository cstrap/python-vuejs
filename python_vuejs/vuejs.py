# -*- coding: utf-8 -*-

import click
from .utils import cd

try:
    from subprocess import call as run
except ImportError:
    from subprocess import run

from subprocess import check_output


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
        if VueJs.vue_cli_check():
            VueJs.project_setup(project)
            click.echo(click.style('Installing dependencies\n', fg='green'))
            VueJs.install_dependencies(project)
            return True
        else:
            click.echo(click.style('Please install vue-cli via `vuecli` command', fg='white', bg='red'))
            return False


@click.command()
def check_env():
    """
    Check if node > 5 and npm > 3 are installed
    """
    if VueJs.node_check():
        click.echo(click.style('Found node and npm', fg='green'))
    else:
        click.echo(click.style('Missing node and npm installation', fg='red'))


@click.command()
def install_vue_cli():
    """
    Install vue-cli
    """
    if VueJs.vue_cli_check():
        click.echo(click.style('Found valid vue-cli', fg='green'))
    else:
        VueJs.install_cli()
        click.echo(click.style('Installed vue-cli globally', fg='green'))


@click.command()
@click.argument('project')
def startvueapp(project):
    """
    Init vue project via vue-cli
    """
    VueJsBuilder.startproject(project)


@click.command()
def vuedev():
    """
    Run frontend dev server via npm
    """
    VueJs.dev()


@click.command()
def vuebuild():
    """
    Build Vue.js project via npm
    """
    VueJs.build()
