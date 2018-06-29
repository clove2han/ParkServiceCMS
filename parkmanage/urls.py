#_*_coding:utf-8_*_

"""parkservicecms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index),
#把post/开头的网址后面的字符串都找出来。
    url(r'^index', views.index,name='index'),
    url(r'^login', views.login,name='login'),
    url(r'^parkinfo', views.parkinfo, name='parkinfo'),
    url(r'^employeeinfo', views.employeeinfo, name='employeeinfo'),
    url(r'^test', views.test, name='test'),

    url(r'add_book$', views.add_book, ),
    url(r'show_books$', views.show_books, ),
]

urlpatterns += staticfiles_urlpatterns()