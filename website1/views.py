from django.shortcuts import render
from django.http import HttpResponse
   

def fun(request):
    return HttpResponse('<h1>hello django<h1/>')


