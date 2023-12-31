from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.db.models import Q
# from .forms import GameForm
import random
import os

#구글 소셜로그인 변수 
state = os.environ.get("STATE")
BASE_URL = 'http://127.0.0.1:8000'
GOOGLE_CALLBACK_URI = BASE_URL + 'api/user/google/callback/'

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
    return render(request, 'games/main.html',)

def game_attack(request):
    players = Player.objects.all()

    if request.method == 'POST':
        selected_card = int(request.POST.get('selected_card'))
        player_id = request.POST.get('player_id')
        my_player = get_object_or_404(Player, user=request.user)
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

        return redirect('games:game_list')

    else:
        random_cards = random.sample(range(1, 11), 5)
        return render(request, 'games/game_attack.html', {'random_cards': random_cards, 'players': players})



def login(request) :
    print("login")
    if request.method == 'POST' :
        print("login post")

        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, username=email, password=password)

        if user is None :
            print('login fail')
            return redirect('/login')
        else :
            auth.login(request, user)
            player, _ = Player.objects.get_or_create(user=user, name=user.username)
            return redirect('/')

    return render(request, 'games/login.html')

def google_login(request):
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id = os.environ.get("SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")

def logout(request) :
    auth.logout(request)
    return redirect('/')

def signup(request):   
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            existing_user = User.objects.get(username=username)
            return redirect('/login/')
        except User.DoesNotExist:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.backend = f'{ModelBackend.__module__}.{ModelBackend.__qualname__}'
            auth.login(request, user)
            player, _ = Player.objects.get_or_create(user=user, name=user.username)
            return render(request, 'games/main.html')

    return render(request, 'games/signup.html')

def game_revenge(request, pk):
    game = Game.objects.get(id=pk)

    game.state = 1
    game.save()
    if request.method == 'POST':
        game.player_card = int(request.POST.get('selected_card'))
        game.save()

        # 게임 결과 계산
        if game.mode == 0:
            if game.my_card < game.player_card:
                game.result = game.my_card  # 플레이어가 이기며 자신이 고른 카드의 숫자만큼의 점수 획득
                game.my_player.score += game.my_card
                game.player.score -= game.player_card
            else:
                game.result = -game.my_card  # 상대가 이기며 자신이 고른 카드의 숫자만큼의 점수 손실
                game.my_player.score -= game.my_card
                game.player.score += game.player_card
        else:
            if game.my_card > game.player_card:
                game.result = game.my_card  # 플레이어가 이기며 자신이 고른 카드의 숫자만큼의 점수 획득
                game.my_player.score += game.my_card
                game.player.score -= game.player_card
            else:
                game.result = -game.my_card
                game.my_player.score -= game.my_card
                game.player.score += game.player_card

        
        game.my_player.save()
        game.player.save()
        game.save()
        return redirect(f"/detail/result/{game.id}")

    else:
        cards = [1,2,3,4,5,6,7,8,9,10]
        cards.remove(int(game.my_card))
        random_cards = random.sample(cards, 5)
        ctx = {'game': game, 'random_cards': random_cards}

        return render(request, 'games/game_revenge.html', context=ctx)

def game_rank(request):
    players=Player.objects.all().order_by('-score')
    return render(request,'games/game_rank.html',{'players':players})

def list(request):
    my_player_instance = request.user.player
    games = Game.objects.filter(Q(my_player=my_player_instance) | Q(player=my_player_instance)).order_by('-id')
    ctx = {
        'games': games,
    }
    return render(request, 'games/game_list.html', context=ctx)

def game_delete(request, pk):
    game = Game.objects.get(id=pk)
    game.delete()
    return redirect('games:game_list')
