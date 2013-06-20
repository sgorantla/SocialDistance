__author__ = 'sgorantla'
from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice

class SocialUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    access_token = models.CharField(max_length=100)
    account_id = models.CharField(max_length=50)
    created_date = models.DateField('date created')
    updated_date = models.DateField('date updated')


