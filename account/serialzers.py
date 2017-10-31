from rest_framework import serializers
from account.models import User

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'password', 'phone')