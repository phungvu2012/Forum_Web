from django.urls import path
from . import views
# ADD 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.listgroup , name='group'),
    path('<int:id>/', views.detailGroup)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)