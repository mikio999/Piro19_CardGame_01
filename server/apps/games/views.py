from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def game_rank(request):
    players=Player.objects.all().order_by('-score')
    return render(request,'games/game_rank.html',{'players':players})