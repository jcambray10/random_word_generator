from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_word_generator),
    path('random_word_generator', views.random_word_generator),
    path('reset', views.reset)
]