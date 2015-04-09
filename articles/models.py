from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify

class Article(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=150, blank=True)
    title_show = models.BooleanField('Display title', default=True)
    header_image = models.ForeignKey('media.Picture', blank=True, null=True)
    thumbnail = models.ForeignKey('media.Picture', related_name='article_thumbnail', blank=True, null=True)
    issue = models.ForeignKey('issue.Issue', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)
    section = models.ForeignKey('Section')
    series = models.ForeignKey('Series', blank=True, null=True)
    part_number = models.IntegerField(blank=True, default=0)
    part_name = models.CharField(max_length=150, blank=True)
    persons = models.ManyToManyField('people.Person')
    sources = models.ManyToManyField('media.Source', blank=True)
    content = models.TextField()
    blurb = models.TextField(blank=True)
    show_blurb = models.BooleanField('Show blurb in full article?', default=False)
    footer = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    pages = models.CommaSeparatedIntegerField(max_length=30)
    def __unicode__(self):
        return '%s %d' % (self.title, self.part_number)
    def get_id(self):
        if self.issue:
            return '/%d/%d-%s' % (self.issue.number, int(self.pages.split(',')[0]), slugify(self.title))
        else:
            return format('/web/%(year)d/%(month)d/%(day)d/%(hour)d-%(minute)d-%(title)s' % {
                'year': self.date.year,
                'month': self.date.month,
                'day': self.date.day,
                'hour': self.date.hour,
                'minute': self.date.minute,
                'title': slugify(self.title) })
    def get_absolute_url(self):
        return reverse('read-article', kwargs={'slug':self.slug})
    def generate_slug(self):
        '''
        Outputs the default, auto-generated slug for the given article, using 
        other properties to create a (hopefully) unique slug.
        Note that this only outputs the slug; the saving is done in this 
        model's modified save() method.
        '''
        if self.issue is not None:
            slug = '%d-%d-%s' % (
                self.issue.number, 
                int(self.pages.split(',')[0]), 
                slugify(self.title))
        elif self.date is not None:
            slug = 'web-%d%d%d-%s' % (
                self.date.year, 
                self.date.month, 
                self.date.day, 
                slugify(self.title))
        else:
            # Unable to generate slug from either issue or date fields
            slug = self.slug
        return slug
    def save(self, *args, **kwargs):
        # Set the slug if field is blank
        if self.slug == 'auto' or not self.slug:
            self.slug = self.generate_slug()
        # Delete annoying '<br>' from blurb
        if self.blurb == '<br>':
            self.blurb = ''
        # Do the real save
        super(Article, self).save(*args, **kwargs)
    class Meta:
        get_latest_by = 'issue'
class Series(models.Model):
    title = models.CharField(max_length=150, blank=True)
    header_image = models.ForeignKey('media.Picture', blank=True, null=True)
    tagline = models.CharField(max_length=150, blank=True)
    def __unicode__(self):
        return self.title
class Section(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True)
    description = models.TextField(default='<p>No description!</p>')
    submission_instructions = models.TextField(blank=True)
    icon_left = models.URLField(blank=True)
    icon_right = models.URLField(blank=True)
    def __unicode__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    def __unicode__(self):
        return self.name
