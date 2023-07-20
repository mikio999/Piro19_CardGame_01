from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from games.views import *

urlpatterns = [
    path('detail/result/<int:pk>/', game_detail_result),
    path('detail/progress/<int:pk>/', game_detail_progress),
    path('detail/respond/<int:pk>/', game_detail_respond),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)