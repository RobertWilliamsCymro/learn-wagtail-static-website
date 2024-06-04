## 9. Start a new internal wagtail app (e.g.blog)
  - create a new wagtail app called `blog` using `python manage.py startapp blog`
  - add `blog` to `INSTALLED_APPS` array in `atlas/settings/base.py`
  - open `blog/models.py` file and create a `BlogIndexPage(Page)` class
    - add fields for:
      - `max_count = 1` only ever one blog index page
      - `parent_page_types = ["home.HomePage"]` sits under home_page
      - `title` comes with `Page` class
      - `summary = models.TextField(blank=True, max_length=500)` to describe blog index page
      - `suscribe_url = models.URLField(bank=True)` to suscribe to blog 
      - create `content_panels = Page.content_panels + [
            FieldPanel("summary"),
            FieldPanel("suscribe_url"),
      ]` to show in wagtail admin UI
      - add `get_context` function to allow BlogPage models to display on the BlogIndexPage
        - `def get_context(self, request): ...`
        - will need to create `BlogPage` model to use

  - to add the model changes to the database, in terminal run
    - `python manage.py make migrations`
    - `python manage.py migrate` 
  - in `blog` folder create `templates/blog/` folder and create `blog_index_page.html` file to display frontend
  *Note: django needs the model `class` name to be similar to the `.html` file name e.g. `class BlogIndexPage()` -> `blog_index_page.html`*
  - open `blog_index_page.html` and 
    - at the top put `{% extends base.html %}` to pick up all the settings from `atlas/templates/base_html` app
    - below that put `{% load static %}` to give access to any images in static folder
    - add a `{% block content %} ... {% endblock content %}` wrapper and copy/paste the static `.html` code into it
    - edit the static html code to replace hard coded text with wagtail fields
      - replace `src` with `"{% static 'img/...' %}` location
      - replace `Blog` with `{{ page.title }}` imported from `BlogIndexPage` model
      - replace hard coded text with `{{ page.summary }}`
      - in `form` element
        - add in `<form .... method="POST" action="{{ page.suscribe_url }}">`
        - wrap `<form>` element in conditional if statement in case `suscribe_url` is blank so `{% if page.suscribe_url %} <form>...</form> {% endif %}`

  - to allow link to Blog Index page from HomePage to be made:
      - open `home/models.py` 
        - import the `BlogIndexPage` model to `HomePage` and add it to the `def get_context` function under `context = super().get_context(request)` as
          - `context['blog_index'] = BlogIndexPage.objects.first()` 
      - open `home_page.html` 
        - edit the `All posts` link to now target `{{ blog_index.url }}` don't need `page` as using `get_context` function to access `BlogIndexPage.url` where `url` is a default field available to `Page` model class similar to `title` field


[return to README](../README.md#course)