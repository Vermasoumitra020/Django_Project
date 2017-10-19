from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import User

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender')
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message


