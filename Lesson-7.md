## 7. Converting HomePage 'hero' to serve wagtail content
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
        - add all fields to `content_panels` as `Page.content_panels + [FieldPanel("author_image"), FieldPanel("summary"), ....]` to edit in wagtail admin UI
      - to add the model changes to the database run
        - `python manage.py make migrations`
        - `python manage.py migrate`
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
            - wrap in default CTA button text `{% else %} Read More &gt;&gt; {% endif %}` in frontend [`home_page.html`](home/templates/home/home_page.html) template
            - *OR* use `@property` decorator again  to provide default string such as `Read More...` if `cta_text` field not filled in for [`home/models.py`](home/models.py)

[return to README](README.md#course)