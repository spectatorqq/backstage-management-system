"""chimingfazhou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mana/', include('mana.urls')),
    path('banner/', include('banner.urls')),
    path('user/', include('userapp.urls')),
    path('article/', include('article.urls')),
    path('album/', include('album.urls')),
    path('authority/', include('authority.urls')),
    re_path('csrf/first_page/(\d+)/(\w+)/(\w*?)(/?)$', views.FirstPage.as_view()),
    re_path('detail/wen/(\d+)/(\d+)$', views.DetailWen.as_view()),
    re_path('account/regist/', views.Regist.as_view()),
]
