## 6. Custom Logo and Website name
  - following on from where we created a new wagtail app called `site_settings` using `python manage.py startapp site_settings` and added `site_settings` to `INSTALLED_APPS` array in `atlas/settings/base.py` ...

  - Want to apply a logo across all webpages in both the header (same level as navigation) and the footer (same level as social media)

  - Want to make it available under the `Settings` menu option in the wagtail admin UI
  - open `site_settings/models.py` file
  - under existing `SocialMedia` class add a new class
    - `class LogoSettings(BaseGenericSetting):`
    - add `logo` field as `models.ForeignKey("wagtailimages.Image", null=True, blank=True ...)`
    - add `panels` for wagtail admin as `FieldPanel("logo"),`
    - add decorator above class as `@register_setting` for wagtail admin UI to pick up
  - to add `LogoSettings` class to database run
    - `python manage.py makemigrations` then
    - `python manage.py migrate`

  - In `app_name/templates/common/navigation.html` add wagtail code injection to display `logo` on same level as `navigation` links 
    - add in `{% load static ... %}` the import `wagtailimages_tags`
    - add in wagtail injection of the logo to the html code
      ``` 
      <div class="mr-auto flex flex-col items-center sm:flex-row">
        <a href="/" class="mr-auto sm:mr-6">
            {% image settings.site_settings.LogoSettings.logo max-48x40 %}
        </a>
      </div>
    - wagtail injection code means
      - *{# from image directory, settings -> app_name - > model name -> field name set max logo size 48x40 #}*
      
  - In `app_name/templates/common/social_media.html` add wagtail code injection as above to display `logo` in footer on same level as `social media` icons
  - Want to set the Website name in the header next to the logo at `navigation` level
  - Want to edit the Wagtail admin UI to provide human readable site name
    - from `settings -> sites -> localhost -> Site name` add a human readable name for the site and save
  - In `navigation.html` 
    - add to `{% load static ... %}` the import `wagtailcore-tags`
    - below add `{% wagtail_site as current_site %}` template tag
    - in the Html code add `{{ current_site.site_name }}` wrapped in a `<p class="...."> ... </p>` after the logo
  - In `social_media.html`
    - repeat steps as above

[return to README](../README.md#course)