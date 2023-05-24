from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def friend(request):
    return HttpResponse('hi friend')
def friend2(request):
    return render(request,'homeapp2.html')