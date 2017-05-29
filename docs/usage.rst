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
    (env) $ pyvue djstartvueapp frontend
    ...

That's it. 

``frontend`` app is a vue project created via ``vue-cli`` behind the scene that is converted into a django app.

``djstartvueapp`` script adds the ``__init__.py`` and ``urls.py`` scritps, then it edits the vue-project build files in order to have the correct django-app directory structure.

Develop process
^^^^^^^^^^^^^^^

Working on ``frontend`` app::

    (env) $ cd frontend
    (env) $ npm run dev  # or pyvue vuedev

This is decupled from django, used only for develop.

Build process
^^^^^^^^^^^^^

The build process is::

    (env) $ cd frontend
    (env) $ npm run build  # or pyvue vuebuild
    (env) $ cd ..
    (env) $ ./manage.py collectstatic --noinput

You can add the "frontend" build to your pipeline (eg if you use fabric, ansible or others)

Refer to the `Vue.js https://vuejs.org/`_ documentation for other stuff not related to python-vuejs wrappers.

The cool thing is that you can detach ``frontend`` app and deploy it wherever you want. Also, you can move it into another repo. 🦄

Happy coding! 👑


