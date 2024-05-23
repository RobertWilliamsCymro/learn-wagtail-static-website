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

- [Lesson 1 install wagtail with virtual environment](#1-install-wagtail-and-create-app_name)
- Lesson 2 n/a
- [Lesson 3 Set up `base.hmtl` template](#3-setting-up-base-project-pages-for-app-atlas)
- [Lesson 4 Global template tags for navigation, social media etc](#4-set-up-global-navigation-component-using-templatetag)
- [Lesson 5 a new global model class is created in site_settings app](#5-set-up-global-social-media-links)
- [Lesson 6 is about manipulating Settings to add global info](#6-custom-logo-and-website-name)
- [Lesson 7 is converting the Home Page hero to serve wagtail content](#7-converting-homepage-hero-to-serve-wagtail-content)
- [Lesson 8 is converting the Home Page body to serve wagtail content](#8-converting-homepage-body-to-serve-wagtail-content)
- [Lesson 9 is](#9-start-a-companion-blog-app)
- [Lesson 10 is](#10-child-pages-and-streamfield-intro)
- [Lesson 11 is](#11-more-wagtail-streamfields)



#### 1. Install Wagtail and create 'atlas' app
  - Create project directory repo in GitHub and `git clone` project to local drive
  - Set project python version in project root directory using `pyenv local <python version>`
  - Create virtual environment for project to install python dependencies in this root folder only using `pyenv activate <name of environment>`
  - Make sure virtual environment is active and run `pip install wagtail` to set up wagtail in this root directory
  - To create an app 
    - run `wagtail start atlas .`
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
    - Go to `localhost:<port>` on your web browser and type user and password to access admin UI
  - Create a `.gitignore` file and copy contents of `.dockerignore` file into it
  - remove `static` folder from `.gitignore` 
  - add your virtual environment name to `gitignore` file

[return to top](#course)
#### 2. Visualise project
  - create a tree hierarchy for where each webpage will exist under Home page
#### 3. Setting up base project pages for app atlas
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
          - `static` loads static files
          - `wagtailcore_tags` loads library of `templatetags` 
          - `wagtailuserbar` loads tool for quick access to wagatil admin interface from site frontend
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
[return to top](#course)
#### 4. Set up Global navigation component using Templatetag
  - want this on every page
  - In `app_name/templates` folder create
    - sub-folder `common`
      - create a  new file `navigation.html`
      - at top of `navigation.html` make sure to add `{% load static %}` for referencing any images or css from `app_name/static` directory in navigation html code
    - make sure`app_name/templates/base.html` file has within the `<body>` element
      - a wrapper for `{% block navigation %} ... {% endblock navigation %}`
      - and inject into it `{% include 'common/navigation.html%}` to receive the navigation html code on the base page
        - *to over-write `navigation` on `base.html` simply add an empty `{% block navigation %} {% endblock navigation %}` wrapper on the `home/templates/home_page.html`*
  - In `home` app
    - create a new directory `home/templatetags`
    - inside create new files
      - `__init__.py`
      - `navbar_tags.py`
        - using standard `django` functions add
          ``` from django import template
              from wagtail.models import Page

              register = template.Library()

              @register.simple_tag
              def get_navbar_pages():
                  return Page.objects.live().public().in_menu().filter(depth_gt=2)      ```
    - now at the top of `app_name/templates/common/navigation.html` in the `{% load ... %}` block
      - add file reference `navbar_tags` after `static` 
    - immediately below `{% load ... %}` block call in the simple_tag function
      - `{% get_navbar_pages as navbar %}`
      - create a list of navbar link items in html code and inject `{% for loop %}` to return all navbar list items as part of `navigation.html`
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

[return to top](#course)
#### 5. Set up Global social media links
  - want these on every page, in footer
  - In `app_name/templates/common` folder
    - create a  new file `social_media.html`
      - at top of `social_media.html` make sure to add `{% load static %}` for referencing any images or css from `app_name/static` directory in social media html code
      - wrap each social media html code link inside wagtail if statement `{% if settings.site_settings.SocialMediaLinks.<icon> %} ... {% endif %}`
    - make sure`app_name/templates/base.html` file has within the `<body>` element
      - a wrapper for `{% block social_media %} ... {% endblock social_media %}`
      - and inject into it `{% include 'common/social_media.html%}` to receive the footer html code on the base page
  - Now we will create a new functional app called `site_settings` for `app_name` to use for social media and other settings
    - in terminal run `python manage.py startapp site_settings`
      - a new folder appears alongside
        - `app_name` (original app)
        - `home`     (default app) 
        - `search`   (default app)
        - `site_settings` (new app *)
      - add `site_settings` to `INSTALLED_APPS` array  in `app_name/settings/base.py` file to include the functionality in `app_name`
      - add `wagtail.contrib.settings` to `INSTALLED_APPS` array as this is not installed by default and it will be needed
    - in `site_settings/models.py` file add
      - new model class
        - call class `SocialMediaLinks` which uses `(BaseGenericSetting)`
        - add `@register_settings` decorator to class `SocialMediaLinks` to allow wagtail to access the class as a setting
        - add URL fields for social media links
          - `twitter = models.URLField(blank=True, null=True)`
          - `facebook = models.URLField(blank=True, null=True)`
          - `linkedin = models.URLField(blank=True, null=True)`
        - add panels to show fields in wagtail UI
          - ```
            panels = [
              FieldPanel("twitter"),
              FieldPanel("facebook),
              ...
            ] 

      - to see the Social Media Links in the frontend you need to go to the `app_name/settings/base.py` file and add `wagtail.contrib.settings.context_processors.settings` to the `TEMPLATES` array object as this is not installed by default
        ```        
        TEMPLATES = [
          {
            ....
            "OPTIONS": {
                "context_processors": [
                    ...
                    "wagtail.contrib.settings.context_processors.settings",
                ],
              }
          }
        ]

    - need to run `python manage.py makemigrations` to include new `SocialMediaLinks` model in database
    - then run `python manage.py migrate` to apply `site_settings` model
    - then run `python manage.py runserver 0.0.0.0:<port>` to refresh frontend wagtail UI with new model settings
    - this adds the Social Media links as a class under the wagtail admin UI settings menu
      - in the `settings/Social media links` wgatail UI
        - add urls to the social media fields and save
      - check links are working on basepage `localhost:<port>`

[return to top](#course)
#### 6. Custom Logo and Website name
  - Want to apply a logo across all webpages in both the header (same level as navigation) and the footer (same level as social media)
  - Want to make it available under the `Settings` menu option in the wagtail admin UI
  - In `site_settings` app `models.py` under `social media` class add a new class
    - `class LogoSettings(BaseGenericSetting):`
    - add `logo` field as `models.ForeignKey("wagtailimages.Image", null=True, blank=True ...)`
    - add `panels` for wagtail admin as `FieldPanel("logo"),`
    - add decorator above class as `@register_setting` for wagtail admin UI to pick up
    - run `python manage.py makemigrations` and `python manage.py migrate` to add `LogoSettings` class to database
  - In `app_name/templates/common/navigation.html` add wagtail code injection to display `logo` on same level as `navigation` links 
    - add in `{% load static ... %}` the import `wagtailimages_tags`
    - add in wagtail injection of the logo to the html code
      ``` 
      <div class="mr-auto flex flex-col items-center sm:flex-row">
        <a href="/" class="mr-auto sm:mr-6">
            {% image settings.site_settings.LogoSettings.logo max-48x40 %}
        </a>
      </div>
    - wagtail injection code means
      - *{# from image directory, settings -> app_name - > model name -> field name set max logo size 48x40 #}*
  - In `app_name/templates/common/social_media.html` add wagtail code injection as above to display `logo` in footer on same level as `social media` icons
  - Want to set the Website name in the header next to the logo at `navigation` level
  - Want to edit the Wagtail admin UI to provide human readable site name
    - from `settings -> sites -> localhost -> Site name` add a human readable name for the site and save
  - In `navigation.html` 
    - add to `{% load static ... %}` the import `wagtailcore-tags`
    - below add `{% wagtail_site as current_site %}` template tag
    - in the Html code add `{{ current_site.site_name }}` wrapped in a `<p class="...."> ... </p>` after the logo
  - In `social_media.html`
    - repeat steps as above

[return to top](#course)
#### 7. Converting HomePage 'hero' to serve wagtail content
  - In app `home`, editing default `home_page` template and `models.py`
    - In `home/models.py`
      - in `HomePage(Page)` class
        - class already inherits `title` field from `Page` model
        - add `author_image` field as `models.ForeignKey(...)` and upload an image
        - add `summary` field as `models.TextField(...)`
        - add CTA button options (link to internal Page or external URL)
          - `cta_text` as `models.CharField(max_length=50, blank=True)`
          - `cta_page` as `models.ForeignKey("wagtailcore.Page", null=True, blank=True, ...)`
          - `cta_url` as `models.URLField(blank=True)`
          - add `@property` decorator and create function to choose from page or url
            - ```
              @property
              def cta_link(self):
                if self.cta_page:
                  return self.cta_page.url (built in Page object method)
                elif self.cta_url:
                  return self.cta_url (use external link)
                else:
                  return None (no internal page and no URL set)
        - add all fields to `content_panels` as `Page.content_panels + [FieldPanel("author_image"), FieldPanel("summary"), ....]` to be able to edit fields on Homepage in wagtail admin UI
        - go into `Home` page and add info to fields
          - change `title`
          - upload `author_image`
          - add `summary` info
          - add CTA info
            - add `cta_text`
    - In [`home/templates/home_page.html`](home/templates/home/home_page.html) 
      - within the `{% block content %} ... {% endblock content%}` wrapper set up your home page HTML code
        - in `{% load static ... %}` add `wagtailimages_tags` library
        - as `HomePage` model is by default available do not need to add as a template
        - inject as wagtail code
          - as `<div>` call in `author_image` as `{% image page.author_image fill-64x64 class="h-16 w-16" %}` with `fill` and class `h` and `w` to set image size boundaries
          - as `<h1>` call in `{{ page.title }}` field
          - as `<p>` call in `{{ page.summary}}` field
          - for CTA, check it exists with `{% if page.cta_link %}` references `@property` decorator in model
            - as `<a>` call in `{{ page.cta_link }}`
        - for CTA text check it exists with `{% if page.cta_text %}`
          - then call it in `{{ page.cta_text }}` 
            - provide default CTA button text `{% else %} Read More &gt;&gt; {% endif %}` in frontend `home_page.html` template
            - *OR* use `@property` decorator again in [`home/models.py`](home/models.py) to provide default string such as `Read More...` if `cta_text` field not filled in

[return to top](#course)
#### 8. Converting HomePage body to serve wagtail content
 - 

[return to top](#course)
#### 9. Start a companion blog app


[return to top](#course)
#### 10. Child pages and StreamField intro


[return to top](#course)
#### 11. More wagtail streamfields


[return to top](#course)

