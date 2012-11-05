from django.shortcuts import render
from ajaxsite.blog.forms import ContactForm

# Create your views here.
def contact_form(req):
    return render(req, "blog/contact_form.html", {'form':ContactForm()})
