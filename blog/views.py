from django.shortcuts import render
from django.http import HttpResponse
from accounts.forms import SignUpForm, LoginForm
from .models import Post, Category, Tag
from django.views.generic import ListView
from django.views.generic import DetailView

def index(request):
    form = LoginForm()
    return render(request, 'index.html', {"form": form})


def about_me(request):
    return render(request, 'categories/about_me.html')

class TechListView(ListView):
    category_id = Category.objects.filter(slug='technology')
    queryset = Post.objects.filter(
        category__in=category_id).order_by('-publication_date')
    template_name = 'categories/tech.html'


class BusinessListView(ListView):
    category_id = Category.objects.filter(slug='business')
    queryset = Post.objects.filter(
        category__in=category_id).order_by('-publication_date')
    template_name = 'categories/business.html'


class MarketingListView(ListView):
    category_id = Category.objects.filter(slug='marketing')
    queryset = Post.objects.filter(
        category__in=category_id).order_by('-publication_date')
    template_name = 'categories/marketing.html'


class ContentStrategyListView(ListView):
    category_id = Category.objects.filter(slug='content-strategy')
    queryset = Post.objects.filter(
        category__in=category_id).order_by('-publication_date')
    template_name = 'categories/content_strategy.html'


class LifeHacksListView(ListView):
    category_id = Category.objects.filter(slug='life-hacks')
    queryset = Post.objects.filter(
        category__in=category_id).order_by('-publication_date')
    template_name = 'categories/life_hacks.html'


class ProjectManagementListView(ListView):
    category_id = Category.objects.filter(title='Project Management')
    queryset = Post.objects.filter(
        category__in=category_id).order_by('-publication_date')
    template_name = 'categories/project_management.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'article.html'

