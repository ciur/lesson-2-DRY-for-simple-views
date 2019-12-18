from django.contrib import admin
from django.urls import path
from demoapp import views as demo_views

urlpatterns = [
    path('admin/', admin.site.urls),
]

pages = [
    'about',
    'terms',
    'privacy_policy',
    'cookies_policy'
]

for page in pages:
    urlpatterns.append(
        path(
            page,
            demo_views.PageView.as_view(template_name=f"demoapp/{page}.html"),
            name=page
        )
    )
