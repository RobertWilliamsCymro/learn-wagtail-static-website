## 16. Wagtail contact pages (with email)
  - add a Contact Page that has a form to send emails when filled out
  - create a new wagtail app called `contact` using `python manage.py startapp contact`
  - add `contact` to `INSTALLED_APPS` array in `atlas/settings/base.py`
  - open `contact/models.py` file 
    -  create a `FormField()` class using `AbstractFormField` instead of `Page`
        - add `page=ParentalKey("ContactPage", on_delete=models.CASCADE, related_name="form_fields",)`
    -  create a `ContactPage()` class using `AbstractEmailForm` instead of `Page`
        - add `template = "contact/contact_page.html"`
        - `title` comes with AbstractEmailForm model
        - add `subpage_types = []` as there will be no child pages
        - add `parent_page_types = ['home.HomePage']` 
        - add `max_count = 1` as only one contact page
        - add `subtitle = models.CharField(max_length=255, blank=True)`
        - add `thank_you_text = models.TextField(blank=True, help_text="Thank you for your feedback")`
        - add `content_panels = AbstractEmailForm.content_panels + []` to include
        - `FieldPanel("subtitle"),`
        - `InlinePanel("form_fields", label="Form fields"),`
        - `FieldPanel("thank_you_text"),`
        - ```
          MultiFieldPanel([
            FieldRowPanel([
              FieldPanel("from_address"),
              FieldPanel("to_address"),
            ]),
            FieldPanel("subject"),
          ])
        - `form_fields, from_address, to_address, subject` come from `FormField` class

  - in `contact` folder open a new file `templates/contact/contact_page.html`
    - add usual template fields
      - `{% extends "base.html" %}`
      - `{% load static wagtailcore_tags %}`
      - `{% block content %} ... {% endblock %}`
      - inside put static html code
      - edit hard code
        - for img `src={% static 'img/icon_contact.png' %}`
        - for h1 `{{ page.title }}`
        - for p `{{ page.subtitle }}`
        - for form
          - add `action="{% pageurl page %}"` and `method="POST"`
          - add `{% csrf_token %}` for django to prove input comes from form page
          - loop through fields in form
            ```
            {% for field in form %}
              <label>
                {{ field.label_tag }}
              </label>
              {{ field }}
            {% endfor %}
          - set button to `type="submit"`
  - need to create a companion page `templates/contact/contact_page_landing.html` for form to return once submit button activated
    - copy in usual `{% %}` template fields
    - copy the img `src="{% static 'img/...' %}"` and h1 `{{ page.title }}` fields
    - add `{{ page.thank_you_text }}`

  - look at adding pypi packages for more control
    - [widgettweaks](https://pypi.org/project/django-widget-tweaks/)
    - [django-extensions](https://pypi.org/project/django-extensions/)

[return to README](README.md#course)