from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from allauth.account.views import SignupView, LoginView, LogoutView

from home.models import Post
from home.models import Donation
from home.models import Book
from home.models import Notice
from home.models import News
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

class NewsView(ListView):
    template_name = 'introduction/news.html'
    model = News
    paginate_by = 5

class NewsDetailView(DetailView):
    template_name = 'introduction/news_detail.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        return context

class NoticesView(ListView):
    template_name = 'introduction/notices.html'
    model = Notice
    paginate_by = 5

class NoticeDetailView(DetailView):
    template_name = 'introduction/notice_detail.html'
    model = Notice

    def get_context_data(self, **kwargs):
        context = super(NoticeDetailView, self).get_context_data(**kwargs)
        return context

# Education

class ContentView(ListView):
    template_name = 'education/content.html'
    model = Book

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

class SponsorView(ListView):
    template_name = 'donation/sponsor.html'
    model = Donation

class HowtoView(TemplateView):
    template_name = 'donation/howto.html'

# Apply
class ApplicationView(TemplateView):
    template_name = 'apply/application.html'

class InquireView(TemplateView):
    template_name = 'apply/inquire.html'

"""
class SignupView(SignupView):
    template_name = 'allauth/account/signup.html'

class LoginView(LoginView):
    template_name = 'allauth/account/login.html'

class LogoutView(LogoutView):
    template_name = 'allauth/account/logout.html'
"""