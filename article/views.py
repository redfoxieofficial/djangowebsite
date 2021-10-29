from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404,reverse
import article
from .models import Comment
from .forms import Article, ArticleForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@csrf_exempt
def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html", {"articles":articles})
    articles = Article.objects.all()
    return render(request,"articles.html",{"articles":articles})

@csrf_exempt
def index(request):
    return render(request,"index.html")
@csrf_exempt
def about(request):
    return render(request,"about.html")
@csrf_exempt
def cv(request):
    return render(request,"cv.html")

@csrf_exempt
def contact(request):
    return render(request,"contact.html")

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all()
    
    return render(request,"detail.html",{"article":article,"comments":comments})


@csrf_exempt
@login_required
def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))
