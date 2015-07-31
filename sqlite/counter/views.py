from django.shortcuts import render
from django.http import HttpResponse
from models import Counter

def index(request):
    counter, _ = Counter.objects.get_or_create()
    counter.counter += 1
    counter.save()
    return HttpResponse("This page has been requested " + str(counter.counter) + " times.")
