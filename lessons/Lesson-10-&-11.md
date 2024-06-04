## 10. Child pages and StreamField intro
  - In `blog/models.py`
    - create a child page from `BlogIndexPage`
    - create new class `BlogPage`which inherits `Page`
    - add the following fields
      - `parent_page_type` which is `BlogIndexPage`
      - `reading_time_in_minutes = models.IntegerField()`
      - `body` which has a `StreamField()` type
        - `StreamField` is a customisable mix 'n' match of different types of content fields
        - StreamField content type `template`s can be accessed outside of just the `BlogPage` model by placing template html code in `atlas/templates/` in a new `blocks/` subfolder 
        - content types within `StreamField([ content types here ])`
          - `('content', blocks.RichTextBlock())`params available include
            - `features` to set [`bold`, `italic`, `link`, `ol`, `ul`, ...]
            - `template='blocks/richtext.html'` source of html code for `content` block type
          - `('image', ImageChooserBlock(...))` params include `(template='blocks/image.html)` 
          - `('quote', BlockQuoteBlock(...))` params include `(template='blocks/quote.html)`
          - `('twitter_block', blocks.StructBlock([...], template... ))`
            - a `StructBlock` is an array of other field types
              - params example `[('text', blocks.CharBlock()), ('author', blocks.CharBlock()),],`
            - also need to include a `template='blocks/twitter_block.html` source of html code
      - add the fields to the content_panels to see in Wagtail admin UI
  - to add the model changes to the database, in terminal run
    - `python manage.py make migrations`
    - `python manage.py migrate` 
  - in `blog/templates/blog/` create a new `blog_page.html` file
    - open `blog_page.html` and 
      - at the top put `{% extends base.html %}` to pick up all the settings from `atlas/templates/base_html` app
      - below that put `{% load static %}` to give access to any images in static folder
      - add a `{% block content %} ... {% endblock content %}` wrapper and copy/paste the static `.html` code into it
      - edit the static html code to replace hard coded text with wagtail fields


## 11. Continue to build wagtail StreamField template
  - use StreamField to add dynamic mix 'n' match content in your page body
    - for the StreamField content add wrapper
    - `{% include_block page.body %}`
      - in `atlas/templates/blocks` create `.html` block component template files eg `richtext.html`, `image.html` etc
      - add any specific html and tailwind code to that component and inject wagtail code `{{ self }}` to use data from StreamField block type

[return to README](../README.md#course)