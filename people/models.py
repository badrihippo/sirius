from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=60)
    photo = models.URLField(blank=True)
    about = models.TextField(blank=True)
    def __unicode__(self):
        return self.name
