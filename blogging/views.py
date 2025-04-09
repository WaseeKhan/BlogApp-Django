from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    top_posts = Post.objects.filter(status='published').order_by('-publish_date')[:2]
    posts = Post.objects.all()
    return render(request, 'blogs/home.html',{'posts':posts, 'top_posts':top_posts})
