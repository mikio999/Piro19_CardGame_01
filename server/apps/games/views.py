from django.shortcuts import render,redirect
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
def game_attack(request,pk):
    
    return render(request,'games/game_attack.html')

def game_rank(request):
    players=Player.objects.all().order_by('-score')
    return render(request,'games/game_rank.html',{'players':players})