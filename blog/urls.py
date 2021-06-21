from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path("about-me", views.about_me, name='about_me'),
    path("technology/", views.TechListView.as_view(), name="tech"),
    path("project-management/",
         views.ProjectManagementListView.as_view(), name="project"),
    path("business/",
         views.BusinessListView.as_view(), name="business"),
    path("marketing/",
         views.MarketingListView.as_view(), name="marketing"),
    path("content-strategy/",
         views.ContentStrategyListView.as_view(), name="content_strategy"),
    path("life-hacks/",
         views.LifeHacksListView.as_view(), name="life-hacks"),
    path('article/<slug:slug>/',
         views.PostDetailView.as_view(), name='article_details')
]
