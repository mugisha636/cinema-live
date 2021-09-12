from django.db import models
import datetime
from django.db.models.fields import CharField

from django.db.models.query_utils import select_related_descend

# Create your models here.


class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class WhatWeDo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title


class Team(models.Model):
    title = models.CharField(max_length=50)
    names = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ' : ' + self.names


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    genre = CharField(max_length=50, default="Action")
    author = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title


class Messages(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.subject
