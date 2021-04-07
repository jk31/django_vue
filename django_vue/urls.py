from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls import url


def index(request):
    return render(request, template_name='index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # new
    url(r'^(?!admin|api-token-auth|static).*$', index, name='index'),
]

