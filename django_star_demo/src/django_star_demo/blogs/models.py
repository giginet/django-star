from django.db import models

class Entry(models.Model):
    title = models.CharField(u'title', max_length=256)
    body  = models.TextField(u'body')
    
    class Meta:
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('blogs-entry-detail', (self.pk,))