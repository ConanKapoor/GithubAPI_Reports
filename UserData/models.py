#Author - Shivam Kapoor
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

#Creating user_data model to store data.
class user_data(models.Model):
    Idx = models.PositiveIntegerField()
    User_name = models.CharField(max_length=200)
    Full_name = models.CharField(max_length=250, blank=True, null=True)
    Location = models.CharField(max_length=200)
    Blog = models.CharField(max_length=200)
    Public_repos = models.PositiveIntegerField()
    Public_gists = models.PositiveIntegerField()
    Email = models.CharField(max_length=250, blank=True, null=True)
    Followers = models.PositiveIntegerField()
    Following = models.PositiveIntegerField()
    Updated_on = models.DateField()
    Image = models.CharField(max_length=500, default='No Picture Available. Weird!')

    #Thumbnail function to show thumbails in admin tables.
    def Thumbnail(self):
        return '<img src="%s" width="30" height="30"/>' % self.Image
    Thumbnail.allow_tags = True

    class Meta(object):
        verbose_name = '1_User Data'
        verbose_name_plural = '1_User Data'

    def __unicode__(self): #Python2 declaration
        return (str(self.Full_name + str(self.Idx)))
