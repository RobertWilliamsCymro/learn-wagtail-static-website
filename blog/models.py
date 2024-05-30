from django.db import models
from wagtail.models import Page, Orderable

from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey

# Create your models here.

# Snippet is a model that can be used to create a reusable piece of content
@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(choices=[
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('grey', 'Grey'),
    ], help_text='Background color', default='grey', max_length=6)

    @property
    def text_color(self):
        if self.color == 'grey':
            return 'blue-dark'
        elif self.color == 'yellow':
            return 'yellow-dark'
        return self.color
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'


# Orderable is a model that can be used to create a relationship between two models
class BlogPageCategory(Orderable):
    page = ParentalKey('blog.BlogPage', related_name='categories')
    category = models.ForeignKey(
        'blog.BlogCategory',
        on_delete=models.CASCADE)
    
    panels = [
        FieldPanel('category')
    ]


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
        InlinePanel('categories', label='Categories'),
        FieldPanel('reading_time_in_minutes'),
        FieldPanel('body'),
    ]


class BlogIndexPage(Page):
    max_count = 1
    subpage_types = ['blog.BlogPage']
    parent_page_types = ['home.HomePage']

    #title - comes with Page model
    summary = models.TextField(blank=True, max_length=500)
    suscribe_url = models.URLField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        # context['posts'] = BlogPage.objects.live().public().order_by('-first_published_at')
        return context
    
    content_panels = Page.content_panels + [    
        FieldPanel('summary'),
        FieldPanel('suscribe_url'),
    ]
