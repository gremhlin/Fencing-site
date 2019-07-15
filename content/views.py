from django.shortcuts import render

def index(request):
    return render(request, 'content/index.html', {})

def about(request):
    return render(request, 'content/about.html', {})

def connect(request):
    return render(request, 'content/connect.html', {})

def partnerships(request):
    return render(request, 'content/partnerships.html', {})
