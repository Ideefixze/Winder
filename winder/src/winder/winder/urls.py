"""winder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from lovematch.views import question_view,startup_view,matches_view
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('question/', question_view),
    path('match/', matches_view),
    path('user/', user_views.profile_view),
    path('settings/', user_views.settings_view),
    path('', startup_view, name='start'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('social-auth/', include('social_django.urls', namespace="social")), 
] 

#In case you want to reload Questions at the beginning, uncomment this
#from lovematch.models import loadQuestions
#loadQuestions()