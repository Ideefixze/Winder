from django.db import models

# Create your models here.

class Question(models.Model):
    content = models.CharField(max_length=200)


class User(models.Model):
    nickname = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    class Meta:
        unique_together = ['nickname', 'group']

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.IntegerField()
    class Meta:
        unique_together = ['question', 'user']

