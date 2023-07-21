from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('game/attack', views.game_attack, name="game_attack"),
    path('game/<int:pk>/revenge', views.game_revenge, name="game_attack"),
    path('rankings', views.game_rank),
    path('', views.main, name="main"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    ]