# python-vuejs

Gluing Python web frameworks and Vue.js with a set of scripts... basically a wrapper :smile:

Work in progress, maybe it could be a bad idea :unicorn:

Projects aims to be agnostic, just use it in order to automate the boring stuff to setup a Vue.js project.

The point is that you start with SPA app inside your current project and then, extract it without having the dependency with backend framework. 

Feel free to contribute with PRs and opening issues.

Thanks!
Cheers! 🍻

## Requirements

- Python 2.7+ or 3.4+
- nodejs > 5 and npm > 3

## Commands list

### Vue.js

| Command     | Description                                 |
|-------------|---------------------------------------------|
| checkenv    | Check if node > 5 and npm > 3 are installed |
| vuecli      | Install vue-cli                             |
| startvueapp | Init Vue.js project via vue-cli             |
| vuedev      | Start frontend dev server                   |
| vuebuild    | Build Vue.js project via npm                |

### Django

| Command     | Description                                  |
|-------------|----------------------------------------------|
| djvue       | Make Vue.js project into a django app        |
| djbuild     | Inject into the django way into `index.html` |

### Flask

* TODO

| Command     | Description                                  |
|-------------|----------------------------------------------|