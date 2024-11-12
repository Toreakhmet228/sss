from my_site.views import HomeView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",HomeView.as_view())
]
