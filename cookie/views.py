from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input (request):
    return render(request,'base.html')
def add (request):
    x=int(request.GET['t1'])
    y=int(request.GET['t2'])
    z=x+y
    res = HttpResponse("data submited successfully ")
    res.set_cookie('z',max_age=30)
    return res
def display (request):
    if 'z' in request.COOKIES:
        sum=request.COOKIES['z']
        return HttpResponse("addition of two numbers:" +sum)
    else:
        return render(request, 'base.html')
