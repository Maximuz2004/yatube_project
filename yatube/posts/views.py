import os.path

from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    template = 'posts/index.html'
    context = {
        'title': 'Это главная страница проекта Yatube',
    }
    return render(request, template, context=context)

def group_posts(request):
    template = 'posts/group_list.html'
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context=context)

def group_post_details(request, slug):
    template = 'posts/{slug}.html'
    return render(request, template)