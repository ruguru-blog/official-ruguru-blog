from django.shortcuts import render
from django.http import HttpResponse
from accounts.forms import SignUpForm, LoginForm


# Create your views here.
def index(response):
    form = LoginForm()
    return render(response, 'index.html', {"form": form})


def tech(request):
    return render(request, "tech.html")
