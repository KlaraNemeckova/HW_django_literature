from django.shortcuts import render
from django.http import HttpResponse

def writers(request):
    return HttpResponse("Name of a writer")