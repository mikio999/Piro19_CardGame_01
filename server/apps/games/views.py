from django.shortcuts import render,redirect
from .models import *
import random

# Create your views here.
def main(request) :
    return render(request, 'games/main.html')

def game_attack(request,pk):
    players=Player.objects.all()
    return render(request,'games/game_attack.html',{'players':players})

def game_rank(request):
    players=Player.objects.all().order_by('-score')
    return render(request,'games/game_rank.html',{'players':players})