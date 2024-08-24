from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print(f"request: %s" % request)
    print(request.body)
    return HttpResponse(f"request : {request}{request.user}{request.session}")

