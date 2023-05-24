from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rrr(request):
    return HttpResponse('bheem')
def rrr2(request):
    return render(request,'homeapp1.html')