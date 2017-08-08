"""secureHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from secureApp import views
from django.conf.urls import include

urlpatterns = [
    
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/getpersoninfo/$',views.postImage ,name='detectImage'),

        url(r'^api/please/$',views.postOwner ,name='sexy'),

        url(r'^api/switchinfo/$',views.switchInfo ,name='sexy1'),

        url(r'^api/addtodatabase/$',views.addDatabase ,name='sexy2'),


        url(r'^api/gethistory/$',views.getHistory ,name='sexy3'),




    url(r'^myrel/$',views.myRel ,name='relatives'),
    url(r'^login/$',views.login ,name='login'),

    url(r'^authfail/$', views.index, name='authfail'),

     url(r'^signin$',views.signIn ,name='signIn'),
     url(r'^home/$',views.home ,name='home'),

     url(r'^history/$',views.history ,name='history'),
     url(r'^settings/$',views.settings ,name='settings'),
     



]
