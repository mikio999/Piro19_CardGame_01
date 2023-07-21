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
    # random_cards=random.sample(range(1,11),5)
    CARD_CHOICES=[]
    state=models.IntegerField(default=0) # 진행중, 패배, 승리
    mode=models.IntegerField(default=0) # 높은 점수가 이기는지/낮은 점수가 이기는지
    result=models.IntegerField(default=0) # 게임에서 얻은 점수
    my_card=models.CharField(
        choices=CARD_CHOICES, max_length=5,blank=True
    )
    player_card=models.IntegerField(default=0)
