from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
import random

# Create your views here.
def main(request) :
    return render(request, 'games/main.html')
def game_attack(request,pk):
    
    return render(request,'games/game_attack.html')

def game_rank(request):
    players=Player.objects.all().order_by('-score')
    return render(request,'games/game_rank.html',{'players':players})

def list(request):
    my_player_instance, _ = Player.objects.get_or_create(user=request.user, name='my_player')

    games = Game.objects.filter(Q(my_player=request.user) | Q(player=my_player_instance)).order_by('-id')
    ctx = {
        'games': games,
    }
    return render(request, 'games/game_list.html', context=ctx)

