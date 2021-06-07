from django.shortcuts import render
from django.http import HttpResponse
from accounts.forms import SignUpForm, LoginForm


# Create your views here.
def index(response):
    form = LoginForm()
    return render(response, 'index.html', {"form": form})


def test(request, id, id2):
    return HttpResponse(f"<H1>THIS IS THE test PAGE: id => {id}//// id2 => {id2}</H2>")
