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
<<<<<<< HEAD
    # CARD_CHOICES=[]
    my_player=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    player=models.ForeignKey(Player,verbose_name="상대",on_delete=models.CASCADE,related_name="games")
    # random_cards=random.sample(range(1,11),5)
    state=models.IntegerField(max_length=20,default=0)
    mode=models.IntegerField(default=0)
    result=models.IntegerField(default=0)
=======
    my_player=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    player=models.ForeignKey(Player,verbose_name="상대",on_delete=models.CASCADE,related_name="games")
    state=models.IntegerField(default=0) # 진행중, 결과, 반격
    mode=models.IntegerField(default=0) # 높은 점수가 이기는지/낮은 점수가 이기는지
    result=models.IntegerField(default=0) # 게임에서 얻은 점수
>>>>>>> 68d88bd534747d4f09f9eef187e24f357c5ecc76
    my_card=models.IntegerField(default=0)
    player_card=models.IntegerField(default=0)
