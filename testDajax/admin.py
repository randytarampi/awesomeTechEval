from testDajax.models import Person
from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    display_fields = ["name", "birthday", "gift_bought"]

admin.site.register(Person, PersonAdmin)
