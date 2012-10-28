from django.db import models

class Poll(models.Model):
    """
    The data model for polls.

    As described in the official Django tutorial. 
    """
    
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    
    def __unicode__(self):
        """
        Return the poll question.
        """
        return self.question
    
    def was_published_today(self):
        """
        Return whether or not the poll was published today.
        """
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'

class Choice(models.Model):
    """
    The data model for poll choices.
    
    As described in the official Django tutorial.
    """
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    
    def __unicode__(self):
        """
        Return a specific choice.
        """
        return self.choice
