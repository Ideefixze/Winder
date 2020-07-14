from django.contrib import admin
from .models import Question
from .models import User
from .models import Answer
# Register your models here.
admin.site.register(Question)
admin.site.register(User)
admin.site.register(Answer)