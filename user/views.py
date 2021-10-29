from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.info(request,"Başarılı Bir Şekilde Kayıt Olundu")
        return redirect("index")
    context = {"form":form}
    return render(request,"register.html",context)
       
@csrf_exempt
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {"form":form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password=password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola hatalı")
            return render(request,"login.html",context)
        messages.info(request,"Başarıyla Giriş Yapıldı")
        login(request,user)
        return redirect("index")
        
    return render(request,"login.html",context)


def logoutUser(request):
    logout(request)
    messages.info(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")
