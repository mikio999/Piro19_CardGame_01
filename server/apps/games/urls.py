from django.urls import path,include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views

app_name = 'games'

urlpatterns = [
    path('game/attack', views.game_attack, name="game_attack"),
    path('rankings', views.game_rank),
    path('list', views.list, name='game_list'),
    path('', views.main, name="main"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('accounts/',include('allauth.urls'), name='google_login'),
    path('detail/result/<int:pk>/', views.game_detail_result, name='detail_result'), 
    path('detail/progress/<int:pk>/', views.game_detail_progress, name='detail_progress'),
    path('detail/respond/<int:pk>/', views.game_detail_respond, name='detail_respond'),
    path('delete/<int:pk>', views.game_delete, name='delete'),
]
