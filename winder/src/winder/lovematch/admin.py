from django.contrib import admin
from .models import Question
from .models import UserGroup
from .models import Answer
# Register your models here.
admin.site.register(Question)
admin.site.register(UserGroup)
admin.site.register(Answer)