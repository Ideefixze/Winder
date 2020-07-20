from django.db import models
from django.contrib.auth.models import User
from enum import Enum


class Question(models.Model):
    content = models.CharField(max_length=200)
    weight = models.IntegerField(default=1)
    pairedquestion = models.ForeignKey('Question',blank=True,null=True,on_delete=models.CASCADE,unique=True)

class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=50)
    class Meta:
        unique_together = ['user', 'group']

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    usergroup = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    answer = models.IntegerField()
    class Meta:
        unique_together = ['question', 'usergroup']

    def score(self, other):
        distance = abs(self.answer - other.answer)
        if distance >= 4:
            return 0
        return (self.question.weight + other.question.weight) * 1/(2**distance)

    def maxscore(self, other):
        return (self.question.weight + other.question.weight)

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def loadQuestions():
    Question.objects.all().delete()
    with open(os.path.join(BASE_DIR,'q-formatted.txt')) as qfile:
        while nr := qfile.readline():
            nr = int(nr)
            content = qfile.readline()
            print(f"Adding: {nr} = {content}")
            q = Question(id=nr, content=content,weight=1)
            q.save()
    
    for i in range(1,81):
        q = Question.objects.get(id=i)
        if i < 41:
            q.pairedquestion=Question.objects.get(id=i+40)
        else:
            q.pairedquestion=Question.objects.get(id=i-40)
        q.save()
            
