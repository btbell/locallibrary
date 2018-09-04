from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

# simple test view to make sure everything's working
def hello(request):
  now = datetime.datetime.now()
  html = "<html><body>TEST PAGE... Howdy! It is %s.</body></html>" % now
  return HttpResponse(html)

def foo(request):
  return HttpResponse('FOO!')