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
from home.views import HomePageView, HomePageListView, AboutView, ProfileView, GreetingView, \
    TimelineView, PeopleView, NewsView, \
    ContentView, CurriculumView, FeatureView, PeriodView, PurposeView

urlpatterns = [
    url(r'^$', HomePageListView.as_view(), name='home'),
    url(r'^(home)', HomePageListView.as_view(), name='home'),
    url(r'^introduction/about/', AboutView.as_view(), name='about'),
    url(r'^introduction/greeting/', GreetingView.as_view(), name='greeting'),
    url(r'^introduction/timeline/', TimelineView.as_view(), name='timeline'),
    url(r'^introduction/people/', PeopleView.as_view(), name='people'),
    url(r'^introduction/news/', NewsView.as_view(), name='news'),

    url(r'^education/content/', ContentView.as_view(), name='content'),
    url(r'^education/curriculum/', CurriculumView.as_view(), name='curriculum'),
    url(r'^education/feature/', FeatureView.as_view(), name='feature'),
    url(r'^education/period/', PeriodView.as_view(), name='period'),
    url(r'^education/purpose/', PurposeView.as_view(), name='purpose'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
