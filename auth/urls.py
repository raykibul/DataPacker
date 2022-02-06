from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.login, name='signup'),
]
