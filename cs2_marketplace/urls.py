from django.contrib import admin
from django.urls import path,include
from skins.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("skins.urls"))
]
