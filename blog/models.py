from django.db import models
from wagtail.models import Page

from wagtail.admin.panels import FieldPanel

from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

# Create your models here.
class BlogIndexPage(Page):
    max_count = 1
    subpage_types = ['blog.BlogPage']
    parent_page_types = ['home.HomePage']

    #title - comes with Page model
    summary = models.TextField(blank=True, max_length=500)
    suscribe_url = models.URLField(blank=True)

    content_panels = Page.content_panels + [    
        FieldPanel('summary'),
        FieldPanel('suscribe_url'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        # context['posts'] = BlogPage.objects.live().public().order_by('-first_published_at')
        return context


class BlogPage(Page):
    parent_page_types = ['blog.BlogIndexPage']
    #subpage_types = [] # TODO

    # title - comes with Page model
    reading_time_in_minutes = models.IntegerField()
    # date - comes with Page model
    # generate in atlas app under templates new sub-directory blocks/ for StreamField .html templates
    body = StreamField([
        ('content', blocks.RichTextBlock(
            features=['bold', 'italic', 'link', 'ol', 'ul', 'hr'],
            template='blocks/richtext.html'
        )),
        ('image', ImageChooserBlock(
            template='blocks/image.html'
        )),
        ('quote', blocks.BlockQuoteBlock(
            template='blocks/quote.html'
        )),
        ('twitter_block', blocks.StructBlock([
            ('text', blocks.CharBlock()),
            ('author', blocks.CharBlock()),
        ], template='blocks/twitter_block.html')),
    ])


    content_panels = Page.content_panels + [    
        FieldPanel('reading_time_in_minutes'),
        FieldPanel('body'),
    ]
