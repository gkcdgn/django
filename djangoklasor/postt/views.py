from django.shortcuts import render
from django.http import HttpResponse

def anasayfa(reguest):
    return HttpResponse("merhaba dünya")

# Create your views here.
