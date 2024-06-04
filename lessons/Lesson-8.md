## 8. Converting HomePage 'body' to serve wagtail content
  - In app `home`, continue editing default [`home/../home_page`](home/templates/home/home_page.html) template and [`home/models.py`](home/models.py)
    - In `home/models.py`
        - in `HomePage(Page)` class
            - add `my_story_title` field as `models.CharField(...)`
            - add `my_story_content` field as `models.TextField(...)`
            *Note: you could use a `RichTextField` here if required*
            - add both to the `content_panels` as a `MultiFieldPanel` with `heading="My Story section"
        - to add the model changes to the database run
            - `python manage.py make migrations`
            - `python manage.py migrate`       
        - go into `Home` page and add info to fields
            - `my_story_title`
            - `my_story_content`
        - to allow blog posts to be pulled into `home_page`
            - add `def get_context(self,request):` function which collects info from `BlogPage` model
            - no need to run `makemigrations` and `migrate` as assumes `BlogPage` model exists
        - no model changes to HomePage needed for `My Projects` section as will link to `ProjectPage` model
    - In [`home/../home_page.html`](home/templates/home/home_page.html) 
        - within the `{% block content %} ... {% endblock content%}` wrapper add the HTML code for the `My Story` part of your webpage
            - edit any `img` tags to load from `{% static 'img/...' %}` directory
            - replace hard code
                - for title with `{{ page.my_story_title }}`
                - for content with `{{ page.my_story_content| linebreakers }}`
            - `|` is way for django to access filters
            - `linebreakers` tells it what filter to apply
        - within the `{% block content %} ... {% endblock content%}` wrapper below the `My Story` code add the HTML code for the `Blog Posts` part of your webpage
            - hard code `Blog Posts` and link to `All blog posts`
            - edit any `img` tags to load from `{% static 'img/...' %}` directory 
            - use `{% for post in blog_posts %} ... {% endfor %}` to iterate through the blog posts you want to display on homepage, set to last 3 posts in `def get_context(self, request):` function in `home/models.py`
            *Note: don't need to use `page` to collect `blog_posts` because `get_context` function overlays `HomePage` model and looks for content in `BlogPage` model*
        - within the `{% block content %} ... {% endblock content%}` wrapper below the `Blog Posts` code add the HTML code for the `My Project` part of your webpage
            - edit any `img` tags to load from `{% static 'img/...' %}` directory
            - links to `Project` pages will be update once they are built

[return to README](../README.md#course)