from calendarapp.models import Entry
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    list_display = ["creator", "date", "title", "snippet"]
    list_filter = ["creator"]

admin.site.register(Entry, EntryAdmin)
