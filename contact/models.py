from dataclasses import field
from django.db import models
from django import forms

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey

# Create your models here.
class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class ContactPage(AbstractEmailForm):
    template = "contact/contact_page.html"
    subpage_types = []
    parent_page_types = ["home.HomePage"]
    max_count = 1

    subtitle = models.CharField(max_length=255, blank=True)
    thank_you_text = models.TextField(
        blank=True,
        help_text="Text displayed on successful form submission",
    )

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("subtitle"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("from_address"),
                FieldPanel("to_address"),
            ]),
            FieldPanel("subject"),
        ])
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == "email":
            return db_field.formfield(widget=forms.EmailInput(
                    attrs={
                        "class": "w-full border border-primary bg-grey-lightest px-5 py-4 font-body font-light text-primary placeholder-primary transition-colors focus:border-secondary focus:outline-none focus:ring-2 focus:ring-secondary dark:text-white",
                        "placeholder": "Drop that email here…",
                        "id": "email",
                    }
                )
            )
        if db_field.name == "text":
            return db_field.formfield(widget=forms.TextInput(
                    attrs={
                        "class": "w-full border border-primary bg-grey-lightest px-5 py-4 font-body font-light text-primary placeholder-primary transition-colors focus:border-secondary focus:outline-none focus:ring-2 focus:ring-secondary dark:text-white",
                        "placeholder": "What should I call you?",
                        "id": "text",
                    }
                )
            )
        if db_field.name == "message":
            return db_field.formfield(widget=forms.Textarea(
                    attrs={
                        "class": "w-full border border-primary bg-grey-lightest px-5 py-4 font-body font-light text-primary placeholder-primary transition-colors focus:border-secondary focus:outline-none focus:ring-2 focus:ring-secondary dark:text-white",
                        "placeholder": "Tell me all the things that you think I need to hear…",
                        "id": "textarea",
                    }
                )
            )
        return field

    @property
    def form_fields_template(self):
        templates = []
        for field in self.form_fields.all():
            if field.field_type == "text":
                templates.append("form_fields/single_line_text.html")
            elif field.field_type == "email":
                templates.append("form_fields/email.html")
            elif field.field_type == "textarea":
                templates.append("form_fields/multi_line_text.html")
        return templates

    def get_context(self, request):
        context = super().get_context(request)
        context["form"] = self.get_form(request)
        context["field_templates"] = self.form_fields_template
        return context
