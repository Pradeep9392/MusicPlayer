from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path('', views.index, name="index"),
]
