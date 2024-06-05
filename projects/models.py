from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


# Create your models here.
class ProjectPage(Page):
    parent_page_types = ["projects.ProjectIndexPage"]
    # subpage_types = [] # TODO

    # title - comes with Page model
    summary = models.TextField(blank=True, max_length=500)

    # use custom .html templates under atlas/templates/blocks/ for StreamField blocks
    body = StreamField([
        ("content", blocks.RichTextBlock(
            features=["bold", "italic", "link", "ol", "ul", "hr"],
            template="blocks/richtext.html")),
        ("image", ImageChooserBlock(
            template="blocks/image.html")),
    ])

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        FieldPanel("body"),
    ]


class ProjectIndexPage(Page):
    max_count = 1
    subpage_types = ["projects.ProjectPage"]
    parent_page_types = ["home.HomePage"]

    # title - comes with Page model
    # date - comes with Page model
    summary = models.TextField(blank=True, max_length=500)

    def get_context(self, request):
        context = super().get_context(request)
        # get all project pages posts
        projects = ProjectPage.objects.live().public().order_by("title")
        # get page from url or default to id=1
        page = request.GET.get('page', 1)
        # tell paginator how many projects allowed per page
        paginator = Paginator(projects, 2)  # TODO: change to higher number
        # paginate projects object
        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            projects = paginator.page(1)
        except EmptyPage:
            projects = paginator.page(paginator.num_pages)
        # add paginated projects to context
        context["projects"] = projects
        return context

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
    ]
