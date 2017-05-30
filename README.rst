======================
Python and Vue.js gule
======================

.. image:: https://img.shields.io/pypi/v/python_vuejs.svg
    :target: https://pypi.python.org/pypi/python_vuejs
.. image:: https://pyup.io/repos/github/cstrap/python-vuejs/shield.svg
    :target: https://pyup.io/repos/github/cstrap/python-vuejs/
    :alt: Updates
.. image:: https://pyup.io/repos/github/cstrap/python-vuejs/python-3-shield.svg
    :target: https://pyup.io/repos/github/cstrap/python-vuejs/
    :alt: Python 3
.. image:: https://img.shields.io/pypi/l/python_vuejs.svg
    :target: https://pypi.python.org/pypi/python_vuejs
.. image:: https://travis-ci.org/cstrap/python-vuejs.svg?branch=master
    :target: https://travis-ci.org/cstrap/python-vuejs
.. image:: https://coveralls.io/repos/github/cstrap/python-vuejs/badge.svg?branch=master
    :target: https://coveralls.io/github/cstrap/python-vuejs?branch=master
.. image:: https://readthedocs.org/projects/python-vuejs/badge/?version=latest
    :target: http://python-vuejs.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Gluing Python and `Vue.js <https://vuejs.org/>`_ with a set of scripts that automate the dev and build process.

Projects aims to be agnostic, just use it in order to automate the boring stuff to setup a Vue.js project.

The point is: you start with SPA app inside your current project and then extract it without having the dependency 
with backend framework, simply changing the ``npm`` build scripts.

Feel free to contribute with PRs and opening issues.

Thanks!
Cheers! 🍻

* Free software: MIT license
* Documentation: https://python-vuejs.rtfd.io

------------
Requirements
------------

* Python 2.7+ or 3.4+
* nodejs > 5 and npm > 3

------------------
Commands reference
------------------

``python-vuejs`` is shipped with a nice cli built on top of click.::

    (env) $ pyvue --help
    Usage: pyvue [OPTIONS] COMMAND [ARGS]...

    Options:
    --help  Show this message and exit.

    Commands:
    djangofy       Convert Vue.js webpack project into a django...
    djbuild        Called inside `package.json`
    djstartvueapp  Run click commands on bash.
    installvuecli  Install vue-cli
    startvueapp    Init vue project via vue-cli
    vuebuild       Build Vue.js project via npm
    vuecheck       Check if node > 5 and npm > 3 are installed
    vuedev         Run frontend dev server via npm

------------
Installation
------------

To install python-vuejs, simply:::

    $ pip install python-vuejs

Vue.js - A quick overview
-------------------------

Wrappers around ``npm`` and ``vue``.
These commands automate the boring stuff of setup vue via vue-cli:::

    $ pyvue startvueapp myapp
    $ cd myapp
    $ pyvue vuedev 
    ...

Before you go on production run:::

    $ cd myapp 
    $ pyvue vuebuild
    ...


Django - A quick overview
-------------------------

Run ``pyvue djstartvueapp`` into your django project directory::

    (env) $ pyvue djstartvueapp myapp
    ...
    Enjoy!

Command installs all dependencies and make the ``myapp`` a django app.

--------
Features
--------

* Vue.js starter via vue-cli
* Django integrations with no dependencies
* Detach backend and frontend with less effort

TODO
----

* Supporting Flask, eg https://github.com/taogeT/flask-vue (without js inside package)
* Supporting other frameworks

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

