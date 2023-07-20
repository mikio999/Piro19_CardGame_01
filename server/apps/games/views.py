from django.shortcuts import render,redirect
from .models import *
import random

# Create your views here.
def game_attack(request,pk):
    
    return render(request,'games/game_attack.html')

def game_rank(request):
    players=Player.objects.all().order_by('-score')
    return render(request,'games/game_rank.html',{'players':players})