from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel

# Create your models here.
class MiscPage(Page):
    # title - comes with Page model
    # date - comes with Page model
    # just to see a different way of doing this, could use RichTextField
    html_subtitle = models.TextField(
        max_length=2000, 
        blank=True, 
        help_text="Optional, this can include RAw HTML, Be careful!"
    )

    body = StreamField([
        ('content', blocks.RichTextBlock(
            features=['bold', 'italic', 'link', 'ol', 'ul', 'hr', 'h3'],
            template='blocks/richtext.html'
        )),
        ('image', ImageChooserBlock(
            template='blocks/image.html'
        )),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('html_subtitle'),
        FieldPanel('body'),
    ]