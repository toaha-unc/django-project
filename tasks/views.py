from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
   return HttpResponse("Welcome to the task management system")

def root(request):
   return HttpResponse("root page")


def contact(request):
   return HttpResponse("<h1 style='color: red'>This is the contact page</h1>")

def show_task(request):
    return HttpResponse("This is our task page")