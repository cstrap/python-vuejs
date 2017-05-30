# -*- coding: utf-8 -*-

import click

from .django import cli as djcli
from .vuejs import cli as vuecli


@click.group()
def cli():
    """
    Main cli: used to collect all the framework cli
    By convention all cli has a cli function with a pass statement
    """
    pass


cli = click.CommandCollection(sources=[cli, djcli, vuecli])


if __name__ == "__main__":
    cli()
