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
from home.views import HomePageView, HomePageListView, AboutView, ProfileView, \
    GreetingView, TimelineView, PeopleView, NewsView, NewsDetailView, NoticeDetailView, NoticesView, \
    ContentView, CurriculumView, FeatureView, PeriodView, PurposeView, \
    SponsorView, HowtoView, ApplicationView, InquireView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', HomePageListView.as_view(), name='home'),
    url(r'^(home)', HomePageListView.as_view(), name='home'),
    url(r'^introduction/about/', AboutView.as_view(), name='about'),
    url(r'^introduction/greeting/', GreetingView.as_view(), name='greeting'),
    url(r'^introduction/timeline/', TimelineView.as_view(), name='timeline'),
    url(r'^introduction/people/', PeopleView.as_view(), name='people'),
    url(r'^introduction/news/', NewsView.as_view(), name='news'),
    url(r'^introduction/news_detail/(?P<pk>[0-9]+)/$', NewsDetailView.as_view(), name='news_detail'),
    url(r'^introduction/notices/', NoticesView.as_view(), name='notices'),
    url(r'^introduction/notice_detail/(?P<pk>[0-9]+)/$', NoticeDetailView.as_view(), name='notice_detail'),

    url(r'^education/content/', ContentView.as_view(), name='content'),
    url(r'^education/curriculum/', CurriculumView.as_view(), name='curriculum'),
    url(r'^education/feature/', FeatureView.as_view(), name='feature'),
    url(r'^education/period/', PeriodView.as_view(), name='period'),
    url(r'^education/purpose/', PurposeView.as_view(), name='purpose'),

    url(r'^donation/sponsor/', SponsorView.as_view(), name='sponsor'),
    url(r'^donation/howto/', HowtoView.as_view(), name='howto'),

    url(r'^apply/application/', ApplicationView.as_view(), name='application'),
    url(r'^apply/inquire/', InquireView.as_view(), name='application'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),



    url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    #url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('social_django.urls', namespace='social')),
    #url(r'^oauth/', include('social.apps.django_app.urls', namespace='social')),

    #url(r'^accounts/', include('allauth.urls')), #python-allauth
    #url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'), #python-allauth
    url(r'^', include('favicon.urls')),
]
