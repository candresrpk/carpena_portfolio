
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapps.portafolios.urls')),
    path('faq/', include('myapps.faq.urls')),
    path('honey/', include('myapps.honey.urls')),
    path('users/', include('myapps.users.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)