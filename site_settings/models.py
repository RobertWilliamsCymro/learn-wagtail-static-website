from django.db import models

from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.admin.panels import FieldPanel

# Create your models here.
@register_setting
class SocialMediaLinks(BaseGenericSetting):
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    panels = [
        FieldPanel("twitter"),
        FieldPanel("facebook"),
        FieldPanel("linkedin"),
    ]