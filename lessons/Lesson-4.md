## 4. Set up Global navigation component using Templatetag
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

[return to README](../README.md#course)