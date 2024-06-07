from django.shortcuts import render

from contact.models import ContactPage


# Create your views here.
def contact(request):
    form=ContactPage()
    field_templates = form.form_fields_template
    return render(
        request,
        "contact_page.html",
        {
            "form": form, 
            "field_templates": field_templates,
        },
    )
