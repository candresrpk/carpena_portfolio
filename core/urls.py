
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapps.portafolios.urls')),
    path('faq/', include('myapps.faq.urls')),
]
