from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("<int:id>/test/<str:id2>", views.test, name="test")
]
