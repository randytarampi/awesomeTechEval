from django.shortcuts import render
from testDajax.forms import PersonForm

# Create your views here.
def index(request):
    return render(request, "dajaxIndex.html", {'form':PersonForm()})
