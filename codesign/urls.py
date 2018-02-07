from django.contrib import admin
from django.urls import path

from sign import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sign),
]

admin.site.site_header = "Signatures"
admin.site.site_title = "Code+Design Signatures"
