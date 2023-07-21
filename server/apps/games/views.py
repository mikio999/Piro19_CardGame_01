from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
import random

# Create your views here.
def main(request) :
    return render(request, 'games/main.html')
    print("login")

def game_attack(request):
    
    
    if request.method=="POST":
        my_player=request.user
        my_card=request.POST['selected_card']
        player_id=request.POST['player_id']
        #mode random 선택도 해줘야 할 듯        
        Game.objects.create(
            my_player=my_player,
            my_card=my_card,
            player=Player.objects.get(id=player_id)
        )   
        return render(request, 'games/game_attack.html')
    else:
        random_cards = random.sample(range(1, 11), 5)
        players=Player.objects.all()
        ctx={'random_cards':random_cards,'players':players}


    return render(request,'games/game_attack.html',context=ctx)

def game_revenge(request,pk):

    game=Game.objects.get(id=pk)

    if request.method=='POST':
        
        game.player_card=request.POST["selected_card"]

    else:
        cards=[1,2,3,4,5,6,7,8,9,10]
        cards.remove(game.my_card)
        random_cards=random.sample(cards,5)
        ctx={'random_cards':random_cards}

    return render(request,'games/game_revenge.html',context=ctx)

def game_rank(request):
    players=Player.objects.all().order_by('-score')
    return render(request,'games/game_rank.html',{'players':players})