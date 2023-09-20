"""DeSmokeinator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from videoapp.views import web_view, livestream, fire1

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('main/', ex_view),
    path('live_stream/', web_view, name='web_view'),
    path('camera/', livestream, name='livestream'),
    path('fire1/', fire1, name='fire1'),
    # path('generate_frames/', live_stream, name='generate_frames'),
    # path('processed/', livestream_processed, name='live_stream_processed')
]
