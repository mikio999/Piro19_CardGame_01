from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
import random

def game_detail_result(request, pk):
    game = Game.objects.get(id=pk)

    return(request, 'game_detail.html')

def game_detail_progress(request, pk):
    return()

def game_detail_respond(request, pk):
    return()

def main(request) :
    return render(request, 'games/main.html')

def login(request) :
    print("login")
    if request.method == 'POST' :
        print("login post")

        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, username=email, password=password)

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

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username=username, email=email, password=password)


        return redirect('/')

    return render(request, 'games/signup.html')


def game_attack(request,pk):
    
    return render(request,'games/game_attack.html')

def game_rank(request):
    players=Player.objects.all().order_by('-score')
    return render(request,'games/game_rank.html',{'players':players})