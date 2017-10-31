from rest_framework.response import Response
from account.models import User
from rest_framework.decorators import api_view
from rest_framework import viewsets
from account.serialzers import UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def login(request):
    data = request.data
    print(data)
    return Response({'data': 0, 'msg': '登录成功'})