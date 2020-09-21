from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime
from .models import Account, Lift
from django.template import loader


def index(request):
    return HttpResponse("you are at index")

sets = {
    0 : {
        "percents" : [.65, .75, .85],
        "reps" : [5, 5, 5]
    },
    1 : {
        "percents" : [.70, .80, .90],
        "reps" : [3, 3, 3]
    },
    2 : {
        "percents" : [.75, .85, .95],
        "reps" : [5, 3, 1]
    },
    3 : {
        "percents" : [.40, .50, .60],
        "reps" : [5, 5, 5]
    },
}
def today(request):
    template = loader.get_template('workout/today.html')
    day = datetime.datetime.today().weekday()
    options = { 0 : "ohp",
                1 : "none",
                2 : "squat+deadlift",
                3 : "bench",
                4 : "ohp",
                5 : "squat+deadlift",
                6 : "ohp",
    }
    if (day==1):
        context = {}
        return HttpResponse(template.render(context, request))
    lift_names = options[day].split("+")
    lift = "max_"+lift_names[0]
    #figure out how to deal with squat and deadlift
    my_account = Account.objects.get(pk=1)
    working_weight = getattr(my_account,lift)*0.9
    week = my_account.days_worked//7
    set0 = [round(sets[week]["percents"][0]*working_weight), sets[week]["reps"][0]]
    set1 = [round(sets[week]["percents"][1]*working_weight), sets[week]["reps"][1]]
    set2 = [round(sets[week]["percents"][2]*working_weight), sets[week]["reps"][2]]
    context = {
        #add current day/day of the week to context
        'lift' : lift_names[0],
        'set0' : set0,
        'set1' : set1,
        'set2' : set2,
    }
    return HttpResponse(template.render(context, request))
    #figure out make submit button increment days_worked



def account(request):
        return HttpResponse("Hello world")
