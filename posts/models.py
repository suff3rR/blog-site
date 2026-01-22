from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=500)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=500)
    image_name = models.CharField(max_length=100)
    date = models.DateField(max_length=10)
    slug = models.SlugField(default="",null=False,db_index=True)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True) # One-to-many relationship with class "Author"

    def __str__(self):
        return self.title
    