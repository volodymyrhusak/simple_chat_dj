from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    user = models.ForeignKey(User)
    message = models.CharField(max_length=100)

    def __unicode__(self):
        return str((self.message , self.user))