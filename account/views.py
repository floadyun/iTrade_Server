from django.shortcuts import render
from rest_framework.response import Response
from account.models import User



# Create your views here.


def login(request,phone):
    try:
        user = User.objects.get(phone=phone)
        return Response('用户已存在,登录成功.')
    except User.DoesNotExist:
        User.objects.create(phone=phone)
        return Response('用户不存在,创建新账号.')