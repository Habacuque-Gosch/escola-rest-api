from django.contrib import admin
from django.urls import path, include
from apps.escola.views import *
# from django.conf import settings
# from django.conf.urls.static import static

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', alunos),
    path('api-auth/', include('rest_framework.urls')),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)