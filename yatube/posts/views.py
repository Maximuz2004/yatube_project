from django.shortcuts import render, get_object_or_404

from .models import Post, Group


# Create your views here.

def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': 'Это главная страница проекта Yatube',
        'posts': posts,
    }
    # print(posts.__dict__)
    return render(request, template, context=context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': slug,
        'group_name': group.title,
        'group_desc': group.description,
        'posts': posts
    }
    return render(request, template, context=context)
