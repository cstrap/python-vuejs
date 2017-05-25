# -*- coding: utf-8 -*-

import click

from .django import djcli
from .vuejs import vuecli


@click.group()
def cli():
    """
    Main cli: used to collect all the framework cli
    """
    pass


cli = click.CommandCollection(sources=[cli, djcli, vuecli])


if __name__ == "__main__":
    cli()
