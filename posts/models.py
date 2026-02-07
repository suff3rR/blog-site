from django.db import models
from django.utils.text import slugify
from datetime import date
from django.core.validators import MinLengthValidator
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):                         # One-to-many relation with Post model
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField()
    
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL ,related_name="posts",null=True)
    tag = models.ManyToManyField(Tag)
     
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
