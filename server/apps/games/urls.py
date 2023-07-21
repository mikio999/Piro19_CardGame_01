from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from apps.games.views import *

app_name = 'games'

urlpatterns = [
    path('rankings', views.game_rank),
    path('', views.main, name="main"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('detail/result/<int:pk>/', game_detail_result),
    path('detail/progress/<int:pk>/', game_detail_progress),
    path('detail/respond/<int:pk>/', game_detail_respond),
]
