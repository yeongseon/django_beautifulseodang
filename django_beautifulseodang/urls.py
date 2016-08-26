"""django_beautifulseodang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from home.views import HomePageView, AboutView, ProfileView, LoginView, LogoutView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^(home)', HomePageView.as_view(), name='home'),
    url(r'^introduction/about/', AboutView.as_view(), name='about'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'),
    #url(r'^accounts/login/', LoginView.as_view(), name='login'),
    #url(r'^accounts/logout/', LogoutView.as_view(), name='logout'),

    url(r'^admin/', include(admin.site.urls)),
]
