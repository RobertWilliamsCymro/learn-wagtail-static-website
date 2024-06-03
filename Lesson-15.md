## 15. Add a miscellaneous page type
  - add a miscellaneous page for a wide range of uses
  - create a new wagtail app called `misc` using `python manage.py startapp misc`
  - add `misc` to `INSTALLED_APPS` array in `atlas/settings/base.py`
  - open `misc/models.py` file and create a `MiscPage(Page)` class
    - `title` comes with Page model
    - `date` comes with Page model
    - add `html_subtitle` field as `models.TextField(max_length=2000, blank=True, help_text="Optional, can add raw HTML here")`
    - add `body` as `StreamField([ ... ])` include
      - ```
        ('content', blocks.RichTextBlock(
          features=['bold', 'italic', 'ol', 'ul', 'h3', 'link'],
          template='blocks/richtext.html')
        ),
      - `('image', ImageChooserBlock(template='blocks/image.html')),`
    - add 
    ```
      content_panels = Page.content_panels + [
        FieldPanel('html_subtitle'),
        FieldPanel('body'),
      ]
    ```

  - create ` misc/templates/misc/` folder and add `misc_page.html` file
    - `{% extends 'base.html'%}`
    - `{% load static wagtailcore_tags %}`
    - `{% block content} ... {% endblock %}`
      - within add
      - `src="{% static 'img/icon-uses.png' %}"`
      - `{{ page.title }}`
      - `{{ page.html_subtitle|safe }}`
      - `{% include_block page.body %}`

[return to README](README.md#course)