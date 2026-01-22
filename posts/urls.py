from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"), #starting page 
    path("posts/",views.posts,name="all-posts"), #/posts
    path("posts/<slug:slug>",views.post_details,name="individual-posts") #/posts/my-first-post
]