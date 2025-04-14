from django.shortcuts import get_object_or_404, render
from .models import *
from datetime import datetime
from django.utils import timezone

# Create your views here.

def home(request):
    top_posts = Post.objects.filter(status='published').order_by('-publish_date')[:2]
    posts = Post.objects.all()
    categories = Category.objects.all()
    featured_posts = Post.objects.filter( featured = True, status = 'published', ).order_by('publish_date')[:1]
    recent_posts =  Post.objects.filter(status='published').exclude(featured=True)[:5]
    context = {

        'top_posts':top_posts,
        'posts':posts,
        'categories':categories,
        'featured_posts':featured_posts,
        'recent_posts':recent_posts,
        
    }
    print(featured_posts)
    return render(request, 'blog/home.html',context)

def post_detail(request, year, month, day, slug):
    publish_date = datetime(year=year, month=month, day=day).date()
    featured_posts = Post.objects.filter( featured = True, status = 'published', ).order_by('publish_date')[:1]
    post = get_object_or_404(
        Post,
        publish_date__year=year,
        publish_date__month=month,
        publish_date__day=day,
        slug=slug,
        status='published'
    )
    categories = Category.objects.all()
    
    # print("=================",post.get_absolute_url())
    context = {
        'post': post,
        'categories':categories,
        'featured_posts':featured_posts,
        
    }
    return render(request, 'blog/view_post.html', context)