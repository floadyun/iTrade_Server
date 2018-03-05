from rest_framework.response import Response
from account.models import User
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from account.serialzers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
@parser_classes((JSONParser,))
def login(request):
    username = request.query_params['user_name']
    result = dict()
    try:
        user = User.objects.get(name=username)
        result['user_name'] = user.name
        result['userInfo'] = UserSerializer(user).data
        result['msg'] = '登录成功'
        return Response(result)
    except User.DoesNotExist:
        return Response({'message': '用户不存在'})

@api_view(['POST'])
def register(request):
    username = request.query_params['user_name']
    password = request.query_params['password']
    try:
        user = User.objects.get(name=username)
        return Response({'msg': '用户已存在'})
    except User.DoesNotExist:
        user = User()
        user.name = username
        user.passWord = password
        user.save()
        return Response({'msg': '注册成功'})