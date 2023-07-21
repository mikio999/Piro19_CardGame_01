from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.db.models import Q
from .forms import GameForm
import random

def game_detail_result(request, pk):
    game = Game.objects.get(id=pk)

    return render(request, 'games/game_detail.html', {'game' : game})

def game_detail_progress(request, pk):
    game = Game.objects.get(id=pk)

    return render(request, 'games/game_detail_progress.html', {'game' : game})

def game_detail_respond(request, pk):
    game = Game.objects.get(id=pk)

    return render(request, 'games/game_detail_respond.html', {'game' : game})

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



def game_revenge(request,pk):

    game=Game.objects.get(id=pk)

    if request.method=='POST':
        
        game.player_card=int(request.POST["selected_card"])

    else:
        cards=[1,2,3,4,5,6,7,8,9,10]
        cards.remove(int(game.my_card)) #models가 charField로 되어있어서
        random_cards=random.sample(cards,5)
        ctx={'game':game,'random_cards':random_cards}

    return render(request,'games/game_revenge.html',context=ctx)

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

def game_delete(request, pk):
    game = Game.objects.get(id=pk)
    game.delete()
    return redirect('games:game_list')
