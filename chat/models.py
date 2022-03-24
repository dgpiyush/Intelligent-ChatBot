from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)





class chatusers(models.Model):
    ip=models.CharField(max_length=255 , unique=True )
    timestamp = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.ip
    
    class Meta:
        ordering = ('timestamp',)
    


class MessageChat(models.Model):
    sender = models.IntegerField()
    receiver = models.IntegerField()
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)

