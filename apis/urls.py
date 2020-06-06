"""heroku_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers, serializers, viewsets
from apis.serializers import TiLoginUserData2SerializerViewSet

router = routers.DefaultRouter()
router.register(r'data', TiLoginUserData2SerializerViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    # url(r'data/$', views.user_id_func),
    # url(r'data/(?P<pk>[0-9]+)$', views.parte_user_id_func)
]
