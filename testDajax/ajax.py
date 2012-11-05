from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from testDajax.models import Person
from testDajax.forms import PersonForm

def _get_person(p):
    dajax = Dajax()
    dajax.add_css_class('#idError', 'hideIt')
    dajax.assign('#idName', 'innerHTML', p.name)
    dajax.assign('#idDay', 'innerHTML', p.birthday.strftime("%B %d"))
    gift = 'Yes' if p.gift_bought else '<a href="#" onclick="Dajaxice.testDajax.bought_gift(Dajax.process, {\'pk\':_cur_person});">No</a>'
    dajax.assign('#idGift', 'innerHTML', gift)
    dajax.script("_cur_person = %d;" % p.pk)
    return dajax.json()

@dajaxice_register
def get_person(req, pk):
    try:
        p = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        dajax = Dajax()
        dajax.remove_css_class('#error', 'hideIt')
        return dajax.json()
    return _get_person(p)

@dajaxice_register
def bought_gift(req, pk):
    p = Person.objects.get(pk=pk)
    p.gift_bought = True
    p.save()
    return _get_person(p)

@dajaxice_register
def add_person(req, form):
    f = PersonForm(form)
    if f.is_valid():
        return _get_person(f.save())
    dajax = Dajax()
    dajax.assign('#personError', 'innerHTML', 'Correct the following fields: %s' % f.errors)
    return dajax.json()

@dajaxice_register
def say_hello(req):
    dajax = Dajax()
    dajax.alert("Hello World!")
    return dajax.json()
