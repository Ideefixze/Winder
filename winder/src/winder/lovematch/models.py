from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    content = models.CharField(max_length=200)

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
        return 1/(abs(self.answer - other.answer) + 1)

