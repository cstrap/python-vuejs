=============================
Python and Vue.js integration
=============================


.. image:: https://img.shields.io/pypi/v/python_vuejs.svg
        :target: https://pypi.python.org/pypi/python_vuejs

.. image:: https://img.shields.io/travis/cstrap/python_vuejs.svg
        :target: https://travis-ci.org/cstrap/python_vuejs

.. image:: https://readthedocs.org/projects/python-vuejs/badge/?version=latest
        :target: https://python-vuejs.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/cstrap/python_vuejs/shield.svg
     :target: https://pyup.io/repos/github/cstrap/python_vuejs/
     :alt: Updates


Gluing Python and Vue.js with a set of scripts


* Free software: MIT license
* Documentation: https://python-vuejs.readthedocs.io.

==================
Commands reference
==================

Vue.js
------

===========  ============================================
Command      Descriptio
===========  =========================================== 
checkenv     Check if node > 5 and npm > 3 are installed
vuecli       Install vue-cli                            
startvueapp  Init Vue.js project via vue-cli            
vuedev       Start frontend dev server                  
vuebuild     Build Vue.js project via npm                

Django
------

=======  ============================================
Command  Description                                
=======  ============================================
djvue    Make Vue.js project into a django app      
djbuild  Inject into the django way into `index.html`

Flask
-----

* TODO

=======  ============================================
Command  Description                                
=======  ============================================

Features
--------

* Vue.js starter via vue-cli
* Basic integration with django 

TODO
----

* Supporting flask, eg https://github.com/taogeT/flask-vue (without js inside package)
* Supporting other frameworks
* Some tests 

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

