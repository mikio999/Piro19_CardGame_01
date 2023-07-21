from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from .forms import GameForm
import random

# Create your views here.
def main(request) :
    return render(request, 'games/main.html')

def game_attack(request):
    player = Player.objects.all()
    if request.method == 'POST':
        selected_cards = request.POST.getlist('selected_cards')
        player_id = request.POST.get('player_id')

        my_player = request.user
        player = Player.objects.get(id=player_id)

        game = Game.objects.create(
            my_player=my_player,
            player=player,
            my_card=','.join(selected_cards)
        )
        return render(request, 'games/game_attack.html', {'players': player})
    else:
        random_cards = random.sample(range(1, 11), 5)
        return render(request, 'games/game_attack.html', {'random_cards': random_cards, 'players': player})
    
def game_revenge(request):
    players=Player.objects.all()
    return render(request,'games/game_revenge.html',{'players':players})

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

