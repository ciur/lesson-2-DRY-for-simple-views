from django.contrib import admin
from django.urls import path
from demoapp import views as demo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', demo_views.about, name="about"),
    path('terms', demo_views.terms, name="terms"),
    path('privacy', demo_views.privacy_policy, name="privacy"),
    path('cookies', demo_views.cookies_policy, name="cookies"),
]
