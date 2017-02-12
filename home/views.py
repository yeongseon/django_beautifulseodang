from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from allauth.account.views import SignupView, LoginView, LogoutView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from home.models import Post
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context

class HomePageListView(ListView):
    template_name = 'home/home.html'
    model = Post
    paginate_by = 5

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

# Education

class ContentView(TemplateView):
    template_name = 'education/content.html'

class CurriculumView(TemplateView):
    template_name = 'education/curriculum.html'

class FeatureView(TemplateView):
    template_name = 'education/feature.html'

class PeriodView(TemplateView):
    template_name = 'education/period.html'

class PurposeView(TemplateView):
    template_name = 'education/purpose.html'

class ProfileView(TemplateView):
    template_name = 'plane/profile.html'

# Donation

class SponsorView(TemplateView):
    template_name = 'donation/sponsor.html'

#

class SignupView(SignupView):
    template_name = 'allauth/account/signup.html'

class LoginView(LoginView):
    template_name = 'allauth/account/login.html'

class LogoutView(LogoutView):
    template_name = 'allauth/account/logout.html'