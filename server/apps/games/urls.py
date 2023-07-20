from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('rankings', views.game_rank),
    path('', views.main, name="main"),]