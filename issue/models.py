from django.db import models
from django.core.urlresolvers import reverse
class Issue(models.Model):
    '''Description of a particular issue of Sirius'''
    
    cover_picture = models.ForeignKey('media.Picture')
    name = models.CharField(max_length=150)
    number = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    squiggle = models.ForeignKey('Squiggle',
        null=True,
        blank=True)
    cover_article = models.OneToOneField('articles.Article',
        null=True,
        blank=True,
        related_name='cover_article')
    sections = models.ManyToManyField('articles.Section')
    def __unicode__(self):
        return '#%d %s to %s "%s"' % (
            self.number,
            self.start_date,
            self.end_date,
            self.name)
    def get_absolute_url(self):
        return reverse('view-issue', args=[self.number])
class Editorial(models.Model):
    issue = models.ForeignKey('Issue')
    content = models.TextField()
    def __unicode__(self):
        return '%s' % self.issue
class Squiggle(models.Model):
    '''Model for squiggles that references the media.Picture model and
    adds additional information. Information from the Picture model is:
    * Caption (Media.caption)
    * Description (Media.description)
    * Image URL, etc. as usual
    New properties defined in squiggle are:
    * Event
    * Event Date
    * Event 2 (in case squiggle references 2 events)
    * Event Date 2
    * Embed code (in case of interactive squiggle)
    * Related articles (ManyToMany field)
    * Tags (keywords)
    '''
    picture = models.ForeignKey('media.Picture')
    event1 = models.CharField(max_length=128)
    date1 = models.DateField()
    event2 = models.CharField(max_length=128, blank=True)
    date2 = models.DateField(blank=True, null=True)
    embed_code = models.TextField(blank=True)
    related_articles = models.ManyToManyField('articles.Article', blank=True)
    tags = models.ManyToManyField('articles.Tag', blank=True)
    def __unicode__(self):
        return format('%(event1)s [%(date1)s]' % {
            'event1': self.event1,
            'date1': self.date1})
    def get_absolute_url(self):
        return reverse('squiggle-by-date', kwargs={
            'year': self.date1.year,
            'month': self.date1.month,
            'day': self.date1.day })
        #return format('/squiggle/%(year)d/%(month)d-%(day)d/' % {
        #    'year': self.date1.year,
        #    'month': self.date1.month,
        #    'day': self.date1.day })
    class Meta:
        ordering = ['-date1']
class UpcomingSquiggle(models.Model):
    '''Model for storing information about upcoming squiggles'''
    event = models.CharField(max_length=128)
    date = models.DateField()
    last_date = models.DateField()
    event_description = models.TextField(blank=True)
    def __unicode__(self):
        return '%(event)s [%(date)s]' % {
            'event': self.event,
            'date': self.date,
            }
        
    
