from django.db import models
import datetime
from django.contrib.auth.models import User as DjangoUser#, AnonymousUser as DjangoAnonymousUser

'''
    This class extends Django User.
    It represents the Q and A user,
    with more attributes to come.
    like whether starred user, has any badges, etc.
'''
class User(models.Model):
    user = models.OneToOneField(DjangoUser)
    is_approved = models.BooleanField(default=False)    

#This class acts as a content holder for\
#Questions and answer.
class Content(models.Model):
    author = models.ForeignKey(User, related_name='%(class)s_author')
    added_at = models.DateTimeField(default=datetime.datetime.now)
    text = models.TextField(null=True)

    class Meta:
        abstract = True

#The Question
class Question(Content):
    title = models.CharField(max_length=300)

#The Answer
class Answer(Content):
    question = models.ForeignKey('Question', related_name='answers')
    accepted    = models.BooleanField(default=False)

'''
    The following classes are for test purpose.
'''
class ExampleFields(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    def __unicode__(self):
        return self.name

class StarWarsCharacter(models.Model):
    name = models.CharField(max_length=200, blank=False)
    def __unicode__(self):
        return self.name

