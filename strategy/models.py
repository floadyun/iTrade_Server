from django.db import models
from account.models import User

# Create your models here.
class Strategy(models.Model):
    strategy_title = models.CharField(max_length=200)
    strategy_content = models.CharField(max_length=1000)
    publish_date = models.DateTimeField(max_length=100, auto_now_add=True)
    browse_count = models.IntegerField(default=0)
    pay_count = models.IntegerField(default=0)
    user_id = models.CharField(max_length=100)
    is_pay_money = models.BooleanField(default=False)