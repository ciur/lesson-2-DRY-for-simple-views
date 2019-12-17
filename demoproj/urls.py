from django.contrib import admin
from django.urls import path
from demoapp import views as demo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demoapp/profile/<int:id>', demo_views.profile, name="profile"),
]
