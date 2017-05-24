=====
Usage
=====

To use Python and Vue.js integration in a project::

    pip install python-vue 

.. _django_quickstart:

Django quickstart
-----------------

Assuming you work inside a virtualenv environment::

    (env) $ pip install django
    ...
    (env) $ pip install python-vuejs
    ...
    (env) $ django-admin startproject djvue
    ...
    (env) $ cd djvue
    (env) $ ./manage.py startapp backend
    ...
    (env) $ djstartvueapp frontend
    ...

That's it. 

``frontend`` app is a vue project created via ``vue-cli`` behind the scene that is converted into a django app.

``djstartvueapp`` script adds the ``__init__.py`` and ``urls.py`` scritps, then it edits the vue-project build files in order to have the correct django-app directory structure.

Develop process
^^^^^^^^^^^^^^^

Working on ``frontend`` app::

    (env) $ cd frontend
    (env) $ npm run dev  # or vuedev

This is decupled from django, used only for develop.

Build process
^^^^^^^^^^^^^

The build process is::

    (env) $ cd frontend
    (env) $ npm run build  # or vuebuild

``djstartvueapp`` added ``djvue`` command to the vue-project build that convert the ``index.html`` file into a django template (with ``loadstatic`` and ``static`` filter).

Refer to the `Vue.js https://vuejs.org/`_ documentation for other stuff not related to python-vuejs wrappers.

The cool thing is that you can detach ``frontend`` app and deploy it wherever you want. Also, you can move it into another repo. 🦄

Happy coding! 👑


