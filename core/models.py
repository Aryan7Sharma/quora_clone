from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    
class Questions(models.Model):
    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=100)
    question = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_answer = models.IntegerField(default=0)

    def __str__(self):
        return f"Question ID: {self.question_id}, Username: {self.username}"
    
class Answer(models.Model):
    answer_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    answer = models.TextField()
    ans_post_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Answer ID: {self.answer_id}, Question ID: {self.question.question_id}, Username: {self.username}"
