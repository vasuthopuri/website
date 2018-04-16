import logging

from music.models import Post

logger = logging.getLogger(__name__)

from django.shortcuts import render





def index(request):
    logger.info('what is this', request)
    return render(request, 'index.html', {'title': 'Welcome to HomePage - Vasu Thopuri'})


def about(request):
    print("request is", request)

    return render(request, 'about.html', {'title': 'About - Vasu Thopuri'})


def blog(request):
     posts = Post.objects.all()
     return render(request, 'blog.html', {'title': 'blog - Vasu thopuri', 'posts': posts})


def gallery(request):
    print("request is", request)

    return render(request, 'gallery.html', {'title': 'gallery - Vasu Thopuri'})

def resume(request):
    print("request is", request)

    return render(request, 'resume.html', {'title': 'resume - Vasu Thopuri'})

def contact(request):
    print("request is", request)

    return render(request, 'contact.html', {'title': 'Contact - Vasu Thopuri'})
