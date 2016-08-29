from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View

from django.views.generic import TemplateView
from allauth.account.views import SignupView, LoginView, LogoutView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home/home.html'

    #def get_context_data(self, **kwargs):
    #    context = super(HomePageView, self).get_context_data(**kwargs)
    #    messages.info(self.request, 'hello http://example.com')
    #    return context

class AboutView(TemplateView):
    template_name = 'introduction/about.html'

class GreetingView(TemplateView):
    template_name = 'introduction/greeting.html'

class TimelineView(TemplateView):
    template_name = 'introduction/timeline.html'

class PeopleView(TemplateView):
    template_name = 'introduction/people.html'

class NewsView(TemplateView):
    template_name = 'introduction/news.html'

class ProfileView(TemplateView):
    template_name = 'plane/profile.html'

class SignupView(SignupView):
    template_name = 'allauth/account/signup.html'

class LoginView(LoginView):
    template_name = 'allauth/account/login.html'

class LogoutView(LogoutView):
    template_name = 'allauth/account/logout.html'