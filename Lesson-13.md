## 13. Reusing Template components in wagtail
  - reuse template components in your wagtail website
  - want to preview some blog posts both on blog index page and on homepage
  - in `blog/models.py`
    - add to the `get_context` function a `context['posts']` instruction which defines `BlogPage.objects.live().public().order_by('-first_published_at')`
  
  - in `home/models.py` 
    - add same to the `get_context` function a `context['blog_posts']` instruction

  - in `blog/templates/blog/blog_index_page.html`
    - add for loop `{% for post in posts %} .. {% endfor %}`
    - inject component using
      - `{% include 'common/blog_preview.html' with post=post %}`

  - in `home/templates/home/home_page.html`
    - add for loop `{% for post in blog_posts %} ... {% endfor %}`
    - inject component using
      - `{% include 'comon/blog_preview.html' with post=post %}`

  - in `atlas/templates/common/` 
    - create new template component called `blog_preview.html`
    - copy/paste html code with tailwind classes
      - replace hard coded text with wagtail fields
        - for multiple category labels read in orderables from categories using for loop
          - `{% for orderable in post.categories.all %}
              ... {{ orderable.category.color }} ... {{ orderable.category.text_color }}
              ... {{ orderable.category.name}} ... 
            {% endfor %}`
        - `{{ post.url }}`
        - `{{ post.title }}`
        - `{{ post.reading_time_in_minutes }}`

[return to README](README.md#course)