from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import login,authenticate,logout
from django.http import request

import article

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = RichTextField()
    article_image = models.FileField(blank=True,null=True,verbose_name="Makale'ye Fotoğraf Ekle")
   # models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return str(self.title)
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete= models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_content = models.CharField(max_length = 250, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

    
