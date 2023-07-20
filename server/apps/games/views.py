from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
import random

# Create your views here.
def main(request) :
    return render(request, 'games/main.html')

def login(request) :
    print("login")
    if request.method == 'POST' :
        print("login post")

        email = request.POST['email']
        pwd = request.POST['pwd']

        user = auth.authenticate(request, username=email, password=pwd)

        if user is None :
            return redirect('/signup')
        else :
            auth.login(request, user)
            return redirect('/')

    return render(request, 'games/login.html')

def logout(request) :
    auth.logout(request)
    return redirect('/')

def signup(request):
    print("signup 실행!")
    if request.method == 'POST' :
        print("여기는 포스팅요청")

        email = request.POST['email']
        pwd = request.POST['pwd']

        User.objects.create_user(username=email, password=pwd)


        return redirect('/')

    print("signup 마지막 부분")
    return render(request, 'games/signup.html')


def game_attack(request,pk):
    
    return render(request,'games/game_attack.html')

def game_rank(request):
    players=Player.objects.all().order_by('-score')
    return render(request,'games/game_rank.html',{'players':players})