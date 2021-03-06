from django.db import models
from django.contrib.auth.models import User

# It may look impressive, but honestly the bulk of this code came from
#http://lightbird.net/dbe/cal1.html

class Entry(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)
    body = models.TextField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True)
    creator = models.ForeignKey(User, blank=True, null=True)
	# I will probably have to put this back in later    
#remind = models.BooleanField(default=False)

    def __unicode__(self):
        if self.title:
            return unicode(self.creator) + u" - " + self.title
        else:
            return unicode(self.creator) + u" - " + self.snippet[:40]

    def short(self):
        if self.snippet:
            return "<i>%s</i> - %s" % (self.title, self.snippet)
        else:
            return self.title
    short.allow_tags = True

    class Meta:
        verbose_name_plural = "entries"

