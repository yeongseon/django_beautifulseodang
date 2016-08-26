from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View

from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.

class MyView(View):
    def get(self, request):
        return HttpResponse('result')

class HomePageView(TemplateView):
    template_name = 'home/home.html'

    #def get_context_data(self, **kwargs):
    #    context = super(HomePageView, self).get_context_data(**kwargs)
    #    messages.info(self.request, 'hello http://example.com')
    #    return context

class AboutView(TemplateView):
    template_name = 'introduction/about.html'
