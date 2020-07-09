
from django.contrib import admin
from django.urls import path
import index.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.views.index),
]
