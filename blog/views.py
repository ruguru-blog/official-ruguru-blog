from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from .models import Post
from .models import Category
from .models import Comment


class IndexListView(ListView):
    queryset = Post.objects.filter(
        status='published').order_by('?')
    template_name = 'index.html'


def about_me(request):
    return render(request, 'categories/about_me.html')


class TechListView(ListView):

    category = get_object_or_404(Category, slug='technology')
    queryset = Post.objects.filter(
        category=category, status='published').order_by('-publication_date')
    template_name = 'categories/tech.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_name"] = self.category.title
        context["category_description"] = self.category.description
        
        return context

class BusinessListView(ListView):
    category = get_object_or_404(Category, slug='business')
    queryset = Post.objects.filter(
        category = category, status='published').order_by('-publication_date')
    template_name = 'categories/business.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_name"] = self.category.title
        context["category_description"] = self.category.description
        return context

class MarketingListView(ListView):
    category = get_object_or_404(Category, slug='marketing')
    queryset = Post.objects.filter(
        category=category, status='published').order_by('-publication_date')
    template_name = 'categories/marketing.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_name"] = self.category.title
        context["category_description"] = self.category.description
        return context


class ContentStrategyListView(ListView):
    category = get_object_or_404(Category, slug='content-strategy')
    queryset = Post.objects.filter(
        category=category, status='published').order_by('-publication_date')
    template_name = 'categories/content_strategy.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_name"] = self.category.title
        context["category_description"] = self.category.description
        return context


class LifeHacksListView(ListView):
    category = get_object_or_404(Category,slug='life-hacks')
    queryset = Post.objects.filter(
        category=category, status='published').order_by('-publication_date')
    template_name = 'categories/life_hacks.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_name"] = self.category.title
        context["category_description"] = self.category.description
        return context


class ProjectManagementListView(ListView):
    category = get_object_or_404( Category, slug='project-management')
    queryset = Post.objects.filter(
        category=category, status='published').order_by('-publication_date')
    template_name = 'categories/project_management.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_name"] = self.category.title
        context["category_description"] = self.category.description
        return context


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    queryset = Post.objects.filter(
        category=category, status='published').order_by('-publication_date')
    
    context = {"category_post_list": queryset,"category_name": category.title}
    return render(request, 'blog/category_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)

    # get 5 latest post
    recent_post = Post.objects.order_by('-publication_date')[:5]
    latest = []

    for i in recent_post:
        latest.append(
            {
                "title": i.title,
                'slug': i.slug
            }
        )

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
    comment_form = CommentForm()
    context = {'post': post, 'comments': comments,
               "comment_form": comment_form, "latest": latest}

    return render(request, 'article.html', context)


def error_404(request, exception):
    return render(request, "404.html")
