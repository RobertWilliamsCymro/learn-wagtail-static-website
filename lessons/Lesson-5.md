## 5. Set up Global social media links
  - want these on every page, in footer
  - In `app_name/templates/common` folder
    - create a  new file `social_media.html`
      - at top of `social_media.html` make sure to add `{% load static %}` for referencing any images or css from `app_name/static` directory in social media html code
      - wrap each social media html code link inside wagtail if statement `{% if settings.site_settings.SocialMediaLinks.<icon> %} ... {% endif %}`
    - make sure`app_name/templates/base.html` file has within the `<body>` element
      - a wrapper for `{% block social_media %} ... {% endblock social_media %}`
      - and inject into it `{% include 'common/social_media.html%}` to receive the footer html code on the base page
      
  - Now we will create a new functional app called `site_settings` for `app_name` to use for social media and other settings
    - in terminal run `python manage.py startapp site_settings`
      - a new folder appears alongside
        - `app_name` (original app)
        - `home`     (default app) 
        - `search`   (default app)
        - `site_settings` (new app *)
      - add `site_settings` to `INSTALLED_APPS` array  in `app_name/settings/base.py` file to include the functionality in `app_name`
      - add `wagtail.contrib.settings` to `INSTALLED_APPS` array as this is not installed by default and it will be needed
    - in `site_settings/models.py` file add
      - new model class
        - call class `SocialMediaLinks` which uses `(BaseGenericSetting)`
        - add `@register_settings` decorator to class `SocialMediaLinks` to allow wagtail to access the class as a setting
        - add URL fields for social media links
          - `twitter = models.URLField(blank=True, null=True)`
          - `facebook = models.URLField(blank=True, null=True)`
          - `linkedin = models.URLField(blank=True, null=True)`
        - add panels to show fields in wagtail UI
          - ```
            panels = [
              FieldPanel("twitter"),
              FieldPanel("facebook),
              ...
            ] 

      - to see the Social Media Links in the frontend you need to go to the `app_name/settings/base.py` file and add `wagtail.contrib.settings.context_processors.settings` to the `TEMPLATES` array object as this is not installed by default
        ```        
        TEMPLATES = [
          {
            ....
            "OPTIONS": {
                "context_processors": [
                    ...
                    "wagtail.contrib.settings.context_processors.settings",
                ],
              }
          }
        ]

    - need to run `python manage.py makemigrations` to include new `SocialMediaLinks` model in database
    - then run `python manage.py migrate` to apply `site_settings` model
    - then run `python manage.py runserver 0.0.0.0:<port>` to refresh frontend wagtail UI with new model settings
    - this adds the Social Media links as a class under the wagtail admin UI settings menu
      - in the `settings/Social media links` wgatail UI
        - add urls to the social media fields and save
      - check links are working on basepage `localhost:<port>`

[return to README](../README.md#course)