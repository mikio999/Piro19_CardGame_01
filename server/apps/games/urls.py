from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from apps.games import views

urlpatterns = [
    path('rankings', views.game_rank),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)