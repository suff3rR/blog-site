from django.shortcuts import render
from django.http import Http404,HttpResponse
from django.template.loader import render_to_string # type: ignore
from datetime import date
from .models import Post



def get_date(post):
    return post['date']


# Create your views here.
def index(request):    #starting page 
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request,"posts/homepage.html",{
        "posts" : latest_posts
    })

def posts(request):    #display all posts
    return render(request,"posts/all_posts.html",{
        "all_posts" : Post.objects.all()
    })

def post_details(request , slug): # Individual post logic
    post = next(post for post in Post.objects.all() if post.slug == slug)  #return the post from all_posts that matches the if condition 
    return render(request, "posts/post-detail.html", {
        "post" : post
    })