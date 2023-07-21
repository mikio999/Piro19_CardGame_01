from django.urls import path,include
from . import views

app_name = 'games'

urlpatterns = [
    path('rankings', views.game_rank),
    path('', views.main, name="main"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('accounts/',include('allauth.urls'), name='google_login'),
    ]