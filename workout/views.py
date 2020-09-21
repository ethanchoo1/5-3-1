from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Account, Lift
from django.template import loader


def index(request):
    return HttpResponse("you are at index")

def account(request):
        return HttpResponse("Hello world")
