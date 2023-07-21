from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.db.models import Q
from .forms import GameForm
import random

def game_detail_result(request, pk):
    game = Game.objects.get(id=pk)

    return(request, 'game_detail.html', {'game' : game})

def game_detail_progress(request, pk):
    game = Game.objects.get(id=pk)

    return(request, 'game_detail_progress.html', {'game' : game})

def game_detail_respond(request, pk):
    game = Game.objects.get(id=pk)

    return(request, 'game_detail_respond.html', {'game' : game})

def main(request) :
    return render(request, 'games/main.html')

def game_attack(request):
    players = Player.objects.all()

    if request.method == 'POST':
        selected_card = int(request.POST.get('selected_card'))
        player_id = request.POST.get('player_id')
        my_player = request.user
        player = Player.objects.get(id=player_id)

        # 게임 모드 선택 (0: 숫자가 더 낮은 쪽이 이기는 모드, 1: 숫자가 더 높은 쪽이 이기는 모드)
        mode = random.randint(0, 1)

        # 플레이어와 상대방이 고른 카드
        my_card = selected_card

        # 게임 객체 생성
        game = Game.objects.create(
            my_player=my_player,
            player=player,
            my_card=my_card,
            mode=mode,
            result=0  # 초기 결과를 0으로 설정
        )

        return redirect('games:game_attack')

    else:
        random_cards = random.sample(range(1, 11), 5)
        return render(request, 'games/game_attack.html', {'random_cards': random_cards, 'players': players})


def game_revenge(request, pk):
    game = Game.objects.get(id=pk)

    if request.method == 'POST':
        game.player_card = int(request.POST["selected_card"])

        # 게임 결과 계산
        if game.mode == 0:
            if game.my_card < game.player_card:
                game.result = game.my_card  # 플레이어가 이기며 자신이 고른 카드의 숫자만큼의 점수 획득
            else:
                game.result = -game.my_card  # 상대가 이기며 자신이 고른 카드의 숫자만큼의 점수 손실
        else:
            if game.my_card > game.player_card:
                game.result = game.my_card  # 플레이어가 이기며 자신이 고른 카드의 숫자만큼의 점수 획득
            else:
                game.result = -game.my_card  # 상대가 이기며 자신이 고른 카드의 숫자만큼의 점수 손실

        game.save()

    else:
        cards = list(range(1, 11))
        cards.remove(int(game.my_card))
        random_cards = random.sample(cards, 5)
        ctx = {'game': game, 'random_cards': random_cards}

    return render(request, 'games/game_revenge.html', context=ctx)

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
