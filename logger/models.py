#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Publication(models.Model):
    '''
        Updates.
    '''
    text = models.CharField(max_length=200)
    datetime = models.DateTimeField('Data da atualização.', auto_now_add=True)
    publisher = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.text
    
    class Meta:
        ordering = ['-datetime']


class Bookmark(models.Model):
    '''
        Bookmarks and favorites.
    '''
    publication = models.ForeignKey(Publication)
    owner = models.ForeignKey(User)


class Friendship(models.Model):
    '''
        Followers model.
    '''
    who = models.ForeignKey(User)
    #whon = models.ForeignKey(User)
