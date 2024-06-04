## 17. Clean up wagtail website codebase
  - Learn which files can be deleted safely
  - in companion apps such as `blog`, `site_settings`, `contact`, `misc` etc
    - not using `admin.py`, `views.py` or `tests.py` so could be deleted
  - in `home` can delete `welcome_page.html` and `static/welcome_page.css`
  - not using `search` app so can delete whole folder BUT
    - remember to also delete `"search"` app from `INSTALLED_APPS` array in `atlas/settings`
    - remeber to edit the `atlas/urls.py` file to remove reference to `search` in `urlpatterns` array

[return to README](README.md#course)