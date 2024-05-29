from django.db import models
from wagtail.models import Page

from wagtail.admin.panels import FieldPanel


# Create your models here.
class BlogIndexPage(Page):
    max_count = 1
    #subpage_types = ['blog.BlogPage'] # TODO
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
