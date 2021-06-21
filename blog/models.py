from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import random
import string
from ckeditor_uploader.fields import RichTextUploadingField
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# def generate_random_slug():
#     """ generate a random string to use for slug """
#     return ''.join(random.choice(string.ascii_letters))

# class Author(models.Model):
#     pass

STATUS_CHOICES = (('published', 'Published'), ('draft', 'Draft'),)


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="Tag")
    slug = models.SlugField(max_length=100, unique=True,
                            allow_unicode=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    slug = models.SlugField(max_length=150, unique=True,
                            allow_unicode=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        unique_together = (('title', 'slug'),)

    def get_absolute_url(self):
        return reverse('categories', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=250, unique=True,
                            allow_unicode=True, blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, verbose_name='status', default='draft')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Category')
    publication_date = models.DateTimeField(verbose_name='Created')
    picture = models.ImageField(
        upload_to='uploads/%Y/%m/%d', blank=True, null=True, verbose_name='Picture as thumbnail')
    post_content = RichTextUploadingField(
        null=False, verbose_name="post content")
    author = models.CharField(
        max_length=64, default='Anonymous', verbose_name='Created by')
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def date_published(self):
        return self.publication_date.strftime("%B %d, %Y %H:%M")

    def get_category(self):
        return self.category.title

    def get_absolute_url(self):
        return reverse('article_details', args=[self.slug])


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Post)
pre_save.connect(slug_generator, sender=Category)
pre_save.connect(slug_generator, sender=Tag)


# class Comment(models.Model):
#     # post
#     # commentor_name
#     # date_added DateTimeField(auto_now_add=True)
#     pass
