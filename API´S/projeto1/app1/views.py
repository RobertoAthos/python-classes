from django.shortcuts import render
# Create your views here.

def index(req):
    return render(req, 'user/index.html')

def create(req):
    return render(req, 'user/criar.html')

