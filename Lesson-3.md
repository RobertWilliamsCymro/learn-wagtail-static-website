## 3. Setting up base project pages for app atlas
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
[return to README.md](README.md#course)