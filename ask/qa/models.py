from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by("-rating")


class Question(models.Model):
    title = models.CharField()
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.CharField()
    likes = models.ManyToManyField(User, related_name='likes_set')
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.CharField()