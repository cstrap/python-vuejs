# -*- coding: utf-8 -*-

import contextlib
import os


@contextlib.contextmanager
def cd(path):
    """
    A context manager which changes the working directory to the given
    path, and then changes it back to its previous value on exit.
    """
    prev_cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(prev_cwd)


def touch(filename, extrapath=''):
    """
    Like `touch` *nix command
    """
    open(os.path.join(extrapath, filename), 'a').close()
