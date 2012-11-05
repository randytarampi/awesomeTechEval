from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from testDajaxice.forms import ContactForm

@dajaxice_register
def send_message(req, form):
    f = ContactForm(form)
    if f.is_valid():
        # Use mail_admin or something to send off the data like you normally would.
        return simplejson.dumps({'status':'Success!'})
    return simplejson.dumps({'status':f.errors})
