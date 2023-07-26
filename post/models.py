from django.db import models 
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

from embed_video.fields import EmbedVideoField



class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', _('Draft')
        PUBLISHED = 'PB', _('Published')

    first_name = models.CharField(max_length=99999999999, null=True, blank=True)
    slug = models.SlugField('Слаг', max_length=999999999, null=True, blank=True)
 
    text = models.TextField()
    image = models.ImageField(upload_to='post/%Y%m/%d')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PUBLISHED, null=True, blank=True)
    publish = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    video = EmbedVideoField(blank=True, null=True, verbose_name='Видео')
    time = models.CharField('Языки',max_length=9999900, null=True, blank=True)
    time_one = models.CharField('Время',max_length=9999900, null=True, blank=True)
    time_two = models.CharField('Режиссер',max_length=9999900, null=True, blank=True)
    time_on = models.CharField('Кинокомпания',max_length=9999900, null=True, blank=True)
    time_of = models.CharField('Жанр',max_length=9999900, null=True, blank=True)
    time_ofe = models.CharField('Бюджет',max_length=9999900, null=True, blank=True)
    time_ofu = models.CharField('Страна',max_length=9999900, null=True, blank=True)






    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.first_name, self.commenter_name)

