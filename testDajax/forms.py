from django.forms import ModelForm
from testDajax.models import Person

# ModelForm? Read https://docs.djangoproject.com/en/dev/topics/forms/modelforms/
class PersonForm(ModelForm):
    class Meta:
	model = Person
