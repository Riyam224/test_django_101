from django.shortcuts import render

# Create your views here.

from .models import Posts



def index(request):
    posts =  Posts.objects.all()
    context = {
        'posts': posts
    }
    return render(request , 'index.html', context)
                  