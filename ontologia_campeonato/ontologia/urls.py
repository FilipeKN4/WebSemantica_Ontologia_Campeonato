from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_campeonato, name='index_campeonato'),
]
