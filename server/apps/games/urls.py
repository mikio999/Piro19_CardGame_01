from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('game/attack', views.game_attack, name="game_attack"),
    path('rankings', views.game_rank),
    path('', views.main, name="main"),]