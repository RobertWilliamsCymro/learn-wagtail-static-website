## 14. Add pagination in wagtail
  - add pagination to the blog post pages
  - pagination comes with wagtail by default inside of `search/views.py`
  - in `blog/models.py`
      - from `search/views.py` copy the `paginator` block and it's `imports`
      - paste the `imports` at the top of the file 
      - paste the `paginator` block within the `BlogIndexPage` model 
        - inside the `def get_context(self, request):` function 
        - create varaiable `posts` equal to `BlogPage.objects.live()...`
        - create varaiable `page` and get the page id `page = request.GET.get('page', 1)`
        - edit the variable `paginator = Paginator(search_results, 10)`
          - change param from `search_results` to `posts`
          - choose the number of posts/page, search_results default is `10`
            - can set it to any number 
        - set `context['posts']` equal to `posts`
        - then `return context` 
  - in `blog/templates/blog/blog_index_page.html` - blog listing page
    - add check to see if posts/page more than 1 page `{% if posts.paginator.num_pages > 1 %}`
    - add for loop to get number of pages of blogs
      - `{% for page_num in posts.paginator.page_range %} ... {% endfor %}`
        Note: `page_num` & `page_range` default methods in paginator object
      - within it add `if` block to allow active/inactive styling on page_num
        `{% if posts.number == page_num %} ... {% else %} ...{% endif %}
    - add Previous and Next blocks either side of the page num_range
      `{% if posts.has_previous %} .. {% endif %}` & `{% if posts.has_next %} .. {% endif %}`

[return to README](README.md#course)