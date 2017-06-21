# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=20,primary_key=True)
#     password = models.CharField(max_length=20)
#     firstname = models.CharField(max_length=20)
#     lastname = models.CharField(max_length=20)
#
#     def __unicode__(self):
#         return self.username+self.password

class Post(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(User,default=None)
    date = models.DateTimeField(auto_now_add=True,blank=False)

    def __unicode__(self):
        return self.content
