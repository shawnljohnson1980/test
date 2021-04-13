from django.db import models
from user_login_app.models import User

class Comment(models.Model):
    comments=models.CharField(max_length=300)
    creator=models.ForeignKey(User,related_name="messages",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Message(models.Model):
    message=models.CharField(max_length=500)
    creator=models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE)
    comments=models.ForeignKey(Comment, related_name="users",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Like(models.Model):
    comment_likes=models.ManyToManyField(User, related_name="comment_likes",blank=True)
    message_likes=models.ManyToManyField(User, related_name='message_likes',blank=True
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
