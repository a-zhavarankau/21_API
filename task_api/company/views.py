from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h2>Hi there!</h2>")
