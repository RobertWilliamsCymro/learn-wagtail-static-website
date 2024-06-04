## 12. Wagtail snippets and repeating objects(Orderables)
  - Create a `category` label for the Blog posts
  - Snippet in wagtail is a reusable data object
  - Can select multiple items from a snippet by registering it in a wagtail page and creating an Orderable model

  - in `blog/models.py`
    - create new class `BlogCategory(models.Model)`
    - add decorator `@register_snippet`
     - add `name` field as a `models.CharField()`
     - add `color` field as a `models.CharField()` to set label background color give it params:
        - `choices` array eg. `[('blue', 'Blue'), ('yellow', 'Yellow'), ('green', 'Green'), etc ]`
        - set `help_text` as 'Background color`
        - set `default` as `'grey'`
        - set `max_length` to match longest `choices` string
      - link the desired `text_color` to the `color` field using `@property` decorator and a custom `if` function `def text_color(self):` to set desired `text_color` for each `color` choice 

    - create another new class `BlogPageCategory(Orderable)`
      - add `page` field and set a `ParentalKey()` with params
        - the linked class model
        - the related name to call in the content_panel
        - e.g `('blog.BlogPage', related_name='categories')`
      - add `category` field and set a `models.ForeignKey()` with params 
        - the linked snippet model
        - the behaviour on delete
        - e.g.`('blog.BlogCategory', on_delete=models.CASCADE)`
        - define `panels` as a `FieldPanel()`

  - in `BlogPage` class add categories to the `content_panels`
    - as an `InlinePanel()` with params 
      - `categories` as the related_name from the Orderable
      - `label` of `Categories` for the wagtail admin UI

    - in `blog/templates/blog/`
      - open `blog_page.html`
        - inject `for loop` of wagtail code to add all the category labels at the top of the  `{% block content %}`
          - e.g. `{% for orderable in page.categories.all %} ... {% endfor %}`
        - for loop iterates through every label to add background color, text color and name within html code for blog page
          - `{{ orderable.category.color }}`
          - `{{ orderable.category.text_color }}`
          - `{{ orderable.category.name }}` 


[return to README](../README.md#course)