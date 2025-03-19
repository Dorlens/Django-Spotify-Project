from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('random_track/', views.random_track, name='random_track'),
]

