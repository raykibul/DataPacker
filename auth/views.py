from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the auth index.")
    

def login(request):
    return HttpResponse("Hello,from login.")