from django.db import models

class Picture(models.Model):
    disp_title = models.CharField(max_length=256, blank=True)
    caption = models.CharField(max_length=300,blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='smedia', blank=True, null=True)
    credit = models.TextField(blank=True)
    url = models.URLField(blank=True)
    illustrators = models.ManyToManyField('people.Person', blank=True)
    sources = models.ManyToManyField('Source', blank=True)
    def __unicode__(self):
        if self.disp_title:
            return self.disp_title
        elif self.caption:
            return self.caption
        else:
            return self.description[:20]
    def get_absolute_url(self):
        if self.image: return self.image.url
        else: return self.url
class Source(models.Model):
    name = models.CharField(max_length=300, blank=True)
    url = models.URLField(blank=True)
    detail = models.TextField(blank=True)
    copyrights = models.ManyToManyField('Copyright', blank=True)
    icon = models.URLField(blank=True)
    sss_copyright = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name
class Copyright(models.Model):
    name = models.CharField(max_length=30, blank=True)
    shortname = models.SlugField(primary_key=True)
    image = models.URLField(blank=True)

    
