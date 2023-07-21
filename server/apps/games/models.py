from django.db import models
from django.conf import settings
import random

# Create your models here.

class Player(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    score=models.IntegerField(default=0)

    # 오버라이딩
    def __str__(self):
        return self.name
    
class Game(models.Model):
    my_player=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    player=models.ForeignKey(Player,verbose_name="상대",on_delete=models.CASCADE,related_name="games")
    state=models.IntegerField(default=0)
    mode=models.IntegerField(default=0)
    result=models.IntegerField(default=0)
    my_card=models.IntegerField(default=0)
    player_card=models.IntegerField(default=0)
