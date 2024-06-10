from django.shortcuts import render

from contact.models import ContactPage


# Create your views here.
def contact(request):
    form = ContactPage()
    return render(
        request,
        "contact_page.html",
        {
            "form": form, 
        },
    )
