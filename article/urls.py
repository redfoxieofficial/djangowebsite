from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('article/<int:id>',views.detail,name="detail"),
    path('',views.articles,name="articles"),
    path('comment/<int:id>',views.addComment,name="comment"),
]

