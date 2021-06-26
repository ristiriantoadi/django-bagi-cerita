from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=120,blank=True)
    date_posted = models.DateTimeField(null=True, blank=True)
    content = RichTextField(blank=True,null=True)
    # content = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    words_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} Cerita'

    class Meta:
        ordering = ["-date_posted"]

class Tag(models.Model):
    name = models.CharField(max_length=120,blank=True)
    # how do you implement many to many relationship to story
    stories = models.ManyToManyField(Story)

    def __str__(self):
        return f'{self.name} Tag'

class Comment(models.Model):
    content = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    story = models.ForeignKey(Story, on_delete=models.CASCADE,default=None)
    replied_comment_id = models.IntegerField(default=0)
    rating = models.IntegerField(default=1)
    read_status = models.BooleanField(default=False)
    date_posted = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-date_posted"]

    # a comment is either an original comment or a reply
    # an original comment have story data, and replied_comment_id = 0
    # a reply have NO story data, and replied_comment_id != 0
    # or, if it's not possible to make the story data = null, then story data AND replied_comment_id != 0
    # either way, a reply HAVE replied_comment_id != 0 -- period
    # that's how you knew it's a reply or a original comment
    
    # replied_comment_id != 0 -- means reply
    # replied_comment_id == 0 -- means original comment    