from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import random
import string
from ckeditor_uploader.fields import RichTextUploadingField

def generate_random_slug():
    """ generate a random string to use for slug """
    return ''.join(random.choice(string.ascii_letters))

# class Author(models.Model):
#     pass

STATUS_CHOICES = ( ('published', 'Published'), ('draft', 'Draft'),)

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="Tag")
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])


    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('Categories', args=[self.slug])


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug  = slugify(generate_random_slug()+'-'+self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=150,unique=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, verbose_name='status', default='draft')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    publication_date = models.DateTimeField(verbose_name='Created')
    post_content = RichTextUploadingField(null=False, verbose_name="post content")
    author = models.CharField(max_length=64, default='Anonymous' ,verbose_name='Created by')
    tags = models.ManyToManyField(Tag)


    def  save(self, *args, **kwargs):
        if not self.slug:
            self.slug  =slugify(generate_random_slug()+'-'+self.title)
        super(Post, self).save(*args, **kwargs)


    def date_published(self):
        return self.publication_date.strftime('%B-%d-%Y')

    def get_absolute_url(self):
        return reverse('articles', args=[self.slug])


# class Comment(models.Model):
#     # post
#     # commentor_name
#     # date_added DateTimeField(auto_now_add=True)
#     pass

