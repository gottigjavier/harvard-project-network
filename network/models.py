from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils import timezone

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='following_field', blank=True, default='')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followers_field', blank=True, default='')
    myposts = models.ManyToManyField('Posts', related_name='myposts', blank=True, default='')
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.username

    def serialize(self):
        if (self.image):
            return {
                "id": self.id,
                "username": self.username,
                "image": self.image.url,
                "date_joined": self.date_joined.strftime("%b %-d %Y, %-I:%M %p"),
                "myposts": [myposts.id for myposts in self.myposts.all()],
                "following": [following.id for following in self.following.all()],
                "followers": [followers.id for followers in self.followers.all()]
            } 
        else:
            return {
                "id": self.id,
                "username": self.username,
                "date_joined": self.date_joined.strftime("%b %-d %Y, %-I:%M %p"),
                "myposts": [myposts.id for myposts in self.myposts.all()],
                "following": [following.id for following in self.following.all()],
                "followers": [followers.id for followers in self.followers.all()]
            }         


class Posts(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User,  related_name='authoruser', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='likesuser', blank=True, default='')


    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "author": self.author.username,
            "created": self.created.strftime("%b %-d %Y, %-I:%M %p"),
            "likes": [likes.id for likes in self.likes.all()]
        } 
