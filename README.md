## Learn Wagtail - Wagtailify your static website

by Kalob Taulien: https://learnwagtail.com/courses/wagtailify-your-static-website/

link to GitHub: https://github.com/CodingForEverybody/wagtailify-your-static-website

use PORT 8002 for `python manage.py runserver 0.0.0.0:8002` cmd for localhost instead of 8000 (avoid clashing with jisc-ac-uk setup)

### Customise python for this project
To use different versions of python in different projects use `pyenv` https://python.land/virtual-environments/pyenv
  - `su localadmin` then `brew install pyenv`
  - add pyenv to zsh shell
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOTbin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```
  - restart your shell using `exec "$SHELL"` cmd

To manage the python virtual environment add `pyenv-virtualenv` as a plugin to pyenv https://github.com/pyenv/pyenv-virtualenv?tab=readme-ov-file
  - `su localadmin` then `brew install pyenv-virtualenv`
  - add pyenv-virtualenv to zsh shell
```
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
```
  - restart your shell using `exec "$SHELL"` cmd

### Set-up
Set python preferred version in project root directory 
- add python version 3.11.4 using `pyenv install 3.11.4` cmd 
- set this project directory to use v3.10 with `pyenv local 3.11.4` cmd
Set up virtual environment in project root directory
- create vitual env using `pyenv virtualenv <venv_name>` cmd
- list all virtual envs with `pyenv virtualenvs` cmd
- start virtual env using `pyenv activate <venv_name>` cmd
- deactivate virtual env using `pyenv deactivate` cmd

### Course
#### 1. Install Wagtail Learnings
  - Create project directory repo in GitHub and `git clone` project to local drive
  - Set project python version in project root directory using `pyenv local <python version>`
  - Create virtual environment for project to install python dependencies in this root folder only using `pyenv activate <name>`
  - Make sure virtual environment is active and run `pip install wagtail` to set up wagtail in this root directory
  - To create an app run `wagtail start <app_name> .`
    - the `.` makes sure the app is created at the root level
    - `wagtail start ...` command generates standard directories `home` and `search`, a `Dockerfile`, a `requirements.txt` file and a `manage.py` file as well as your `app_name` directory
    - Run `pip install -r requirements.txt` just to confirm django & wagtail installed correctly
    - Start server by opening a terminal and run `python manage.py runserver 0.0.0.0:<port>` 
      - default port is `8000`, but if you have other apps using that choose another port e.g. `8001`, `8002` etc
      - You will have a number of unapplied migrations which will need to run to provision the database
    - Open a 2nd terminal and run `python manage.py migrate` to install all the migrations on the server
    - Run `python manage.py createsuperuser` to create a login user for wagtail admin UI
      - name
      - email (optional)
      - password (8 characters requested, can overide)
      - repeat password
    - Go to `localhost:<port>` on oyur web browser and type user and password to access admin UI
  - Create a `.gitignore` file and copy contents of `.dockerignore` file into it
  - remove `static` folder from `.gitignore` 
  - add your virtual environment name to `gitignore` file
#### 2. Visualise project
  - create a tree hierarchy for where each webpage will exist under Home page
#### 3. Setting up base project `app_name`
  - Inside default `home` app, there are pre-generated standard directories
    - migrations
    - static/css
      - `welcome_page.css`
    - templates/home
      - `home_page.html`
      - `welcome_page.html`
    - as well as standard files
      - `__init__.py`
      - `models.py`
  - In `home_page.html` (layer zero: 0) edit code to remove all the existing code except for:
    ```   
    {% extends "base.html" %}
    {% load static %}

    {% block content %}
      Hello World - temporary placeholder for homepage content
    {% endblock content %} 
    ```
    - this will allow the `app_name/templates/base.html` page to become the wagtail UI `home` page

  - Inside `app_name` folder will be pre-generated standard directories
  - `app_name`
    - `settings`
      - `__init.py__`
      - `base.py`
      - `dev.py`
      - `production.py`
    - `static`
      - `css`
        - `app_name.css` (empty file)
      - `js`
        - `app_name.js` (empty file)
    - `templates`
      - `404.html`
      - `500.html`
      - `base.html`
    - as well as files
      - `__init__.py`
      - `urls.py`
      - `wsgi.py`

  - File `templates/base.html` is the base layer (layer one: 1)page of each webpage and will be reference loading place for components needed on every page
    - It is a standard `<!DOCTYPE html>` template with wagtail injections
      - at the top
        - `{% load static wagtailcore_tags wagtailuserbar %}`
      - within the `<head>` element
        - as part of the `<title>` element
        - ```
          <head>
            ....
            <title>
              {% block title %}
                ....
              {% endblock %}
            </title>
            ....
          </head>
          ```      
      - within the link to `.css` stylesheets stored in `app_name/static` directory
        - `<link crossorigin="anonymous" href="{% static 'styles/main.css' %}" media="screen" rel="stylesheet"/>`
      - within the `<body>` element
        - insert `{% wagtailuserbar %}` at top
        - within the `<div id='main'>` container
          - insert wrapper blocks to represent reusable items such as `navigation` and `content`
          - within the `footer` link to any `images` loaded from the `static` directory, `img/img_name.svg` file
      - within the `<script>` element
        - reference in the `src` attribute by loading from `static` directory the `js/main.js` file
      - example
        ```
        <body>
          {% wagtailuserbar %}

          <div id='main'>
            <div class='container mx-auto'>

              {% block navigation %} 
                {% include 'common/navigation.html' %}
              {% endblock navigation %}
          
              {% block hero_content %}
                {% include 'common/hero.html' %}
              {% endblock hero_content %}

              {% block main_content %}
                {% include 'common/main.html' %}
              {% endblock main_content %}

            <!-- Footer -->
              <div>
                <a href="/" class="mr-auto sm:mr-6">
                  <img src="{% static 'img/logo.svg' %}" alt="logo" />
                  ...
                </a>
              </div>
            
            </div>
          </div>
          
          <script type='text/javascript' src="{% static 'js/main.js' %}"></script>

        </body>
        ```
#### 4. Set up Global navigation component using Templatetag
  - want this on every page
  - In `app_name/templates` folder create
    - sub-folder `common`
      - add new file `navigation.html`
      - at top of `navigation.html` make sure to add `{% load static %}` for referencing any images or css from `app_name/static` directory in navigation html code
    - make sure`templates/base.html` file has within the `<body>` element
      - a wrapper for `{% block navigation%} {% endblock navigation %}`
      - and inject into it `{% include 'common/navigation.html%}` to receive the navigation html code on the base page
        - *to over-write `navigation` on `base.html` simply add an empty `{% block navigation %} {% endblock navigation %}` wrapper on the `home/templates/home_page.html`*
  - In `home` app
    - create a new directory `home/templatetags` alongside `home/templates`
    - inside create new files
      - `__init__.py`
      - `navbar_tags.py`
        - using standard `django` functions
          ``` from django import template
              from wagtail.models import Page

              register = template.Library()

              @register.simple_tag
              def get_navbar_pages():
                  return Page.objects.live().public().in_menu().filter(depth_gt=2)      ```
       - now in the `{% load ... %}` block at the top of `app_name/templates/common/navgation.html`
    - add file reference `navbar_tags` after `static` 
    - immediately below it call in the simple_tag function
      - `{% get_navbar_pages as navbar %}`
      - create a list of navbar link items in html code and inject `{% for loop %}`to return all navbar list items 
      ```
      <div class="hidden lg:block">
        <ul class="flex items-center">
          {% for navbar_page in navbar_pages %}
            <li class="group relative mr-6 mb-1">
              <a href="{{ navbar_page.url }}"
                 class="px-2 font-body text-lg">
                {{ navbar_page.title }} 
              </a>
            </li>
          {% endfor %}
        </ul>
      </div>

    - *REMEMBER*: any changes to `template` folder you must re-run `python manage.py runserver 0.0.0.0:<port>` cmd in terminal to pick up frontend changes
#### 5. Set up Global social media links
  - want these on every page
  - 

