from django.shortcuts import render
from testDajaxice.forms import ContactForm

# Create your views here.
def contact_form(request):
    return render(request, "dajaxiceIndex.html", {'form':ContactForm()})
