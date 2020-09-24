from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/bloodtests/', include('bloodtests.urls')),
]
